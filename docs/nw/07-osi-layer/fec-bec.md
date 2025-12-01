---
layout: default
title: FEC·BEC
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 19
---

# FEC (Forward Error Correction), BEC (Backward Error Correction)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Parity Check` `Stop and Wait` `Go-back-N` `Selective-Repeat` `Adaptive ARQ` `Block Sum` `CRC` `Check Sum` `Hamming Code`

---

## 정의/개념

- **FEC**: 수신 측에서 오류를 스스로 정정할 수 있는 방법으로 오류복구를 위한 잉여비트를 추가하여 전송하는 방식
- **BEC**: 수신 측에서 오류를 검출하고 이를 송신 측에 알려주어 재전송을 통하여 에러를 정정하게 하는 방식

---

## FEC 동작기법

```
  송신측                    수신측
    │                        │
    │                        │
    └────────────────────────┘
              │
           자체 정정
              │
              ▼
            오류
```

| 구분 | 분류 | 기법 | 설명 |
|:-----|:-----|:-----|:-----|
| **FEC** | 블록코드 (Block Code) | 해밍코드 | 필요한 수 만큼의 패리티 비트를 정해진 위치에 두어 오류가 발생했을 때 오류 발생 비트를 알아내어 정정이 가능하도록 하는 오류 정정 코드 |
| | | RS코드 | 비 2진 순환부호로 오류정정능력이 우수하며, 통신로 상에서 발생하는 랜덤오류(Random Error)와 연집오류(Burst Error)까지 모두 정정 |
| | 논-블록 코드 (Non-block Code) | 컨볼루션 코드 (Convolutional Code) | 해당 블록에만 의존하는 블록부호화와 달리 부호화 때 현재의 입력신호와 과거의 일부 신호를 함께 활용하는 메모리를 갖는 부호화 |
| | | 터보코드 (Turbo Code) | Convolutional Code중에 쉽게 부호화 할 수 있는 것들을 조합하여 랜덤하게 병렬 연결한 부호 |

---

## BEC 동작기법

```
  송신측                    수신측
    │                        │
    │                        │  오류
    │                        │   │
    │                        │   ▼
    │◄───────────────────────┤ 검출 후
    │      재전송 요청        │ 재전송 요청
    │                        │
```

| 구분 | 분류 | 기법 | 설명 |
|:-----|:-----|:-----|:-----|
| **BEC** | 오류검출 (Error Detect) | Parity Check | 데이터의 끝에 한 비트를 추가하여 1의 개수로 오류 유무 판단 |
| | | Block Sum | 이차원 패리티 검사, 가로와 세로로 두 번 검사하는 방식 |
| | | CRC | 이진 나눗셈 연산을 기반으로 오류를 검출하는 방식 |
| | | Check Sum | 전송 데이터의 맨 마지막에 앞서 보낸 모든 데이터를 다 합한 합계를 보내는 방법의 검사하는 방법 |
| | 재전송 (Retransmission) | Stop and Wait | 송신 측에서 1 개의 프레임을 송신하고, 수신 측에서 에러 유무를 판단하여 송신 측에 ACK 나 Nack를 기다림 |
| | | Go-Back-N | 오류가 발생한 (NACK) 프레임 이후 또는 오류 발생 현 프레임 만을 재전송하는 방식 |
| | | Selective-Repeat | 오류가 발생한 (NACK) 프레임 이후 또는 오류 발생 된 프레임 만을 재전송하는 방식 |
| | | Adaptive ARQ | 채널 효율을 최대로 높이기 위해 블록의 길이를 동적으로 변경할 수 있는 방식 |

---

## 연계 토픽

- [ARQ](/docs/nw/07-osi-layer/arq)
- [H-ARQ](/docs/nw/07-osi-layer/h-arq)
- [해밍코드](/docs/nw/07-osi-layer/hamming-code)

---

## 학습 체크리스트

- [ ] FEC vs BEC 개념 이해
- [ ] 각 기법의 동작 원리 파악
- [ ] 오류 검출/정정 방식 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


