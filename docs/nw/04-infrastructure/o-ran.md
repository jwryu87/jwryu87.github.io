---
layout: default
title: O-RAN
parent: 4. 네트워크 구축
grand_parent: NW (네트워크)
nav_order: 1
---

# O-RAN (Open Radio Access Network)
{: .fs-8 }

4.1 네트워크 구축
{: .label .label-purple }

---

## 핵심 키워드

`무선접속망(Radio Access Network)` `규격 통일` `가상화` `O-RU` `O-DU` `O-CU`

---

## 정의/개념

네트워크 장비 운용에 필요한 RAN(Radio Access Network) 구간에 가상화 기술을 적용하여 Hardware와 Software를 분리하기 위한 **Apache 2.0 License의 개방형 아키텍처**

---

## 구성요소

| 구성 요소 | 기반 기술 | 설명 |
|:---------|:---------|:-----|
| **RIC**<br>(RAN Intelligent Controller) | RIC near-RT(Realtime)<br>RIC non-RT (Realtime) | 데이터 수집과 분석을 기반으로 RAN 요소와 자원을 제어하고 최적화를 수행 |
| **O-CU**<br>(O-RAN Centralized Unit) | RRC (Radio Resource Control)<br>SDAP (Service Data Adaption Protocol)<br>PDCP (Packet Data Convergence Protocol) | RRC, PDCP 실행하는 중앙 집중 장치<br>CU Control Plane과 CU User Plane으로 구성<br>Midhaul 인터페이스 통해 여러 O-DU 제어 |
| **O-DU**<br>(O-RAN Distributed Unit) | RLC (Radio Link Control)<br>MAC (Media Access Control)<br>High PHY | O-RU 근처에 위치해서 RLC, MAC 및 PHY 계층 일부를 실행하는 분산 장치 |
| **O-RU**<br>(O-RAN Radio Unit) | Digital Front End (DFE)<br>RF Front End (RF FE)<br>Low PHY, Beamforming | 안테나 근처에 위치 혹은 통합<br>안테나에서 송수신되는 무선 신호를 Fronthaul 통해 O-DU로 전송할 수 있는 디지털 신호로 변환 |

---

## 아키텍처 구조

```
┌────────────────────────────────────────────────────────────────┐
│  RAN Intelligent Controller (RIC) non-RT                       │
│  Orchestration & Automation (e.g. ONAP): MANO, NMS             │
└────────────────────────────────────────────────────────────────┘
                              │ A1
                              ▼
┌────────────────────────────────────────────────────────────────┐
│        RAN Intelligent Controller (RIC) near-RT                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                  Applications Layer                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │               Radio-Network Information Base              │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
                     │ E2: btw RIC near-RT and CU/DU
                     ▼
┌────────────────────────────────────────────────────────────────┐
│  Multi-RAT          │  CU-CP: RRC, PDCP-C  │  CU-UP: SDAP,     │
│  CU Protocol Stack  │                       │  PDCP-U          │
└────────────────────────────────────────────────────────────────┘
                     │ F1
                     ▼
┌────────────────────────────────────────────────────────────────┐
│  NFVI Platform: Virtualization layer and COTS platform         │
│  O-DU: RLC/MAC/PHY-high                                        │
└────────────────────────────────────────────────────────────────┘
                     │ Open Front Haul
                     ▼
┌────────────────────────────────────────────────────────────────┐
│  O-RU: PHY-low/RF                                              │
└────────────────────────────────────────────────────────────────┘
```

---

## 연계 토픽

- [RAN-Sharing](/docs/nw/04-infrastructure/ran-sharing)
- [5G 특화망](/docs/nw/04-infrastructure/5g-private-network)

---

## 학습 체크리스트

- [ ] O-RAN 개념 및 목적 이해
- [ ] RIC, O-CU, O-DU, O-RU 역할 구분
- [ ] 아키텍처 구조 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


