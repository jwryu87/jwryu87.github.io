---
layout: default
title: Docker
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 5
---

# 도커 (Docker)
{: .fs-8 }

7.2 컨테이너
{: .label .label-green }

---

## 핵심 키워드

`하이퍼바이저` `컨테이너` `LXC` `이미지`

---

## 정의/개념

하이퍼바이저(hypervisor) 없이 **리눅스 컨테이너(Linux Container, LXC) 기술**을 바탕으로 애플리케이션을 격리 상태에서 실행하는 **가상화 기술**

---

## 도커 개념도

| 가상화 | 도커 |
|:-------|:-----|
| App A, App B → Bins/Libs → Guest OS → 하이퍼바이저 → 호스트 운영체제 → 서버 | App A, App B → Bins/Libs → 도커 엔진 → 호스트 운영체제 → 서버 (컨테이너) |

### 가상화 vs 도커 비교

| 구분 | 가상화 | 도커 |
|:-----|:-------|:-----|
| **특징** | 다양한 OS 환경을 운영하는데 적합. 한 하드웨어에서 여러버전의 리눅스를 쓸 수 있다 | 단일 기종의 OS를 더 빠르게 생성하고 사용에 유리. 물리적 서버와 가상 서버 간 애플리케이션 이동이 쉽다 |
| **용도** | **특정 애플리케이션에 최적화** | |

---

## 도커 구성요소

| 구성 요소 | 설명 | 세부 기술 |
|:---------|:-----|:---------|
| **Client** | 도커 컨테이너를 관리하고 실행하기 위해서 데몬과 상호작용하는 Binary 파일 | CLI, Remote API |
| **이미지 (IMAGES)** | 필요한 프로그램과 라이브러리, 소스를 설치한 뒤 파일로 만든 것 | aufs, btrfs, devicemapper |
| **컨테이너 (Container)** | 이미지를 실행한 상태. 한개의 이미지로 여러 개의 컨테이너 생성 가능 | LXC (namespace, cgroups, SELinux,) |
| **데몬 (daemon)** | Host에 설치되어 client와 상호 작용하여 도커 컨테이너를 관리하는 프로세스 | service |
| **레지스트리** | 도커 이미지가 저장되어 있는 장소. 허브에 등록하여 공유 및 배포하거나 저장소를 직접 만들어 관리 | docker hub, docker registry |

---

## 도커와 하이퍼바이저 비교

| 비교 | 도커 | Hypervisor |
|:-----|:-----|:-----------|
| **추상화** | OS 커널 | 전체 H/W Device를 추상화 |
| **OS** | 단일 OS상의 다양한 에디션 | 여러 OS를 동시 사용 |
| **호환성** | Linux 유리, 타 플랫폼은 미비 | 여러 플랫폼 지원 |
| **성능** | 직접 OS를 Access하여 우수 | Guest/Host OS Layer로 인해 저하 |

---

## 연계 토픽

- [Container](/docs/ds/07-virtualization/container)
- [Kubernetes](/docs/ds/07-virtualization/kubernetes)

---

## 학습 체크리스트

- [ ] Docker 정의 이해
- [ ] 가상화 vs 도커 차이점 숙지
- [ ] 5가지 구성요소 (Client, 이미지, 컨테이너, 데몬, 레지스트리) 숙지
- [ ] Docker vs Hypervisor 비교

---

## 참고자료

- 정보관리기술사 DS 학습자료
