import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DB_PATH = Path(__file__).parent / "data" / "kleague.sqlite3"
SPEC_PATH = Path(__file__).parent / "data" / "kleague_api.md"
MAX_ROWS = 1000  # ponytail: cap output so a SELECT * on a 47k-row table can't flood the context

# Open the prebuilt DB read-only at startup; build it once if missing.
# check_same_thread=False because FastMCP may serve tool calls from a worker thread.
db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True, check_same_thread=False)
db.row_factory = sqlite3.Row
mcp = FastMCP(
    "kleague",
    instructions=(
        "K League (Korean football) data as read-only SQLite, one table per Open API "
        "endpoint. ALWAYS call docs() first: it explains opaque columns and codes "
        "(e.g. meet_seq 1=K1/2=K2, HOME_TYPE 1=home/2=away) you cannot guess from "
        "column names. Then list_tables() / describe(table) to find columns, and "
        "query(sql) to run SELECTs. All columns are TEXT, so CAST for numeric work."
    ),
)


@mcp.tool()
def list_tables() -> str:
    """List all available K League data tables with their row counts.

    Each table maps to one Open API endpoint (e.g. match_info, club_rank,
    match_player_record). Call describe() to see a table's columns before querying.
    """
    rows = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    out = []
    for r in rows:
        n = db.execute(f'SELECT count(*) c FROM "{r["name"]}"').fetchone()["c"]
        out.append(f'{r["name"]}\t{n} rows')
    return "\n".join(out)


@mcp.tool()
def describe(table: str) -> str:
    """Return the column names of a table (use list_tables first to get names).

    Note: every table has meta columns __endpoint, __fetched_at and the request
    params as param_* (e.g. param_meet_year). All values are stored as TEXT.
    """
    cols = db.execute(f'PRAGMA table_info("{table}")').fetchall()
    if not cols:
        return f"no such table: {table}"
    return ", ".join(c["name"] for c in cols)


@mcp.tool()
def docs() -> str:
    """Return the K League API spec: every table's fields with Korean descriptions,
    code meanings (e.g. HOME_TYPE 1=home/2=away, meet_seq 1=K1/2=K2), and notes like
    the B_/A_/EB_/EA_ time-window prefixes. Read this before writing non-trivial SQL
    so you know what opaque columns (GAINGOAL_PER_STQTY, HALF_TYPE, ACT_CODE...) mean.
    """
    return SPEC_PATH.read_text(encoding="utf-8")


@mcp.tool()
def query(sql: str) -> str:
    """Run a read-only SQL SELECT against the K League data and return TSV rows.

    The DB is SQLite, read-only. One table per endpoint; all columns are TEXT, so
    cast for numeric work (e.g. CAST(GAIN_POINT AS INT)). Output is capped at
    1000 rows. Example: SELECT TEAM_NAME, RANK FROM club_rank ORDER BY CAST(RANK AS INT).
    """
    try:
        cur = db.execute(sql)
    except sqlite3.Error as e:
        return f"SQL error: {e}"
    if cur.description is None:
        return "(no result set)"
    header = [d[0] for d in cur.description]
    rows = cur.fetchmany(MAX_ROWS)
    lines = ["\t".join(header)]
    lines += ["\t".join("" if v is None else str(v) for v in r) for r in rows]
    if len(rows) == MAX_ROWS:
        lines.append(f"... (truncated at {MAX_ROWS} rows)")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
