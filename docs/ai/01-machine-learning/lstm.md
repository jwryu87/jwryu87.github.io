---
layout: default
title: LSTM
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 24
---

# LSTM(Long Short Term Memory)
{: .fs-8 }

5.1 딥러닝
{: .label .label-blue }

> 암기: **시시탄시탄** (Sigmoid, Sigmoid, tanh, Sigmoid, tanh)

---

## 핵심 키워드

`Input gate` `Output gate` `Forget gate`

---

## 정의/개념

RNN 장기 의존성으로 인한 기울기 소실 문제 해결, input, output, forget gate 구성 신경망 알고리즘

---

## 개념도

```
                                    ┌──────────────────────────────────────┐
                                    │                                      │
    C_t-1  ────────────────→  [×] ─────────→ [+] ─────────────────→ C_t
                               ↑              ↑
                               │         ┌────┴────┐
                               f_t       │   [×]   │
                               │         │    ↑    │
                        ┌──────┴───┐     i_t  │    │
                        │   σ      │     │   tanh  │
                        │ Forget   │     │    │    │
                        │  Gate    │     │    │    │
                        └────┬─────┘     └────┴────┘
                             │
    h_t-1 ──────────────────────────────────────────────────────→ [tanh] ─→ [×] ─→ h_t
                                                                    ↑         ↑
                                                                    │        o_t
                                                                   C_t        │
                                                                              │
                        ┌────────────┐   ┌────────────┐   ┌────────────┐     │
                        │   Forget   │   │   Input    │   │   Output   │     │
                        │    Gate    │   │    Gate    │   │    Gate    │─────┘
                        └────────────┘   └────────────┘   └────────────┘
    x_t ────────────────────────────────────────────────────────────→
```

> 단일 뉴럴 네트워크 레이어를 가지는 대신 4개의 상호작용 가능한 구조를 가지고 있음

---

## 구성요소

| 구분 | 설명 | 특징 |
|:-----|:-----|:-----|
| **Cell State** | 이전 정보에 마이너 한 선형 연산을 거쳐 다음단계로 정보를 전달 | Forget Gate와의 × 연산, Input Gate와 + 연산으로 전달할 Cell 상태 결정 |
| **Forget Gate** | cell state에서 어떤 정보를 버릴지 선택<br>0과 1 사이의 출력값을 가지는 ht-1과 xt를 입력값으로 받아 출력값이 1이면 유지, 값이 0이면 버림 | $f_t = σ(W_f·[h_{t-1},x_t] + b_f)$<br>시그모이드 함수를 이용 0과 1사이의 값을 출력함으로써 이전 값이 유지, 삭제 여부 결정 |
| **Input Gate** | 새로운 정보가 cell state에 저장될지 결정<br>input gate: 어떤 값을 업데이트 할지결정<br>tanh 레이어는 cell state에 더해질 새로운 후보 값을 생성<br>두가지를 합쳐서 다음 스테이트로 업데이트 | $i_t = σ(W_i·[h_{t-1},x_t] + b_i)$<br>$\tilde{C}_t = tanh(W_C·[h_{t-1},x_t] + b_C)$<br>시그모이드로 어떠한 값을 업데이트할지 결정하고, tanh 레이어에서 Cell state에 더해질 후보값 생성 |
| **Output Gate** | 어떤 출력값을 출력할지 결정<br>cell state를 tanh 함수를 거쳐 1과 1사이 값을 생성, output gate의 출력값과 곱하여 결과값 반영 | $o_t = σ(W_o·[h_{t-1},x_t] + b_o)$<br>$h_t = o_t * tanh(C_t)$<br>tanh함수와 시그모이드 출력을 곱하여 원하는 값만 반영하여 출력 |

> LSTM의 복잡성 개선을 위해 GRU 사용

---

## 연계 토픽

- [RNN](/docs/ai/01-machine-learning/rnn)
- [GRU](/docs/ai/01-machine-learning/gru)
- [기울기 소실](/docs/ai/01-machine-learning/vanishing-gradient)

---

## 학습 체크리스트

- [ ] LSTM의 정의와 개념도 이해
- [ ] 3가지 게이트(Forget, Input, Output) 역할 암기
- [ ] Cell State의 역할 이해
- [ ] RNN 장기 의존성 문제 해결 방법 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
