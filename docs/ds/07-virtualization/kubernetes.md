---
layout: default
title: Kubernetes
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 8
---

# 쿠버네티스 (Kubernetes)
{: .fs-8 }

7.2 컨테이너
{: .label .label-green }

---

## 핵심 키워드

`오케스트레이션` `Master Node` `Worker Node` `Container`

---

## 정의/개념

컨테이너화 된 **워크로드와 서비스를 관리**하기 위한 이식성과 확장성을 갖춘 **오픈소스 오케스트레이션 플랫폼**

---

## kubectl

- **외부에서 Kubernetes 명령어 전송**하는 CLI 도구

---

## 쿠버네티스 구성요소

### Master Node 구성

| 구성요소 | 설명 |
|:---------|:-----|
| **API Server** | 외부 요청 수신, REST 방식 통신 |
| **Scheduler** | 요청에 대한 적합한 Node 선출 |
| **Controller Manager** | 노드 상태 파악하고 관리 |
| **etcd** | Master/Worker의 상태 저장 (Key/Value) |

### Worker Node 구성

| 구성요소 | 설명 |
|:---------|:-----|
| **Kube-Proxy** | Pod간 라우팅, Load Balancing 관리 |
| **Kubelet** | API Server로부터 요청받고 실행, 노드 제어 |
| **Docker/CRI-O** | Container Engine |
| **Pod** | 컨테이너 집합, Pod 단위 배포 |

---

## 쿠버네티스 구성요소 상세

| 구분 | 구성 | 설명 |
|:-----|:-----|:-----|
| **Master Node (Control Plane)** | Kube API Server | - 간단하게 명령어를 전달해주는 역할 진행, etcd 클러스터와 REST방식 통신<br>- kubectl 명령어를 통해 받은 작업을 API서버로 전송 |
|  | Kube Scheduler | - Pod, 서비스 등 각 자원을 적절한 노드에 할당하는 역할<br>- 공유 상태 스케줄링(Shared-State Scheduling)으로 리소스 할당을 결정 |
|  | Kube Controller Manager | - 여러 Controller들을 생성하고 각 Node에 배포 및 관리 역할 |
|  | Cloud Controller Manager | - 클라우드 제공자 전용 컨트롤러 (사내 또는 PC내부 환경에서는 제외) |
|  | etcd | - 모든 클러스터 데이터를 담는 저장소 |
| **Worker Node** | Pod | - 쿠버네티스에서 가장 기본적인 배포 단위로, 컨테이너 포함하는 단위 |
|  | Kubelet | - Node에 배포되는 에이전트, Pod에서 컨테이너 동작을 관리<br>- Master의 API 서버를 통해 명령 수행 및 상태 정보를 Master 로 전달 |
|  | Kube-Proxy | - 컨테이너(Pod)간 네트워크 프록시 및 Load Balancing 수행, 간단한 L3 프록시<br>- 가상 네트워크 상에서 네트워크 트래픽 라우팅 수행 및 서비스와 Pod IP 관리 |
|  | 컨테이너 런타임 | - Pod를 통해서 배포된 컨테이너를 실행, Docker, containerd, CRI-O, Kubernetes CRI 구현 |
| **User** | kubectl | - 쿠버네티스의 명령 실행 도구 |
| **애드온** | DNS | - 쿠버네티스 서비스를 위해 DNS레코드를 제공해주는 DNS서버 |
|  | Dashboard | - 쿠버네티스 클러스터를 위한 범용의 웹기반 UI |
|  | 컨테이너 리소스 모니터링 | - 중앙DB 내의 컨테이너들에 대한 시계열 메트릭스를 기록하고, 데이터 열람을 위한 UI 제공 |
|  | 클러스터-레벨 로깅 | - 검색/열람 인터페이스와 함께 중앙 로그 저장소에 컨테이너 로그를 저장 |

---

## 연계 토픽

- [Docker](/docs/ds/07-virtualization/docker)
- [Container Orchestration](/docs/ds/07-virtualization/container-orchestration)

---

## 학습 체크리스트

- [ ] Kubernetes 정의 이해
- [ ] Master Node 구성요소 5가지 숙지
- [ ] Worker Node 구성요소 4가지 숙지
- [ ] Pod, Kubelet, Kube-Proxy 역할 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
