---
layout: default
title: MSA (Micro Service Architecture)
parent: 4. 아키텍처
grand_parent: SW (소프트웨어공학)
nav_order: 1
---

# MSA (Micro Service Architecture)
{: .fs-8 }

4.1 아키텍처 패턴
{: .label .label-purple }

---

## 핵심 키워드

`Client Layer(Rest API, Orchestration)` `Application Layer(API G/W, Containerization)` `Persistence Layer(Polyglot, 대용량 분산 DB)`

---

## 정의/개념

서비스 단위의 독립적인 세부단위로 분할해 작은 애플리케이션으로 쪼개어 변경/조합이 가능하도록 만든 아키텍처

---

## 개념/기술요소

### MSA(Micro Service Architecture)의 개요

| 구분 | 설명 |
|:-----|:-----|
| **개념** | 서비스 단위의 독립적인 세부단위로 분할해 작은 어플리케이션으로 쪼개어 변경/조합이 가능하도록 만든 아키텍처 |

### MSA의 기술요소

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **Client Layer** | Rest API | 자원에 대해서 HTTP기반 경량 프로토콜로 응답/요청 가능 |
| | Orchestration | 이전 시스템의 구축된 서비스의 API 재활용하여 적용 가능 |
| **Application Layer** | API GW | 요청/응답에 대한 서비스 관리 트래픽 제어, 권한 부여 |
| | Containerization | 환경과 인프라 종속탈피, 트래픽에 따른 Auto Scaling 지원 |
| **Persistence Layer** | Polyglot | 각 시스템에 적합한 개발언어 및 DB를 사용이 가능 |
| | 대용량 분산 DB | 성능/안전성 극대화된 DB 사용, 대용량/고성능 트랜잭션 처리 |

- MSA의 원칙인 자율성, 회복성, 투명성, 자동화, 동기화 기반하여 구축 필요
- MSA와 SOA는 유사하지만 목적, 조직, 아키텍처 등의 측면에서 차이점 존재

---

## 비교

### SOA와 MSA 상세 비교

| 비교 항목 | SOA (Service Oriented Architecture) | MSA (Micro Service Architecture) |
|:---------|:-----------------------------------|:---------------------------------|
| **목적** | 비즈니스 로직에 대한 재사용을 통한 비즈니스 민첩성 확보(재사용) | 빠른 배포 및 개발 적용을 통한 비즈니스 민첩성 확보(배포와 적용) |
| **조직** | 조직과 서비스의 연관 관계가 없음 | 서비스 단위와 업무 조직 단위의 연계<br>(콘웨이 법칙, Conway's law) |
| **아키텍처** | 전사적, 분산, 모놀리식(Monolithic) 아키텍처 | 표준 정책 기반 프로젝트 중심 아키텍처<br>서비스 별 독립적인 아키텍처 구성 |
| **서비스** | 전체 서비스 단위로 배포<br>서비스 도출 시 재사용이 가장 우선 순위로 선정 | 업무 간의 독립성이 가장 우선 순위로 평가되는 서비스<br>서비스 단위라는 큰 개념 |
| **관계** | 수평적 분해된 관계 | 수직적 분해된 관계 |
| **중계** | ESB(Enterprise Service bus) | API Gateway |
| **기반기술** | ESB라는 제품과 이를 공급하는 벤더 기반으로 전개<br>SOAP, WDSL, UDDI<br>XML | 글로벌 서비스 업체들의 자신 서비스 확장하는 과정에서 진화<br>REST, CQRS, Containerization<br>JSON, XML |
| **적용대상** | B2B기반 엔터프라이즈 시스템<br>크고 복잡한 비즈니스 어플리케이션 적용 | B2C기반 대용량 분산 웹서비스<br>작은 단위로 세분화된 개별 시스템 |

- SOA와 MSA는 각 각의 서비스는 다른 서비스에 대한 의존성이 최소화되어 구현 필요하고 서비스별 개별 배포 가능

---

## 연계 토픽

- [SOA](/docs/sw/04-architecture/soa)
- [CQRS](/docs/sw/04-architecture/cqrs)
- [SAGA](/docs/sw/04-architecture/saga)
- [Service Mesh](/docs/sw/04-architecture/service-mesh)

---

## 학습 체크리스트

- [ ] MSA 정의 및 개념 이해
- [ ] 3개 Layer별 기술요소 이해
- [ ] SOA vs MSA 비교 이해
- [ ] 콘웨이 법칙(Conway's law) 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

