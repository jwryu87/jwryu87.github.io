---
layout: default
title: TCP
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 7
---

# TCP (Transmission Control Protocol)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`혼잡제어` `흐름제어` `오류제어` `3-way handshake` `4-way handshake`

---

## 정의/개념

신뢰성, 바이트 스트림, 혼잡, 흐름, 오류 **연결지향형 프로토콜**

---

## 연결 (3-way handshake)

| 구분 | 설명 |
|:-----|:-----|
| **초기연결시도** | Client는 접속하고자 하는 서버의 포트번호와 클라이언트의 초기순서번호(Init Sequence Number)를 지정한 SYN 세그먼트를 전송 |
| **서버응답** | 서버의 초기순서번호(ISN)를 포함한 자신의 SYN세그먼트로 응답<br>클라이언트의 ISN + 1 ACK를 보냄으로써 클라이언트의 SYN에 확인 응답 |
| **클라이언트 응답** | 클라이언트는 서버로부터 보내온 SYN에 대하여 서버의 ISN + 1 ACK로 확인응답을 전송 |

---

## 해제 (4-way handshake)

| 구분 | 설명 |
|:-----|:-----|
| **연결종료 요청** | Client가 Server에게 연결 종료를 요청 |
| **서버 ACK 신호** | 서버는 바로 종료하지 않고 ACK를 전송해 CLOSE_WAIT 상태로 넘어감 |
| **서버 FIN 신호** | 잔여 작업 종료후 서버는 FIN 신호를 보내고 연결 종료 시도 |
| **클라이언트 ACK** | 클라이언트는 서버의 FIN을 잘 받았다는 ACK를 서버에게 보내고, 클라이언트의 ACK를 받으면 서버는 종료 |

{: .note }
> TCP는 3-way handshaking을 통해 신뢰성 있는 연결 수행하지만, UDP는 신뢰성 고려하지 않음

---

## 연계 토픽

- [TCP 혼잡제어](/docs/nw/07-osi-layer/tcp-congestion)
- [TCP 흐름제어](/docs/nw/07-osi-layer/tcp-flow)
- [UDP](/docs/nw/07-osi-layer/tcp-udp)
- [SCTP](/docs/nw/07-osi-layer/sctp)

---

## 학습 체크리스트

- [ ] TCP 연결/해제 과정 이해
- [ ] 3-way / 4-way handshake 절차 파악
- [ ] TCP 특징(신뢰성, 연결지향) 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


