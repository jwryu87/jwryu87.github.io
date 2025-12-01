---
layout: default
title: SDN
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 4
---

# SDN (Software Defined Network)
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

`Control Plane` `Data Plane` `NBI` `CDPI` `Openflow`

---

## 정의/개념

개방형 프로토콜, SW 기반 네트워크 구성, **제어 네트워크 기술**

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                    Application Plane                             │
│  ┌──────────────────┐ ┌──────────────────┐ ┌────────────────┐   │
│  │  SDN Application │ │  SDN Application │ │ SDN Application│   │
│  │  ┌─────────────┐ │ │  ┌─────────────┐ │ │ ┌────────────┐ │   │
│  │  │ SDN App Logic│ │ │  │ SDN App Logic│ │ │ │SDN App Logic│ │   │
│  │  ├─────────────┤ │ │  ├─────────────┤ │ │ ├────────────┤ │   │
│  │  │  NBI Driver  │ │ │  │  NBI Driver  │ │ │ │ NBI Driver │ │   │
│  │  └─────────────┘ │ │  └─────────────┘ │ │ └────────────┘ │   │
│  └──────────────────┘ └──────────────────┘ └────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │ NBI (Northbound Interfaces)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Control Plane                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    SDN Controller                           │ │
│  │  NBI Agent    SDN Control Logic    Configure                │ │
│  │               CDPI Driver          Monitor Performance      │ │
│  └────────────────────────────────────────────────────────────┘ │
│      SDN Control-Data-Plane Interface (CDPI)                    │
└─────────────────────────────────────────────────────────────────┘
                              │ CDPI
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Data Plane                                 │
│  ┌────────────────────┐    ┌────────────────────┐               │
│  │   Network Element   │    │   Network Element   │               │
│  │  ┌──────────────┐  │    │  ┌──────────────┐  │               │
│  │  │ SDN Datapath  │  │    │  │ SDN Datapath  │  │               │
│  │  │  CDPI Agent   │  │    │  │  CDPI Agent   │  │               │
│  │  ├──────────────┤  │    │  ├──────────────┤  │               │
│  │  │Forwarding Eng│  │    │  │Forwarding Eng│  │               │
│  │  │Processing Func│  │    │  │Processing Func│  │               │
│  │  └──────────────┘  │    │  └──────────────┘  │               │
│  └────────────────────┘    └────────────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

{: .note }
> Server-client → Peer to Peer 형태 트래픽으로 다양화 가능하며, Network Overay 기반 NW슬라이싱 및 병목현상 완화와 벤더 종속현상(Lock-in)을 해결할 수 있음

---

## 핵심기술

| 구분 | 기술요소 | 상세설명 |
|:-----|:---------|:---------|
| **SDN 응용 프로그램** | - | NBI 프로그래밍 방식의 네트워크 동작을 컨트롤러에 전달, 추상화<br>NBI 에이전트를 통해 다수 상위 NBI 제공 |
| **SDN 계층별 기술 측면** | SDN 컨트롤러 | SDN 응용 프로그램 계층의 요구 사항을 SDN Datapath 로 변환<br>SDN 응용 프로그램에 네트워크 추상화 제공, 논리적 중앙화 |
| | SDN Datapath | 전달 및 데이터 처리 기능 가시화와 논리적 네트워크 제어 장치<br>CDPI 에이전트와 트래픽 포워딩 엔진 세트 및 트래픽 처리 기능 |
| **SDN Interface 측면** | CDPI<br>(Control to DataPlain Interface) | SDN 컨트롤러와 SDN Datapath 간에 정의 된 인터페이스<br>프로그래밍 방식의 포워딩 제어, 기능공고, 통계보고, 이벤트를 알림 |
| | NBI<br>(Northbound Interface) | SDN 응용 프로그램-컨트롤러 간 Interface, 추상 네트워크 가시화 |
| **드라이버/에이전트** | - | 벤더중립적 상호 운용 가능 방식으로 구현<br>각 인터페이스는 드라이버, 에이전트 쌍으로 구성 및 실행<br>Southbound, Bottom → 인프라, Northern, Top → 응용 프로그램 |

{: .highlight }
> Control Plane 과 Data Plane 간의 인터페이스 CDPI 에 오픈플로우(Openflow) 규격이 활용됨

---

## 연계 토픽

- [Openflow](/docs/nw/06-management/openflow)
- [NFV](/docs/nw/06-management/nfv)
- [SDDC](/docs/nw/06-management/sddc)

---

## 학습 체크리스트

- [ ] SDN 개념 및 필요성 이해
- [ ] Control Plane, Data Plane 분리 구조 파악
- [ ] NBI, CDPI 인터페이스 역할 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


