---
layout: default
title: SW 아키텍처 패턴/스타일
parent: 4. 아키텍처
grand_parent: SW (소프트웨어공학)
nav_order: 4
---

# SW 아키텍처 패턴/스타일
{: .fs-8 }

4.1 아키텍처 패턴
{: .label .label-purple }

---

## 정의/개념

시스템 개발 효율성 향상, 아키텍처 반복 문제 해결, 품질 속성 달성 설계방법 기술 패턴

---

## 소프트웨어 아키텍처 스타일 유형

| 아키텍처 스타일 | 패턴 | 설명 |
|:---------------|:-----|:-----|
| **Blackboard** | Knowledge Source, Blackboard, Control | - blackboard: 솔루션에서 가져온 객체를 보유한 구조화된 전역메모리<br>- knowledge source: 각각의 표현 기술<br>- control: 선택, 설정, 실행모듈 |
| **Repository** | Data Store, Components | - 데이터 출처와 관계없이 동일 인터페이스로 데이터에 접근하는 패턴<br>- 도메인과 데이터 사이를 중계하는 매핑레이어 |
| **Layered Architecture** | Layer n, Layer n-1, Layer 1 | - N-tier 아키텍처 스타일<br>- Presentation layer<br>- Application layer<br>- Business logic layer<br>- Data Access layer |
| **Micro Service Architecture** | Service 단위 분리 | - 각 응용프로그램을 독립적으로 배치 가능한 서비스 단위로 분리하고, 이들의 조합으로 시스템을 구성하는 아키텍처 스타일<br>- REST API를 이용하여 Micro service와 API Gateway간 통신 |
| **Micro Kernel(Plug-in)** | Core, Plug-ins | - 자주 사용되는 모듈을 Micro kernel로 집합, 추가 기능 및 서비스는 plug-in 형태로 제공 |
| **Master and Slave** | Master, Slave 1~N | - 마스터 컴포넌트는 일을 분산시키고 Salve 컴포넌트가 반환하는 결과값들을 종합하여 처리 |
| **Pipe and Filter** | Source, Filter 1~N, Sink | - 각 처리 과정은 필터 컴포넌트에서 종료, 처리될 데이터는 파이프를 통해 전달 |
| **Batch Process** | 순차적 처리 | - 빅데이터를 일괄적으로 처리할 수 있는 단위로 구분하여 순차적으로 데이터를 처리 |
| **MVC Pattern** | Model, View, Controller | - 사용자 인터페이스로부터 비즈니스 로직을 분리하여 상호 영향 최소화<br>- model: 데이터와 핵심기능 포함<br>- view: 사용자에게 정보 표현<br>- controller: 사용자 입력 처리 |
| **Peer to Peer** | Peer (Client and Server) | - 각 peer는 클라이언트처럼 다른 peer에게 서비스 요청<br>- 각 peer는 서버처럼 다른 peer에게 서비스 제공 |
| **Event-bus Pattern** | Source 1~N, Channel 1~N, Listener 1~N | - 이벤트 소스, 이벤트 리스너<br>이벤트 채널, 이벤트 버스<br>- 소스는 채널의 이벤트 버스를 통해 메시지 전달, 리스너들은 채널 구독 |
| **Broker** | Client, Broker, Server 1~N | - 서버의 서비스 정보를 broker에 제공<br>- 클라이언트는 broker에게 서비스요청<br>- broker는 통칭된 서버에 정렬함<br>- 서버 응답(이벤트와 콜백)은 클라이언트 |
| **Client and Server** | Client, Server | - 클라이언트는 서버에게 서비스를 요청하고 서버는 관련된 서비스를 클라이언트에게 제공 |

- 각 스타일 별로 구체적인 구현상의 제약사항이나 요구사항 변경에 대응하는 방법을 제시하여 생산성 향상과 안정적인 아키텍처 제공

---

## 연계 토픽

- [SW 아키텍처 스타일, 디자인 패턴 비교](/docs/sw/04-architecture/architecture-pattern-comparison)
- [MSA](/docs/sw/04-architecture/msa)
- [Clean Architecture](/docs/sw/04-architecture/clean-architecture)

---

## 학습 체크리스트

- [ ] 주요 아키텍처 패턴/스타일 종류 이해
- [ ] 각 패턴별 특징 및 구성요소 이해
- [ ] 적용 시나리오 파악

---

## 참고자료

- 정보관리기술사 SW 학습자료

