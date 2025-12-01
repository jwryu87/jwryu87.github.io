---
layout: default
title: Cross Validation
parent: 6. ML 평가/검증
grand_parent: AI (인공지능)
nav_order: 1
---

# 머신러닝 교차검증(Cross Validation)
{: .fs-8 }

머신러닝 검증
{: .label .label-blue }

---

## 핵심 키워드

`Train Set` `Validation Set` `Test Set` `K-fold` `LOOCV` `LpOCV` `과적합/학습데이터 부족 해결`

---

## 정의/개념

학습 데이터 부족 현상 극복 및 평균성능(Mean Performance)과 성능분산(Performance Variance)을 구하기 위하여 Training set, Validation Set을 교차하여 사용하는 Overfitting 방지를 위한 기법

---

## 교차검증 기법 비교

| 기법 | 영문명 | 방법 | 특징 |
|:-----|:------|:-----|:-----|
| **홀드 아웃 교차 검증** | Holdout Cross Validation | 비복원추출<br>랜덤으로 나눔 | 데이터손실O<br>계산/비용적음 |
| **랜덤 서브 샘플링** | Random Sub-Sampling | 무작위랜덤추출<br>홀드아웃반복 | 비용 가장적음 |
| **K-Fold** | K-Fold Cross Validation | 무작위추출<br>동등분할<br>부분집합 K개<br>평가집합 1개 | 전체데이터N개<br>평가데이터1개<br>작은데이터적합<br>비용 가장비쌈 |
| **LOOCV** | Leave-One-Out Cross Valid. | 전체데이터N개<br>평가데이터1개<br>작은데이터적합 | - |
| **LpOCV** | Leave-p-Out Cross Valid. | 전체데이터N개<br>평가데이터p개<br>계산시간부담↑<br>nCp번 반복 | - |
| **RLT** | Repeated Learning-Testing | 비복원추출<br>랜덤추출<br>평균오류율계산 | - |
| **부트스트랩** | Bootstrap | 단순랜덤<br>복원추출(중복O)<br>동일크기표본옴<br>여러개생성함 | - |

---

## 시각화

```
┌─────────────────────────────────────────────────────────────────┐
│ Holdout          K-Fold            LOOCV           LpOCV        │
│                                                                 │
│ ┌─────┬─────┐   ┌─────┬───┐       ┌─┬─────┐      ┌─┬─┬─────┐   │
│ │Train│Test │   │Train│   │       │1│Train│      │p│p│Train│   │
│ └─────┴─────┘   ├─────┼───┤       ├─┼─────┤      ├─┼─┼─────┤   │
│                 │Train│   │       │2│Train│      │p│p│Train│   │
│                 ├─────┼───┤       ├─┼─────┤      ├─┼─┼─────┤   │
│                 │Train│   │       │ │     │      │ │ │     │   │
│                 ├─────┼───┤       │:│  :  │      │:│:│  :  │   │
│                 │     │   │       ├─┼─────┤      ├─┼─┼─────┤   │
│                 └─────┴───┘       │n│Train│      │ │p│Train│   │
│                                   └─┴─────┘      └─┴─┴─────┘   │
│                                                                 │
│ RLT                                                             │
│ ┌─┬─────┬─┬─┐                                                   │
│ │ │Train│ │ │                                                   │
│ ├─┼─────┼─┼─┤  → Test                                           │
│ │ │     │ │ │                                                   │
│ └─┴─────┴─┴─┘                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 기법 선택 가이드

| 상황 | 권장 기법 |
|:-----|:---------|
| 데이터 충분 | Hold-out |
| 데이터 부족 | K-Fold, LOOCV |
| 계산 자원 제한 | Random Sub-Sampling |
| 정밀한 평가 필요 | K-Fold (K=5 or 10) |

---

## 연계 토픽

- [모델 평가 방법](/docs/ai/06-ml-evaluation/model-evaluation)
- [Confusion Matrix](/docs/ai/06-ml-evaluation/confusion-matrix)
- [과적합/과소적합](/docs/ai/01-machine-learning/overfitting-underfitting)

---

## 학습 체크리스트

- [ ] 교차검증의 목적과 필요성 이해
- [ ] 7가지 기법의 특징 및 차이점 파악
- [ ] K-Fold, LOOCV, LpOCV 구분

---

## 참고자료

- 정보관리기술사 AI 학습자료
