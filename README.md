# K League API MCP

K리그 공식 Open API 데이터를 LLM이 SQL로 조회할 수 있게 해주는 MCP 서버입니다.
빌드된 SQLite DB(약 25MB)를 함께 배포하므로 API 키나 네트워크 없이 바로 동작합니다.

## 제공 도구 (tools)

| 도구 | 설명 |
|------|------|
| `list_tables` | 모든 데이터 테이블과 행 수 목록 |
| `describe(table)` | 테이블의 컬럼 목록 |
| `docs()` | API 스펙 문서 (한글 필드 설명, 코드값 의미) |
| `query(sql)` | 읽기 전용 SQLite SELECT 실행 (TSV 반환, 최대 1000행) |

`club_rank`, `match_info`, `player_info`, `match_player_record` 등 22개 테이블을 포함합니다.
엔드포인트 1개 = 테이블 1개이며, 모든 값은 TEXT로 저장되어 있습니다.

## 설치

Python 3.10+ 필요.

```bash
git clone https://github.com/UoS-CIDA-Lab/k-league-api-mcp.git
cd k-league-api
pip install -r requirements.txt
```

DB는 `data/kleague.sqlite3`에 이미 포함되어 있어 별도 빌드가 필요 없습니다.

## 등록 방법

이 서버는 stdio로 통신합니다. 사용하는 클라이언트의 설정 파일에 아래 항목을 추가하세요.
`/absolute/path/to`는 clone 받은 실제 경로로 바꿔야 합니다.

### Claude Desktop

설정 파일 위치:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "kleague": {
      "command": "python",
      "args": ["/absolute/path/to/k-league-api/kleague_mcp.py"]
    }
  }
}
```

저장 후 Claude Desktop을 재시작하면 도구가 나타납니다.

### Claude Code

프로젝트 폴더에서 한 줄로 등록:

```bash
claude mcp add kleague -- python /absolute/path/to/k-league-api/kleague_mcp.py
```

### Cursor / 기타 MCP 클라이언트

대부분의 클라이언트가 동일한 `mcpServers` JSON 형식을 사용합니다.
위 Claude Desktop 예시의 `command` / `args`를 해당 클라이언트의 MCP 설정에 그대로 넣으면 됩니다.

> `python`이 PATH에 없거나 가상환경을 쓴다면 `command`를 해당 파이썬 절대경로
> (예: `/path/to/venv/bin/python`)로 지정하세요.

## 사용 예시

등록 후 클라이언트에서 자연어로 물어보면 됩니다:

> "K리그1 현재 순위를 알려줘"

LLM이 내부적으로 다음과 같이 호출합니다:

```sql
SELECT TEAM_NAME, RANK FROM club_rank ORDER BY CAST(RANK AS INT)
```

모든 컬럼이 TEXT이므로 숫자 정렬·연산 시 `CAST(... AS INT)`가 필요합니다.
컬럼 의미가 궁금하면 LLM이 `docs()`를 먼저 읽도록 되어 있습니다.

## 라이선스

데이터 출처: K League Open API.
