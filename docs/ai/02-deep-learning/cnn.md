---
layout: default
title: CNN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 28
---

# CNN(Convolutional Neural Network)
{: .fs-8 }

2.1 딥러닝
{: .label .label-blue }

---

## 핵심 키워드

`Convolution` `Pooling` `Fully Connected Layer`

---

## 정의/개념

영상, 이미지 처리 목적 Convolution, Pooling, Fully Connected Layer 구성 신경망 알고리즘

---

## 개념도

```
                                           ┌─── bird    Pbird
                                           │
  ┌──────┐    ┌──────┐    ┌──────┐        │─── sunset  Psunset
  │ 🦅   │    │      │    │      │        │
  │ 이미지 │ → │ conv │ → │ pool │ → ... → │─── dog     Pdog
  │      │    │      │    │      │        │
  └──────┘    └──────┘    └──────┘        │─── cat     Pcat
              convolution  max pooling     └─────────────────
              + nonlinearity              fully connected layers
                                          Nx binary classification
```

---

## 계층(Layer) 구성요소

| 계층(Layer) | 특징 | 설명 |
|:------------|:-----|:-----|
| **Convolution** | Feature Map<br>Filter | 이미지를 분류하기 위한 특징을 추출<br>Filter에서 추출한 각각의 Feature 집합<br>Edge filter, Convolution Filter |
| **Pooling** | Max Pooling<br>Down Sampling | Feature Map 대표값 추출<br>기존 이미지 축소 및 형태 유지 |
| **Fully Connected** | Dropout<br>flatten<br>Classification | 오버피팅을 막기 위한 정규화 작업<br>각 Layer를 1차원 벡터로 변환하는 평탄화 작업<br>Softmax 함수 등을 사용하여 Output 분류 |

> CNN 각 Layer의 성능 향상을 위해 하이퍼파라미터 사용자 조정 필요

---

## 연계 토픽

- [RNN](/docs/ai/02-deep-learning/rnn)
- [YOLO](/docs/ai/01-machine-learning/yolo)
- [Pooling Layer](/docs/ai/01-machine-learning/pooling-layer)

---

## 학습 체크리스트

- [ ] CNN의 정의와 구조 이해
- [ ] 3가지 계층(Convolution, Pooling, Fully Connected) 역할 암기
- [ ] 각 계층의 특징과 설명 파악

---

## 참고자료

- 정보관리기술사 AI 학습자료
