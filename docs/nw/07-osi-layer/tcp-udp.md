---
layout: default
title: TCP·UDP 비교
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 12
---

# TCP, UDP 비교
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

- TCP: 바이트 스트림, 연결지향, 세그먼트 단위, 1대 1 통신
- UDP: 메시지 스트림, 비연결지향, 데이터그램 단위, 1대 N 통신

---

## 정의/개념

- **TCP**: 전송계층에서 신뢰성 있는 바이트 스트림 전송 위해 혼잡, 흐름, 오류제어 **연결지향형 프로토콜**
- **UDP**: 전송계층에서 속도에 중점을 둔 메시지 스트림 전송 위해 오류체크 하는 **비연결지향형 프로토콜**

---

## TCP vs UDP 비교

### 연결 방식 비교

| 동작 | TCP | UDP |
|:-----|:----|:----|
| **연결 설정** | 3-way handshake 통한 연결 설정 | Client 요청에 의한 데이터그램 전송 |
| **연결 해제** | 4-way handshake 통한 해제 설정 | 별도 연결 해제 절차 없음 |

### 상세 비교

| 구분 | TCP | UDP |
|:-----|:----|:----|
| **연결성** | 연결지향형 프로토콜 | 비 연결지향형 프로토콜 |
| **표준** | RFC 793 | RFC 768 |
| **스트림** | Byte Stream Service<br>(데이터의 경계 미구분) | Message Stream Service<br>(데이터의 경계 구분) |
| **단위** | Segment | Datagram |
| **혼잡** | Congestion Avoidance<br>Slow Start, TCP Tahoe, Reno | 혼잡 미지원 |
| **흐름** | 슬라이딩 윈도우 | 제어 미지원 |
| **오류** | Checksum, Retransmission<br>(오류시 재전송 요청) | Checksum<br>(오류시 탐지 및 폐기) |
| **순서** | Sequence Number<br>통한 순서 재조립 | 순서 미지원 |
| **대상** | 1 : 1 통신 | 1:1, 1:M, M:N 통신 |
| **속도** | 상대적 느림 | 상대적 빠름 |
| **어플리케이션** | HTTP, SMTP 등 | DNS, DHCP 등 |
| **보안** | TLS | DTLS |

{: .note }
> TCP의 신뢰성 특징과 UDP의 속도 특징에 맞춰 다양한 서비스에 활용

---

## 연계 토픽

- [TCP](/docs/nw/07-osi-layer/tcp)
- [SCTP](/docs/nw/07-osi-layer/sctp)

---

## 학습 체크리스트

- [ ] TCP vs UDP 차이점 이해
- [ ] 각 프로토콜의 적용 분야 파악
- [ ] 혼잡/흐름/오류 제어 방식 비교

---

## 참고자료

- 정보관리기술사 NW 학습자료


