---
layout: default
title: K-Means
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 17
---

# k-평균 군집(k-means clustering)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 핵심 키워드

`K개 Centroid` `유클라디안 거리`

---

## 정의/개념

K개 군집, Centroid 설정, 좌표기반, 유클리디안 거리 사용 비지도 학습 알고리즘

---

## 메커니즘

```
Unlabelled Data              Labelled Clusters

    ● ●                      ⭕ ● ●
  ●   ● ●    ──K-means──→    ● ● ●    ← Cluster 1
    ● ● ●                    
  ● ●   ●                    ⭕ ● ●
    ● ●                      ● ● ●    ← Cluster 2
                               
                             ⭕ ● ●
                             ● ● ●    ← Cluster 3
                             
                             ⭕ = Centroid
```

---

## 프로세스

| # | 프로세스 | 핵심 |
|:--|:--------|:-----|
| 1 | K개 객체 선택 | K개 객체 임의 선택 |
| 2 | 할당 | 자료 가까운 군집 중심 할당 |
| 3 | 중심 갱신 | 군집 내 자료 평균 계산 군집 중심 갱신 |
| 4 | 반복 | 반복 |

---

## K값 식별 기법

- **엘보우 (Elbow Method)**: 군집 수에 따른 분산 감소율 확인
- **실루엣 (Silhouette Method)**: 군집 내 응집도와 군집 간 분리도 측정
- **덴드로그램**: 계층적 군집화 결과 시각화

---

## 연계 토픽

- [KNN](/docs/ai/01-machine-learning/knn)
- [군집분석](/docs/ai/01-machine-learning/unsupervised-learning)
- [DBSCAN](/docs/ai/01-machine-learning/dbscan)

---

## 학습 체크리스트

- [ ] K-Means 알고리즘의 정의와 메커니즘 이해
- [ ] 프로세스(선택-할당-갱신-반복) 암기
- [ ] K값 식별 기법(엘보우, 실루엣, 덴드로그램) 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
