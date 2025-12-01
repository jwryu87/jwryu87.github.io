---
layout: default
title: SNN
parent: 3. 신경망
grand_parent: AI (인공지능)
nav_order: 2
---

# SNN(Spiking Neural Network)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`뉴런` `시냅스` `뉴로모픽 칩`

---

## 정의/개념

두뇌에서 실제로 정보가 전달되고 가공되는 과정을 모사하여, 뇌를 구성하는 뉴런과 시냅스로 이루어진 신경망 구성 방식으로 인공지능을 구현하는 기술

---

## 아키텍처

```
                    시냅스(Synapse)
                         │
        ────────────────→│
                         ↓
        입력(Input Spike) ─→ [X] ─┐
                              │   │
                             W1   │
                              │   │
                              ↓   │
                             [Σ] ─┴─→ 출력(Output Spike)
                              │
                       뉴론(Neuron)
                              │
                         ────│────
                              │
                        입력(Input Spike) ─→ [X]
                                            │
                                           W2
                                            │
                        ────────────────────┘
        
        ├─────────────┤├─────────────┤├─────────────┤
             Input         Hidden         Output
```

---

## 기술 구성요소

| 구분 | 동작기술 | 설명 |
|:-----|:--------|:-----|
| **Input** | Synapse | 수상돌기(dendrit) 역할을 하는 Spiking 전송 |
| | Weight | 시냅스의 가중치를 곱하여 뉴런 전달 |
| **Hidden** | Neuron | 막전위(membrane potential) 값이 문턱전압(threshold voltage)을 넘게 되면 출력으로 전달 |
| **Output** | Output Spike | 축삭돌기(axon) 역할을 하는 Spiking 전송 |
| | Initialized | 뉴런 내부의 막전위 값 초기화 |

---

## SNN vs ANN 비교

| 구분 | SNN | ANN |
|:-----|:----|:----|
| **신호 전달** | 스파이크(Spike) | 연속적 값 |
| **시간 정보** | 포함 | 미포함 |
| **에너지 효율** | 높음 | 낮음 |
| **하드웨어** | 뉴로모픽 칩 | GPU/TPU |

---

## 연계 토픽

- [뉴로모픽](/docs/ai/03-neural-network/snn)
- [인공신경망](/docs/ai/02-deep-learning/mlp)

---

## 학습 체크리스트

- [ ] SNN의 정의와 아키텍처 이해
- [ ] 구성요소(Synapse, Neuron, Spike) 역할 파악
- [ ] ANN과의 차이점 암기

---

## 참고자료

- 정보관리기술사 AI 학습자료
