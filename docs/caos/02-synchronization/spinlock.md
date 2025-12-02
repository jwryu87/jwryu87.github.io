---
layout: default
title: 스핀락
parent: 2. 동기화
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 6
---

# 스핀락 (Spin Lock)
{: .fs-8 }

2.2 도구
{: .label .label-green }

---

## 핵심 키워드

`DPC` `IRQL` `루프`

---

## 정의/개념

**스핀락(Spin Lock)**은 임계 구역 진입이 불가능할 때 진입이 가능할 때 까지 **루프를 돌면서 재시도** 하는 **상호배제 기술**입니다.

---

## 스핀락 메커니즘

```
     낮은 IRQL                    높은 IRQL
┌────────────────┐          ┌────────────────┐
│   Process A    │          │   Process B    │
└───────┬────────┘          └───────┬────────┘
        │                           │
        │    Spinlock               │    Spinlock
        │    획득 계속시도           │    획득 계속시도
        │         │                 │         │
        │         ▼                 │         ▼
        │    ┌─────────┐           │
        └───▶│ Spinlock │◀──────────┘
             └────┬────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
     ┌─────┐ ┌─────────┐ ┌─────┐
     │ DPC │ │DPC Queue│ │ DPC │
     └─────┘ └─────────┘ └─────┘
     DPC Queue           DPC Queue
       제거                 추가
```

---

## 스핀락 동작 절차

| No | 동작절차 | 상세설명 |
|:---|:---------|:---------|
| 1 | 현재 IRQL 반환 준비 | - 모든 스핀락은 자신과 연관된 최소 DISPATCH_LEVEL 이상의 IRQL을 보유<br>- 스핀락을 획득하기 위해 실행되는 스레드보다 IRQL 높이기 위해 현재 IRQL을 반환 |
| 2 | 현재 CPU의 IRQL 상승 | - 스핀락과 연관된 IRQL만큼 현재 CPU의 IRQL을 상승 |
| 3 | 스핀락 획득 시도 (반복) | - Loop을 돌면서 실행 중 스레드가 종료 될 때 까지 스핀락 획득 시도<br>- 획득을 시도하면서 IRQL을 조금씩 상승 |
| 4 | 종료 후 반환 | - 스핀락 획득, 프로세스 처리 완료 후 스핀락 반환 |

---

## 스핀락 함수

| 구분 | 함수 | 특성 |
|:-----|:-----|:-----|
| **스핀락 실행** | spin_lock_init | `static inline void spin_lock_init(spinlock_t *lock)`<br>커널에 스핀락을 등록 및 초기화 |
| | spin_lock | `static inline void spin_lock(spinlock_t *lock)`<br>스핀락을 실행하는 함수. 기본적인 스핀락 실행 함수이며 성능이 좋음<br>- CPU 인터럽트에 대한 제어 불가 |
| | spin_unlock | `static inline void spin_unlock(spinlock_t *lock)`<br>스핀락을 해제하는 함수 |
| **데드락 방지** | spin_lock_irq | `static inline void spin_lock_irq(spinlock_t *lock)`<br>스핀락 사용중인 스레드가 CPU 인터럽트를 disable하는 함수<br>스핀락 사용중인 경우 구간에서는 CPU 인터럽트가 발생하지 않음 |
| | spin_unlock_irq | `static inline void spin_unlock_irq(spinlock_t *lock)`<br>CPU 인터럽트를 enable하는 함수<br>disable 횟수에 상관없이 모든 enable 상태를 disable 함 |
| **상태 저장** | spin_lock_irqsave | `static inline unsigned long spin_lock_irqsave(spinlock_t *lock)`<br>spin_lock_irq 실행 및 직전 spin_lock_irq 상태(enable, disable)를 저장<br>스핀락을 이용하는 시점에 CPU 인터럽트 상태 여부를 확인할 수 없는 경우<br>- 스핀락 획득 → 인터럽트 disable → 직전 인터럽트 상태 저장 |
| | spin_unlock_irqrestore | `static inline void spin_unlock_irqrestore(spinlock_t *lock, unsigned long flags)`<br>스핀락을 해제하고 spin_lock_irqsave에서 저장한 인터럽트 상태 값을 이용하여 CPU인터럽트 활성화 |

---

## 연계 토픽

- [스레드](/docs/caos/07-process/thread)
- [뮤텍스](/docs/caos/02-synchronization/mutex)

---

## 학습 체크리스트

- [ ] 스핀락의 루프 재시도 방식 이해
- [ ] IRQL 개념 이해
- [ ] 스핀락 함수 종류 파악

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

