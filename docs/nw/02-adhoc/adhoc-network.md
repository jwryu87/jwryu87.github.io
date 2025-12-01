---
layout: default
title: Ad-hoc Network
parent: 2. Ad-hoc
grand_parent: NW (네트워크)
nav_order: 1
---

# Ad-hoc Network
{: .fs-8 }

2.1 드론
{: .label .label-purple }

---

## 핵심 키워드

`Proactive(Table Driven)` `Reactive(On-Demand Driven)` `Hybrid` `FANET`

---

## 정의/개념

**인프라 미존재**, 각 단말기 상호 라우팅 데이터 송신 가능 **자율적 네트워크**

---

## 라우팅 프로토콜 유형

| 구분 | 프로토콜 | 설명 |
|:-----|:---------|:-----|
| **Proactive**<br>(Table Driven) | DSDV | - Destination Sequenced Distance Vector<br>- 목적지 순차 번호를 사용하여 루프 발생 방지<br>- Bellman-Ford 알고리즘 구현 |
| | WRP | - Wireless Routing Protocol<br>- 라우팅 정보를 이웃 노드에게만 전송, 오버헤드 감소 |
| **Reactive**<br>(On-Demand Driven) | AODV | - Ad-Hoc On-demand Vector<br>- 목적지 순차번호 사용<br>- DSR과 유사한 루트 탐색 절차 |
| | DSR | - Dynamic Source Routing<br>- 소스 라우팅 방식에 기초<br>- 모든 노드는 루트 캐시를 유지 |
| | ABR | - Associativity Based Long-lived Routing<br>- 경로의 지속성을 고려한 라우팅<br>- 가장 작은 홉수 루트보다 가장 오랫동안 유지될 수 있는 루트 선택<br>- 이동성 적은 노드로 구성 |
| **Hybrid** | ZRP | - Zone Routing Protocol<br>- 동일 영역 내에서는 Proactive 기반 IARP(IntrAzone)<br>- 외부 영역 탐색은 Reactive 기반 IERP(IntErzone) |

---

## 네트워크 구축 유형

### 가. Multi-Hop 네트워크

| 항목 | 설명 |
|:-----|:-----|
| **개념** | 메시지가 송신 노드 로부터 직접적으로 최종 목적 노드로 전달되는 것이 아니라 1개 이상의 중간 노드를 경유하는 전송 방식 |
| **MAC** | DCF: Distributed Coordination Function |
| **장점** | 넓은 지유도, 이동성 우수 |
| **단점** | 잦은 블로킹, 핸드오버 |

### 나. Single-Hop 네트워크

| 항목 | 설명 |
|:-----|:-----|
| **개념** | Ad-hoc 네트워크에 포함된 기기 중 하나라도 인터넷에 연결되면 Ad-hoc 네트워크에 포함된 모든 단말이 인터넷에 접속하는 방식 |
| **MAC** | PCF: Point Coordination Function |
| **장점** | 높은 전송속도, 안전성 |
| **단점** | 중앙 부하 집중 |

{: .note }
> Single-Hop 네트워크는 기반망과 연동한 네트워크 구조이며, Gateway를 통해 기반망 연결

---

## 연계 토픽

- [FANET](/docs/nw/02-adhoc/fanet)
- [거리벡터 라우팅](/docs/nw/07-osi-layer/distance-vector)

---

## 학습 체크리스트

- [ ] Proactive vs Reactive 방식 차이 이해
- [ ] Multi-Hop vs Single-Hop 구조 비교
- [ ] 각 프로토콜(DSDV, AODV, DSR, ZRP) 특징 암기

---

## 참고자료

- 정보관리기술사 NW 학습자료


