---
layout: default
title: HTTP/3
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 3
---

# HTTP/3
{: .fs-8 }

7.2 응용계층
{: .label .label-yellow }

---

## 핵심 키워드

`QUIC(QUICK UDP Internet Connections)` `TLS 1.3` `UDP` `HTTP 1.1 HOL 블로킹 문제 해결` `멀티 플렉싱` `0-RTT Handshake`

---

## 정의/개념

UDP+TLS 웹 페이지 로딩 시간 개선과 동시에 혼잡제어 및 손실 복구 가능한 **구글 QUIC 기반의 응용계층 프로토콜**

---

## 프로토콜 스택

| HTTP/2 | HTTP/3 |
|:-------|:-------|
| TLS 1.2+ | QUIC (TLS 1.3) |
| TCP | TCP-like congestion control, loss recovery |
| | UDP |
| IP | IP |

---

## 특징

| 특징 | 설명 |
|:-----|:-----|
| **0-RTT 및 1-RTT 연결** | UDP 기반 이전 연결의 캐시된 자격 증명을 사용 |
| **HOL 블로킹 해결** | 다중 Stream 제공 및 개별 Stream 내에서 흐름 제어 제공 |
| **멀티스트리밍 전송** | 멀티 플렉싱된 스트림을 제공 통해 트래픽 손실 최소화 |
| **Selective ACK(SACK)** | 오류 발생시 재전송 통해 에러를 복구하는 ARQ 방식 사용 |
| **Seamless Connection** | Connection ID사용 IP, Port 변경 시 에도 지속적 연결 유지 |

---

## 연결관점 주요기능

| 연결 유형 | 구분 | 설명 |
|:---------|:-----|:-----|
| **1-RTT Connection** | Client | Inchoate CHLO(Client Hello) 서버로 전송 |
| **Initial 1-RTT Handshake** | Server | Diffie-Hellman 공개키, 서버 인증서, 공인 IP 주소 암호화를 포함한 REJ(Rejection)을 Client 로 전송 |
| | Client | Complete CHLO 를 서버 전송 후 Handshake 완료<br>암호화된 데이터 패킷 전송 가능 |
| **Successful 0-RTT Handshake** | Client & Server | 이전 연결의 캐시된 자격 증명을 사용<br>암호화된 요청 서버로 전송 |
| **Rejected 0-RTT Handshake** | Client & Server | 클라이언트의 캐싱된 정보가 오래된 경우 다시 1-RTT Handshake 를 재수행 |

{: .highlight }
> TLS1.3 기능이 QUIC 내부에 포함되어 있으므로 1-RTT 후에 데이터 전송이 가능
> 클라이언트는 0-RTT 즉, 연결 설정 과정 없이 곧 바로 데이터를 서버에게 전송함

---

## 연계 토픽

- [QUIC](/docs/nw/07-osi-layer/quic)
- [TLS](/docs/nw/07-osi-layer/tls)

---

## 학습 체크리스트

- [ ] HTTP/3 개념 이해
- [ ] QUIC 프로토콜 특징 파악
- [ ] 0-RTT, 1-RTT Handshake 동작 원리 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


