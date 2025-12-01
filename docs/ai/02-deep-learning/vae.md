---
layout: default
title: VAE
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 13
---

# VAE(Variational Autoencoder)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`Encoder` `Decoder` `Sample Latent` `평균` `표준편차 벡터`

---

## 정의/개념

평균과 표준편차를 학습하여 사후확률을 최대화하여 입력 데이터와 유사한 새로운 데이터를 생성하는 AI 기술

> 확률 분포를 이용해 입력 데이터와 유사한 새로운 데이터를 생성하는 인공지능 기술

---

## 개념도

```
              학습       변균       추론
                ↓        ↓         ↓
     ┌──────────────────────────────────────────┐
     │                                          │
     │   축소       평균        Sample    최대화   │
 X ──┼──→ Encoder ───→ Latent ───→ Decoder ───→ X'
     │            표준편차   vector            │
     │                ↓                        │
     │              표준                        │
     │              편차                        │
     │                ↓                        │
     │              추론                        │
     │                                          │
     └──────────────────────────────────────────┘
     <Input>                           <Output>
     
     ├─────────┤     ├─────────┤     ├─────────┤
       Encoder      Latent Space       Decoder
```

---

## 구성요소

| 구분 | 구성 요소 | 설명 |
|:-----|:---------|:-----|
| **Encoder** | Input Layer | 학습할 x의 입력 데이터 |
| | Encoder | 입력 데이터의 차원을 축소하여 학습, Auto Encoder 사용 |
| | 평균, 표준편차 벡터 | Input 값의 평균과 표준편차를 학습한 벡터 값 |
| **Latent Space** | Sample Latent | 평균, 표준편차를 통한 사후 확률 추론<br>변분추론을 통하여 근사적으로 학습 |
| **Decoder** | Decoder | 사후 확률을 최대화하는 확률 분포를 학습하여 네트워크의 출력값을 도출 |
| | Output Layer | Input 데이터와 유사하지만 새로운 데이터를 생성 |

---

## 활용 분야

- 양질의 의료 데이터의 생성
- 금융 경제의 이상 거래 탐지
- FDS, 엔터테인먼트 분야에서 활용

---

## 연계 토픽

- [GAN](/docs/ai/02-deep-learning/gan)
- [Autoencoder](/docs/ai/02-deep-learning/vae)

---

## 학습 체크리스트

- [ ] VAE의 정의와 개념도 이해
- [ ] Encoder, Latent Space, Decoder 역할 파악
- [ ] 평균, 표준편차를 통한 확률 분포 학습 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
