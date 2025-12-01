---
layout: default
title: GRU
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 25
---

# GRU(Gated Recurrent Units)
{: .fs-8 }

5.1 딥러닝
{: .label .label-blue }

> 암기: **시시탄** (Sigmoid, Sigmoid, tanh)

---

## 핵심 키워드

`Update Gate` `Reset Gate`

---

## 정의/개념

RNN 기울기 소실 문제 해결, Update, Reset Gate 구성 신경망 알고리즘

---

## 개념도

```
                    Hidden state
                      H_t-1       ─────────○─────────[+]─────────→ H_t
                                            │         ↑
                                           │1-│      │
                                            │        │
                                           [⊗]      [⊗]
                                            ↑        ↑
                        ┌───────────────────┼────────┤
                        │                   │        │
                       [σ]                 [σ]     [tanh] .... Candidate
                        │                   │        │         hidden state
                      R_t                  Z_t      H̃_t
                    Reset                Update
                    gate                  gate
                        └───────────────────┴────────┘
                                    │
                                 Input X_t
```

> Gate의 축소로 인하여 간결성 기반으로 정보에 대한 학습 수행

---

## 구성요소

| 구분 | 개념도 | 설명 |
|:-----|:------|:-----|
| **Reset Gate** | $r^{(t)} = σ(W_r h^{(t-1)} + U_r x^{(t)})$ | 과거의 정보를 적당히 리셋<br>Sigmoid 함수를 출력으로 이용해 0과 1 값을 유지<br>은닉층에 곱을 연산 |
| **Update Gate** | $u^{(t)} = σ(W_u h^{(t-1)} + U_u x^{(t)})$ | 과거와 현재의 정보의 최신화 비율을 결정<br>Sigmoid 통한 현시점 정보의 양 결정<br>1-Sigmoid 통해 직전 시점의 정보 결정 |
| **Candidate** | $\tilde{h}^{(t)} = τ(W_h (r^{(t)} * h^{(t-1)}) + U_h x^{(t)})$ | 현 시점의 정보 후보군을 게산하는 단계<br>은닉층의 정보를 그대로 이용하지 않고 리셋 게이트의 결과에 곱을 연산하여 이용 |
| **Hidden Layer Calculation** | $h^{(t)} = (1-u^{(t)}) * h^{(t-1)} + u^{(t)} * \tilde{h}^{(t)}$ | update gate 결과와 candidate 결과를 결합 |

---

## LSTM vs GRU 비교

| 구분 | LSTM | GRU |
|:-----|:-----|:-----|
| **게이트 수** | 3개 (Input, Output, Forget) | 2개 (Update, Reset) |
| **복잡도** | 높음 | 낮음 (LSTM 경량화) |
| **Cell State** | 있음 | 없음 |
| **파라미터** | 많음 | 적음 |
| **학습 속도** | 느림 | 빠름 |

---

## 연계 토픽

- [RNN](/docs/ai/01-machine-learning/rnn)
- [LSTM](/docs/ai/01-machine-learning/lstm)

---

## 학습 체크리스트

- [ ] GRU의 정의와 개념도 이해
- [ ] Reset Gate, Update Gate 역할 암기
- [ ] LSTM과의 차이점 파악
- [ ] 수식 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
