# 블로그 메뉴 구조 및 페이지 생성 프롬프트

## 작업 목표

Confluence 위키의 토픽 목록을 기반으로 Jekyll 블로그에 계층적 메뉴 구조와 개별 토픽 페이지를 자동 생성합니다.

---

## [설정 섹션] - 주제별 커스터마이징

### 기본 설정

```yaml
# 주제 정보 (아래 값을 변경하세요)
SUBJECT_CODE: "SW"                     # 예: DS, AI, SEC, NW, SW, DB
SUBJECT_NAME: "소프트웨어공학"          # 한글 주제명
SUBJECT_NAME_FULL: "SW (소프트웨어공학)" # 전체 표시명
NAV_ORDER: 3                           # 네비게이션 순서 (DS=2, SW=3, AI=4, SEC=5...)

# 경로 설정
BLOG_ROOT: "/Users/jaewoo.ryu/woowa/dev/jwryu87.github.io"
DOCS_PATH: "{{BLOG_ROOT}}/docs/{{SUBJECT_CODE_LOWER}}/"

# Confluence 페이지 정보
CONFLUENCE_PAGE_ID: "898702097"        # 토픽 목록이 있는 페이지 ID
CONFLUENCE_URL: "https://cloud.wiki.woowa.in/wiki/..."
```

---

## 작업 순서

### Step 1: Confluence 페이지 읽기

```
Confluence 페이지를 읽어서 토픽 구조를 파악합니다.

명령: confluence_get_page(page_id="{{CONFLUENCE_PAGE_ID}}")
```

### Step 2: 토픽 구조 분석

Confluence 테이블에서 다음 정보를 추출:
- **상위 토픽**: 1차 카테고리 (예: 1. 소프트웨어 안전)
- **중위 토픽**: 2차 카테고리 (예: 1.1 소프트웨어 안전 개념)
- **하위 토픽**: 실제 페이지 (예: FMEA, FTA, HAZOP)

### Step 3: 디렉토리 구조 설계

```
docs/{{SUBJECT_CODE_LOWER}}/
├── index.md                    # 메인 인덱스 (전체 토픽 목록)
├── 01-카테고리1/
│   ├── index.md               # 카테고리 인덱스
│   ├── topic1.md
│   └── topic2.md
├── 02-카테고리2/
│   ├── index.md
│   └── ...
└── ...
```

### Step 4: 파일명 규칙

| 원본 토픽명 | 파일명 변환 규칙 |
|:-----------|:----------------|
| 한글 토픽 | 영문 소문자 + 하이픈 |
| 영문 토픽 | 소문자 변환 |
| 특수문자 | 제거 또는 하이픈 |
| 공백 | 하이픈(-) |

예시:
- "소프트웨어 안전" → `sw-safety`
- "ISO 26262" → `iso-26262`
- "CI/CD" → `ci-cd`
- "품질보증(QA)" → `qa`

---

## 파일 템플릿

### 1. 메인 index.md

```markdown
---
layout: default
title: {{SUBJECT_NAME_FULL}}
nav_order: {{NAV_ORDER}}
has_children: true
permalink: /docs/{{SUBJECT_CODE_LOWER}}
---

# {{SUBJECT_NAME_FULL}}

{{SUBJECT_NAME}} 관련 학습 자료입니다. 총 **N개** 항목

---

## 1. 카테고리명 (N개)

| 구분 | 토픽 |
|:-----|:-----|
| 1.1 소분류 | [토픽1](/docs/{{SUBJECT_CODE_LOWER}}/01-category/topic1) \| [토픽2](/docs/{{SUBJECT_CODE_LOWER}}/01-category/topic2) |
| 1.2 소분류 | [토픽3](/docs/{{SUBJECT_CODE_LOWER}}/01-category/topic3) |

---

## 2. 카테고리명 (N개)

...
```

### 2. 카테고리 index.md

```markdown
---
layout: default
title: N. 카테고리명
parent: {{SUBJECT_NAME_FULL}}
nav_order: N
has_children: true
permalink: /docs/{{SUBJECT_CODE_LOWER}}/NN-category
---

# 카테고리명

카테고리 설명...

---

## N.1 소분류

| 토픽 | 설명 |
|:-----|:-----|
| [토픽명](/docs/{{SUBJECT_CODE_LOWER}}/NN-category/topic) | 간단 설명 |

---

## N.2 소분류

...
```

### 3. 토픽 페이지 템플릿

```markdown
---
layout: default
title: 토픽명
parent: N. 카테고리명
grand_parent: {{SUBJECT_NAME_FULL}}
nav_order: N
---

# 토픽명
{: .fs-8 }

N.N 소분류
{: .label .label-purple }

---

## 핵심 키워드

`키워드1` `키워드2` `키워드3`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 {{SUBJECT_NAME}} 학습자료
```

---

## 라벨 색상 가이드

| 색상 | 용도 | 예시 |
|:-----|:-----|:-----|
| `.label-purple` | 기본/핵심 개념 | 1.1 기본 개념 |
| `.label-yellow` | 표준/기법 | 1.2 안전 표준 |
| `.label-green` | 응용/활용 | MSA 패턴 |
| `.label-blue` | 이론/원리 | 아키텍처 기타 |
| `.label-red` | 보안/위험 | 취약점 |

---

## 실행 명령어

### 전체 구조 생성 요청

```
Confluence 페이지 {{CONFLUENCE_URL}}의 토픽 목록을 읽어서
{{SUBJECT_NAME_FULL}} 블로그 메뉴와 페이지를 만들어줘.

설정:
- 주제 코드: {{SUBJECT_CODE}}
- 주제명: {{SUBJECT_NAME_FULL}}
- nav_order: {{NAV_ORDER}}
- 경로: docs/{{SUBJECT_CODE_LOWER}}/
```

### 예시 명령어

```
# SW 주제
Confluence 페이지 https://cloud.wiki.woowa.in/wiki/spaces/~jaewoo.ryu/pages/898702097/SW 의 
토픽 목록을 읽어서 SW (소프트웨어공학) 블로그 메뉴와 페이지를 만들어줘.

# AI 주제
Confluence 페이지 https://cloud.wiki.woowa.in/wiki/spaces/~jaewoo.ryu/pages/XXXXXX/AI 의 
토픽 목록을 읽어서 AI (인공지능) 블로그 메뉴와 페이지를 만들어줘.

# SEC 주제
Confluence 페이지 https://cloud.wiki.woowa.in/wiki/spaces/~jaewoo.ryu/pages/XXXXXX/SEC 의 
토픽 목록을 읽어서 SEC (보안) 블로그 메뉴와 페이지를 만들어줘.
```

---

## 주제별 설정 템플릿

### DS (디지털서비스)
```yaml
SUBJECT_CODE: "DS"
SUBJECT_NAME: "디지털서비스"
SUBJECT_NAME_FULL: "DS (Digital Service)"
NAV_ORDER: 2
```

### SW (소프트웨어공학)
```yaml
SUBJECT_CODE: "SW"
SUBJECT_NAME: "소프트웨어공학"
SUBJECT_NAME_FULL: "SW (소프트웨어공학)"
NAV_ORDER: 3
```

### AI (인공지능)
```yaml
SUBJECT_CODE: "AI"
SUBJECT_NAME: "인공지능"
SUBJECT_NAME_FULL: "AI (인공지능)"
NAV_ORDER: 4
```

### SEC (보안)
```yaml
SUBJECT_CODE: "SEC"
SUBJECT_NAME: "보안"
SUBJECT_NAME_FULL: "SEC (정보보안)"
NAV_ORDER: 5
```

### NW (네트워크)
```yaml
SUBJECT_CODE: "NW"
SUBJECT_NAME: "네트워크"
SUBJECT_NAME_FULL: "NW (네트워크)"
NAV_ORDER: 6
```

### DB (데이터베이스)
```yaml
SUBJECT_CODE: "DB"
SUBJECT_NAME: "데이터베이스"
SUBJECT_NAME_FULL: "DB (데이터베이스)"
NAV_ORDER: 7
```

---

## 주의사항

1. **파일명 일관성**: 모든 파일명은 영문 소문자와 하이픈만 사용
2. **링크 경로**: `/docs/{{SUBJECT_CODE_LOWER}}/...` 형식 사용
3. **nav_order**: 카테고리/토픽 순서대로 번호 부여
4. **parent/grand_parent**: 계층 구조에 맞게 정확히 지정
5. **라벨**: 소분류에 맞는 색상 사용

---

## 작업 완료 후

1. `jekyll serve`로 로컬에서 확인
2. 메뉴 구조 및 링크 정상 동작 확인
3. git commit 및 push

```bash
cd {{BLOG_ROOT}}
git add docs/{{SUBJECT_CODE_LOWER}}/
git commit -m "Structure: {{SUBJECT_NAME_FULL}} 블로그 구조 생성 (N개 카테고리, M개 토픽)"
git push
```

