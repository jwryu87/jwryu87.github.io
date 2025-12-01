---
layout: default
title: 심층강화학습
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 23
---

# 심층강화학습(Deep Reinforcement Learning)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`DNN` `MDP` `Q-learning` `Environment` `State` `Agent` `Action` `Reward`

---

## 정의/개념

강화학습 정책 또는 가치함수를 심층신경망으로 구성 AI 학습 기법

> 심층강화학습은 강화학습과 심층학습(딥러닝)을 결합하여, 시행착오를 통해 결정 내리는 방법을 학습

---

## 개념도

```
┌──────────────────────────────────────────────────────────────┐
│                    심층 강화 학습                             │
│                (Deep Reinforcement Learning)                 │
├───────────────────────┬──────────────────────────────────────┤
│      강화 학습         │              딥러닝                  │
│                       │                                      │
│    ┌─────────┐       │        ┌─────────────────────┐       │
│    │ 에이전트 │◀──────┼────────│                     │       │
│    │ (Agent) │상태    │        │   Input layer       │       │
│    └────┬────┘(State)│   ╋    │     ○ ○ ○ ○        │       │
│  관찰정보│  보상  행동 │        │   Hidden layer 1    │       │
│(Observ.)│(Reward)│(Act)│        │     ○ ○ ○ ○        │       │
│    Ot   │  Rt    │ At │        │   Hidden layer 2    │       │
│    ↓    ↓        ↓    │        │     ○ ○ ○ ○        │       │
│    ┌────────────────┐ │        │   Output layer      │       │
│    │ 환경            │ │        │     ○ ○ ○          │       │
│    │ (Environment)  │ │        └─────────────────────┘       │
│    │ 현재상태(Env State)│        │                            │
│    └────────────────┘ │                                      │
└───────────────────────┴──────────────────────────────────────┘
```

---

## 구성요소

| 구분 | 구성요소 |
|:-----|:---------|
| **딥러닝 측면** | DNN |
| **강화학습 측면** | MDP |
| | Q-learning |
| | Environment |
| | State |
| | Agent |
| | Action |
| | Reward |

---

## 연계 토픽

- [강화학습](/docs/ai/01-machine-learning/reinforcement-learning)
- [Q-Learning](/docs/ai/01-machine-learning/q-learning)
- [DNN](/docs/ai/02-deep-learning/mlp)

---

## 학습 체크리스트

- [ ] 심층강화학습의 정의 이해
- [ ] 강화학습 + 딥러닝 결합 구조 파악
- [ ] 구성요소(DNN, MDP, Q-learning 등) 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
