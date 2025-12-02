---
layout: default
title: CRI/CRI-O
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 7
---

# CRI / CRI-O
{: .fs-8 }

7.2 컨테이너
{: .label .label-purple }

> 암기: CRI 구성 - **프지라**

---

## CRI 정의

**CRI (Container Runtime Interface)**: Kubernetes가 다양한 컨테이너 런타임과 통신하기 위한 **표준 인터페이스**

---

## CRI 구성 (프지라)

| 구성요소 | 설명 |
|:---------|:-----|
| **프로토콜 버퍼** | 컨테이너와 통신 기능 |
| **gRPC API** | 이미지 관리, 컨테이너 생명주기 |
| **라이브러리** | 다양한 라이브러리 제공 |

---

## CRI-O 정의

**OCI (Open Container Initiative)** 표준을 준수하여 Docker를 대체하는 것을 목적으로 **CRI 표준 컴포넌트를 최소한의 런타임으로 구현**한 오픈소스 컨테이너 엔진

---

## CRI-O 기능 및 도구 (BPS)

| 구분 | 항목 | 설명 |
|:-----|:-----|:-----|
| **기능** | 이미지 관리 | 컨테이너 이미지 Pull/Push |
| | 컨테이너 관리 | 컨테이너 생성/삭제/관리 |
| | CRI 표준 준수 | Kubernetes와 호환 |
| **도구** | **B**uildah | Docker 없이 컨테이너 빌드 |
| | **P**odman | 이미지 유지 관리 |
| | **S**kopeo | 명령줄 도구 (이미지 전송) |

---

## Docker vs CRI-O 비교

| 구분 | Docker | CRI-O |
|:-----|:-------|:------|
| **용도** | 범용 컨테이너 | Kubernetes 전용 |
| **표준** | Docker API | OCI 표준 |
| **구성** | 올인원 | 최소화/모듈화 |
| **데몬** | dockerd 필요 | 데몬리스 가능 |

---

## 관련 개념

- [Docker](/docs/ds/07-virtualization/docker)
- [Kubernetes](/docs/ds/07-virtualization/kubernetes)
- [Container](/docs/ds/07-virtualization/container)

---

## 학습 체크리스트

- [ ] CRI 정의 이해
- [ ] CRI 구성 3가지 (프지라) 암기
- [ ] CRI-O 정의 및 특징 이해
- [ ] BPS 도구 (Buildah, Podman, Skopeo) 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료 
