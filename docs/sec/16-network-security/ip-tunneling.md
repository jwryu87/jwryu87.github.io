---
layout: default
title: IP 터널링
parent: 네트워크 보안
grand_parent: 보안
nav_order: 1
---

# IP 터널링 (IP Tunneling)
{: .fs-8 }

16.1 네트워크 보안
{: .label .label-yellow }

---

## 핵심 키워드

`캡슐화` `역캡슐화` `Passenger` `Carrier` `Transport`

---

## 정의/개념

개별통신망 환경에서 사용하는 통신 규약을 **IP 통신 규약으로 캡슐화/역캡슐화** 하여 **가상의 터널을 형성**하고 안전하게 데이터를 송수신 하는 기술

---

## 구성도

```
                        ┌─────────────────────┐
                        │     전송 네트워크     │
                        │                     │
┌──────────┐           │    ┌───────────┐    │           ┌──────────┐
│ A Client │◀─────────▶│    │  IP 터널  │    │◀─────────▶│ B Client │
└──────────┘           │    └───────────┘    │           └──────────┘
     │                 │                     │                 │
     │캡슐화            └─────────────────────┘           역캡슐화│
     │                                                          │
     ▼                                                          ▼
┌──────────────────┐                              ┌──────────────────┐
│ 애플토크, CLNS,  │                              │ 애플토크, CLNS,  │
│ IP, IPX          │                              │ IP, IPX          │
├──────────────────┤    Passenger Protocol        ├──────────────────┤
│ GRE, IPSec, IP in│                              │ GRE, IPSec, IP in│
│ IP, L2TP, MPLS,  │    Carrier Protocol          │ IP, L2TP, MPLS,  │
│ STUN, DLSw+      │                              │ STUN, DLSw+      │
├──────────────────┤    Transport Protocol        ├──────────────────┤
│        IP        │                              │        IP        │
└──────────────────┘                              └──────────────────┘
```

---

## IP 터널링 구성요소

| 프로토콜 | 설명 | 프로토콜 유형 |
|:---------|:-----|:-------------|
| **Passenger Protocol** | 캡슐화가 되어야할 프로토콜 | 애플토크, CLNS, IP, IPX |
| **Carrier Protocol** | 캡슐화 시킬 프로토콜 | GRE, IPSec, IP-in-IP, L2TP, MPLS, STUN, DLSw+ |
| **Transport Protocol** | Carrier Protocol 을 전송할 프로토콜 | IP |

- 가상의 터널 형성 및 데이터 전송을 위한 프로토콜로 구성됨

---

## IP 터널링 기술 유형

### 2 계층 (Layer 2)

| 유형 | 설명 | 특징 |
|:-----|:-----|:-----|
| **PPTP** | PPP 패킷을 IP 패킷 내 캡슐화<br>Client / Server 모드, MS 社 개발 | 사용자 인증, 캡슐화 제공<br>데이터 암호화 기능 미제공 |
| **L2TP** | PPTP 및 L2F 의 기술적 장점 결합<br>터널 유지 위해 UDP 사용 | 사용자 인증, 데이터 압축<br>암호화 기능 제공 |

### 3 계층 (Layer 3)

| 유형 | 설명 | 특징 |
|:-----|:-----|:-----|
| **GRE** | Site to Site IP 터널링 프로토콜<br>종단 라우터 간 연결, CISCO 社 개발 | 가상 시리얼 링크 인터페이스<br>데이터 암호화 기능 미제공 |
| **IPSec** | 가상 보안 통로 형성 (VPN 활용)<br>인증(AH), 암호화(ESP), 키관리(IKE) | 터널모드(패킷 전체 보호)<br>전송모드(데이터 보호) 제공 |

### 4 계층 (Layer 4)

| 유형 | 설명 | 특징 |
|:-----|:-----|:-----|
| **SSL/TLS** | 웹서버와 브라우저간의 안전한 통신<br>서버인증, 클라이언트인증, 기밀성 | Handshake, 압축, 암호화<br>인증서 기반, 443 port |
| **SOCKS v5** | 클라이언트와 서버간 패킷 교환<br>TCP 연결을 임의의 IP주소에 프록시 | IP를 숨기고 뛰어난 성능 제공<br>터널링 기능을 이용한 프록시 |

---

## 터널링 프로토콜 비교

| 구분 | PPTP | L2TP | GRE | IPSec | SSL/TLS |
|:-----|:-----|:-----|:----|:------|:--------|
| **계층** | L2 | L2 | L3 | L3 | L4 |
| **인증** | O | O | X | O | O |
| **암호화** | X | O | X | O | O |
| **표준** | MS | RFC | CISCO | IETF | IETF |
| **용도** | 원격접속 | 원격접속 | Site-to-Site | VPN | 웹 보안 |

---

## 연계 토픽

- [IPsec](/docs/sec/16-network-security/ipsec)
- [VPN](/docs/sec/16-network-security/vpn)
- [TLS](/docs/sec/10-cryptography/)

---

## 학습 체크리스트

- [ ] IP 터널링의 정의와 구성요소 이해
- [ ] Passenger, Carrier, Transport 프로토콜 구분
- [ ] 2/3/4 계층별 터널링 프로토콜 특징 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료

