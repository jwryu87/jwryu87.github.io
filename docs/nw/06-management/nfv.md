---
layout: default
title: NFV
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 7
---

# NFV (Network Function Virtualization)
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

`NFVI` `VNF(EMS)` `NFV MANO(VIM)`

---

## 정의/개념

가상화 구현, 소프트웨어적 제어 및 관리, **NFVI, VNF, NFV MANO 네트워크 아키텍처**

{: .note }
> 참고로 ETSI(유럽통신표준협회)는 NFV 인프라 아키텍처를 VNF, NFVI, MANO 3가지 구성요소로 정의한다.

---

## 메커니즘

```
┌───────────────────────────────────────────────────────────────┐
│                         OSS/BSS                                │
└───────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────┼─────────────────────────────────┐
│                             │                                  │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │        Virtualized Network Functions (VNFs)              │  │
│  │  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐                     │  │
│  │  │ VNF │  │ VNF │  │ VNF │  │ VNF │                     │  │
│  │  └─────┘  └─────┘  └─────┘  └─────┘                     │  │
│  └─────────────────────────────────────────────────────────┘  │
│                              │                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              NFV Infrastructure (NFVI)                   │  │
│  │  ┌───────────────────────────────────────────────────┐  │  │
│  │  │              Virtual Infrastructure               │  │  │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐           │  │  │
│  │  │  │ Virtual │  │ Virtual │  │ Virtual │           │  │  │
│  │  │  │ Compute │  │ Storage │  │ Network │           │  │  │
│  │  │  └─────────┘  └─────────┘  └─────────┘           │  │  │
│  │  └───────────────────────────────────────────────────┘  │  │
│  │  ┌───────────────────────────────────────────────────┐  │  │
│  │  │              Physical Infrastructure               │  │  │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐           │  │  │
│  │  │  │ Compute │  │ Storage │  │ Network │           │  │  │
│  │  │  └─────────┘  └─────────┘  └─────────┘           │  │  │
│  │  └───────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────┘
        │                                           │
        │                                           │
        ▼                                           ▼
┌─────────────────┐                      ┌──────────────────┐
│ NFV Orchestrator │                      │ Virtual          │
│                  │                      │ Infrastructure   │
│  VNF Manager     │                      │ Manager (VIM)    │
└─────────────────┘                      └──────────────────┘
        Management and Network Orchestration (MANO)
```

---

## NFV의 기술요소

| 구분 | 항목 | 내용 |
|:-----|:-----|:-----|
| **핵심 기술** | NFVI<br>(NFV Infrastructure) | 가상 네트워크 기능 수행 시 필수 기술요소<br>한 가상 자원을 제공하며, COTS 범용 하드웨어와 가속기능 및 하드웨어 가상화에 필요한 소프트웨어 계층으로 구성 |
| | VNF<br>(Virtual Network Function) | NFVI 상에서 실행될 수 있는 네트워크 기능을 구현한 소프트웨어<br>EMS (Element Management System) 내포 |
| | NFV MANO<br>(NFV Management & Orchestration) | NFVI의 물리 및 가상 자원과 VNF의 조율 및 라이프 사이클 관리 담당<br>OSS(Operation Support System)/ BSS(Business Support System)와 연동하여 기존 환경의 전반적인 관리가 가능 |
| **가상화** | Live migration | 한 서버에서 다른 서버로 운용 중인 VM을 이동시킬 수 있는 기술 |
| | Charge back | 자원 사용량을 정확히 측정할 수 있는 기술 |

---

## 연계 토픽

- [SDN](/docs/nw/06-management/sdn)
- [네트워크 슬라이싱](/docs/nw/06-management/network-slicing)

---

## 학습 체크리스트

- [ ] NFV 개념 이해
- [ ] NFVI, VNF, NFV MANO 역할 구분
- [ ] Live migration, Charge back 가상화 기술 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


