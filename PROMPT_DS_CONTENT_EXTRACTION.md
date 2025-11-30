# DS 토픽 내용 추출 및 작성 프롬프트

## 작업 목표
DS (Digital Service) 학습 자료의 PDF 이미지에서 내용을 추출하여 Jekyll 마크다운 파일에 구조화된 형식으로 작성합니다.

## 현재 진행 상황
- ✅ 완료: 약 34개 토픽 (01. 클라우드 ~ 07. 가상화/컨테이너 일부)
- ⏳ 진행 중: 나머지 약 40개 토픽
- 📁 이미지 위치: `/Users/jaewoo.ryu/woowa/dev/jwryu87.github.io/assets/jpeg/DS/`
- 📁 마크다운 위치: `/Users/jaewoo.ryu/woowa/dev/jwryu87.github.io/docs/ds/`

## 작업 방법

### 1. 이미지 읽기
```python
# 예시: 4개씩 배치로 읽기
read_file("assets/jpeg/DS/DS_045.jpg")
read_file("assets/jpeg/DS/DS_046.jpg")
read_file("assets/jpeg/DS/DS_047.jpg")
read_file("assets/jpeg/DS/DS_048.jpg")
```

### 2. 내용 추출 및 구조화
이미지에서 다음 정보를 추출:
- **핵심 키워드**: 주요 기술 용어들
- **정의/개념**: 토픽의 핵심 정의
- **특징/기술요소**: 표 형식으로 정리
- **구성요소**: 아키텍처, 메커니즘 등
- **암기법(두음매직)**: 있으면 포함
- **비교표**: 다른 기술과의 비교 (있는 경우)

### 3. 마크다운 파일 작성 형식

#### 기본 구조
```markdown
---
layout: default
title: [토픽명]
parent: [카테고리명]
grand_parent: DS (Digital Service)
nav_order: [순서]
---

# [토픽명]
{: .fs-8 }

[소분류] (예: 3.1 블록체인 기본)
{: .label .label-purple }

> 암기: **[두음매직]** (있는 경우)

---

## 핵심 키워드

`키워드1` `키워드2` `키워드3`

---

## 정의/개념

[핵심 정의]

---

## [주요 섹션]

[표 형식으로 정리]

---

## 연계 토픽

- [관련 토픽](/docs/ds/...)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료
```

#### 표 작성 규칙
- **구분/카테고리** 컬럼은 첫 번째 컬럼
- **설명** 컬럼은 마지막에 배치
- 복잡한 내용은 `<br>`로 줄바꿈
- 예시:
```markdown
| 구분 | 요소 | 설명 |
|:-----|:-----|:-----|
| **특징** | 복제성 | 물리 모델을 사이버에 그대로 구현 |
```

### 4. 파일명 매핑 규칙
- 이미지 번호와 실제 토픽 파일명은 다를 수 있음
- 이미지 내용을 보고 적절한 파일을 찾아야 함
- 예: "IaC" → `docs/ds/23-infra/iac.md`
- 예: "IoT" → `docs/ds/08-iot/iot.md`
- 예: "NB-IoT" → `docs/ds/08-iot/nb-iot.md`
- 예: "UAM" → `docs/ds/09-drone-uam/uam.md`

### 5. 카테고리별 디렉토리 구조
```
docs/ds/
├── 01-cloud/
├── 02-xr-metaverse/
├── 03-blockchain/
├── 04-autonomous/
├── 05-smart-factory/
├── 06-smart-grid/
├── 07-virtualization/
├── 08-iot/
├── 09-drone-uam/
├── 10-healthcare/
├── 11-distributed/
├── 12-ui-ux/
├── 13-api/
├── 14-spatial/
├── 15-design-thinking/
├── 16-e-gov/
├── 17-gartner/
├── 18-etc/
├── 19-robot/
├── 20-recommendation/
├── 21-vision/
├── 22-finops/
├── 23-infra/
└── 24-web/
```

## 작업 예시

### 예시 1: IaC (Infrastructure as Code)
**이미지**: `DS_049.jpg`
**파일**: `docs/ds/23-infra/iac.md`

**작성 내용**:
- 정의: "인프라 구성을 마치 소프트웨어를 프로그래밍하는 것처럼 스크립트를 사용하여 처리하는 방식"
- 메커니즘: code → Version Control → code review → integrate → deploy
- 구성요소: Bootstrap (Vagrant, Docker, CLI), Configuration (Chef, Puppet, Ansible), Orchestration (SaltStack, Jenkins+Fabric)

### 예시 2: IoT
**이미지**: `DS_050.jpg`
**파일**: `docs/ds/08-iot/iot.md`

**작성 내용**:
- 정의: "센서, 네트워크, 인터페이스 모든 사물 연결 제공 기술"
- 3대 핵심 기술: 센싱기술, 유무선 통신, IoT 서비스 인터페이스 기술
- 메커니즘: IoT 디바이스 → IoT 네트워크 → IoT 플랫폼 → IoT 서비스

### 예시 3: NB-IoT
**이미지**: `DS_051.jpg`
**파일**: `docs/ds/08-iot/nb-iot.md`

**작성 내용**:
- 정의: "LPWA 네트워크 실현, 15km 커버리지, 200KHz 대역폭, 100kbps 속도 IoT 기술"
- 스펙: Coverage ~15Km, 배터리 수명 ~10년, 디바이스 수용 5만개 이상
- 운영모드: Standalone, Guard-band, In-band

### 예시 4: UAM
**이미지**: `DS_052.jpg`
**파일**: `docs/ds/09-drone-uam/uam.md`

**작성 내용**:
- 정의: "수직 이착륙(V-TOL)이 가능한 개인항공기(PAV)와 목적 기반 모빌리티(PVB)를 이용하는 하늘을 이동 통로로 활용하는 미래의 도시 교통 체계"
- 기술요소: 기체/부품, 항행 교통관리, 인프라, 서비스, 비행기술

## 주의사항

1. **파일명 확인**: 이미지 내용을 보고 정확한 파일을 찾아야 함
2. **링크 경로**: 연계 토픽 링크는 `/docs/ds/...` 형식으로 작성
3. **표 형식**: 복잡한 내용도 표로 구조화
4. **암기법**: "두음매직"이 있으면 반드시 포함
5. **라벨 색상**: 
   - `.label-purple`: 기본 토픽
   - `.label-green`: 활용/서비스
   - `.label-yellow`: 기술/표준
   - `.label-blue`: 개념/이론

## 작업 순서

1. 4개씩 이미지 읽기
2. 각 이미지에서 내용 추출
3. 해당하는 마크다운 파일 찾기
4. 구조화된 형식으로 작성
5. 4개 완료 후 커밋 (선택사항)

## 커밋 메시지 형식

```bash
git add docs/
git commit -m "Content: DS 토픽 N개 추가 ([카테고리명])

- [토픽1]
- [토픽2]
- [토픽3]
..."
```

## 시작 명령어

다음 명령어로 시작하세요:

```python
# 다음 이미지들 읽기
read_file("assets/jpeg/DS/DS_049.jpg")  # IaC
read_file("assets/jpeg/DS/DS_050.jpg")  # IoT
read_file("assets/jpeg/DS/DS_051.jpg")  # NB-IoT
read_file("assets/jpeg/DS/DS_052.jpg")  # UAM
```

그리고 각각의 내용을 추출하여 해당 마크다운 파일에 작성하세요.

