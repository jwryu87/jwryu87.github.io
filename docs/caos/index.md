---
layout: default
title: CAOS (컴퓨터구조/OS)
nav_order: 8
has_children: true
permalink: /docs/caos
---

# CAOS (컴퓨터구조/OS)

컴퓨터 구조(Computer Architecture) 및 운영체제(Operating System) 관련 학습 자료입니다. 총 **40개** 항목

---

## 0. Computer (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 0. 기본 개념 | [Computer](/docs/caos/00-computer/computer) \| [Computer Architecture](/docs/caos/00-computer/computer-architecture) |

---

## 1. CPU 스케줄링 (3개)

| 구분 | 토픽 |
|:-----|:-----|
| 1.1 스케줄링 | [CPU 스케줄링](/docs/caos/01-cpu-scheduling/cpu-scheduling) |
| 1.2 효과/문제 | [호위효과/노화](/docs/caos/01-cpu-scheduling/convoy-effect-aging) \| [우선순위 역전](/docs/caos/01-cpu-scheduling/priority-inversion) |

---

## 2. 동기화 (6개)

| 구분 | 토픽 |
|:-----|:-----|
| 2.1 문제 | [경쟁조건](/docs/caos/02-synchronization/race-condition) \| [Mutual Exclusion](/docs/caos/02-synchronization/mutual-exclusion) |
| 2.2 도구 | [세마포어](/docs/caos/02-synchronization/semaphore) \| [뮤텍스](/docs/caos/02-synchronization/mutex) \| [모니터](/docs/caos/02-synchronization/monitor) \| [스핀락](/docs/caos/02-synchronization/spinlock) |

---

## 3. 교착상태 (3개)

| 구분 | 토픽 |
|:-----|:-----|
| 3.1 개념/해결 | [교착상태](/docs/caos/03-deadlock/deadlock) \| [은행가 알고리즘](/docs/caos/03-deadlock/bankers-algorithm) \| [Wait-die, Wound-wait](/docs/caos/03-deadlock/wait-die-wound-wait) |

---

## 4. 가상메모리 (8개)

| 구분 | 토픽 |
|:-----|:-----|
| 4.1 개념 | [가상메모리 개념](/docs/caos/04-virtual-memory/virtual-memory-concept) \| [가상메모리 관리기법](/docs/caos/04-virtual-memory/virtual-memory-management) |
| 4.2 기법 | [페이징 기법](/docs/caos/04-virtual-memory/paging) \| [세그멘테이션 기법](/docs/caos/04-virtual-memory/segmentation) |
| 4.3 문제/최적화 | [가상메모리 단편화](/docs/caos/04-virtual-memory/fragmentation) \| [지역성](/docs/caos/04-virtual-memory/locality) \| [페이지 교체 알고리즘](/docs/caos/04-virtual-memory/page-replacement) \| [스레싱](/docs/caos/04-virtual-memory/thrashing) |

---

## 5. 캐시메모리 (4개)

| 구분 | 토픽 |
|:-----|:-----|
| 5.1 개념 | [캐시 메모리 개념](/docs/caos/05-cache-memory/cache-memory-concept) |
| 5.2 일관성 | [캐시 일관성](/docs/caos/05-cache-memory/cache-coherence) \| [MESI 프로토콜](/docs/caos/05-cache-memory/mesi-protocol) |
| 5.3 쓰기 정책 | [Cache Memory Write](/docs/caos/05-cache-memory/cache-memory-write) |

---

## 6. RAID (1개)

| 구분 | 토픽 |
|:-----|:-----|
| 6.1 저장장치 | [RAID](/docs/caos/06-raid/raid) |

---

## 7. 프로세스 (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 7.1 프로세스 | [문맥교환](/docs/caos/07-process/context-switching) \| [스레드](/docs/caos/07-process/thread) |

---

## 8. 파이프라인 (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 8.1 파이프라인 | [파이프라인](/docs/caos/08-pipeline/pipeline) \| [파이프라인 해저드](/docs/caos/08-pipeline/pipeline-hazard) |

---

## 9. 메모리 (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 9.1 신기술 | [CXL](/docs/caos/09-memory/cxl) \| [PNM](/docs/caos/09-memory/pnm) |

---

## 10. 인터럽트 (1개)

| 구분 | 토픽 |
|:-----|:-----|
| 10.1 인터럽트 | [인터럽트](/docs/caos/10-interrupt/interrupt) |

---

## 11. 운영체제 (1개)

| 구분 | 토픽 |
|:-----|:-----|
| 11.1 운영체제 | [이중 모드](/docs/caos/11-os/dual-mode) |

---

## 12. 반도체 (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 12.1 프로세서 | [NPU/DPU](/docs/caos/12-semiconductor/npu-dpu) |
| 12.2 메모리 | [메모리 반도체와 비메모리 반도체](/docs/caos/12-semiconductor/memory-semiconductor) |

---

## 13. CPU/GPU (2개)

| 구분 | 토픽 |
|:-----|:-----|
| 13.1 프로세서 | [CPU, GPU, FPGA, ASIC](/docs/caos/13-cpu-gpu/cpu-gpu-fpga-asic) |
| 13.2 아키텍처 | [하버드/폰노이만 아키텍처](/docs/caos/13-cpu-gpu/harvard-von-neumann) |

---

## 14. CA 기타 (4개)

| 구분 | 토픽 |
|:-----|:-----|
| 14.1 기타 | [워치독 타이머](/docs/caos/14-ca-etc/watchdog-timer) \| [DMA](/docs/caos/14-ca-etc/dma) \| [메모리 인터리빙](/docs/caos/14-ca-etc/memory-interleaving) |

---

## 학습 체크리스트

- [ ] CPU 스케줄링 알고리즘 이해
- [ ] 동기화 기법 비교 (세마포어 vs 뮤텍스 vs 모니터)
- [ ] 교착상태 조건 및 해결방법
- [ ] 가상메모리 개념 및 페이지 교체 알고리즘
- [ ] 캐시 일관성 프로토콜 (MESI)
- [ ] 파이프라인 해저드 유형
- [ ] 프로세스 vs 스레드 차이

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료
- TOP (Together Of PE) 베이스라인 기본필수토픽 720제

