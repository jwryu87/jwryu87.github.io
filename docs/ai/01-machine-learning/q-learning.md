---
layout: default
title: Q-Learning
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 25
---

# Q-Learning
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`Q함수 사용` `최적의 정책 학습` `Q-Table` `Agent` `Reward 구성`

---

## 정의/개념

에이전트가 특정 상태에서 특정 행동을 취했을 때 얻을 수 있는 기대 보상을 학습하는 강화학습 기법

---

## 프로세스

| # | 프로세스 |
|:--|:--------|
| 1 | Q 테이블 초기화 |
| 2 | 현재 상태 관찰 |
| 3 | Action 선택 |
| 4 | Reward 확인 |
| 5 | 새로운 상태 관찰 |
| 6 | Q 테이블 갱신 |

---

## 구성요소

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **Q 함수** | 벨만 방정식 | 현재 상태의 가치함수와 다음 상태의 가치함수 사이의 관계를 표현한 방정식<br>Q(s,a) = r + lr * max(Q(s',a')) |
| | Q 함수 | 입력값이 state(현재상태), action(동작)이고, 출력이 reward(보상값)인 함수<br>Q(state, action) = reward |
| | MAX Q | 임의의 상태 s(state)에서 Q 가 가질 수 있는 최대 보상값<br>Q(state, action) = reward |
| | 정책(π) | 임의의 상태 s(state)에서 Q 가 최대값을 가지게 하는 a(action)값<br>π*(s) = argmax Q(s, a) |
| **Q Learning 알고리즘** | Q-Table | 각각의 state-s 에서 각각의 action-a 이가지는 Q(s,a)값을 모두 포함하는 테이블 |
| | 학습률 | Q 값의 갱신 완급을 결정하는 파라미터 |
| | Agent | Q-Table 을 기준으로 매 state 에서 가장 적절한 action 을 선택 |
| | Rewards | Agent 의 Action 에 따른 보상값<br>최대 보상값을 탐색하여 선택 |

---

## 연계 토픽

- [DQN](/docs/ai/01-machine-learning/deep-reinforcement-learning)
- [강화학습](/docs/ai/01-machine-learning/reinforcement-learning)
- [MDP](/docs/ai/01-machine-learning/mdp)

---

## 학습 체크리스트

- [ ] Q-Learning의 정의와 프로세스 이해
- [ ] 벨만 방정식과 Q 함수 개념 파악
- [ ] Q-Table의 역할 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
