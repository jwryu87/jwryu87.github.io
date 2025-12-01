---
layout: default
title: SD-WAN
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 6
---

# SD-WAN (Software Defined-Wide Area Network)
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

`SD-WAN Controller` `SD-WAN Edge` `VPN`

---

## 정의/개념

데이터센터, 기업\, 대학 등의 LAN에서 Data Plane과 Control Plane을 분리하는 SDN을 통신망 사업자와 서비스 제공자 등의 **WAN(Wide Area Network)으로 확장 적용한 네트워크 기술**

---

## 메커니즘

```
┌─────────────────────────────────────────────────────────────────┐
│              End-to-End SD-WAN Overlay                          │
│                                                                  │
│                 ┌──────────────────┐                            │
│                 │  SD-WAN Controller │                            │
│                 └──────────────────┘                            │
│                          │                                       │
│        ┌─────────────────┼─────────────────┐                    │
│        │                 │                 │                    │
│  ┌──────────┐      ┌───────────┐     ┌──────────┐              │
│  │  Branch  │      │Private/MPLS│     │   HQ/DC  │              │
│  │SD-WAN CPE│──────│  Path 1   │─────│SD-WAN CPE│              │
│  └──────────┘      │           │     └──────────┘              │
│        │           │  Path 2   │           │                    │
│       LAN          │Ethernet,DSL│         LAN                   │
│                    │cable, LTE │                                │
│                    │  Path 3   │                                │
│                    │ Internet  │                                │
│                    └───────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 기술요소

### 장비 측면

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **SD-WAN Controller** | - | 액세스 노드의 네트워크 및 정책 설정, 네트워크 토폴로지 관리<br>QoS 및 액세스에 대한 정책 설정 및 배포, 사용량 및 성능 보고 |
| **SD-WAN CPE (SD-WAN Edge)** | - | 별도의 CPE 장비 또는 범용 서버에 가상화된 VNF 로 구현<br>가상의 오버레이 네트워크를 생성해내기 위한 라우팅 및 터널링 엔진<br>방화벽, 보안, 암호화, WAN 최적화(캐싱, 감축, 에러 정정, 로드밸런싱) |

### 기술 측면

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **Dynamic Path Switching** | - | 여러 경로 중에 한 경로의 성능이 저하될 경우 다른 경로를 선택해 트래픽을 스위칭 |
| **Packet Duplication** | - | 중요한 패킷의 경우 여러 경로에 중복으로 패킷을 전송해서 한 경로의 패킷이 중간에 유실되어도 다른 경로에서 들어온 온전한 패킷을 사용해 통신 |
| **Link Aggregation** | - | 물리적인 여러 회선을 논리적인 하나의 회선으로 만들어 대역폭을 확장하는 기술(Traffic Load Balancing, Tunnel Bonding) |
| **Network Segmentation** | - | LAN 에서는 세그먼트 별로 VLAN을 할당하여 LAN 망을 논리적으로 분리(Segmentation)하고, 각 세그먼트 간에 통신이 필요한 경우는 해당 트래픽 Flow를 Firewall에 등록하여 세그먼트간 통신하는 기술 |

---

## 연계 토픽

- [SASE](/docs/nw/06-management/sase)
- [오버레이 네트워크](/docs/nw/06-management/overlay-network)
- [SDN](/docs/nw/06-management/sdn)

---

## 학습 체크리스트

- [ ] SD-WAN 개념 이해
- [ ] Controller, CPE(Edge) 역할 구분
- [ ] Dynamic Path Switching, Packet Duplication 등 기술요소 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


