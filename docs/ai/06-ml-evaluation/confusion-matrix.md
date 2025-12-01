---
layout: default
title: Confusion Matrix
parent: 6. ML 평가/검증
grand_parent: AI (인공지능)
nav_order: 3
---

# 혼동행렬(Confusion Matrix)
{: .fs-8 }

머신러닝 검증
{: .label .label-blue }

---

## 핵심 키워드

`정확도` `재현율` `특이도` `정밀도` `F1-Score`

---

## 정의/개념

통계적 분류 문제에서 분류 알고리즘 성능을 시각화하여, 예측값이 실제 관측값을 얼마나 정확하게 예측했는지 보여주는 행렬

---

## 혼동행렬의 구성

|  | **Condition(실제)** | |
|:--:|:--:|:--:|
| **Prediction(예측)** | **Positive** | **Negative** |
| **Positive** | **TP** (True Positive) | **FP** (False Positive) |
| **Negative** | **FN** (False Negative) | **TN** (True Negative) |

### 각 항목의 의미

| 항목 | 설명 |
|:-----|:-----|
| **TP(True Positive)** | 실제 관측한 값이 참으로 예측한 결과와 같음, 관심 범주를 정확하게 분류 |
| **FP(False Positive)** | 실제 결과는 거짓인데 참으로 예측한 경우로 관심 범주로 잘못 분류 |
| **FN(False Negative)** | 실제 결과가 참인데 거짓으로 예측한 경우로 관심 범주가 아닌 것으로 잘못 분류 |
| **TN(True Negative)** | 실제 관측한 값이 거짓으로 예측한 결과와 같음, 관심 범주가 아닌 것을 정확히 분류 |

> 혼동행렬을 이용하여 각각의 경우에 대한 비율을 구함으로써 알고리즘의 성능을 평가

---

## 성능평가 항목

| 항목 | 산식 | 설명 |
|:-----|:-----|:-----|
| **Error Rate (오차 비율)** | $\frac{FP + FN}{TP + FP + FN + TN}$ | 오류율<br>- 분류 범주를 잘못 분류한 비율 = 1 - 정확도<br>- 전체 데이터 수에서 잘못 분류한 데이터 수의 비율 |
| **Accuracy (정확도)** | $\frac{TP + TN}{TP + FP + FN + TN}$ | 분류 범주를 정확하게 예측한 비율<br>- 전체 중에서 올바르게 실제 범주를 추정한 전체 비율<br>- 오류율과 상반된 개념 |
| **Recall (재현율)** | $\frac{TP}{TP + FN}$ | 진양성율, Sensitivity, True Negative Rate<br>- Positive인 범주 중 Positive로 올바르게 예측(TP)된 비율<br>- 실제 참인 경우를 참으로 분류하여 판정하는 비율 |
| **Specificity (특이도)** | $\frac{TN}{TN + FP}$ | Negative인 범주 중 부정으로 올바르게 예측(TN)한 비율<br>- 1 – FP Rate<br>- 실제 거짓인 경우를 거짓으로 분류하여 판정하는 비율 |
| **Precision (정밀도)** | $\frac{TP}{TP + FP}$ | Positive로 예측한 비율 중에서 실제 긍정(TP)인 비율 |
| **FP Rate** | $\frac{FP}{TN + FP}$ | Negative인 범주 중 긍정으로 잘못 예측(FP)한 비율<br>- 1 – 특이도 |
| **F1 Score** | $\frac{2 \times Precision \times Recall}{Precision + Recall}$ | 정밀도와 재현율을 하나로 합친 성능 평가지표<br>- 정밀도와 재현율의 조화 평균<br>- 0~1 사이의 범위를 가짐 |
| **Kappa** | $\frac{Accuracy - Pr(e)}{1 - Pr(e)}$ | 코헨의 카파 계수<br>- Pr(e): 두 평가자의 평가가 우연히 일치할 확률<br>- 모델의 예측값과 실제값이 우연히 일치할 확률을 제외한 위의 값으로 0~1 사이의 값을 가짐<br>- 1에 가까울수록 모델의 예측값과 실제값이 정확히 일치하고 0에 가까울수록 불일치 |

---

## 주요 지표 관계도

```
                    ┌─────────────────┐
                    │  Confusion Matrix │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐         ┌─────────┐         ┌─────────┐
   │ Accuracy│         │Precision│         │ Recall  │
   └─────────┘         └────┬────┘         └────┬────┘
                            │                   │
                            └─────────┬─────────┘
                                      │
                                      ▼
                               ┌───────────┐
                               │ F1-Score  │
                               └───────────┘
```

---

## 활용 시나리오

| 시나리오 | 중요 지표 | 이유 |
|:---------|:---------|:-----|
| **암 진단** | Recall (재현율) | 실제 양성을 놓치면 안됨 |
| **스팸 필터** | Precision (정밀도) | 정상 메일을 스팸으로 분류하면 안됨 |
| **균형 데이터** | F1-Score | 정밀도와 재현율 모두 중요 |

---

## 연계 토픽

- [ROC Curve](/docs/ai/06-ml-evaluation/roc-curve)
- [Precision & Recall](/docs/ai/06-ml-evaluation/precision-recall)
- [모델 평가 방법](/docs/ai/06-ml-evaluation/model-evaluation)

---

## 학습 체크리스트

- [ ] TP, FP, FN, TN의 의미 이해
- [ ] Accuracy, Precision, Recall, F1-Score 수식 암기
- [ ] 시나리오별 적합한 평가 지표 선택

---

## 참고자료

- 정보관리기술사 AI 학습자료
