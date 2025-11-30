# 정보관리기술사 학습 시스템 가이드

## 📚 개요

이 Jekyll 블로그에 정보관리기술사(PE) 학습을 위한 섹션이 추가되었습니다.

## 🏗️ 구조

```
jwryu87.github.io/
├── _config.yml                 # PE 메뉴 추가됨
├── pe.md                        # PE 메인 페이지
├── _posts/
│   └── pe/
│       ├── database/            # 데이터베이스
│       ├── software-engineering/# 소프트웨어공학
│       ├── system-architecture/ # 시스템 아키텍처
│       ├── information-security/# 정보보안
│       ├── new-technology/      # 신기술
│       ├── network/             # 네트워크
│       ├── project-management/  # 프로젝트관리
│       └── data-science/        # 데이터사이언스
└── PE_README.md                 # 이 파일
```

## 📝 포스트 작성 방법

### 1. 파일 위치
`_posts/pe/{카테고리}/YYYY-MM-DD-제목.md` 형식으로 작성

### 2. Front Matter 형식
```yaml
---
layout: post
title: (PE) 제목
date: 2025-01-01 10:00:00 +09:00
categories: pe
tags: [pe, 태그1, 태그2]
comments: true
---
```

### 3. 포스트 구조 권장사항

```markdown
# 주제명

## 개념
간단한 정의

<!-- more -->  ← 이 위까지가 미리보기

## 상세 내용
### 소제목 1
내용...

### 소제목 2
내용...

## 실무 적용 사례
실제 예시...

## 주의사항
주의할 점...

## 관련 개념
- 관련 주제1
- 관련 주제2

---

**학습 체크리스트:**
- [ ] 항목1
- [ ] 항목2
```

## 🚀 로컬 실행 방법

### 1. 의존성 설치
```bash
cd /Users/jaewoo.ryu/woowa/dev/pe-study
bundle install
```

### 2. 서버 실행
```bash
bundle exec jekyll serve
```

### 3. 브라우저에서 확인
```
http://localhost:4000
```

## 📖 사용 가이드

### 새 포스트 작성하기

1. **카테고리 선택**: `_posts/pe/` 아래 적절한 폴더 선택

2. **파일 생성**: 
```bash
# 예시
touch _posts/pe/database/2025-01-15-transaction-isolation.md
```

3. **내용 작성**: Front Matter + 본문 작성

4. **로컬 확인**: Jekyll 서버로 확인

5. **커밋 & 푸시**:
```bash
git add .
git commit -m "Add: 트랜잭션 격리 수준 정리"
git push origin main
```

### 카테고리별 주제 추천

#### Database
- 정규화/반정규화
- 인덱스 설계
- 트랜잭션 관리
- 쿼리 최적화
- NoSQL vs RDBMS

#### Software Engineering
- 디자인 패턴
- 개발 방법론 (Agile, Waterfall)
- 테스트 전략
- 리팩토링
- 코드 품질

#### System Architecture
- 마이크로서비스
- 클라우드 아키텍처
- 로드밸런싱
- 캐싱 전략
- 메시지 큐

#### Information Security
- 인증/인가
- 암호화
- 보안 위협 및 대응
- 네트워크 보안
- 보안 아키텍처

#### New Technology
- AI/ML 개념
- 빅데이터
- 블록체인
- IoT
- 컨테이너/쿠버네티스

## 🎯 학습 전략

### 1. 일일 학습 루틴
1. 새로운 주제 학습
2. Jekyll 포스트로 정리
3. 로컬에서 확인
4. GitHub에 푸시
5. 블로그에서 복습

### 2. 주간 복습
- PE 메인 페이지에서 이번 주 작성한 포스트 리뷰
- 태그별로 관련 주제 함께 복습

### 3. 모의고사 전 복습
- 카테고리별로 중요 포스트 선별
- PDF로 출력하여 하드카피 제작
- 체크리스트 활용

## 🔧 유용한 스크립트

### 새 포스트 템플릿 생성 스크립트

`scripts/new_post.sh` 생성:
```bash
#!/bin/bash
# 사용법: ./scripts/new_post.sh database "트랜잭션 격리수준"

CATEGORY=$1
TITLE=$2
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)
FILENAME="${DATE}-${TITLE// /-}.md"
FILEPATH="_posts/pe/${CATEGORY}/${FILENAME}"

cat > "$FILEPATH" << EOF
---
layout: post
title: (PE) ${TITLE}
date: ${DATE} ${TIME} +09:00
categories: pe
tags: [pe, ${CATEGORY}]
comments: true
---

# ${TITLE}

## 개념

<!-- more -->

## 상세 내용

## 관련 개념

---

**학습 체크리스트:**
- [ ] 
EOF

echo "Created: ${FILEPATH}"
```

## 📊 진행 상황 추적

### Git 커밋 메시지 컨벤션
```
Add: 새로운 주제 추가
Update: 기존 내용 보완
Fix: 오류 수정
Refactor: 구조 개선
```

### 학습 로그 남기기
매주 작성한 포스트 수와 주요 학습 내용을 `pe.md`에 업데이트

## 🎓 추가 기능 아이디어

### 1. AI 요약 스크립트 (향후 구현)
- OpenAI API를 활용한 자동 요약
- 핵심 키워드 추출
- 퀴즈 문제 생성

### 2. PDF 생성 (향후 구현)
- 카테고리별 PDF 출력
- 암기장 레이아웃
- 체크리스트 포함

### 3. 복습 스케줄러 (향후 구현)
- 간격 반복 학습 알고리즘
- 복습 알림
- 학습 통계

## 📱 모바일 접근

블로그는 반응형으로 되어 있어 모바일에서도 잘 보입니다:
- `https://jwryu87.github.io/pe/`

## 🔗 유용한 링크

- **Jekyll 문서**: https://jekyllrb.com/
- **Markdown 가이드**: https://www.markdownguide.org/
- **Front Matter 참고**: https://jekyllrb.com/docs/front-matter/

## 💡 팁

1. **이미지 추가**: `assets/` 폴더에 이미지 저장 후 `![설명]({{ site.url }}/assets/이미지.png)` 형식으로 참조

2. **코드 하이라이팅**: 
```python
def hello():
    print("Hello PE!")
```

3. **표 작성**:
```markdown
| 항목 | 설명 |
|------|------|
| A    | 설명A |
| B    | 설명B |
```

4. **수식 지원** (필요시 MathJax 추가):
```
$$E = mc^2$$
```

---

**문의사항**: jwryu87@gmail.com


