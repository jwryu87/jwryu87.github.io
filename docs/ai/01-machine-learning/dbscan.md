---
layout: default
title: DBSCAN
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 18
---

# 밀도기반 클러스터링(DBSCAN)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 핵심 키워드

`Core Point` `Border Point` `Noise Point` `Epsilon` `minPTS`

---

## 정의/개념

밀도기반 군집화, Epsilon 내 중심점 P 기준, 군집판단기준(mPTS) 계산 비지도 학습 알고리즘

---

## 개념도

```
          Cluster
       ┌──────────────┐
       │   Core point │
       │     ●────────│─── epsilon
       │    ╱│╲       │
       │   ● ● ●      │     Border point
       │  ╱   ╲       │        ↓
       │ ●     ●      │   ──→  ○
       └──────────────┘
                           Noise point
                               ↓
                              ◇
```

> Epsilon 내에 중심점 P기준으로 군집판단기준(mPTS)을 계산하여 군집 판단

---

## 구성요소/동작방식

### 구성요소

| 구성요소 | 설명 |
|:---------|:-----|
| **Core Point** | 거리 ε(Epsilon)이내에 데이터가 m개 이상 존재하여 한의 군집으로 인정되는 데이터 집합 |
| **Border Point** | 군집의 중심이 되는 core point는 되지 못하지만, core point로 하는 군집에는 속하는 데이터 |
| **Connected** | core point 와 core point가 반경내에 겹칠 경우 연결되 있다고 보고 하나의 군집으로 정의 |
| **Noise Point** | 어떤 점의 중심으로도 조건을 만족시키지 못하는 데이터 |

### 동작방식

| # | 단계 | 설명 |
|:--|:-----|:-----|
| 1 | Epsilon 설정 | 두 인스턴스 최대 허용 거리<br>이 거리 이내에 있는 인스턴스는 neighbor로 분류 |
| 2 | minPts 설정 | 군집을 형성하기 위해 Epsilon 내에 포함되어야 하는 인스턴스의 최소 개수<br>낮은 minPts 값은 많은 noise point를 생성 |
| 3 | Core point 분류 | Epsilon 내에 minPts만큼의 neighbor가 포함된 포인트<br>군집(cluster)를 형성하는 포인트 |
| 4 | Border Point 분류 | Epsilon 내에 minPts만큼의 neighbor가 포함되지 않는 포인트지만, 군집에는 포함되는 포인트<br>군집의 경계 형성하는 포인트 |

> Epsilon(Eps), minPts 초기 파라미터 값에 따라서 군집 및 속도 성능이 크게 차이남

---

## 연계 토픽

- [K-Means](/docs/ai/01-machine-learning/k-means)
- [군집분석](/docs/ai/01-machine-learning/unsupervised-learning)

---

## 학습 체크리스트

- [ ] DBSCAN의 정의와 개념 이해
- [ ] 구성요소(Core/Border/Noise Point) 차이점 암기
- [ ] Epsilon, minPts 파라미터의 역할 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
