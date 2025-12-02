---
layout: default
title: DID
parent: 3. 블록체인
grand_parent: DS (Digital Service)
nav_order: 13
---

# DID (Decentralized Identity)
{: .fs-8 }

3.5 ID/Wallet
{: .label .label-purple }

---

## 특징

| 특징 | 설명 |
|:-----|:-----|
| **Decentralized** | 중앙화된 인증 등록이 요구되지 않음 |
| **Digital Hub** | 개인이 Identity를 저장, 소유, 제어 가능 |
| **블록체인** | 블록체인 기반 인증 |

---

## 구성도 및 기술요소

```
┌──────────────────────────────────────────────────────┐
│                    Holder (소유자)                    │
│                         │                            │
│   ┌─────────────────────┼─────────────────────┐      │
│   │                     ▼                     │      │
│   │  ┌─────────┐   DID Auth   ┌─────────┐    │      │
│   │  │  Issuer │◄────────────►│ Verifier│    │      │
│   │  │ (발급자) │             │ (검증자) │    │      │
│   │  └────┬────┘             └────┬────┘    │      │
│   │       │                       │         │      │
│   │       ▼                       ▼         │      │
│   │  Verifiable           DIDs(URN)         │      │
│   │  Credentials          검증              │      │
│   └─────────────────────────────────────────┘      │
│                         │                          │
│                         ▼                          │
│               ┌─────────────────┐                  │
│               │   Blockchain     │                  │
│               │   (DID Registry) │                  │
│               └─────────────────┘                  │
└──────────────────────────────────────────────────────┘
```

---

## 기술요소

| 기술 | 설명 |
|:-----|:-----|
| **Verifiable Credentials (VC)** | 증명서, 신원증명 (디지털 인증서) |
| **DIDs** | Decentralized Identifiers, 통합자원이름(URN) |
| **DID Auth** | DID 소유자가 사설키로 인증 |
| **DKMS** | Decentralized Key Management System, 사설키 공개 표준 |

---

## DID vs 기존 인증 비교

| 구분 | 기존 인증 | DID |
|:-----|:----------|:----|
| **관리 주체** | 중앙 기관 | 사용자 본인 |
| **저장 위치** | 중앙 서버 | 분산 저장 |
| **개인정보** | 기관에 제공 | 최소 정보만 제공 |
| **검증 방식** | 기관 인증 | 블록체인 검증 |

---

## 관련 개념

- [디지털 ID](/docs/ds/03-blockchain/디지털-id)
- [디지털 신분증](/docs/ds/03-blockchain/디지털-신분증)
- [영지식 증명](/docs/ds/03-blockchain/영지식-증명)

---

## 학습 체크리스트

- [ ] DID 3가지 특징 이해
- [ ] 기술요소 4가지 (VC, DIDs, DID Auth, DKMS) 이해
- [ ] DID vs 기존 인증 차이점 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료 
