---
layout: default
title: Container
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 6
---

# 가상머신 vs 컨테이너
{: .fs-8 }

7.2 컨테이너
{: .label .label-green }

---

## 핵심 키워드

- **가상머신**: 전가상화, 반가상화, 독점, SDDC, Monolithic
- **컨테이너**: LXC, cgroups, namespaces, 격리, SaaS, DevOps

---

## 정의/개념

- **가상머신**: 하이퍼바이저, 물리자원 독점 **가상화 기술**
- **컨테이너**: 컨테이너 엔진, 물리자원 공유 및 격리 **가상화 기술**

---

## 아키텍처 비교

| 구분 | 가상머신 | 컨테이너 |
|:-----|:--------|:---------|
| **구조** | App → Guest OS → Hypervisor → Host OS → Server (HW) | App → Container → Container Engine (LXC, cgroups, namespaces) → Host OS → Server (HW) |
| **아키텍처 설명** | - 하이퍼바이저를 HW 위에 바로 생성하는 여부에 따라 Type-1/2 로 구성<br>- Guest OS 의 HW 접근 여부에 따라 전/반가상화로 구성 | - 리눅스 환경에서 자원의 격리 및 공유를 담당하는 C-group, namespace, 이를 관리하는 LXC 로 구성 |

---

## 기술 비교

| 구분 | 가상머신 | 컨테이너 |
|:-----|:--------|:---------|
| **Application 환경** | **전가상화**: Guest OS 는 하이퍼바이저로만 HW 접근(저성능)<br>**반가상화**: Guest OS 는 직접 HW 접근 (고성능, Guest OS 한정) | **LXC**: namespaces 와 Cgroup 표준을 정의한 OCI(Open Container Initiative) 스펙을 구현한 컨테이너 기술의 구현체 |
| **HW 관리** | **Type-1**: 베어메탈 서버에 하이퍼바이저 기동(고성능, 저호환성)<br>**Type-2**: Host OS 에서 하이퍼바이저 기동 (저성능, 고호환성) | **Namespaces**: 각 게스트 머신 별로 독립적인 공간을 제공하는 기능<br>**Cgroups**: 자원에 대한 제어를 가능하게 해주는 리눅스 커널 기능 |
| **지원 환경** | 다양한 OS (Guest OS 선택) 지원<br>대용량 서버 인프라 제공 | 단일 OS 선택 가능<br>경량(프로세스 수준) 실행환경 제공 |

---

## 가상머신과 컨테이너 차이점

- 가상머신과 컨테이너는 자원에 대한 독점 및 **공유/격리가 가장 큰 차이점**임
- 자원에 대한 독점을 제공하는 가상머신보다 효율적으로 자원 관리가 가능한 **컨테이너 부상중**

---

## 연계 토픽

- [Docker](/docs/ds/07-virtualization/docker)
- [Kubernetes](/docs/ds/07-virtualization/kubernetes)
- [Hypervisor](/docs/ds/07-virtualization/hypervisor)

---

## 학습 체크리스트

- [ ] 가상머신 vs 컨테이너 차이점 이해
- [ ] 전가상화 vs 반가상화 구분
- [ ] Type-1 vs Type-2 하이퍼바이저 구분
- [ ] LXC, cgroups, namespaces 개념 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
