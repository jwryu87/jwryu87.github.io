---
layout: default
title: MLP
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 5
---

# MLP(Multi Layer Perceptron)
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 핵심 키워드

`Input Layer` `Hidden Layer` `Output Layer`

---

## 정의/개념

단층 퍼셉트론 XOR 문제 해결, 은닉층 다수 보유 피드포워드 신경망 네트워크

---

## 개념도

```
    Input 1  ──────→○──┐
                      ╲
    Input 2  ──────→○──┼──→○──→ Property 1
                      │      ╲
    Input 3  ──────→○──┤       ╲
                      │        ○──→ Property 2
    Input 4  ──────→○──┤       ╱
                      │      ╱
    Input 5  ──────→○──┴──→○──╱

    ├──────────┤ ├────────┤ ├──────────┤
      Input       Hidden      Output
      layer       layer       layer
```

---

## 구성요소

| # | 기법 | 핵심 |
|:--|:-----|:-----|
| 1 | **Input Layer** | 입력값 구성 |
| 2 | **Hidden Layer** | 활성화 함수 적용, 피드포워드 사용 |
| 3 | **Output Layer** | 모델 출력값 |

> 다층 퍼셉트론 문제점으로 기울기 소실 문제와 기울기 폭주 문제가 발생

---

## 문제점 및 해결방안

| 기법 | 핵심 |
|:-----|:-----|
| **역전파** | 가중치 갱신 신경망 학습 |
| **경사하강법** | Local Minimum 찾기 |
| **규제화** | Dropout |

---

## 연계 토픽

- [퍼셉트론](/docs/ai/01-machine-learning/perceptron)
- [역전파](/docs/ai/02-deep-learning/mlp)
- [경사하강법](/docs/ai/01-machine-learning/activation-function)
- [Dropout](/docs/ai/02-deep-learning/dropout)

---

## 학습 체크리스트

- [ ] MLP의 정의와 개념도 이해
- [ ] 3가지 Layer(Input, Hidden, Output) 역할 암기
- [ ] 문제점(기울기 소실/폭주)과 해결방안 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
