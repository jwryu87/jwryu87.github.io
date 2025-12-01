---
layout: default
title: TCP 혼잡제어
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 10
---

# TCP 혼잡제어
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Slow Start` `Congestion Avoidance` `Fast Retransmission` `Fast Recovery`

---

## 정의/개념

네트워크로 유입되는 사용자 트래픽(데이터에 대한 표현)의 양이 네트워크 용량을 초과하지 않도록 유지시키는 **메커니즘**

---

## 혼잡제어 메커니즘

| 혼잡제어 매커니즘 | 구성 | 설명 |
|:----------------|:-----|:-----|
| **느린 출발 (Slow Start)** | 느린 출발 | 네트워크 연결 초기에는 CNWD 크기를 전송시마다 2배씩 증가시키고, ACK 수신 실패시 감소시키는 전송방식 |
| **혼잡회피 (Congestion Avoidance)** | 혼잡회피 | ACK 수신시 마다 CNWD 크기를 선형적으로 증가시키는 전송방식 |
| **빠른전송 (Fast Retransmission)** | 빠른전송 | 송신자에게 다음 수신할 Sequence Number를 알려주고 그 이후에는 Slow Start 로 전송하는 방식 |
| **빠른회복 (Fast Recovery)** | 빠른회복 | Fast Retransmission 통해 손실 세그먼트를 전송한 후 Congestion Avoidance를 수행하는 전송방식 |

---

## 알고리즘 유형

| 알고리즘 분류 | 설명 | 알고리즘 |
|:------------|:-----|:---------|
| **손실기반 혼잡제어** | 패킷 손실, 타임 아웃, ACK 손실 발생시 혼잡상황으로 판단하고 혼잡 윈도우 크기 조절 | Tahoe, Reno, NewReno, BIC, CUBIC, H-tCP |
| **지연기반 혼잡제어** | 측정한 RTT (Round Trip Time) 값이 늘어나는 경우 혼잡 상황으로 판단하고 혼잡 윈도우 크기 조절함 | TCP Vegas, Westwood, Fast TCP |
| **하이브리드** | 손실 기반 혼잡 제어와 지연기반 혼잡제어 방식 융합 | Illinois, CTCP(Compound TCP), DCTCP(Datacenter TCP) |

---

## 연계 토픽

- [TCP](/docs/nw/07-osi-layer/tcp)
- [TCP 흐름제어](/docs/nw/07-osi-layer/tcp-flow)

---

## 학습 체크리스트

- [ ] 혼잡제어 개념 이해
- [ ] 4가지 메커니즘(Slow Start, Congestion Avoidance, Fast Retransmission, Fast Recovery) 구분
- [ ] 알고리즘 유형별 특징 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


