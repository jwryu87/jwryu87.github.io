---
layout: default
title: KNN
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 13
---

# KNN(K Near Neighborhood)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 핵심 키워드

`Fingerprint` `유클라디안` `맨하튼 거리`

---

## 정의/개념

Fingerprint 내 거리기반 K개 데이터 추출, 유클리디안, 맨하튼 거리 사용 분류 알고리즘

---

## 개념도

```
        Y-Axis
           │
           │     ★ ★        Class A (★)
           │   ★ ★ ★        Class B (▲)
           │     ★ ★
           │      ⬜ ← New example to classify
           │  K=3 ○───┐
           │   K=7 ○───┼─▲ ▲ ▲ ▲
           │         ▲ ▲ ▲
           └──────────────────── X-Axis
```

---

## 프로세스

| # | 프로세스 |
|:--|:--------|
| 1 | 새로운 Fingerprint 확인 |
| 2 | 거리 기반 K개 데이터를 Training Set에서 추출 |
| 3 | 추출 데이터 분류 확인 |
| 4 | 다수결로 분류 매핑 |

---

## 구성요소

| 구분 | 설명 |
|:-----|:-----|
| **K 의미** | 다수결 이후 완료 |
| **거리측정** | 유클리디안 거리, 마할라노비스 거리 |

---

## 연계 토픽

- [K-Means](/docs/ai/01-machine-learning/k-means)
- [SVM](/docs/ai/01-machine-learning/svm)

---

## 학습 체크리스트

- [ ] KNN 알고리즘의 정의와 프로세스 이해
- [ ] K 값의 의미와 선택 방법 파악
- [ ] 거리 측정 방법(유클리디안, 맨하튼) 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
