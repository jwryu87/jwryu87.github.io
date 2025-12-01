---
layout: default
title: 과적합/과소적합
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 18
---

# 과적합(Overfitting), 과소적합(Underfitting)
{: .fs-8 }

모델 성능
{: .label .label-yellow }

---

## 핵심 키워드

- **과적합**: 저편향, 고분산
- **과소적합**: 고편향, 저분산

---

## 정의/개념

- **과적합(Overfitting)**: 샘플데이터에 너무 정확하게 학습되어 샘플데이터에는 정확도가 높지만 다른 데이터에서는 정확도가 떨어지는 현상
- **과소적합(Underfitting)**: 샘플데이터가 모자라거나 제대로 학습이 되지 않아 학습데이터에 대해서도 정확한 결과를 도출하지 못하는 현상

---

## 과적합 (Overfitting)

| 구분 | 원인/방안 | 상세설명 |
|:-----|:---------|:--------|
| **발생원인** | 학습데이터의 노이즈 | 학습데이터가 대표성을 가지지 못하는 경우 |
| | 독립변수의 과다 | 고려해야 할 독립변수가 너무 많아 차원의 저주 발생 |
| | 모델의 복잡성 과다 | 오컴의 면도날의 원리를 위배하여 복잡한 모델이 생성되어 독립변수와 종속변수간의 관계 설명 실패 |
| **대응방안** | Regularization(정규화) | 데이터를 일정한 규칙에 따라 변형하여 Coefficient(계수값)를 낮추는 방법 |
| | Cross Validation(교차검증) | 샘플데이터를 Training Data와 Test Data로 구분하여 교차검증 |
| | 충분한 데이터 | 충분한 데이터로 Training Set, Validation Set, Test Set으로 나누어 교차 검증 |
| | Reduce Dimension(차원축소) | 비중이 다른 Features가 섞이면 좋지 않은 결과 발생하므로 Feature를 축소 |
| | Drop out | 전체 노드의 Weight(가중치) 중 Layer에 포함된 주요 노드 Weight의 일부만 연산에 참여 |
| | 조기종료(Early Stopping) | 딥러닝에서 학습을 반복하다가 Validation Accuracy가 더 이상 상승하지 않을 때 정지 |

---

## 과소적합 (Underfitting)

| 구분 | 원인/방안 | 상세설명 |
|:-----|:---------|:--------|
| **발생원인** | Less Features | Feature(차원)가 너무 단순하여 학습정확도 저하 |
| | Gradient Vanishing | Back Propagation에서 Sigmoid함수로 인해 Gradient Vanishing 문제 발생시 언더피팅 발생 |
| **대응방안** | Find More Features | Feature(차원, 변수)를 추가하여 Variance를 증가 |
| | 학습모델 변경 | High Variance 기계학습모델인 의사결정트리, K-NN, SVM과 같은 학습모델을 사용 |
| | ReLU함수 사용 | Sigmoid 함수를 ReLu함수로 대체 |

---

## 적정 수준의 학습을 통한 적정적합(Generalized-fitted) 모델

```
                             저편향                 고편향
                        ┌─────────────────────────────────┐
                        │      적정 포인트                 │
                   저분산│         ●                       │
                        │        ╱ ╲    에러율            │
                        │       ╱   ╲                     │
                   편향  │      ╱     ╲                    │
                        │     ╱       ╲                   │
                        │    ╱    분산  ╲                  │
                   고분산│   ╱           ╲                 │
                        │  언더피팅      오버피팅           │
                        │  에 가까워짐   에 가까워짐         │
                        └─────────────────────────────────┘
```

> 에러율을 가장 낮출 수 있도록 최대의 효과를 얻을 수 있는 적정 포인트를 갖는 적정 적합 모델 도출 필요

---

## 연계 토픽

- [Bias-Variance](/docs/ai/09-model-performance/bias-variance)
- [Cross Validation](/docs/ai/06-ml-evaluation/cross-validation)
- [정규화](/docs/ai/01-machine-learning/parameters)

---

## 학습 체크리스트

- [ ] 과적합과 과소적합의 정의와 차이 이해
- [ ] 각각의 발생원인과 대응방안 암기
- [ ] 적정적합 모델 도출의 중요성 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
