---
layout: default
title: SVM
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 14
---

# SVM(Support Vector Machine)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 핵심 키워드

`결정경계` `Support Vector` `Margin` `Hyperplane(초평면)` `Slack 변수` `OSH` `하드 마진` `소프트 마진`

---

## 정의/개념

데이터 사상된 공간 Support Vector간 거리가 가장 큰 경계 식별 지도학습 기반 알고리즘

---

## 개념도

```
  X₂ ↑  최대 마진
     │  ─────────────────  - 최대 마진을 위해 분류 수행
     │      Support Vectors
     │    ○       ○         - 마진이 클수록 훈련 외 데이터도 정확한 분류
     │  ○   ○               
     │    ○     ○           - 마진과 학습 오류는 Trade-off 관계
     │      ○ ●              
     │    ○     ●    OSH    - 선형적 분류 불가시 오차 허용을 위한 슬랙 변수 활용
     └───────────────────→ X₁
```

> 슬랙 변수(이상값 처리 목적)의 엄격한 적용시 오버피팅 발생하며, 반대의 경우 언더피팅 발생

---

## 구성요소

| 구분 | 핵심 |
|:-----|:-----|
| **결정경계** | 데이터 분류 기준 경계 |
| **Support Vector** | 훈련 데이터 중 결정경계 가장 근접 데이터 집합 |
| **Margin** | 결정 경계에서 서포트 벡터까지 거리 |
| **Hyperplane(초평면)** | 데이터 분류 위한 기준 |
| **Slack 변수** | 완벽한 분리 불가능시 허용된 오차 위한 변수 |
| **OSH** | Optimal Separating Hyperplane, 최적 경계선 |

---

## 기법

| 기법 | 핵심 |
|:-----|:-----|
| **Soft Margin** | 마진 안쪽 바깥쪽 이상값 허용 |
| **Hard Margin** | 마진 안쪽 바깥쪽 이상값 미허용 |
| **커널 기법** | 비선형 패턴 분리 |

---

## 연계 토픽

- [KNN](/docs/ai/01-machine-learning/knn)
- [지도학습](/docs/ai/01-machine-learning/supervised-learning)

---

## 학습 체크리스트

- [ ] SVM의 정의와 개념도 이해
- [ ] 구성요소(결정경계, Support Vector, Margin 등) 암기
- [ ] Soft Margin vs Hard Margin 차이점 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
