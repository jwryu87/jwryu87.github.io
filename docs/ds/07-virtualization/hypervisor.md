---
layout: default
title: Hypervisor
parent: 7. 가상화/컨테이너
grand_parent: DS (Digital Service)
nav_order: 3
---

# Hypervisor
{: .fs-8 }

7.1 가상화 기본
{: .label .label-purple }

> 암기: 전가상화 - **전일바**, 반가상화 - **반영하**

---

## 정의

물리 하드웨어 위에서 **가상머신(VM)을 생성/관리**하는 **가상화 소프트웨어**

---

## 하이퍼바이저 유형

### 호스트 타입

| 유형 | 설명 | 예시 |
|:-----|:-----|:-----|
| **Type-1 (Bare Metal)** | HW 위에 직접 설치 | VMware ESXi, Xen, Hyper-V |
| **Type-2 (Hosted)** | Host OS 위에 설치 | VMware Workstation, VirtualBox |

### 가상화 방식

| 유형 | 설명 |
|:-----|:-----|
| **전가상화** | Guest OS는 Ring 1, Binary Translation 사용 |
| **반가상화** | Guest OS는 Ring 0, HyperCalls 사용 |

### H/W 드라이버 레벨

| 유형 | 설명 |
|:-----|:-----|
| **Monolithic Kernel** | 드라이버가 하이퍼바이저 내부 |
| **Micro Kernel** | 드라이버가 별도 VM에서 실행 |

---

## 전가상화 vs 반가상화

| 구분 | 전가상화 (Full) | 반가상화 (Para) |
|:-----|:---------------|:---------------|
| **암기** | 전일바 | 반영하 |
| **Guest OS 위치** | Ring 1 | Ring 0 |
| **명령어 처리** | Binary Translation | HyperCalls |
| **Guest OS 수정** | 불필요 | 필요 |
| **성능** | 상대적 저하 | 고성능 |
| **호환성** | 높음 | 낮음 (수정 필요) |

---

## HyperCall

하이퍼바이저 콜(Hypercall)은 **반가상화**에서 Guest OS가 **직접 서비스에 접근**하기 위한 호출

---

## 관련 개념

- [가상화 종류](/docs/ds/07-virtualization/가상화-종류)
- [HCI](/docs/ds/07-virtualization/hci)
- [Container](/docs/ds/07-virtualization/container)

---

## 학습 체크리스트

- [ ] 하이퍼바이저 정의 이해
- [ ] Type-1 vs Type-2 구분
- [ ] 전가상화 vs 반가상화 비교 (전일바/반영하)
- [ ] HyperCall 개념 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료 
