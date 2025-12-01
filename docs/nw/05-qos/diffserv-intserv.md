---
layout: default
title: DiffServ·IntServ
parent: 5. 네트워크 품질
grand_parent: NW (네트워크)
nav_order: 3
---

# QoS - DiffServ와 IntServ
{: .fs-8 }

5.1 네트워크 품질
{: .label .label-purple }

---

## 핵심 키워드

### DiffServ
`Packet Classifier(패킷헤더 분석)` `DSCP(TOS 필드, Traffic Class 필드)` `PHB(홉별 행위)`

### IntServ
`RSVP`

---

## 정의/개념

- **DiffServ**: DS, DSCP, PHB, Class별 QoS 보장, **차별화 QoS 보장모델**
- **IntServ**: 종단간 개별 트래픽 흐름 단위, 라우터 자원 예약, RSVP 사용, Flow별 종단간 **QoS 보장모델**

---

## DiffServ (Differentiated Services)

### 구성요소

| 주요 요소 | 설명 |
|:---------|:-----|
| **Packet Classifier** | 최종적으로 어떤 PHB(Per-Hop Behavior)를 활당할 것인지 패킷헤더를 분석 |
| **DSCP**<br>(Differentiated Service Code Point) | DiffServ에서는 모든 IP 헤더에 DSCP를 붙임<br>IPv4 헤더의 TOS 필드, IPv6 헤더의 Traffic class 필드의 8비트 등급 필드<br>8비트 중 앞 6 비트(DSCP)에 차등 서비스의 종류 또는 등급을 표시, 뒤 2비트는 미사용<br>Edge에서는 DSCP 값을 정하고, Core에서는 DSCP 값에 따라 패킷을 분류 전달 |
| **PHB**<br>(Per-Hop-Behaviour, 홉별 행위) | DiffServ 이 구현된 라우터에서 다양한 등급으로 마킹되어진 일련의 들어오는 패킷들에 대해 어떤 일관된 행위를 통해 다음 홉으로 전달 방식<br>PHB 구분: EF (Expedited Forwarding), AF (Assured Forwarding), BEF (Best-Effort Forwarding) 등 |

---

## IntServ (Integrated Services)

### 핵심기술

| 구분 | 설명 |
|:-----|:-----|
| **개념** | 종단 간 개별 트래픽(단일 패킷) 흐름 단위로 경로 상 라우터 자원을 예약하는 종단간 QoS 보장 모델<br>패킷의 Flow를 구분한 후 RSVP(Resource Reservation Protocol)를 이용하여 자원을 미리 예약하는 방식 |
| **특징** | 확장성이 불리하고 Flow별 자원예약은 라우터의 과부하를 야기함<br>망전체의 연결정보 유지필요 → 소규모용 |

### 개념도

```
                    ┌─────┐
              ┌────>│ R1  │<────┐
              │     └─────┘     │
        ┌───────┐           ┌───────┐
  H1 ───│  QoS  │───────────│  QoS  │─── H2
        │  R    │    call   │  R    │
        │ setup │           │ setup │
        └───────┘           └───────┘
              │     ┌─────┐     │
              └────>│ R3  │<────┘
                    └─────┘
                        │
              ┌─────────┼─────────┐
              │     ┌─────┐       │
              └────>│ R4  │<──────┘
                    └─────┘
```

| 구분 | 설명 |
|:-----|:-----|
| **통신의 인터넷에서는 상태(state)가 없는데 반해, InterServ 모델은 각 라우터에서 흐름단위(Per-Flow)로 상태를 유지해야 함** | 흐름 단위의 상태 유지로 복잡한 수용제어 및 트래픽 스케줄링 기법이 가능(이에따른 새로운 신호 방식으로서 RSVP(자원예약프로토콜)가 필요.<br>각 라우터 장비에서 플로우 당 상태 유지 및 예약 처리가 필요함에 따라, 대규모 망에서 상당한 부담이 되며, 따라서 확장성(Scalability)에 불리 |

---

## 연계 토픽

- [QoS](/docs/nw/05-qos/qos)
- [Traffic Shaping·Policing](/docs/nw/05-qos/traffic-shaping)

---

## 학습 체크리스트

- [ ] DiffServ와 IntServ 개념 이해
- [ ] DSCP, PHB 구성요소 파악
- [ ] RSVP 프로토콜 역할 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


