---
layout: default
title: Optimizer
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 6
---

# 딥러닝 옵티마이저(Optimizer)
{: .fs-8 }

5.2 퍼셉트론
{: .label .label-purple }

---

## 핵심 키워드

`가중치 갱신` `epoch` `러닝레이트` `경사하강법` `SGD` `Momentum` `NAG` `AdaGrad` `RMSProp` `AdaDelta` `Adam`

---

## 정의/개념

손실함수의 최소값을 찾기 위해 신경망의 가중치를 갱신하여 신경망 모델을 최적화하는 알고리즘

---

## 옵티마이저 유형

| 유형 | 수식 | 설명 |
|:-----|:-----|:-----|
| **SGD (Stochastic Gradient Descent)** | $\omega_t = \omega_{t-1} - η \frac{\partial L}{\partial \omega}$ | 학습률 기준으로 손실함수그래프 경사를 가면서 가중치 Update하는 알고리즘<br>오버슈팅 문제 및 지역 최소점(Local Minimum) 문제가 발생 |
| **Momentum** | $V_t = m × V_{t-1} - η∇_\omega J(\omega_t)$<br>$\omega_{t+1} = \omega_t + V_t$ | 이동거리와 관성계수에 따라 파라미터를 업데이트하는 옵티마이저<br>SGD에 관성의 개념을 적용하여 지역최소점 문제를 해결 |
| **NAG (Nesterov Accelerated Gradient)** | $V_t = m × V_{t-1} - η∇_\omega J(\omega_t - m × V_{t-1})$<br>$\omega_{t+1} = \omega_t + V_t$ | Momentum으로 이동된 지점에서의 기울기를 활용하여 업데이트를 수행<br>관성에 의해 빨리 이동하는 이점을 누리면서 전역최소점에 중지해야 하는곳에 효과적으로 제동하여 Momentum의 오버슈팅(Over Shooting) 문제를 해결 |
| **AdaGrad** | $G_t = G_{t-1} - η∇_\omega J(\omega_t)^2 = \sum_{i=1}^{k}∇_\omega J(\omega_i)$<br>$\omega_{t+1} = \omega_t - \frac{η}{\sqrt{G_t + ε}}∇_\omega J(\omega_t)$ | 각각의 파라미터에 개별 기준을 적용해 업데이트하는 알고리즘<br>최적화된 파라미터는 작은 변화를 주고 적게 이동한 파라미터는 큰 변화 적용<br>파라미터별 업데이트를 하는 개념은 장점이나 학습이 진행됨에 따라 변화의 폭이 눈에 띄게 감소 |
| **RMSProp** | $G_t = γG_{t-1} + (1-γ)(∇_\omega J(\omega_t))^2$<br>$\omega_{t+1} = \omega_t - \frac{η}{\sqrt{G_t + ε}}∇_\omega J(\omega_t)$ | Adagrad의 문제점을 개선하기 위해 지수이동평균법을 적용한 옵티마이저<br>지수이동평균법을 이용하여 학습이 진행됨에 따라 파라미터사이 차별하는 유지하되 학습의 최소 Step 유지하여 0에 수렴하는 것을 방지 |
| **AdaDelta** | $\Delta_\omega = \frac{\sqrt{s + ε}}{\sqrt{G_t + ε}} · ∇_\omega J(\omega_t)$<br>$\omega_{t+1} = \omega_t - \Delta_\omega$<br>$s = γs + (1-γ)\Delta_\omega^2$ | Adagrad의 개선을 위해 제안된 방법<br>일수 계산은 RMSProp와 동일하게 수행되지만 가중치를 업데이트하는 과정에서 학습률을 사용하지 않음 |
| **Adam** | $m_t = β_1 m_{t-1} + (1-β_1)∇_\omega J(\omega_t)$<br>$v_t = β_2 m_{t-1} + (1-β_2)(∇_\omega J(\omega_t))^2$<br>$\omega_{t+1} = \omega_t - m_t \frac{η}{\sqrt{V_t + ε}}$ | RMSProp와 Momentum의 기법을 합친 옵티마이저<br>기울기 값과 기울기의 제곱값의 지수이동평균을 활용하여 Step변화량을 조절 |

---

## 연계 토픽

- [경사하강법](/docs/ai/01-machine-learning/activation-function)
- [역전파](/docs/ai/02-deep-learning/mlp)

---

## 학습 체크리스트

- [ ] 옵티마이저의 정의와 목적 이해
- [ ] 각 옵티마이저(SGD, Momentum, Adam 등)의 특징 암기
- [ ] 수식과 동작 원리 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
