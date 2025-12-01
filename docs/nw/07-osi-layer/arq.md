---
layout: default
title: ARQ
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 20
---

# ARQ (Automatic Repeat Request)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Stop and Wait` `Go-back-N` `Selective Repeat`

---

## 정의/개념

데이터 수신 측에서 오류 검출 후 송신측에 오류 사실을 알리고 **재전송을 요청하여 오류를 수정하는 네트워크 오류제어 기술**

---

## ARQ 유형

### 1. Stop and Wait

| 구분 | 설명 |
|:-----|:-----|
| **개념도** | Data1 에 대한 ACK 를 수신 후에 Data2 송신할 수 있는 구조 |
| **설명** | 송신측에서 전송한 하나의 블록에 대해 수신측에서 오류의 발생을 점검하고 ACK 나 Nack를 기다림<br>즉, 데이터 블록을 1개씩 보내고 수신측으로 정상수신에 대한 ACK를 받은 후에 다음 데이터 블록을 전송하는 방식 |

### 2. Go-Back-N

| 구분 | 설명 |
|:-----|:-----|
| **개념도** | Data1, Data2, Data3 를 연속적으로 송신<br>수신측에서 Data1 은 수신하고 Data2 에 대해 미수신하여 Data2 에 대해 NACK 응답<br>송신측은 Data2 부터 재송신<br>즉, Data3 는 수신되었다 하더라도 Data2 에 이어 다시 송신하게 됨 |
| **설명** | 송신측에서 프레임을 연속적으로 송신하고 수신측은 오류발생시 NACK 와 함께 오류 프레임 번호 통보, 송신측에서는 오류 발생한 프레임부터 나머지 프레임을 계속 송신함 |

### 3. Selective Repeat

| 구분 | 설명 |
|:-----|:-----|
| **개념도** | Data1에 대한 ACK를 수신 후에 Data2 송신할 수 있는 구조 |
| **설명** | 송신측에서 NAK를 수신하면 오류가 발생된 프레임 번호를 확인 후에 해당 프레임 만 재전송<br>즉, 데이터 블록을 1개씩 보내고 수신측으로 정상수신에 대한 ACK를 받은 후에 다음 데이터 블록을 전송하는 방식 |

{: .note }
> 송신측에서 NAK를 수신하면 오류가 발생된 프레임의 재전송까지 다음 프레임을 저장할 기억 공간과 재전송 프레임을 다시 삽입할 수 있는 논리회로 필요

---

## 연계 토픽

- [H-ARQ](/docs/nw/07-osi-layer/h-arq)
- [FEC·BEC](/docs/nw/07-osi-layer/fec-bec)

---

## 학습 체크리스트

- [ ] ARQ 개념 이해
- [ ] Stop and Wait, Go-back-N, Selective Repeat 비교
- [ ] 각 방식의 장단점 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


