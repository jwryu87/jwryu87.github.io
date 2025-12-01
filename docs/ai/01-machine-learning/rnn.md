---
layout: default
title: RNN
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 23
---

# RNN(Recurrent Neural Network)
{: .fs-8 }

5.1 딥러닝
{: .label .label-blue }

---

## 핵심 키워드

`Directed Cycle 구조` `Recurrent Weight` `BPTT` `Sequential Data`

---

## 정의/개념

Directed Cycle 구조, Recurrent Weight, BPTT, Sequential Data 사용 신경망 알고리즘

> RNN에 대한 기본적인 아이디어는 순차적인 정보를 처리한다는 데 있음

---

## 개념도

```
                o              o              o
                ↑              ↑              ↑
                V              V              V
    s    W           s_t-1          s_t           s_t+1
    ─────────   ─────────────────────────────────────────
              W      W      W      W      W      W
    Unfold  ═══════════════════════════════════════════
              U              U              U
              ↑              ↑              ↑
    x         x             x_t-1          x_t           x_t+1
```

- **Xt**: 시간스텝 t에서의 입력값
- **St**: 시간스텝 t에서의 hidden state
- **Ot**: 시간스텝 t에서의 출력값

---

## 구성요소

| 구분 | 핵심 기술 | 설명 |
|:-----|:---------|:-----|
| **신경망 구조** | Input Layer | Sequential Data를 Input으로 사용 |
| | Hidden Layer | 활성화 함수 tanh, ReLU 등을 사용 |
| | Output Layer | Prediction Data<br>RNN을 통해 최종 예측된 값 |
| **원리** | Recurrent Weight | Hidden Layer간 연결시 가중치 |
| | BPTT (Backpropagation Through Time) | 일정 시간 동안 에러 값들을 합한 값을 역전파<br>현재 시간의 에러를 과거 시간 상태까지 역전파 |
| | Sequential Data | 데이터 집합 내의 객체들이 어떤 순서를 가진 데이터<br>순서 정보 유실될 경우 데이터 고유 특성 상실 |

> RNN의 순환 구조로 인해 은닉층의 깊이가 깊어질수록 장기 의존성 문제가 발생하여 LSTM으로 발전

---

## 연계 토픽

- [LSTM](/docs/ai/01-machine-learning/lstm)
- [GRU](/docs/ai/01-machine-learning/gru)
- [CNN](/docs/ai/02-deep-learning/cnn)

---

## 학습 체크리스트

- [ ] RNN의 정의와 개념도 이해
- [ ] 구성요소(Input/Hidden/Output Layer) 파악
- [ ] BPTT 역전파 개념 이해
- [ ] Sequential Data의 특성 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
