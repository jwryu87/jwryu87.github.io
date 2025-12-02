---
layout: default
title: CPU 스케줄링
parent: 1. CPU 스케줄링
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 1
---

# CPU 스케줄링
{: .fs-8 }

1.1 스케줄링
{: .label .label-purple }

> 암기: **선R, 비P** (선점형, 비선점형)

---

## 핵심 키워드

`CPU 할당` `선점` `비선점` `알고리즘 유형들`

---

## 정의/개념

**CPU 스케줄링**은 다중 프로세스 환경에서 **CPU를 효율적으로 사용**하기 위해 CPU를 할당 받는 **프로세스 순서 관리 기법**입니다.

---

## 스케줄링 알고리즘 유형

### 선점형 (Preemptive)

| 알고리즘 | 설명 |
|:---------|:-----|
| **RR (Round Robin)** | 단위시간 동안 CPU를 할당 받고 시간 내 처리하지 못한 경우 준비 큐 마지막으로 이동 |
| **SRT (Shortest Remaining Time)** | 준비 큐에 처리시간이 짧은 프로세스가 발생하면 선점하는 알고리즘 |
| **MLQ (Multi Level Queue)** | 프로세스를 종류별로 분류, 다수의 큐를 이용하여 높은 우선 순위 가진 프로세스가 선점, CPU 할당 받는 알고리즘 |
| **MLFQ (Multi Level Feedback Queue)** | 각각의 큐에 다른 Time Quantum 부여하고 프로세스 수행시간이 길어질수록 낮은 우선순위의 큐로 이동하여 CPU를 할당하는 알고리즘 |
| **Priority** | 프로세스에 우선순위 부여, 해당 순위에 따라 CPU 할당하는 알고리즘 |

### 비선점형 (Non-Preemptive)

| 알고리즘 | 설명 |
|:---------|:-----|
| **FCFS (First Come First Served)** | 프로세스들이 대기 큐에 도착한 순서에 따라 CPU를 할당하는 알고리즘 |
| **SJF (Shortest Job First)** | 준비 큐 내의 작업 중 Burst Time이 가장 짧다고 판단되는 것을 먼저 수행하는 알고리즘 |
| **HRN (Highest Response Ratio Next)** | SJF의 약점을 보완한 기법으로 긴 작업과 짧은 작업간의 불평등을 완화하는 알고리즘<br>우선순위 = (대기 시간 + 버스트 시간) / 버스트 시간 |

---

## 호위효과와 기아상태

| 구분 | 설명 | 해결방안 |
|:-----|:-----|:---------|
| **호위효과 (Convoy Effect)** | FCFS CPU 스케줄링 시 선행 프로세스의 긴 수행시간에 의해 이후 도착한 짧은 프로세스 수행지연, 프로세스들의 평균대기시간의 증가 현상 | - SJF 스케줄링<br>- Priority 스케줄링 |
| **기아상태 (Starvation)** | 우선순위 기반 CPU 스케줄링 시 높은 우선순위 프로세스의 지속적 진입으로 인해, 낮은 우선순위 프로세스가 수행 되지 못하고 무한대기 하는 현상 | - HRN 스케줄링<br>- MLFQ 스케줄링 |

---

## 연계 토픽

- [호위효과/노화](/docs/caos/01-cpu-scheduling/convoy-effect-aging)
- [우선순위 역전](/docs/caos/01-cpu-scheduling/priority-inversion)
- [RM (Rate Monotonic)](/docs/caos/01-cpu-scheduling/rm)
- [EDF (Earliest Deadline First)](/docs/caos/01-cpu-scheduling/edf)

---

## 학습 체크리스트

- [ ] 선점형 vs 비선점형 구분
- [ ] 각 알고리즘 특징 이해
- [ ] 호위효과와 기아상태 개념 및 해결방안

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

