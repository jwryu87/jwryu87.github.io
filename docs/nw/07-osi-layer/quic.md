---
layout: default
title: QUIC
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 4
---

# QUIC (Quick UDP Internet Connection)
{: .fs-8 }

7.2 응용계층
{: .label .label-yellow }

---

## 핵심 키워드

`UDP+TLS` `TCP HOL 해결` `RTT 최소화`

---

## 정의/개념

**UDP+TLS, TCP HOL 해결, RTT 최소화 프로토콜**

---

## 메커니즘

```
Initial 1-RTT Handshake              Successful 0-RTT Handshake
┌──────┐        ┌──────┐           ┌──────┐        ┌──────┐
│Client│        │Server│           │Client│        │Server│
└──┬───┘        └──┬───┘           └──┬───┘        └──┬───┘
   │               │                  │               │
   │ Inchoate CHLO │                  │Complete CHLO  │
   │──────────────>│                  │──────────────>│
   │               │                  │Encrypted req  │
   │     REJ       │                  │               │
   │<──────────────│                  │     SHLO      │
   │               │                  │<──────────────│
   │ Complete CHLO │                  │Encrypted resp │
   │──────────────>│                  │               │
   │ Encrypted req │                  │               │
   │               │                  │               │
   │     SHLO      │                  │               │
   │<──────────────│                  │               │
   │Encrypted resp │                  │               │
   │               │                  │               │
```

---

## Handshake 절차

| 구분 | 단계 | 설명 |
|:-----|:-----|:-----|
| **Initial 1-RTT Handshake** | Client | Inchoate CHLO(Client Hello) 서버로 전송 |
| | Server | Diffie-Hellman 공개키, 서버 인증서, 공인 IP 주소 암호화를 포함한 REJ(Rejection)을 Client 로 전송 |
| | Client | Complete CHLO 를 서버 전송 후 Handshake 완료<br>암호화된 데이터 패킷 전송 가능 |
| **Successful 0-RTT Handshake** | Client & Server | 이전 연결의 캐시된 자격 증명을 사용<br>암호화된 요청 서버로 전송 |
| **Rejected 0-RTT Handshake** | Client & Server | 클라이언트의 캐싱된 정보가 오래된 경우 다시 1-RTT Handshake 를 재수행 |

---

## 연계 토픽

- [HTTP/3](/docs/nw/07-osi-layer/http3)
- [TLS](/docs/nw/07-osi-layer/tls)

---

## 학습 체크리스트

- [ ] QUIC 개념 이해
- [ ] 1-RTT, 0-RTT Handshake 절차 파악
- [ ] TCP와의 차이점 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


