---
layout: default
title: Zero-shot Learning
parent: 7. 학습 기법
grand_parent: AI (인공지능)
nav_order: 4
---

# 제로샷 러닝(Zero-Shot Learning)
{: .fs-8 }

학습 기법
{: .label .label-green }

---

## 핵심 키워드

`Seen Data` `Unseen Data` `Side Information(Semantic Information)` `속성` `텍스트` `class`

---

## 정의/개념

훈련 중 관찰되지 않은 클래스의 샘플을 관찰함으로써 샘플이 속하는 범주를 예측하는 학습 기법

---

## 메커니즘

```
     Training phase                      Prediction phase
    ┌─────────────────┐               ┌─────────────────┐
    │                 │               │                 │
    │  ┌───────────┐  │               │  ┌───────────┐  │    Stripes: 0.9
    │  │   Zebra   │  │  Stripes: ✓   │  │   Tiger   │  │    Orange: 0.0
    │  └───────────┘  │  Orange:  ✗   │  └───────────┘  │    Hooves: 0.1
    │                 │  Hooves:  ✓   │                 │
    │  ┌───────────┐  │               │  ┌───────────┐  │    Stripes: 0.0
    │  │   Horse   │  │  Stripes: ✗   │  │   Horse   │  │    Orange: 0.4
    │  └───────────┘  │  Orange:  ✗   │  └───────────┘  │    Hooves: 0.7
    │                 │  Hooves:  ✓   │                 │
    │  ┌───────────┐  │               │  ┌───────────┐  │    Stripes: ✗
    │  │    Fox    │  │  Stripes: ✗   │  │   Horse   │  │    Orange: ✗
    │  └───────────┘  │  Orange:  ✓   │  └───────────┘  │    Hooves: ✓
    │                 │  Hooves:  ✗   │                 │
    └─────────────────┘               └─────────────────┘
           │                                  │
    Seen classes                        Unseen classes
           │                                  │
           ▼                                  ▼
    Labeled visual     Class          Unlabeled visual    Estimated      Class
      instances     attributes          instances        attributes   attributes
           │            │                    │               │             │
           └────────────┴─────regression─────┴───similarity──┴─────────────┘
                              model              function
```

---

## Side Information 유형

Zero-Shot Learning은 **Side Information(Semantic Information)**을 통해 학습합니다:

| # | 유형 | 설명 |
|:--|:-----|:-----|
| 1 | **속성을 이용한 학습** | 클래스의 시각적/의미적 속성 활용 |
| 2 | **텍스트 설명을 통해 학습** | 클래스에 대한 텍스트 설명 활용 |
| 3 | **클래스 유사성(Class)** | 클래스 간 계층/관계 정보 활용 |

> **Side Information**: 데이터의 특성을 설명하는 정보

---

## Zero-Shot Learning vs Open Set Recognition

| Zero-Shot Learning | Open Set Recognition |
|:-------------------|:---------------------|
| 알고 있는 class의 **seen data**와 알고 있는 class의 **unseen data**를 **모두 올바르게 분류**하는 알고리즘 | 알고 있는 class의 seen data는 올바르게 분류하고, **unseen data는 특정 class가 아닌 unknown data 자체로 분류**하는 알고리즘 |

---

## Zero-Shot vs Few-Shot Learning

| 구분 | Zero-Shot | Few-Shot |
|:-----|:----------|:---------|
| **훈련 샘플** | 0개 | 1~5개 |
| **학습 방식** | 의미적 정보만 활용 | 소수 샘플 학습 |
| **난이도** | 높음 | 중간 |
| **활용** | 완전 새로운 클래스 | 소량 데이터 클래스 |

---

## 연계 토픽

- [Few-shot Learning](/docs/ai/07-learning-techniques/few-shot-learning)
- [Transfer Learning](/docs/ai/07-learning-techniques/transfer-learning)
- [Meta Learning](/docs/ai/07-learning-techniques/meta-learning)

---

## 학습 체크리스트

- [ ] Zero-Shot Learning의 정의와 메커니즘 이해
- [ ] Seen Data vs Unseen Data 개념 파악
- [ ] Side Information 3가지 유형 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
