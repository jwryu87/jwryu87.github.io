---
layout: default
title: HCI
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 4
---

# HCI (Hyper Converged Infrastructure)
{: .fs-8 }

7.1 가상화
{: .label .label-blue }

---

## 핵심 키워드

`Controller VM` `Hypervisor` `x86 서버` `RAIN+RAID`

---

## 정의/개념

x86 서버, 컴퓨팅&스토리지 통합 소프트웨어 관리 **통합 어플라이언스**

---

## HCI 구성요소

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **가상화** | 가상화 컴퓨팅 | ESXi, vCenter, vSphere 기반 가상머신 |
|  | Controller VM | VM과 물리 Disk간 Direct Path 수행, 리소스 할당 및 디스크 사용관리 |
|  | Hypervisor (Data store) | VM별 Virtual Disk 할당 |
| **Disk** | x86 서버 | CPU, Memory, SSD, Disk Controller |
|  | RAIN + RAID | SSD를 중복배열기술(RAIN: Redundant array of independent nodes)을 활용해 여러 개의 스토리지를 RAID 구성. 데이터의 가용성 및 성능 개선 |
| **관리** | VMware vSphere | Web 환경에서 가상화된 자원 통합 관리 |

- 가상화 컴퓨팅 기능에 스토리지와 네트워킹을 단일화 시켜 모든 요소를 SDI(Software Defined Infrastructure)로 적용한 랙 서버 형태의 Scale-out 인프라 솔루션

---

## 주요기능

| 기능 | 설명 |
|:-----|:-----|
| **Abstraction** | SDS(Software Defined Storage)기반의 저장 기능을 통해 데이터 저장의 추상화 제공 |
| **Virtualization** | 하이퍼바이저를 통해 여러 VM을 제공하여 SDS 구현 |
| **Auto-Tiering** | 스토리지 Pool용량 내 자유롭게 사용 가능 |
| **Orchestration** | 통합된 프로세스와 단일화된 워크플로우 제공 |

---

## 연계 토픽

- [가상화 종류](/docs/ds/07-virtualization/가상화-종류)
- [Hypervisor](/docs/ds/07-virtualization/hypervisor)

---

## 학습 체크리스트

- [ ] HCI 정의 이해
- [ ] 가상화, Disk, 관리 구성요소 숙지
- [ ] 4가지 주요기능 숙지
- [ ] SDI, RAIN+RAID 개념 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
