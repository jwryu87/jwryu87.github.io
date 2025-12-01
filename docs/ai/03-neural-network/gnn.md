---
layout: default
title: GNN
parent: 3. 신경망
grand_parent: AI (인공지능)
nav_order: 1
---

# GNN(Graph Neural Network)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`인접 행렬` `Target Node` `Hidden State` `회귀` `분류` `Node` `Edge`

---

## 정의/개념

노드, 엣지 구성 그래프 데이터 적합 신경망 알고리즘

> 주어진 데이터를 인접 행렬 등 그래프로 표현할 수 있는 자료 구조로 변환하는 과정 필요

---

## 아키텍처

```
                    인접
                   /특성
        Input  →  행렬   →  [GNN Layer] → ... → [GNN Layer] → Output
                    │           #1                  #n         │
                   변환     ① Aggregate                     Node 임베딩
                           ② Combine                       Edge 임베딩
                           ③ Readout                       Graph 임베딩
                            │
        ├──────────────┤├──────────────────────────────┤├─────────────┤
            Data 변환           GNN Layers                   Output
```

---

## 프로세스

| # | 프로세스 | 기술 | 핵심 |
|:--|:--------|:-----|:-----|
| 1 | **변환(Transformation)** | 인접 행렬 | 신경망 학습 적합 변환 |
| 2 | **취합(Aggregate)** | Target Node | 타겟 노드 인접 은닉 변수 취합 |
| 3 | **결합(Combine)** | Hidden State | 타겟 노드 업데이트 |
| 4 | **생성(Readout)** | 회귀, 분류 | 그래프 단위 은닉 변수 생성 |
| 5 | **출력(Output)** | Node, Edge | Layer1-n 반복 진행, 임베딩 계산 |

---

## GNN 활용 분야

| 분야 | 설명 |
|:-----|:-----|
| **소셜 네트워크** | 사용자 관계 분석, 영향력 예측 |
| **분자 구조 분석** | 신약 개발, 화학 물질 특성 예측 |
| **추천 시스템** | 사용자-아이템 그래프 기반 추천 |
| **교통 네트워크** | 교통 흐름 예측, 경로 최적화 |

---

## 연계 토픽

- [CNN](/docs/ai/02-deep-learning/cnn)
- [RNN](/docs/ai/01-machine-learning/rnn)

---

## 학습 체크리스트

- [ ] GNN의 정의와 아키텍처 이해
- [ ] 프로세스 5단계(변환-취합-결합-생성-출력) 암기
- [ ] 그래프 데이터의 특성 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
