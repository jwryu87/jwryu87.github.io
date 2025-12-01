---
layout: default
title: Knowledge Distillation
parent: 7. 학습 기법
grand_parent: AI (인공지능)
nav_order: 3
---

# 지식 증류(Knowledge Distillation)
{: .fs-8 }

학습 기법
{: .label .label-green }

---

## 핵심 키워드

`Teacher Model` `Student Model` `Soft Labels` `Hard Labels`

---

## 정의/개념

앙상블 기법 활용, 학습된 모델로부터 작은 모델에 지식 전달 방법

---

## 아키텍처

```
    ┌─────────────────────────────────────────────────────┐
    │                      Teacher                        │
    │  ┌─────┐  ┌─────┐  ┌─────┐  ┌────────┐             │
    │  │Layer│→ │Layer│→ │Layer│→ │Softmax │→ predictions│
    │  └─────┘  └─────┘  └─────┘  └────────┘             │
    │                                   │                 │
    │                              soft labels            │
    └───────────────────────────────────┼─────────────────┘
                                        │
                         지식 증류 (Knowledge Distillation)
                                        │
                                        ▼
    ┌─────────────────────────────────────────────────────┐
    │                      Student                        │
    │  ┌─────┐  ┌─────┐  ┌─────┐  ┌────────┐             │
    │  │Layer│→ │Layer│→ │Layer│→ │Softmax │→ predictions│→ true label
    │  └─────┘  └─────┘  └─────┘  └────────┘             │
    │                                   │                 │
    │                              hard labels            │
    └───────────────────────────────────┼─────────────────┘
                                        │
                                  Training data
```

---

## 구성요소

| 구분 | 핵심 기술 | 설명 |
|:-----|:---------|:-----|
| **Model** | Teacher Model | 미리 학습된 데이터 모델 |
| | Student Model | Teacher Model의 데이터를 전달 받아 학습 |
| **Function** | 활성화 함수 | 입력값을 활성화 여부를 결정하는 함수<br>- 예) Softmax: 입력값을 0 ~ 1값으로 출력, 출력 총합은 1 |
| | 손실함수 | 모델의 학습 결과의 손실을 계산 |

> 손실함수의 결과로 Student Model의 학습결과를 확인 가능

---

## Soft Label vs Hard Label

| 구분 | Soft Label | Hard Label |
|:-----|:-----------|:-----------|
| **정의** | Teacher 모델의 확률 분포 출력 | 실제 정답 레이블 (0 또는 1) |
| **정보량** | 클래스 간 관계 정보 포함 | 정답 정보만 포함 |
| **예시** | [0.7, 0.2, 0.1] | [1, 0, 0] |
| **역할** | 지식 전달 | 정답 학습 |

---

## Knowledge Distillation 손실 함수

$$
L = \alpha \cdot L_{soft} + (1 - \alpha) \cdot L_{hard}
$$

| 항목 | 설명 |
|:-----|:-----|
| $L_{soft}$ | Teacher의 soft label과 Student 출력 간의 KL divergence |
| $L_{hard}$ | Student 출력과 실제 정답 간의 Cross-entropy |
| $\alpha$ | 두 손실의 가중치 조절 |

---

## 장점

| 장점 | 설명 |
|:-----|:-----|
| **모델 경량화** | 작은 모델로도 높은 성능 |
| **추론 속도 향상** | 계산량 감소 |
| **Edge 배포 용이** | 리소스 제한 환경에 적합 |
| **앙상블 효과** | Teacher 앙상블 지식 압축 |

---

## 연계 토픽

- [Transfer Learning](/docs/ai/07-learning-techniques/transfer-learning)
- [Active Learning](/docs/ai/07-learning-techniques/active-learning)
- [모델 경량화](/docs/ai/07-learning-techniques/knowledge-distillation)

---

## 학습 체크리스트

- [ ] Knowledge Distillation의 정의와 아키텍처 이해
- [ ] Teacher-Student 모델 개념 파악
- [ ] Soft Label vs Hard Label 차이 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
- Hinton et al., "Distilling the Knowledge in a Neural Network" (2015)
