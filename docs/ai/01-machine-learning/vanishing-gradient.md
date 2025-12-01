---
layout: default
title: 기울기 소실 문제
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 17
---

# 기울기 소실 문제(Vanishing Gradient Problem)
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 핵심 키워드

`오차 미전달` `지역 최소점`

---

## 정의/개념

심층 신경망 역전파 알고리즘 이용 학습 시 앞쪽 은닉층으로 오차 전달되지 않는 현상

---

## 발생원인

| 구분 | 발생 원인 | 핵심 |
|:-----|:---------|:-----|
| **Layer 측면** | 복잡한 문제 해결 위한 층 확장 | Local Minimum 수렴 |
| **활성함수 측면** | 시그모이드 함수 Squash 특성 | 역전파 시 최대 미분값 1/4 |

---

## 해결방안

| 구분 | 해결방안 | 핵심 |
|:-----|:---------|:-----|
| **학습 효율성 향상 측면** | LSTM 활용 | 메모리 기억 기반 |
| | DBN 활용 | 사전 학습 기반 |
| **활성함수 개선 측면** | ReLU | 미분 값 보존 |
| | Leaky ReLU | 음의 값 활용 |

---

## ReLU vs Leaky ReLU

| 구분 | ReLU | Leaky ReLU |
|:-----|:-----|:----------|
| **수식** | $f(x) = max(0, x)$ | $f(x) = max(αx, x)$ |
| **특징** | x가 음수일 경우 0 출력 | x가 음수일 경우에도 작은 기울기 유지 |
| **장점** | 계산 효율성, 기울기 소실 해결 | Dead ReLU 문제 해결 |

---

## 연계 토픽

- [오류역전파](/docs/ai/01-machine-learning/perceptron)
- [활성화 함수](/docs/ai/01-machine-learning/activation-function)
- [LSTM](/docs/ai/01-machine-learning/lstm)

---

## 학습 체크리스트

- [ ] 기울기 소실 문제의 정의와 발생원인 이해
- [ ] Layer 측면, 활성함수 측면 원인 파악
- [ ] 해결방안(LSTM, ReLU, Leaky ReLU) 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
