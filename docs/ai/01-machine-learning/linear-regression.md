---
layout: default
title: 선형 회귀
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 7
---

# 선형 회귀(Linear Regression)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 핵심 키워드

`연속형` `최소자승법` `Gradient Descent`

---

## 정의/개념

종속변수 y와 한 개 이상의 독립변수 x와의 선형 상관관계를 모델링하는 회귀분석 기법

---

## 선형 회귀분석 vs 로지스틱 회귀분석

| 구분 | 선형 회귀분석 | 로지스틱 회귀분석 |
|:-----|:-------------|:-----------------|
| **개념** | 종속변수 y와 한 개 이상의 독립변수 x와의 선형 상관관계를 모델링하는 회귀분석 기법 | 데이터를 두개의 그룹으로 분류하기 위해 사용되는, 종속변수의 값이 0또는 1인 회귀분석 기법 |
| **종속변수** | 연속형 | 이산형 |
| **모형탐색방법** | 최소자승법 | 최대우도법, 가중최소자승법 |
| **선형회귀식** | $y = \beta x + \varepsilon$ | $y(x) = \frac{1}{1 + e^{-x}}$ |
| **최적화** | Gradient Descent | Cross Entropy |
| **목적** | 예측기반 | 분류기반 |
| **활성함수** | 선형함수 | Sigmoid |
| **종류** | 단순선형 회귀분석, 다중선형 회귀분석 | 로지스틱 회귀분석 |

---

## 연계 토픽

- [로지스틱 회귀](/docs/ai/01-machine-learning/logistic-regression)
- [회귀분석](/docs/ai/01-machine-learning/regression-analysis)

---

## 학습 체크리스트

- [ ] 선형 회귀의 정의와 수식 이해
- [ ] 선형 회귀 vs 로지스틱 회귀 차이점 암기
- [ ] 최소자승법과 Gradient Descent 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
