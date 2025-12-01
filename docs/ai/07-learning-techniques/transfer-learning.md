---
layout: default
title: Transfer Learning
parent: 7. 학습 기법
grand_parent: AI (인공지능)
nav_order: 2
---

# 전이학습(Transfer Learning)
{: .fs-8 }

학습 기법
{: .label .label-green }

---

## 핵심 키워드

`미세조정(Fine Tuning)` `과업/도메인 전이` `Inductive/Transductive/Unsupervised`

---

## 정의/개념

기존의 학습된 모델과 비슷한 유형의 다른 모델로 학습된 결과를 옮겨서 부족한 데이터를 통한 학습이나 훈련 시간을 단축시키는 머신 러닝 기법

---

## 아키텍처

```
       Pretrained A                    B (A와 비슷한 모델)
    ┌───────────────┐              ┌───────────────┐
    │    Output     │              │    Output     │
    ├───────────────┤              ├───────────────┤
    │ Hidden layer 5│              │ Hidden layer 4│
    ├───────────────┤              ├───────────────┤   Trainable
    │ Hidden layer 4│──────────────│ Hidden layer 3│◀─────────
    ├───────────────┤              ├───────────────┤
    │ Hidden layer 3│──────────────│ Hidden layer 2│◀── Freeze
    ├───────────────┤    재사용     ├───────────────┤   (가중치고정)
    │ Hidden layer 2│──────────────│ Hidden layer 1│
    ├───────────────┤              ├───────────────┤
    │ Hidden layer 1│              │  Input layer  │
    ├───────────────┤              └───────────────┘
    │  Input layer  │
    └───────────────┘
```

---

## 유형/기법

### 전이 유형

| 구분 | 유형 | 설명 |
|:-----|:-----|:-----|
| **과업(Task) 전이** | - | 영상인식에서 음성인식으로 전이하는 것처럼 응용분야가 변경되는 경우 |
| | - | 동결(Freeze): 유사 학습모델의 일부 가중을 재사용 |
| | - | 미세조정(Fine Tuning): 현재 학습모델을 위한 새로운 구조를 적용하여, 가지고 있는 데이터 셋으로 학습 진행. 원래 가중치가 훼손되지 않도록 학습률을 낮게 설정하여 진행 |
| **적용 범위** | - | 영상변역기를 영상변역기로 적이하는 것처럼 특징공간의 데이터 확률분포가 다른 경우 |
| **도메인(Domain) 전이** | - | Daume2009: 특징 공간을 3배로 확장하여 두 도메인의 확률분포 맞춤 |
| | - | Sun2016: 화이트닝 변환과 컬러링 변환으로 두 도메인의 확률분포 맞춤 |

### 데이터 label 여부

| 구분 | 유형 | 설명 |
|:-----|:-----|:-----|
| **귀납(Inductive)** | - | Multi-task: 하나의 Training Set을 가지고 동시에 여러 가지 분류문제를 처리하는 것으로 일반화된 모델을 만든 후 특정 Layer로 분리하는 방법 |
| | - | Self-taught: 원본 데이터를 Labeled 데이터를 변형, feature를 만든 후 Linear classifier로 학습 시키는 방법 |
| **변형(Transductive)** | - | Source data의 label을 이용하여 target data에 맞도록 확장 |
| **자율(Unsupervised)** | - | Unlabeled Data만 학습 진행 |

---

## 학습기법

| 학습기법 | 설명 |
|:---------|:-----|
| **Fine-tuned CNN** | 미리 학습된 CNN의 마지막 Fully Connected Layer만 변경해 분류 수행 |
| **Pre-trained Model** | 미리 학습된 모델의 가중치를 새로운 모델에 적용 |
| **Domain Adaptation** | 동일한 데이터를 바탕으로 훈련 시 도메인 구분 능력은 약하게 학습하여 Target Data 를 분류가능하도록 모델 구축 |
| **Layer Re-use** | 기존 모델의 일부 Layer를 재사용하여 부족 Data Domain 모델 구축에 활용 |

---

## 전이학습의 장점

| 장점 | 설명 |
|:-----|:-----|
| **학습 시간 단축** | 사전학습된 가중치 활용 |
| **적은 데이터로 학습** | 소량의 데이터로도 높은 성능 |
| **일반화 성능 향상** | 다양한 특징 학습 |
| **비용 절감** | 처음부터 학습 대비 자원 절약 |

---

## 연계 토픽

- [Active Learning](/docs/ai/07-learning-techniques/active-learning)
- [Knowledge Distillation](/docs/ai/07-learning-techniques/knowledge-distillation)
- [Fine-tuning](/docs/ai/07-learning-techniques/transfer-learning)

---

## 학습 체크리스트

- [ ] 전이학습의 정의와 아키텍처 이해
- [ ] 과업 전이 vs 도메인 전이 구분
- [ ] Inductive/Transductive/Unsupervised 유형 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
