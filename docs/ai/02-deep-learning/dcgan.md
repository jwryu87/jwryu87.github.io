---
layout: default
title: DCGAN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 12
---

# DCGAN(Deep Convolution GAN)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`GAN Fully Connected Layer 제거` `배치 정규화 구조 사용` `Fractional-Strided Convolution`

---

## 정의/개념

GAN Fully Connected Layer 제거, 배치 정규화 구조 사용 GAN 알고리즘

---

## 아키텍처

```
Generator:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  In │ →  │DeConv1│ → │DeConv2│ → │DeConv3│ → │DeConv4│
└─────┘    └─────┘    └─────┘    └─────┘    └─────┘
4x4x512    8x8x256    16x16x128  32x32x64   64x64x3
(Random)   (BN,ReLU)  (BN,ReLU)  (BN,ReLU)  (BN,tanh)

Discriminator:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  In │ →  │Conv1 │ → │Conv2 │ → │Conv3 │ → │Conv4 │
└─────┘    └─────┘    └─────┘    └─────┘    └─────┘
64x64x3    32x32x32   16x16x64   8x8x128    4x4x256
           (BN,ReLU)  (BN,ReLU)  (BN,ReLU)  (ReLU)

                    Image generated
```

---

## 기술 구성요소

| 구분 | 구성요소 | 핵심 |
|:-----|:---------|:-----|
| **네트워크 구조** | Convolution | Feature Map, Filter, Stride, Padding |
| | Fractional-Strided Convolution | 이미지 업스케일링 수행 |
| | 배치정규화 | 활성화 함수 값의 정규분포화(평균0, 분산1) |
| **활성화 함수** | ReLU | 생성자 모든 층 ReLU사용 |
| | Tanh | 마지막 결과 도출 시 Tanh 사용 |
| | Leaky ReLU | 판별자 모든 층 Leaky ReLU 사용 |

---

## GAN vs DCGAN 비교

| 구분 | GAN | DCGAN |
|:-----|:----|:------|
| **구조** | Fully Connected Layer 사용 | Fully Connected Layer 제거 |
| **정규화** | 없음 | 배치 정규화 사용 |
| **활성화 함수** | 단순 | 층별 다른 활성화 함수 사용 |
| **이미지 품질** | 저품질 | 고품질 |

---

## 연계 토픽

- [GAN](/docs/ai/02-deep-learning/gan)
- [CNN](/docs/ai/02-deep-learning/cnn)

---

## 학습 체크리스트

- [ ] DCGAN의 정의와 아키텍처 이해
- [ ] GAN과의 차이점(FC Layer 제거, 배치정규화) 파악
- [ ] 네트워크 구조 및 활성화 함수 특징 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
