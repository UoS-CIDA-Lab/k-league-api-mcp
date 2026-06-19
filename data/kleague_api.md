# K League Open API 명세 정리

> 출처: https://api.kleague.com/docs/index.jsp
> 정리일: 2026-06-10

## 공통 사항

- **Base URL:** `https://api.kleague.com`
- **HTTP Method:** 전 API `GET`
- **인증:** `authKey` 파라미터 필수 (Header 전송 권장 / Query string 레거시 / Bearer 토큰 2027 예정)
- **공통 응답 래퍼:** `apiName`, `resultCode`(`"00"`=성공), `resultMsg`, 데이터 배열 `list`
- **공통 키 파라미터:** `meet_year`(대회년도), `meet_seq`(대회순번: 1=K1, 2=K2, 3=R리그…), `game_id`(경기번호)

---

## 1. 기초 / 마스터 정보

### 공통코드 마스터 — `/api/codeType.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |

| 필드 | 타입 | 설명 |
|---|---|---|
| CODE_TYPE | numeric(3,0) | 공통코드 마스터 번호 |
| TYPE_NAME | varchar(30) | 공통코드 유형 명칭 |
| USE_YN | char(1) | 사용여부 (Y/N) |

### 공통코드 상세 — `/api/comCode.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| code_type | numeric(3,0) | Y | 조회할 공통코드 마스터 번호 |

| 필드 | 타입 | 설명 |
|---|---|---|
| CODE_TYPE | numeric(3,0) | 공통코드 마스터 번호 |
| COM_CODE | numeric(4,0) | 상세 코드값 |
| CODE_NAME | varchar(40) | 코드명 |
| CODE_E_NAME | varchar(40) | 관리항목1 (정렬순서/기타) |
| CODE_CLASS | varchar(3) | 관리항목2 (그룹핑) |
| SORT_SEQ | int | 정렬순서 |
| USE_YN | varchar(1) | 사용여부 (Y/N) |

### 리그 정보 — `/api/leagueInfo.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |
| meet_year | String(4) | Y | 시즌 년도 (예: 2026) |

| 필드 | 타입 | 설명 |
|---|---|---|
| MEET_YEAR | String | 리그 년도 |
| MEET_SEQ | Number | 리그 순번 (고유 식별자) |
| LEAGUE_ID | Number | 리그구분 코드 (2=K1, 3=K2) |
| MEET_NAME | String | 공식 리그명 |
| GAME_QTY | Number | 총 경기수 |
| TEAM_QTY | Number | 참가 팀수 |
| MEET_TYPE / MEET_TYPE_NAME | Number / String | 리그 유형 코드 / 명칭 |
| START_DATE / END_DATE | String | 리그 시작/종료일 (YYYY/MM/DD) |
| MEET_YN | String | 리그 종료 여부 (Y/N) |

### 구단 정보 — `/api/clubInfo.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |

| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID | String | 구단 코드 (예: K25) |
| TEAM_NAME / TEAM_S_NAME / TEAM_F_NAME | String | 구단명 / 약칭 / 공식 전체명 (국문) |
| TEAM_ENG_NAME / TEAM_ENG_F_NAME | String | 구단 영문명 / 공식 영문 전체명 |
| START_DATE / END_DATE | String | 창립일 / 해체일 (활동중 빈값) |
| RELATION_AREA_NAME | String | 연고지 |
| MANAGER_NAME | String | 현재 감독명 |
| HOMEPAGE | String | 공식 홈페이지 URL |
| LEAGUE_ID | Number | 소속 리그 코드 (활동중단시 0) |
| R_LEAGUE_YN / U18_LEAGUE_YN | String | R리그 / U18리그 운영여부 (Y/N) |

### 선수·코칭스태프 정보 — `/api/playerInfo.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |
| last_update | String(10) | N | 최종 수정일 (YYYY/MM/DD) |
| teamd_id | String(3) | N | 팀 ID (예: K01) |
| act_type | String(1) | N | 활동상태 (1:현역, 2:은퇴, 3:해외, 4:대기) |

| 필드 | 타입 | 설명 |
|---|---|---|
| PLAYER_ID | varchar(8) | 인물 고유 코드 |
| CORP_CD / TEAM_S_NAME | varchar | 팀 코드 / 팀 약칭 |
| POS_NAME / JOB_NAME | varchar(40) | 역할 구분 / 직책 |
| NAME / PLAYER_NAME_ENG | varchar | 성명 (국문/영문) |
| COUNTRY_NAME | varchar(40) | 국적 |
| BIRTH_DATE | varchar(10) | 생년월일 (YYYY/MM/DD) |
| BACK_NO | int | 등번호 |
| POSITION_NAME | varchar(40) | 포지션 (FW/MF/DF/GK) |
| HEIGHT / WEIGHT | numeric | 키(cm) / 몸무게(kg) |
| BLOOD_TYPE_NAME | varchar(40) | 혈액형 |
| ARMY_NAME | varchar(40) | 병역 상태 |
| MIDDLESCHOOL / HIGHSCHOOL / UNIVERSITYSCHOOL | varchar | 중/고/대 학력 |
| ACT_TYPE_NAME | varchar(40) | 활동 상태 |
| CONTACT_SDATE / CONTACT_EDATE | varchar(10) | 계약 시작/종료일 |
| LASTUPDATE | varchar(40) | 최종 수정 시각 |

### 경기장 정보 — `/api/stadiumInfo.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |

| 필드 | 타입 | 설명 |
|---|---|---|
| FIELD_ID | Number | 경기장 고유 ID |
| FIELD_NAME / FIELD_S_NAME / FIELD_FULLNAME | String | 경기장명 / 약칭 / 공식 전체명 |
| FIELD_ENG_NAME | String | 경기장 영문명 |
| FIELD_ADDRESS | String | 주소 |
| START_DATE | String | 개장일 (YYYY/MM/DD) |
| FIELD_CAPA | Number | 수용 인원 |
| TEAM_ID / TEAM_S_NAME | String | 주 사용 구단 코드 / 약칭 |
| LEAGUE_ID | Number | 리그 구분 코드 |
| USE_YN | String | 사용여부 (Y/N) |

---

## 2. 일정 / 경기 기본

### 대회 일정 — `/api/meetSchedule.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |
| meet_year | String(4) | Y | 대회 년도 |
| meet_seq | String | Y | 대회순번 (1:K1, 2:K2 등) |

| 필드 | 타입 | 설명 |
|---|---|---|
| GAME_ID | Number | 경기 고유 번호 |
| ROUND_ID | Number | 라운드 번호 |
| HOME_TEAM_NAME / AWAY_TEAM_NAME | String | 홈팀 / 원정팀명 |
| FIELD_NAME | String | 경기장명 |
| GAME_DATE / GAME_TIME / GAME_DAY | String | 경기 일자(YYYY/MM/DD) / 시각(HH:mm) / 요일 |
| GAME_TYPE_NAME | String | 경기 유형 (정규/결승 등) |
| END_YN | String | 경기 종료 여부 (Y/N) |
| REC_SUM_YN / AUDIENCE_YN / POINT_SUM_YN | String | 기록/관중수/승점 합산 여부 (Y/N) |

### 경기 일반정보 — `/api/matchInfo.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | String | Y | API 인증키 |
| meet_year | String(4) | Y | 대회 년도 |
| meet_seq | Integer | Y | 대회순번 |
| game_id | Integer | Y | 경기번호 |

| 필드 | 타입 | 설명 |
|---|---|---|
| MEET_NAME_KOR / LEAGUE_NAME | varchar | 대회명 / 리그명 |
| GAME_DATE / GAME_TIME | varchar | 경기 일자 / 시각 |
| HOME_TEAM_NAME / AWAY_TEAM_NAME | varchar | 홈/원정팀명 |
| HOME_GAIN_GOAL / AWAY_GAIN_GOAL | int | 홈/원정 득점 |
| FIELD_NAME / AUDIENCE_QTY | varchar / int | 경기장 / 관중수 |
| WEATHER_NAME / TEMPERATURE / HUMIDITY | varchar / numeric | 날씨 / 기온(℃) / 습도(%) |
| REFREE_NAME1~4 | varchar | 주심 / 부심1 / 부심2 / 대기심 |
| INSPECTOR_NAME1~2 / RECORDER | varchar | 경기감독관 / 심판감독관 / 기록원 |
| MOM_TEAM_NAME / MOM_PLAYER_NAME | varchar | MOM 소속팀 / 선수명 |
| B_STIME / B_ETIME / B_DIFF_TIME | varchar / int | 전반 시작/종료/소요(분) |
| A_STIME / A_ETIME / A_DIFF_TIME | varchar / int | 후반 시작/종료/소요(분) |
| EB_STIME / RUNMIN | varchar / int | 연장 시작 / 총 경기시간(분) |
| H_JCOLOR_KOR / A_JCOLOR_KOR | varchar | 홈/원정 유니폼 색 |
| NEUTRAL_YN / END_YN | varchar | 중립경기 / 종료 여부 (Y/N) |
| HOME_TK_GOAL / AWAY_TK_GOAL | int | 홈/원정 승부차기 득점 |

---

## 3. 경기별 상세 기록

> 공통 파라미터: `authKey`, `meet_year`, `meet_seq`, `game_id` (별도 표기 외)

### 경기별 팀 기록 — `/api/matchRecord.do`
| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / HOME_TYPE / WIN_TYPE | varchar / numeric | 구단 / 홈어웨이(1홈2어웨이) / 승패(1승2패3무) |
| MANAGER_NAME / FORMATION | varchar | 감독 / 포메이션 (예: 4-4-2) |
| GAIN_GOAL / LOSS_GOAL | int | 득점 / 실점 |
| HALF_B_GOAL / HALF_A_GOAL / EXTEND_GOAL | int | 전반/후반/연장 득점 |
| GAIN_POINT / GAP_GOAL | float / int | 획득 승점 / 득실차 |
| ST_QTY / B_ST_QTY / A_ST_QTY / VALID_ST_QTY | int | 슈팅(전체/전반/후반) / 유효슈팅 |
| CK_QTY / AS_QTY / PK_QTY / OS_QTY | int | 코너킥 / 어시스트 / PK / 오프사이드 |
| FO_QTY / WARN_QTY / EXIT_QTY | int | 파울 / 경고 / 퇴장 |
| TEAM_TIME / TEAM_SHARE | varchar / numeric | 점유시간(HH:mm) / 점유율(%) |
| CHANGE_QTY | int | 교체 횟수 |
| GAINGOAL_PER_STQTY / STVALIDQTY_PER_STQTY | numeric | 슈팅 대비 득점율 / 유효슈팅 비율 |

### 경기별 엔트리 — `/api/matchEntry.do`
| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / TEAM_NAME | varchar | 팀 코드 / 팀명 |
| PLAYER_ID / PLAYER_NAME / PLAYER_NAME_ENG | varchar | 선수 ID / 국문명 / 영문명 |
| PLAYER_SEQ / BACK_NO | int | 선수 순번 / 등번호 |
| POSITION_CODE / POSITION_NAME | numeric / varchar | 포지션 코드 / 명칭 (GK/DF/MF/FW) |
| CAPTAIN_YN | char(1) | 주장 여부 (Y/N) |
| PLAYER_FORMATION_PLACE | varchar(10) | 하프코트 포메이션 위치 매핑 |
| XPOS / YPOS | numeric(7,2) | 전체 경기장 기준 좌표 (좌상단 0,0 원점) |
| LASTUPDATE | varchar | 최종 수정 시각 |

### 경기별 세트피스 — `/api/playerSetPiece.do`
> `game_id` 미입력(0/null)시 전체 경기 조회

| 필드 | 타입 | 설명 |
|---|---|---|
| GROUP_SEQ / SEQ | int | 세트피스 그룹 순번 / 세부 진행 번호 |
| TEAM_ID / TEAM_NAME | varchar | 구단 코드 / 명 |
| PLAYER_ID_RUN / PLAYER_NAME | varchar | 실행 선수 ID / 명 |
| HALF_TYPE / HALF_TYPE_NAME | numeric / varchar | 전후반 코드 / 명칭 |
| TIME_MIN / TIME_SEC | numeric | 경과 분 / 초 |
| AST_POS / AST_POS_NAME | numeric / varchar | 어시스트 위치 코드 / 명칭 |
| AST_WAY / AST_WAY_NAME | varchar | 어시스트 방법 코드 / 명칭 |
| GOAL_WAY / GOAL_WAY_NAME | varchar | 득점 방법 코드 / 명칭 |
| GOAL_YN / GOAL_TOUCH | char / numeric | 득점 여부(Y/N) / 득점 터치수 |
| FAIL_CD_NAME | varchar | 실패 사유 명칭 |
| X_POS / Y_POS | numeric(7,2) | 경기장 좌표 |
| PLAYER_FORMATION_PLA | varchar(10) | 포메이션 위치 번호 |

### 경기별 교체 — `/api/inOutRecord.do`
> 파라미터에 `team_id` 추가 (game_id는 varchar(3))

| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / TEAM_NM | varchar | 구단 코드 / 명 |
| OUT_PLAYER / OUT_PLAYER_NM | varchar | 교체 OUT 선수 ID / 명 |
| IN_PLAYER / IN_PLAYER_NM | varchar | 교체 IN 선수 ID / 명 |
| HALF_TYPE | numeric | 전후반 구분 |
| TIME_MIN / TIME_SEC / OFFICIAL_TIME | numeric | 교체 분 / 초 / 공식시간 표기 |
| POSITION_CODE / POSITION_NM | numeric / varchar | 포지션 코드 / 명 |

### 경기별 선수 기록 — `/api/matchPlayerRecord.do`
> 모든 지표는 시간대 접두사 변형 존재: (없음)=풀타임, `B_`=전반, `A_`=후반, `EB_`=연장전반, `EA_`=연장후반

| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / HOME_TYPE | varchar | 구단 / 홈어웨이(1H 2A) |
| PLAYER_ID / PLAYER_NAME / BACK_NO | varchar / int | 선수 ID / 명 / 등번호 |
| POSITION_NAME / CAPTAIN_YN | varchar | 포지션 / 주장 여부 |
| GAIN_GOAL / AS_QTY / ATTACK_POINT | int / numeric | 득점 / 도움 / 공격포인트 |
| ST_QTY / VALID_ST_QTY | int | 슈팅 / 유효슈팅 |
| PK_QTY / PK_Y_QTY / PK_N_QTY | int | PK 획득 / 성공 / 실패 |
| TK_L_GOAL / TK_R_GOAL / TK_L_MISS / TK_R_MISS | int | 승부차기 방향별 성공/실패 (좌/우) |
| CK_QTY / FO_QTY / OS_QTY / FS_QTY | int | 코너킥 / 파울 / 오프사이드 / 피파울 |
| WARN_QTY / EXIT_QTY | int | 경고 / 퇴장 |
| CHANGE_QTY / CHANGE_I_QTY / CHANGE_O_QTY | int | 교체 / 투입 / 교체아웃 횟수 |
| CHANGE_I_TIME / CHANGE_O_TIME | numeric | 투입/아웃 시간 |
| CHANGE_PLAYER_ID / CHANGE_PLAYER_NAME | varchar | 교체 상대 선수 ID / 명 |
| PLAYER_POINT / WORK_TIME | numeric / int | 선수 평점 / 출전시간(분) |
| GAINGOAL_PER_STQTY / SELF_GOAL / LOSS_GOAL | numeric / int | 슈팅대비득점율 / 자책골 / 실점(GK) |

### 경기별 승부차기 — `/api/tkRecord.do`
| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / TEAM_NAME | varchar | 구단 코드 / 명 |
| TK_SEQ | int | 키커 순번 |
| PLAYER_ID / PLAYER_NAME | varchar | 선수 ID / 명 |
| GAIN_YN / R_L_TYPE | char | 성공 여부(Y/N) / 주발(R/L) |
| ERR_CAUSE_CODE / ERR_CAUSE_NAME / ERR_CAUSE_NAME_ENG | numeric / varchar | 실축 사유 코드/국문/영문 |
| GOAL_POS / GOAL_POS_NAME / GOAL_POS_NAME_ENG | numeric / varchar | 골 방향 코드/국문/영문 |
| OTHER_GK_ID / OTHER_GK_NAME | varchar | 상대 GK ID / 명 |

### 경기별 관중수 — `/api/audienceInfo01.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| league_gubun | varchar(1) | Y | 대회구분 (1:K1, 2:K2, 3:PO, 4:리그컵, 0:전체) |
| meet_year | varchar(4) | Y | 대회 년도 |
| team_id | varchar(3) | N | 팀 코드 |
| sdate / edate | varchar(10) | N | 시작/종료일 (YYYY/MM/DD) |

| 필드 | 타입 | 설명 |
|---|---|---|
| MEET_NAME / GAME_DATE / FIELD_NAME | varchar | 대회명 / 경기일 / 경기장 |
| HOME_TEAM_NAME / HOME_GAIN_GOAL | varchar / int | 홈팀 / 홈 득점 |
| AWAY_TEAM_NAME / AWAY_GAIN_GOAL | varchar / int | 원정팀 / 원정 득점 |
| AUDIENCE_QTY / AUDIENCE_AWAY_QTY | int | 관중수(유료 합계) / 원정 관중 |
| WEEKEND / NEUTRAL_YN / RANK | varchar / int | 주말 여부 / 중립경기 / 관중 순위 |

### 경기별 선수별 상세기록 v1 (타임시트) — `/api/matchTimeSheet.do`
| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / TEAM_NAME | varchar | 구단 코드 / 명 |
| PLAYER_ID / PLAYER_NAME / PLAYER_NAME_ENG | varchar | 선수 ID / 국문 / 영문 |
| ACT_CODE / ACT_CODE_NAME | numeric / varchar | 경기행동 코드(공통코드 49) / 명 |
| HALF_TYPE / HALF_TYPE_NAME | numeric / varchar | 전후반(공통코드 47) / 명 |
| TIME_MIN / TIME_SEC / OFFICIAL_TIME | numeric | 분 / 초 / 공식시간 표기 |
| MISGOAL_POSI / MISGOAL_POSI_NAME | numeric / varchar | 유효슈팅 구분(공통코드 52) / 명 |
| ACT_POS / ACT_POS_NAME | numeric / varchar | 필드 위치(공통코드 71) / 명 |
| GOAL_YN / PK_YN | char(1) | 득점 / PK 여부 (Y/N) |
| X_POS / Y_POS | numeric(7,2) | 경기장 정밀 좌표 (0,0 원점) |
| RELATION_NO | varchar(12) | 득점 시퀀스 연결 번호 |

### 경기별 선수별 상세기록 v2 — `/api/matchTimeSheet2.do`
| 필드 | 타입 | 설명 |
|---|---|---|
| RECTYPE / GUBUN / SUB_KEY | varchar | 기록유형(goal/warn/inout 등) / 세부구분 / 상세키 |
| TEAM_ID / TEAM_NAME / TEAM_NAME_ENG | varchar | 구단 코드 / 국문 / 영문 |
| PLAYER_ID / PLAYER_NAME / PLAYER_NAME_ENG | varchar | 선수 ID / 국문 / 영문 |
| HALF_TYPE / TIME_MIN / TIME_SEC | numeric | 전후반(공통코드 47) / 분 / 초 |
| REMARK / REMARK_ENG | varchar(500) | 상세 이벤트 기록 (국/영문) |
| ETC1~ETC10 | varchar(30) | 보조 데이터 필드 1~10 |

---

## 4. 순위 / 집계

### 리그별 팀 순위 — `/api/clubRank.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| meet_year | varchar(4) | Y | 대회 년도 |
| meet_seq | varchar(3) | Y | 대회순번 |
| game_type | varchar(1) | Y | 경기 유형 구분 |
| live_yn | varchar(1) | Y | 실시간(Y) / 최종(N) |
| excludingPO | varchar(1) | Y | K2 PO 기록 제외 여부 (Y제외/N포함) |

| 필드 | 타입 | 설명 |
|---|---|---|
| TEAM_ID / TEAM_NAME | varchar | 구단 코드 / 명 |
| RANK / GAIN_POINT | int | 순위 / 승점 |
| WIN_CNT / TIE_CNT / LOSS_CNT | int | 승 / 무 / 패 |
| GAP_CNT / GAIN_GOAL / LOSS_GOAL | int | 득실차 / 득점 / 실점 |
| GAINGOAL_PER_WORKQTY / LOSSGOAL_PER_WORKQTY | numeric(10,5) | 경기당 득점 / 실점 |
| CONTINUE_WINTYPE / WORK_QTY | varchar / int | 연승·연패 상태 / 경기수 |
| GAME_TYPE / GAME_TYPE2 | varchar / int | 경기상태 구분 / 요청 유형 반환값 |

### 리그별 팀 기록 집계 — `/api/clubRecordForMeet.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| meet_year | varchar(4) | Y | 대회 년도 |
| meet_seq | varchar(3) | Y | 대회순번 |

**순위·기본 기록:** TEAM_ID, TEAM_NAME, RANK, GAIN_POINT, WIN/TIE/LOSS_CNT, GAIN/LOSS_GOAL, GAP_CNT, WORK_QTY, CONTINUE_WINTYPE

**기술 지표 합계(`_SUM`):** ST(슈팅), ST_VALID(유효슈팅), FO(파울), CK(코너), OS(오프사이드), WARN/EXIT(경고/퇴장), PASS / PASS_SUCCESS, DRIBBLE / DRIBBLE_SUCCESS, TACKLE / TACKLE_SUCCESS, INTERCEPT, AIR_CHAG(공중볼), CROSS / CROSS_SUCCESS

**경기당 평균(`_AVG`, numeric(6,2)):** 위 항목 전부의 평균 + TEAM_SHARE_AVG(평균 점유율)

---

## 5. 부가 데이터 (고급 트래킹 / `unOfficial` 계열)

### 아디다스 포인트 (라운드) — `/api/unOfficialPointByRound.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| meet_year | varchar(4) | Y | 대회 년도 |
| meet_seq | varchar(3) | Y | 대회순번 |
| round_id | int | Y | 라운드 ID |
| top_rank | int | Y | 출력 순위 제한 (~까지) |

**기본:** TOT_RANK, GAME_TOT_POINT, MEET_YEAR, TEAM_ID, PLAYER_ID, PLAYER_NAME, BACK_NO

**카테고리 합계:** GAME_ATT_POINT(공격), GAME_PAS_POINT(패스), GAME_DEF_POINT(수비), GAME_GKD_POINT(수비+GK), GAME_GKP_POINT(GK), GAME_ETC_POINT(기타)

**세부 항목(numeric(5,0)):**
- *공격:* GOAL, PK_GOAL, OFF_GOAL, SHOT_ON_TARGET, DRIBBLE_SUCCESS, PK_MISS(감점)
- *패스:* ASSIST, PASS_ACC, KEY_PASS, CROSS_ACC
- *수비/GK:* TACKLED, BLOCKING_BALL, INTERCEPT, CHALG_GROUND, CHALG_AIR, PK_GIVE, GOAL_AGAINST, CLEAN_SHEET, CLEARING, GK_PUNCH, GK_CATCH, GK_AIR_CLEAR, GK_PK_SAVE
- *징계/기타:* OWN_GOAL, WIN, LOSE, ACQUIRE, BALL_MISS, YELLOW_CARD, YELLOW_CARD_2, RED_CARD

### 아디다스 포인트 (기간) — `/api/unOfficialPointByDay.do`
| 파라미터 | 타입 | 필수 | 설명 |
|---|---|---|---|
| authKey | varchar | Y | API 인증키 |
| meet_year | varchar(4) | Y | 대회 년도 |
| meet_seq | varchar(3) | Y | 대회순번 |
| top_rank | int | Y | 순위 (~까지) |
| sdate / edate | varchar(10) | Y | 시작/종료일 (yyyy/mm/dd) |
| excludingPO | varchar(1) | N | K2 PO 기록 제외 여부 (Y/N) |

→ 응답 필드는 라운드 버전과 동일 (기간 누적 기준)

### 경기별 팀 기록 (부가) — `/api/unOfficialMatchClubRecord.do`
> 약 98개 필드. 파라미터에 `team_id` 추가

**마스터:** MEET_YEAR, MEET_SEQ, ROUND_ID, GAME_ID, TEAM_ID, TEAM_NM, HOME_TYPE(공통코드 58), HOME_TYPE_NM

**공격/슈팅:** GOAL_CNT, ASSIST_CNT, ST_CNT, ST_VALID_CNT, SHOT, SHOT_ON_TARGET, DEFENDER_BLOCKED_SHOT, SHOOTING_OFF, SHOOTING_IN_PA(PA안), SHOOTING_OUT_PA(PA밖), FREEKICK_SHOT, FREEKICK_SHOT_ON_TARGET

**패스/빌드업:** PASS, PASS_ACC, PASS_ACC_PCNT, FORWARD_PASS(+SUCCESS), TRANSVERSE_PASS(+SUCCESS), SHORT/MEDIUM/LONG_PASS, ATT/MIDDLE/DEFS_AREA_PASS(구간별)

**수비/경합:** TACKLE(+SUCCESS, PCNT), INTERCEPT, CUT_OFF, BLOCKING_SHOT, CHAG(+WON, PCNT), AIR_CHAG(+WON, PCNT)

**GK/징계:** GOAL_CONCEDED, CATCH, PUNCH, GOAL_KICK(+SUCCESS, PCNT), FOUL, WARN_QTY, EXIT_QTY, OS_QTY, FS_QTY, CORNER, THROW_INS, DRIBBLE(+SUCCESS)

### 경기별 선수 기록 (부가) — `/api/unOfficialMatchPlayerRecord.do`
> 약 103개 필드. 파라미터에 `team_id` 추가. 선수 단위로 위 팀 부가데이터 전부 + 아래 추가

**참여:** PLAYER_ID, NAME, BACK_NO, POSITION_CODE/NAME, WORK_TIME(출전분), WORK_QTY(출전여부)

**드리블/키패스:** DRIBBLE(+SUCCESS, PCNT_SUCCESS_DRIBBLE), KEY_PASS, EX_ATT_KEY_PASS_ACC, BACK_PASS

**GK 전용:** GOAL_CONCEDED, SHOT_SAVED(세이브), GOAL_MISTAKE(실책), CATCH, PUNCH, DROPS, GOAL_KICK(+SUCCESS, PCNT)

**경합/수비:** CHALG(+WON, PCNT), AIR_CHALG(+WON, PCNT), TACKLE(+SUCCESS, PCNT), INTERCEPT, CUT_OFF, BLOCKING_SHOT, CLEARING

### 경기별 패스매트릭스 — `/api/unOfficialMatchPassMatrixRecord.do`
> 파라미터에 `team_id` 추가. 패서→리시버 쌍별 패스 네트워크

| 필드 | 타입 | 설명 |
|---|---|---|
| MEET_YEAR / MEET_SEQ / GAME_ID / TEAM_ID | - | 마스터 키 |
| PLAYER_ID / PLAYER_NM | varchar | 패스한 선수(패서) ID / 명 |
| PLAYER_POSITION_CD / PLAYER_POSITION_NM | numeric / varchar | 패서 포지션 코드 / 명 |
| PLAYER_ID_RECEIVED / PLAYER_ID_RECEIVED_NM | varchar | 받은 선수(리시버) ID / 명 |
| PLAYER_RECEIVED_POSITION_CD / _NM | numeric / varchar | 리시버 포지션 코드 / 명 |
| PASS_COUNT | numeric(3,0) | 두 선수 간 성공 패스 횟수 |

---

## 데이터 성격 요약

| 분류 | API | 비고 |
|---|---|---|
| 정적 마스터 | 공통코드, 리그, 구단, 선수, 경기장 | 시즌 단위 갱신 |
| 일정/결과 | 대회 일정, 경기 일반정보, 팀 순위 | |
| 표준 경기 기록 | 팀/선수 기본 스탯, 엔트리, 교체, 세트피스, 승부차기, 관중, 타임시트 | |
| 고급 트래킹 (`unOfficial`) | 팀/선수 부가데이터, 패스매트릭스 | 패스 방향·구간, 성공률, 좌표 등 정밀 분석용 |
| 포인트 시스템 | 아디다스 포인트(라운드/기간) | 행동별 가중 점수 랭킹 |

**시각화 활용:** `XPOS/YPOS`, `X_POS/Y_POS` 좌표가 엔트리·세트피스·타임시트에, 패스 네트워크가 패스매트릭스에 제공되어 슈팅맵·히트맵·패스네트워크 구성 가능.
