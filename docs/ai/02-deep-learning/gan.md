---
layout: default
title: GAN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 11
---

# GAN(Generative Adversarial Networks)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`Generator` `Discriminator` `적대적 학습` `내쉬균형 적용`

---

## 정의/개념

Generator, Discriminator, 적대적 학습, 내쉬균형 적용, Fake Data 생성 신경망 알고리즘

---

## 아키텍처

```
                   Generator
                      │
           ┌─────────┴─────────┐
           │                   │
    (z)    │      Fake         │
    Latent ├───→  G(z)  ───────┤
    Vector │                   │          Discriminator
           │                   │              │
           │      Real         │              │      → Fake
           │───→  (x)  ────────┴──────→ [▷] ──┤
           │                                  │      → Real
           │                                  │
           └──────────────────────────────────┘
                    Fine Tune Training
```

---

## 학습원리

| 구분 | 설명 |
|:-----|:-----|
| **목적함수** | $min_G max_D V(D,G) = E_{x \sim P_{data}(x)}[logD(x)] + E_{z \sim P_z(z)}[log(1 - D(G(z)))]$ |
| **활성함수** | Sigmoid function 통한 이진분류, Real 또는 Fake 판별 |
| **Generator** | Zero-Mean 가우시안 노이즈 기반 Fake Sample 생성<br>Real Data와 유사한 특성을 가지도록 학습 |
| **Discriminator** | Real Data와 Fake Data 구별을 위한 확률 계산<br>판별 정확도 향상을 위해 학습 |

### 학습 목표

| 구분 | 설명 |
|:-----|:-----|
| **$max_D V(D)$** | D(x)=1, D(G(z))=0이 되도록 학습, V(D,G) 최대값 |
| **$min_G V(G)$** | D(G(z))=1, V(D,G) 최소값 |

> 학습 불안정, 성능 한계가 존재, 고해상도 이미지 생성불가

---

## 연계 토픽

- [DCGAN](/docs/ai/02-deep-learning/dcgan)
- [딥페이크](/docs/ai/02-deep-learning/gan)
- [VAE](/docs/ai/02-deep-learning/vae)

---

## 학습 체크리스트

- [ ] GAN의 정의와 아키텍처 이해
- [ ] Generator, Discriminator 역할 파악
- [ ] 목적함수 수식 이해
- [ ] 학습 불안정성 문제 인식

---

## 참고자료

- 정보관리기술사 AI 학습자료
