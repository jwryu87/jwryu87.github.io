---
layout: default
title: 모델 평가 방법
parent: 6. ML 평가/검증
grand_parent: AI (인공지능)
nav_order: 2
---

# 머신러닝 모델 평가방법
{: .fs-8 }

머신러닝 검증
{: .label .label-blue }

---

## 핵심 키워드

`혼동행렬` `ROC Curve` `AUC` `RMSE` `Dunn's Index`

---

## 평가 방법 분류

머신러닝 모델 평가는 크게 **예측값과 실제값 비교 기반**과 **그래프 시각화 기반**으로 나눕니다.

---

## 예측값과 실제값 비교 기반

| 평가방법 | 세부기법 | 설명 |
|:---------|:--------|:-----|
| **혼동행렬 (Confusion Matrix)** | TP, FP, FN, TN | 데이터 분석에서 잘못된 예측의 영향을 간편하게 파악하기 위해 예측된 값과 실제 값이 일치하는지 여부를 행렬로 분류하는 모델 평가 기법 |
| **평균 제곱근 오차 (RMSE)** | Root Mean Squared Error | 데이터들의 오차를 계산하여 제곱근을 통해 절대값으로 회귀 문제 평가하는 기법<br>$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(p_i - y_i)^2}$ |
| **Dunn's Index** | 클러스터링 평가 | 컴팩트하고 다른 군집과 잘 분리됨을 나타내는 척도<br>- 클러스터간 거리 최소값 / 클러스터 사이즈 최대값<br>$DI_m = \frac{\min_{1 \le i < j \le n}\delta(C_i, C_j)}{\max_{1 \le k \le m}\Delta_k}$ |

---

## 그래프 시각화 기반

| 평가방법 | 세부기법 | 설명 |
|:---------|:--------|:-----|
| **ROC, AUC** | ROC Curve | 평가지식 정량화, 평가결과 시각화<br>- FP Rate(1-특이도) 대비 민감도 그래프 기반 평가 기법<br>- TPR, FRR, AUC = 1(최고), 0.5(성능 0) |
| **Precision Recall Plot** | PR Curve | 라벨 분포 불균등 결과 판단에 유리<br>- Precision, Recall baseline = P/(P+N) |

---

## ROC Curve

```
         TPR (민감도)
          ↑
        1 ┤        ┌────────────┐
          │       /             │
          │      /              │
          │     /  AUC          │
          │    /                │
          │   /                 │
          │  /                  │
        0 ┼──────────────────────→ FPR
          0                    1
```

> **AUC(Area Under Curve)**: ROC 커브 면적으로 측정되며 '1'에 가까울수록 학습모델의 성능이 우수함

---

## 평가 지표 요약

| 지표 | 수식 | 목적 |
|:-----|:-----|:-----|
| **RMSE** | $\sqrt{\frac{1}{n}\sum(p_i - y_i)^2}$ | 회귀 오차 측정 |
| **ROC-AUC** | 곡선 아래 면적 | 분류 성능 평가 |
| **Dunn's Index** | 클러스터 분리도 | 클러스터링 품질 |

---

## 연계 토픽

- [Confusion Matrix](/docs/ai/06-ml-evaluation/confusion-matrix)
- [ROC Curve](/docs/ai/06-ml-evaluation/roc-curve)
- [Precision & Recall](/docs/ai/06-ml-evaluation/precision-recall)

---

## 학습 체크리스트

- [ ] 예측값 비교 기반 vs 그래프 시각화 기반 구분
- [ ] RMSE 수식 이해
- [ ] ROC-AUC의 의미 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
