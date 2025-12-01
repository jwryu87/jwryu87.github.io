---
layout: default
title: SDDC
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 3
---

# SDDC (Software Defined Data Center)
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

`Orchestration` `Controller` `Provisioning` `SDC` `SDN` `SDS`

---

## 정의/개념

서버, 스토리지, 네트워킹, 보안시스템 등 데이터센터 모든 인프라 가상화 소프트웨어 자동 통제 관리 기술

---

## 아키텍처

```
┌──────────────────────────────────────────────────────────────┐
│                      Orchestration                            │
│  ┌───────────────┐                                           │
│  │   소프트웨어   │                                           │
│  │    개방형 API  │    워크 플로우 기반 1:N 자동화              │
│  └───────────────┘                                           │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ 소프트웨어 │  │ 소프트웨어 │  │ 소프트웨어 │             │
│  │  개방형 API │  │  개방형 API │  │  개방형 API │             │
│  ├────────────┤  ├────────────┤  ├────────────┤             │
│  │ Controller │  │ Controller │  │ Controller │             │
│  │ 1:N 프로비저닝│  │ 1:N 프로비저닝│  │ 1:N 프로비저닝│             │
│  └────────────┘  └────────────┘  └────────────┘             │
├──────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │  하드웨어  │  │  하드웨어  │  │  하드웨어  │               │
│  │           │  │           │  │           │               │
│  │ ■■■■■■   │  │ ▣▣▣▣▣▣   │  │ ≡≡≡≡≡≡   │               │
│  │  Compute  │  │  Network  │  │  Storage  │               │
│  │   SDC     │  │   SDN     │  │   SDS     │               │
│  └───────────┘  └───────────┘  └───────────┘               │
└──────────────────────────────────────────────────────────────┘
```

{: .note }
> 인공신경망 기반의 Word Embedding 으로 CBOW, Skip-gram 모델이 있음

---

## 핵심기술

| 구분 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **소프트웨어 측면 (SW)** | SDC | Virtual Machine: Hypervisor(ESXi, HYPER-V, KVM)<br>Container: Docker, LXC/LXD, JAIL, Zones |
| | SDN | OverlayN/W: Networkslice(VxLAN)<br>Control Plane: North Bound API(Overlay, LeafSpine, Auto Configuration), SouthBoundProtocol(FlowRule)<br>오픈플로우: Forwarding, Drop, Shaping, Reactive Processing |
| | SDS | Scale-Out Storage: Node 단위로 용량 및 성능 확장<br>Ceph, lustre, gluster |
| | Automation | Orchestration: 자원관리, SW Provisioning<br>통합 모니터링: 여러 벤더 및 오픈 리소스의 통합 관리 (Openstack Monasca, Apache kafka) |
| | Intelligence | AnomalyDetection(MultivariateAnalysis, DeepLearning) |
| **하드웨어 측면 (HW)** | 오픈 소스 | OCP(OpenComputeProject) |
| | 하드웨어 | 개방형 구조의 서버, 스위치, 스토리지 |
| | 네트워크 | SDN 기반의 Leaf-SpineFabric<br>Dataplane: WhiteBox, 베어메탈의 오픈 소스 스위치 |
| | 기타 | PCIeJBOF, All-FlashMediaServer |

{: .highlight }
> 데이터센터에 비하여 오픈 소스 소프트웨어와 오픈 소스 하드웨어 구현 시, Vendor Lock-in 탈피 및 LicenseFee 절감 효과

---

## 연계 토픽

- [SDN](/docs/nw/06-management/sdn)
- [SDx](/docs/nw/06-management/sdx)
- [NFV](/docs/nw/06-management/nfv)

---

## 학습 체크리스트

- [ ] SDDC 개념 이해
- [ ] 아키텍처 구조(Orchestration, Controller, 하드웨어) 파악
- [ ] SDC, SDN, SDS 역할 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


