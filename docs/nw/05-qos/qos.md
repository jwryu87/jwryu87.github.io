---
layout: default
title: QoS
parent: 5. 네트워크 품질
grand_parent: NW (네트워크)
nav_order: 1
---

# QoS (Quality of Service)
{: .fs-8 }

5.1 네트워크 품질
{: .label .label-purple }

---

## 핵심 키워드

`대지터패` `CBQ` `WFQ` `Traffic Policing` `Traffic Shaping` `Leaky/Token Bucket` `IntServ` `DiffServ`

---

## 정의/개념

한정된 네트워크 자원 내 트래픽과 대역폭 정책적 관리 **네트워크 서비스 품질 보장 기술**

---

## 주요 지표

| 유형 | 구분 | 주요 지표 |
|:-----|:-----|:---------|
| **일반 인터넷망** | 현상 기준 | 지연, 지터(Jitter), 패킷 손실 |
| | 처리 능력 | 대역폭, 신뢰성, 가용성 |
| **휴대 인터넷망** | 트래픽 | 트래픽 우선 순위, 최대 지속 트래픽 속도, 최대 트래픽 버스트 크기 |
| | 회선 변경 | 셀 손실률, 최대 지연 시간, 허용 지터 |

---

## 보장 기술

### QoS 관리

| 분류 | 기술 | 설명 |
|:-----|:-----|:-----|
| **Queue 관리**<br>(장비의 처리 능력) | FIFO Queue | First In-First Out |
| | Priority Queue | High, Medium, Normal, Low 차등 서비스 |
| | CBQ | PQ + 기아현상 방지 |
| | WFQ | 클래스 마다 IP Precedence로 가중치 |
| **Traffic Policing**<br>(Packet Drop) | - | 정해진 대역폭 초과 시 패킷 Drop |
| **Traffic Shaping**<br>(Buffer Save & Send) | Leaky Bucket | 용량 제어 기법 |
| | Token Bucket | 속도 제어 기법 |
| | Hybrid | Leaky + Token 결합 |
| **혼잡 제어** | RED | 혼잡 전 Drop |
| | WRED | 중요도 비율로 Drop |
| | Tail Drop | 버퍼 초과시 Drop |

### QoS 보장

| 분류 | 기술 | 설명 |
|:-----|:-----|:-----|
| **혼잡 상황 회피&제어** | IntServ | 트래픽 호급, RSVP |
| | DiffServ | DSCP, 서비스 우선 |
| | Best Effort | 기본 처리 방식 |

---

## 연계 토픽

- [Traffic Shaping·Policing](/docs/nw/05-qos/traffic-shaping)
- [DiffServ·IntServ](/docs/nw/05-qos/diffserv-intserv)

---

## 학습 체크리스트

- [ ] QoS 개념 및 필요성 이해
- [ ] 주요 지표(지연, 지터, 패킷손실, 대역폭) 파악
- [ ] Queue 관리, Traffic 제어, 혼잡 제어 기술 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


