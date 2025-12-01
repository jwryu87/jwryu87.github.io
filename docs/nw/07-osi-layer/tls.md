---
layout: default
title: TLS
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 6
---

# TLS (Transport Layer Security)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-yellow }

---

## 핵심 키워드

`암호화 알고리즘` `X.509 인증서` `443 포트` `TLS 1.3` `핸드쉐이크`

---

## 정의/개념

암호화 알고리즘, X.509 인증서, 443 포트 **보안 프로토콜**

---

## 프로토콜 구조

| 계층 | 구성요소 |
|:-----|:---------|
| **Application** | Application (HTTP, ...) |
| **Session (TLS)** | Protocol: Alert, ChangeCipherSpec, Handshake |
| **Record** | Fragmentation, Integrity, Authentication, Encryption |
| **Transport** | TCP |
| **Network** | IP |
| **Data Link / Physical** | 하위 계층 |

---

## 특징

| 분류 | 특징 | 상세 설명 |
|:-----|:-----|:---------|
| **인증** | 상호 인증 | 공개키 인증서 통한 서버, 클라이언트 상호 인증 |
| | 개별적 인증 | 키교환과 암호화 방식 개별적 결정 |
| **메시지 교환** | 0-RTT 모드 추가 | 1-RTT(완전 협상)와 0-RTT(단축 협상) 모드 추가 |
| | ECDHE 기본 지원 | 타원곡선 임시 디피헬만 알고리즘 키교환 알고리즘 기본 |
| **보안 통신** | 기밀성 | 서버, 클라이언트 양단간 암호화로 기밀성 제공 |
| | 무결성 | 메시지 중간 변경되지 않음 보장 |

{: .note }
> TLS 1.3 에서 키교환 방식으로 RSA 배제하고 옵션 최대한 감소로 단순화

---

## TLS 1.3 핸드쉐이크 절차

| 단계 | 메시지 | 절차 상세 |
|:-----|:------|:---------|
| **Client Hello** | Client Hello | 클라이언트가 서버에 보안 연결 요청 |
| | Supported Cipher Suites | 지원되는 암호 스위트 목록 송신 |
| | Guesses Key Agreement Protocol | 서버가 선택할 가능성 큰 키 교환 방법 추측 |
| | Key Share | 암호화 알고리즘, 키 교환, 인증 한번에 전송 |
| **Server Hello** | Server Hello | 서버가 공개 해당 답장 및 서버 암호 메시지 |
| | Key Agreement Protocol | 키 교환에 대한 프로토콜을 동의 |
| | Key Share | 키 공유 메시지 전송 |
| | Server Finished | 서버의 종료 단계 메시지 |
| **Finish** | Checks Certificate | 서버 인증서 확인 |
| | Generates Keys | 암호 통신 위한 세션 키 생성 |
| | Client Finished | 핸드쉐이크 종료 메시지 송신 |

{: .highlight }
> 기존 2회 왕복에서 1회의 왕복으로 대기시간 크게 단축
> 초기 핸드쉐이크는 1-RTT 실행하며, 재접속시 Pre-Shared Key(PSK) 활용 0-RTT로 지연 감소

---

## 연계 토픽

- [QUIC](/docs/nw/07-osi-layer/quic)
- [HTTP/3](/docs/nw/07-osi-layer/http3)

---

## 학습 체크리스트

- [ ] TLS 개념 및 구조 이해
- [ ] TLS 1.3 핸드쉐이크 절차 파악
- [ ] 인증/암호화 특징 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


