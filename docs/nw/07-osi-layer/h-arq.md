---
layout: default
title: H-ARQ
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 21
---

# H-ARQ (Hybrid Automatic Repeat Request)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Type 1 ARQ` `Type 2 ARQ(CC-HARQ)` `Type 3 ARQ(IR-HARQ)`

---

## 정의/개념

재전송 요구 줄임, **ARQ+FEC, Link Adaptation ARQ 프로토콜**

---

## H-ARQ의 유형

### Type 1 ARQ

| 구분 | 설명 |
|:-----|:-----|
| **에러 수정 가능범위 이내** | 에러 정정(FEC)<br>잉여비트를 이용하여 데이터 복원 |
| **에러 수정 불가** | 에러 폐기 및 재전송 요구(ARQ)<br>수신된 데이터를 폐기하고 재전송 요청 |
| **특징** | FEC와 ARQ의 단순 조합 방식 |

### Type 2 ARQ (CC-HARQ)

| 구분 | 설명 |
|:-----|:-----|
| **1차 전송** | Systematic Bits + Parity 1 Bits + Parity 2 Bits (Punctured Bits) |
| **2차 전송** | Transmitted Bits |
| **수신측 메커니즘** | 오류 패킷 보존<br>재 수신된 패킷과 결합하여 복원 시도 |
| **송신측 메커니즘** | 전체 Data 재전송<br>이전에 송신한 데이터와 동일한 데이터 전송 |
| **특징** | 모든 Retransmission이 동일한 정보를 전달함<br>같은 채널을 이용하여 Encoding된 패킷은 동일한 Coded Bit을 가짐 |

### Type 3 ARQ (IR-HARQ)

| 구분 | 설명 |
|:-----|:-----|
| **1차 전송** | Systematic Bits + Parity 1 Bits + Parity 2 Bits (Punctured Bits) |
| **2차 전송** | Transmitted Bits |
| **수신측 메커니즘** | 오류 패킷 보존<br>재 수신된 패킷과 결합하여 복원 시도 |
| **송신측 메커니즘** | 오류가 발생한 packet에 잉여비트를 증가시켜 재전송<br>잉여비트만 전송 |
| **특징** | 이전에 송신한 Packet보다 잉여비트만 증가시켜 재전송<br>IR-HARQ는 5G NR 및 4G LTE에서 사용되는 HARQ 기법임 |

---

## 연계 토픽

- [ARQ](/docs/nw/07-osi-layer/arq)
- [FEC·BEC](/docs/nw/07-osi-layer/fec-bec)

---

## 학습 체크리스트

- [ ] H-ARQ 개념 이해
- [ ] Type 1, Type 2, Type 3 차이 구분
- [ ] CC-HARQ vs IR-HARQ 비교

---

## 참고자료

- 정보관리기술사 NW 학습자료


