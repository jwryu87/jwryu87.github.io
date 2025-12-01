---
layout: default
title: 강화학습
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 22
---

# 강화학습(Reinforcement Learning)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`Agent` `State` `Action` `Environment` `Reward 최대화`

---

## 정의/개념

에이전트가 환경과 상호작용하며 보상을 최대화하는 방법을 학습하는 기계 학습

---

## 개념도

```
                    ┌─────────┐
                    │  Agent  │
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              ↓          │          ↓
         State(s)     Reward(r)   Action(a)
              │          │          │
              └──────────┼──────────┘
                         │
                    ┌────┴────┐
                    │Environment│
                    └──────────┘
```

---

## 기법

| # | 기법 | 핵심 |
|:--|:-----|:-----|
| 1 | **MDP** | 강화학습 수식화 지원 알고리즘 |
| 2 | **Markov Chain** | 다음 단어가 나올 확률 예측 방식 |
| 3 | **Q-learning** | Q 함수 사용 |
| 4 | **DQN** | 딥러닝과 Q러닝 조합 |

---

## 연계 토픽

- [심층강화학습](/docs/ai/01-machine-learning/deep-reinforcement-learning)
- [Q-Learning](/docs/ai/01-machine-learning/q-learning)
- [MDP](/docs/ai/01-machine-learning/mdp)

---

## 학습 체크리스트

- [ ] 강화학습의 정의와 개념도 이해
- [ ] 구성요소(Agent, State, Action, Environment, Reward) 암기
- [ ] 주요 기법(MDP, Markov Chain, Q-learning, DQN) 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
