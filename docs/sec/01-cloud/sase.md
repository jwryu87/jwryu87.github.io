---
layout: default
title: SASE
parent: 클라우드 보안
grand_parent: 보안
nav_order: 3
---

# SASE (Secure Access Service Edge)
{: .fs-8 }

1.1 클라우드 보안
{: .label .label-purple }

---

## 핵심 키워드

`SD-WAN` `SDP` `POP` `CASB` `ZTNA` `NGFW` `SECaaS` `FWaaS`

---

## 정의/개념

기존의 SD-WAN과 같은 네트워크 서비스와 **ZTNA(Zero Trust Network Access)**, **NGFW(Next Generation FireWall)**, **SECaaS**, **FWaaS**와 같은 클라우드 보안 기능을 통합한 **보안 아키텍처**

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────────────────┐
│                           On-Network                                 │
│                                                                      │
│   ┌─────────┐                    POP                                │
│   │ Branch  │───SD-WAN──┬────────────────────────┬───────► SaaS     │
│   └─────────┘           │   App    │   URL      │   SSL  │         │
│                         │ Control  │ Filtering  │Inspect │         │
│   ┌─────────┐           │          │            │        │ Private │
│   │ User/   │───SDP─────┤   ZTNA   │  Sandbox   │ FWaaS  │ Cloud   │
│   │ Device  │           │          │            │        │         │
│   └─────────┘           └────────────────────────┘        │ Public  │
│                           Cloud Delivered SASE            │ Cloud   │
│                         Off-Network                       │         │
│   ┌─────────┐                                  Secured    │         │
│   │ Client  │──────────────────────────────►  Cloud      │         │
│   └─────────┘                                  Service    │         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 핵심기술

### 네트워크 가상화

| 구분 | 핵심 기술 | 설명 |
|:-----|:----------|:-----|
| **SD-WAN** | - SDN(Software Define Network) + WAN(Wide Area Network)<br>- 인터넷망 기반 Overlay Network 구현(비용 저렴) |
| **SDP** | - 신원을 기반으로 리소스에 대한 액세스 제어 프레임워크<br>- SDP(Software Defined Perimeter) Controller, Host |
| **POP** | - Point of Presence<br>- 원격 사용자와 클라우드 보안 연동 접점 |

### 클라우드 보안

| 구분 | 핵심 기술 | 설명 |
|:-----|:----------|:-----|
| **ZTNA** | - Zero Trust Network Access, 최소 권한(Least Privilege) 원칙<br>- 기본 비신뢰 (Zero Trust) 기반 보안 정책 Whitelist 정책 |
| **CASB** | - Cloud Access Security Broker<br>- 클라우드 사용자 모니터링, 보안 정책 준수 |
| **FWaaS / NGFW** | - FireWall as a Service / Next Generation FireWall<br>- URL 필터링, APT, IPS, DNS 보안 기능 제공 |
| **SWG** | - Secure Web Gateway<br>- 웹, 인터넷 트래픽 기준 악성코드 탐지, 접속 차단 수행 |

---

## SASE vs 기존 보안 비교

| 구분 | 기존 보안 | SASE |
|:-----|:----------|:-----|
| **경계** | 네트워크 경계 기반 | 사용자/디바이스 기반 |
| **접근방식** | Castle & Moat | Zero Trust |
| **확장성** | 제한적 | 클라우드 기반 확장 |
| **통합** | 개별 솔루션 | 통합 플랫폼 |

---

## 연계 토픽

- [CASB](/docs/sec/01-cloud/casb)
- [SECaaS](/docs/sec/01-cloud/secaas)
- [Zero Trust](/docs/sec/12-security-solution/zero-trust)
- [SDP](/docs/sec/12-security-solution/sdp)

---

## 학습 체크리스트

- [ ] SASE 핵심 구성요소 이해 (SD-WAN, SDP, ZTNA, CASB)
- [ ] 기존 보안과 SASE의 차이점 파악
- [ ] 네트워크 가상화와 클라우드 보안 기술 연계 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료
- Gartner SASE Framework

