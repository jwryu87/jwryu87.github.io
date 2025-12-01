---
layout: default
title: HMM
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 26
---

# 은닉 마르코프 모델(HMM : Hidden Markov Model)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`Hidden Parameter 추정` `문맥 의존 데이터/순차데이터 인식` `상태전이 행렬 사용` `이중 확률론적 모델`

---

## 정의/개념

시스템의 내부 상태가 직접 관찰되지 않고, 관찰 가능한 결과물을 통해 간접적으로 추론하는 통계적 모델

---

## 개념도 및 유형

### 기본 모델

- **마르코프 모델**: 은닉상태간 확률 및 HMM 모수바탕으로, 보이지 않는 상태(날씨)를 예측
- **은닉 마르코프 모델**: Initialization, State Transition, Observation 확률기반 산출

### HMM 유형

| 유형 | 설명 |
|:-----|:-----|
| **Ergodic Model** | 모든 상태가 연결, 상태간 확률 연계 (순환모델) |
| **Left to Right Model** | 상태 전이가 순차발생 (일자형모델) |

> 은닉상태/관찰가능상태 집합, 상태전이/관찰확률 행렬 및 파이벡터기반 HMM 모델링

---

## 구성요소

| 구분 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **주요 변수 확률** | Initialization 확률 | HMM Start 시점에 어느 상태에서 시작할지 결정하는데 사용되는 확률 (예. 내일 날씨 예측시, 오늘 날씨 확률) |
| | State transaction 확률 | 상태 전이시 발생하는 확률 (예. 오늘 비가 왔을 때, 내일 날씨가 맑을 확률) |
| | Observation 확률 | 어느 한 상태에서, 관측 된 상태의 확률 (예. 맑을 때 청소할 확률, 맑을 때 외출할 확률) |

### HMM 구성 표기법

**Notation: λ = ( A, B, Π )**

| 구성요소 | 설명 |
|:---------|:-----|
| **은닉상태 집합** | 마르코프 프로세스에 의해 표현되는 상태들의 집합<br>1) N : Number of states |
| **관찰가능상태 집합** | 외형적으로 표현되는 상태 및 전이상태들의 집합<br>2) M : Number of symbols observable in states<br>V = {v₁, ⋯, vₘ} |
| **상태전이 확률 행렬** | 이전 은닉상태에서 현재 은닉상태로의 전이 확률<br>모델 내부의 은닉 상태들간 전이 확률을 나타내는 행렬<br>3) A : State transition probability distribution<br>A = {aᵢⱼ}, 1 ≤ i, j ≤ N |
| **관찰확률 행렬** | 특정 은닉상태에서 관찰 가능한 각각의 상태들에 대한 확률을 나타내는 행렬<br>4) B : Observation symbol probability distribution<br>B = {bⱼ(vₖ)}, 1 ≤ i ≤ N, 1 ≤ j ≤ M |
| **파이 벡터** | 특정 은닉상태가 시간 t = 1 일 때, 모델의 확률<br>5) Π : Initial state distribution<br>πᵢ = P(q₁ = i), 1 ≤ i ≤ N |

---

## 연계 토픽

- [MDP](/docs/ai/01-machine-learning/mdp)
- [강화학습](/docs/ai/01-machine-learning/reinforcement-learning)

---

## 학습 체크리스트

- [ ] HMM의 정의와 개념 이해
- [ ] HMM 유형(Ergodic, Left to Right) 차이점 파악
- [ ] 구성요소(A, B, Π) 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
