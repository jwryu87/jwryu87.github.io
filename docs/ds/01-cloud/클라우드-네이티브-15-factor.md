---
layout: default
title: 클라우드 네이티브 15 Factor
parent: 1. 클라우드
grand_parent: DS (Digital Service)
nav_order: 7
---

# 클라우드 네이티브 15 Factor
{: .fs-8 }

1.1 클라우드 개념
{: .label .label-purple }

---

## 핵심 키워드

`15가지`

> 암기: **코종설B/빌무포동/폐환로관/A관인**

---

## 정의/개념

클라우드 플랫폼 모델에 사용하는 기업들의 개발, 운영, 확장 등을 관찰한 **Heroku 기업에서 작성한 클라우드 네이티브 애플리케이션 개발 방법론**

---

## 15 Factor

### 원본 12 Factors

| No | 방법론 | 설명 | 중요도 |
|:--:|:-------|:-----|:------:|
| 1 | 코드 베이스 (One Code, One App) | 버전 관리되는 하나의 코드 베이스와 다양한 배포 | Non-negotiable |
| 2 | 종속성 (Dependency Management) | 명시적으로 선언되고 분리된 종속성 기반의 개발 | High |
| 3 | 설정 (Configuration, Credentials) | 코드로부터 분리된 배포환경에 저장되는 설정 (Sprint Cloud config) | Medium |
| 4 | Back-end 서비스 (Backing Services) | Config에 백엔드 서비스 URL 저장, 연결 리소스 취급 | High |
| 5 | 빌드, 릴리즈, 실행 (Build, Release, Run) | 철저하게 분리된 Build, Release Run 단계 개발 | High |
| 6 | 무상태 프로세스 (Stateless Process) | App, 하나 이상 프로세스 실행, 해당 프로세스 메모리 파일 공유 불가 | High |
| 7 | 포트 바인딩 (Port Binding) | 배포된 App을 타 App에 접근 가능, 포트 바인딩 통한 서비스 공개 | Medium |
| 8 | 동시성 (Concurrency) | App 수평 확장 기능 및 Process Model 의한 동시성 상성 제공 | - |
| 9 | 폐기 가능 (Disposability) | Process의 빠른 시작, 종료 통한 안정성 극대화 | Medium |
| 10 | 개발, 프로덕션 환경 일치 (Environment Parity) | 개발, 스테이징, 프로덕션 환경 최대한 일치 유지 | Medium |
| 11 | 로그 (Logs) | App에 영향을 받지 않기 위해 Log를 Stream 위주, 별도 저장 보관 관리 | Low |
| 12 | 관리 프로세스 (Administrative Process) | 관리와 유지보수에 관련된 작업을 단일 Process로 진행 | High |

### 추가 3 Factors (Beyond 12 Factors)

| No | 방법론 | 설명 | 특징 |
|:--:|:-------|:-----|:-----|
| 13 | API 우선 (API First) | API 설계 우선시하여, 코드 작성 이전에 서비스 의도와 기능 명확화 | Web, Mobile, 타 서비스 연계 기능 |
| 14 | 관측 (Telemetry) | 애플리케이션 성능 모니터링, 비즈니스 차원 예측 분석 위한 관측 | 이벤트 관측, 데이터 관측 |
| 15 | 인증과 권한 (Authentication and Authorization) | 애플리케이션 리소스에 대한 요청에 대해 역할 및 권한 부여 결정 | 요청 관리, 수정 관리 관련 |

> 계번 오프만은 3가지의 새로운 내용 (API 우선, 관측, 인증과 권한)을 추가한 12 Factors의 후속버전을 변경한 15 Factors 제안

---

## 클라우드 네이티브 애플리케이션 개발 방법론

클라우드 네이티브 애플리케이션 개발 방법론 통합 구축을 통해 **Lock-in 탈피**, **EU GDPR 보장 기준 충족**

---

## 관련 개념

- [클라우드 네이티브](/docs/ds/01-cloud/클라우드-네이티브)
- [클라우드 컴퓨팅](/docs/ds/01-cloud/클라우드-컴퓨팅)

---

## 학습 체크리스트

- [ ] 15 Factor 정의 이해
- [ ] 원본 12 Factors 암기 (코종설B/빌무포동/폐환로관)
- [ ] 추가 3 Factors 암기 (A관인: API, 관측, 인증)
- [ ] 각 Factor별 중요도 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료
- Heroku 12 Factor App
