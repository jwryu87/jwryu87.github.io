---
layout: default
title: MDP
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 27
---

# MDP(Markov Decision Process)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`상태` `확률밀도함수` `행동` `보상함수 구성` `이산 확률 프로세스 사용`

---

## 정의/개념

에이전트가 환경과 상호작용하며 보상을 최대화하는 문제를 수학적으로 모델링한 강화학습 기법

---

## 개념도

```
                    ┌─────────┐
< S, A, P, R, γ > 라는 Tuple 로 정의   │  Agent  │
- agent 는 sₜ에 해당하는 state 에서 Aₜ에  └────┬────┘
  해당하는 action 을 수행                     │
- environment 는 다음 state 에 해당하는  state │ reward  action
  sₜ₊₁과 그에 상응하는 reward rₜ₊₁을       Sₜ  │  Rₜ     Aₜ
  agent 에게 반환                           ↓     ↓      ↓
                                   ┌──────────────────────┐
                                   │    Environment       │
                                   │   sₜ₊₁              │
                                   │   rₜ₊₁              │
                                   └──────────────────────┘
```

---

## 구성요소

| 구성요소 | 핵심 |
|:---------|:-----|
| **상태** | 에이전트 관찰 가능 상태 집합 |
| **행동** | 에이전트가 상태에서 할 수 있는 행동 집합 |
| **상태전이 확률분포** | 확률밀도함수 |
| **즉시보상** | 에이전트가 학습할 수 있는 유일한 정보 |
| **할인율** | 보상 가치 고려 현재 가치 변환 |
| **정책** | 각각 State마다 Action 분포 표현 함수 |

---

## 연계 토픽

- [Q-Learning](/docs/ai/01-machine-learning/q-learning)
- [강화학습](/docs/ai/01-machine-learning/reinforcement-learning)
- [HMM](/docs/ai/04-nlp/hmm)

---

## 학습 체크리스트

- [ ] MDP의 정의와 개념도 이해
- [ ] Tuple < S, A, P, R, γ > 구성요소 암기
- [ ] 각 구성요소의 역할 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
