---
layout: default
title: BGP
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 17
---

# BGP (Border Gateway Protocol)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`iBGP` `eBGP` `Path Vector` `AS` `Local Preference` `MED`

---

## 정의/개념

AS(Autonomous System) 번호가 서로 다른 네트워크간에 라우팅 정보를 주고 받기 위해 Open, Update 패킷 이용, 라우팅 우선순위는 Weight, Local Preference 메트릭으로 이용하는 **Exterior Gateway 라우팅 프로토콜**

---

## 기술요소

### 경로 속성

| 구분 | 기술 요소 | 설명 |
|:-----|:---------|:-----|
| **경로 속성** | Next-Hop | BGP 정보를 전송하는 라우터의 IP 주소<br>목적지까지 가는 경로의 필수 경유 라우터의 주소를 말함 |
| | Local Preference | 외부로 나가는 경로의 우선 순위 값(기본값 100)<br>해당 목적지 AS 도착시 경유되는 AS 번호들 |
| | AS-Path | 개수가 적을수록 짧은 경로로 판단되어 선택 |
| | MED | Multi-Exit-Discriminator<br>인입 경로 다중일 경우 우선 순위 값 |

### 프로토콜 메시지

| 구분 | 기술 요소 | 설명 |
|:-----|:---------|:-----|
| **프로토콜 메시지** | Open | TCP 포트번호 179번을 이용한 회선 연결 시도를 위한 오픈 메시지<br>라우터간에 BGP Neighbor 설정(이웃관계의 설정)을 위해 사용 |
| | Update | BGP 정보 교환 및 정보 갱신을 위해 비정기적 사용<br>도달 가능성 정보를 전송 |
| | Notification | 문제가 발생 및 이웃관계의 단절을 알리는데 사용 |
| | Keepalive | BGP Neighbor 라우터 Health Check 메시지 |
| | Route-Refresh | BGP Neighbor 라우터 정보 재확인 목적 |

---

## 네트워크 구성도

```
             AS 200        "외부 eBGP"        AS 100
         ┌──────────┐                    ┌──────────┐
         │   iBGP   │                    │   iBGP   │
    ┌────┴────┐ ┌───┴────┐    eBGP   ┌───┴────┐ ┌───┴────┐
    │  ALU-E  │ │  ALU-B │◄──────────►│  ALU-B │ │  ALU-A │
    └────┬────┘ └───┬────┘           └───┬────┘ └───┬────┘
         │   iBGP   │                    │   iBGP   │
    ┌────┴────┐ ┌───┴────┐           ┌───┴────┐ ┌───┴────┐
    │  ALU-D  │ │  ALU-A │           │  ALU-D  │ │  ALU-C │
    └─────────┘ └────────┘           └─────────┘ └────────┘
         "내부 iBGP"                      "내부 iBGP"
```

---

## 연계 토픽

- [거리벡터 라우팅](/docs/nw/07-osi-layer/distance-vector)
- [링크스테이트 라우팅](/docs/nw/07-osi-layer/link-state)

---

## 학습 체크리스트

- [ ] BGP 개념 및 목적 이해
- [ ] iBGP vs eBGP 차이 파악
- [ ] 경로 속성(Next-Hop, Local Preference, AS-Path, MED) 암기

---

## 참고자료

- 정보관리기술사 NW 학습자료


