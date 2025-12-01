---
layout: default
title: MPTCP
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 8
---

# MPTCP (Multi Path TCP)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Subflow` `RFC 6824` `HTTP` `MPTCP` `Subflow TCP` `IP`

---

## 정의/개념

단말 간에 복수 네트워크 주소 활용 통해, TCP 호스트 간 subflow를 동시에 다중으로 구성하여 **다중 경로 TCP 연결을 가능하게 하는 전송 계층 프로토콜**

---

## 프로토콜 스택

| 계층 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **Application Layer** | HTTP | 응용 계층 통신을 위한 프로토콜 |
| **Transport Layer** | MPTCP | 다수 Subflow TCP 제어 관리 계층 |
| | Subflow TCP (Src 1234 → Dst 80) | 개별 TCP 연결 흐름 관리 계층 |
| | Subflow TCP (Src 6512 → Dst 80) | 개별 TCP 연결 흐름 관리 계층 |
| **Network Layer** | IP (Src A1 → Dst B1) | 다중 IP를 통한 Multi Path 지원 |
| | IP (Src A2 → Dst B2) | 다중 IP를 통한 Multi Path 지원 |

---

## MPTCP 핸드쉐이킹 과정

| 단계 | 상세 설명 |
|:-----|:---------|
| **1. 연결 요청** | SYN 패킷 + MP_CAPABLE 메시지 전송 |
| **2. 연결 요청 응답** | SYN/ACK 패킷 + MP_CAPABLE 메시지 전송 |
| **3. 연결 설정** | ACK 패킷 + MP_CAPABLE 메시지 전송 |
| **4. Subflow 연결 요청** | SYN 패킷 + MP_JOIN 메시지 전송 |
| **5. Subflow 연결 요청 응답** | SYN/ACK 패킷 + MP_JOIN(HMAC-B, R-B) 메시지 전송 |
| **6. Subflow 연결 추가 설정** | ACK 패킷 + MP_JOIN 메시지 전송 |
| **7. Subflow 연결 확인** | ACK 패킷 전송 |

{: .note }
> 초기 연결 설정 시 3-way handshake 과정에서 MP_CAPABLE 헤더의 Key 교환을 통해 인증 수행, Subflow 연결 추가 시 4-way handshake 과정을 MP_JOIN 메시지를 사용 하여 연결, 해쉬 기반 HMAC 인증 사용

---

## 연계 토픽

- [TCP](/docs/nw/07-osi-layer/tcp)
- [TCP 혼잡제어](/docs/nw/07-osi-layer/tcp-congestion)

---

## 학습 체크리스트

- [ ] MPTCP 개념 및 구조 이해
- [ ] Subflow 연결 과정 파악
- [ ] 핸드쉐이킹 절차 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


