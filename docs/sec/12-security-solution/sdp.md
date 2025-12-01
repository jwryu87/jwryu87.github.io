---
layout: default
title: SDP
parent: 보안솔루션
grand_parent: 보안
nav_order: 5
---

# SDP (Software Defined Perimeter)
{: .fs-8 }

12.5 보안솔루션
{: .label .label-purple }

---

## 핵심 키워드

`SDP Agent` `SDP Controller` `SDP Gateway` `PKI` `SAML` `Zero Trust` `RBAC` `IPSec` `SPA`

---

## 정의/개념

**선 인증, 후 연결**, 사용자 상태 및 ID 기반 **클라우드 환경 네트워크 접근제어 프레임워크**

- 인증/인가가 되기 전에는 DNS 정보나 IP주소를 알 수 없어 보안성이 향상됨

---

## 메커니즘/구성요소

### SDP 아키텍처

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│                          SDP                    ② 정보전달           │
│     ① 접속요청        Controller ───────────────────▶  서비스        │
│           │               │                                          │
│           │          ③ 접속허가                                      │
│           │               │                                          │
│         SDP              SDP                                         │
│        Agent ─────────▶ G/W ─────────▶  서비스                       │
│           │          ④ 보안접속                                      │
│           │                          ⑤ 허용 서비스 접속               │
│           │                              서비스                       │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### 동작 절차

| 구분 | 절차 | 설명 |
|:-----|:-----|:-----|
| **① 접속요청** | 인증 | 인증 기술을 활용해 접속 요청 (OAuth 등) |
| **② 정보전달** | 인증 | SPA(Single Packet Authorization) 활용한 사용자 인증 |
| **③ 접속허가** | 인증 | Zero Trust 기반의 보안 접근 정책 및 통제 |
| **④ 보안접속** | 접속 | IPSec 활용한 전송모드, 터널모드 방식의 보안 접속 |
| **⑤ 허용 서비스 접속** | 접속 | 인증된 사용자의 보호된 서비스 접속 후 서비스 제공 |

---

## SDP의 구성요소

| 구성요소 | 핵심 기술 | 설명 |
|:---------|:---------|:-----|
| **SDP Agent** | PKI, SAML<br>OAuth | - SDP Controller와 통신 후 접속허가와 SDP Gateway로 보안접속 처리 |
| **SDP Controller** | Zero Trust<br>RBAC | - 모든 SDP 구성요소와 통신하며 관리자 역할을 수행함<br>- 정책에 따른 구성요소 간의 연결 가능여부 결정<br>- Agent의 접속 요청에 따라 신뢰 및 상태 등 확인, 접근제어 정책 결정 |
| **SDP Gateway** | IPSec<br>SPA (단일 패킷인증) | - SDP Controller로 제어된 모든 접속 요청을 거부함(reject)<br>- SDP Controller에 의해 신뢰이 확인된 사용자 및 어플리케이션에 대한 연결 기능 제공 |

---

## SDP와 VPN 비교

| 구분 | SDP | Site to Site VPN | Remote Access VPN |
|:-----|:----|:-----------------|:-----------------|
| **특징** | 권한이 없는 서버는 노출되지 않음 | 가상 사설망 내의 서버IP, 서비스 포트 노출 | 가상 사설망 내의 서버IP, 서비스 포트 노출 |
| **에이전트 프로그램** | 제로트러스트 위해 필요 | 에이전트 방식, 비 에이전트 방식 제공 | 에이전트 불필요 |
| **인증방식** | 선인증 후 접속방식으로 SDP Gateway의 목적지 노출 | 선접속, 후 인증방식으로 VPN Gateway의 목적지 노출 | 선접속, 후 인증방식으로 VPN Gateway의 목적지 노출 |
| **채널구분** | 제어(Control) 채널과 데이터(Data) 채널 구분 | 채널구분 없음 | 채널구분 없음 |
| **방화벽 운영방식** | 화이트리스트 방식, ID 기반 동적설정(운영 및 관리 편리) | 블랙리스트 방식, IP 기반 정적 설정(운영 및 관리 난해) | 블랙리스트 방식, IP 기반 정적 설정(운영 및 관리 난해) |
| **취약점 및 완방법** | 장비등록후의 디바이스키와 사용자 계정정보 일치, 이 후 2차 인증을 통과해야 연결 허가 | 에이전트 프로그램, ID/PW 노출시 타 장비에서 접근가능, 보안위험 솔루션 필요(IPM, NAC등) | 신규 단말은 모든 서버에 접근가능, 보안위협 솔루션 필요(IPM, NAC등) |

- VPN은 블랙리스트 방식의 IP 기반 정적 결정, SDP는 화이트 리스트 방식의 ID 기반 동적 결정임

---

## SDP 핵심 원리

| 원리 | 설명 |
|:-----|:-----|
| **선 인증, 후 연결** | 접속 전 인증 수행, 인증 후 연결 허용 |
| **최소 권한 원칙** | 필요한 리소스만 접근 허용 |
| **네트워크 은닉** | 인증 전 서비스 정보 비공개 |
| **SPA** | Single Packet Authorization으로 1차 검증 |

---

## 연계 토픽

- [ZTNA](/docs/sec/01-cloud/sase)
- [제로 트러스트](/docs/sec/12-security-solution/zero-trust)
- [VPN](/docs/sec/16-network-security/)
- [SASE](/docs/sec/01-cloud/sase)

---

## 학습 체크리스트

- [ ] SDP 3가지 구성요소 (Agent, Controller, Gateway) 이해
- [ ] SDP vs VPN 비교 항목 파악
- [ ] SPA(Single Packet Authorization) 개념 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료
- CSA(Cloud Security Alliance) SDP Specification


