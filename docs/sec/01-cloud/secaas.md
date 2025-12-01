---
layout: default
title: SECaaS
parent: 클라우드 보안
grand_parent: 보안
nav_order: 2
---

# SECaaS (Security as a Service)
{: .fs-8 }

1.1 클라우드 보안
{: .label .label-purple }

> 암기: **미러링**

---

## 핵심 키워드

`CSP` `MSP` `SSP` `엔드포인트` `Cloud보안서비스`

---

## 정의/개념

클라우드 형태로 보안서비스를 제공하는 것으로 **클라우드 인프라를 통해 전문화된 보안서비스**

---

## 구성도

```
┌─────────────────────────────────────────────────────────────┐
│                        SECaaS                               │
│  ┌─────────────────┐      ┌──────────────────────────────┐  │
│  │ Security        │      │         (SECaaS)             │  │
│  │ Manager Cloud   │──IPS─│  Security as a Service       │  │
│  │                 │      │                              │  │
│  │  Security Cloud─┼──────│    ┌────┐ ┌────┐            │  │
│  │  Security Cloud─┼──────│    │ IAM│ │SIEM│            │  │
│  │  Security Cloud─┼──────│    └────┘ └────┘            │  │
│  └─────────────────┘      └──────────────────────────────┘  │
│           ↑                                                  │
│      Cloud User                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 평가지표

| 카테고리 | 설명 | 카테고리 | 설명 |
|:---------|:-----|:---------|:-----|
| **BCDR**(Business Continuity and Disaster Recovery) | 비즈니스 연속성 및 재해복구 | **Intrusion Management** | 침입 시도 탐지 및 방지 |
| **Continuous monitoring** | 지속적인 위험관리 | **Network Security** | 네트워크 보안 |
| **DLP**(Data Loss Prevention) | 데이터 암호화, 민감 데이터 관리 | **Security Assessment** | 거버넌스 & 리스크 관리, 컴플라이언스 감사 |
| **E-Mail Security** | 악성 첨부파일과 스팸으로부터 조직보호 | **SIEM**(Security Information and Event Management) | 실시간 로그, 보안이벤트, 시스템 정보 수집 |
| **Encryption** | 데이터 암호화 | **Vulnerability Scanning** | 취약점 검사 |
| **IAM**(Identity and Access Management) | 인증, 신원보증, 권한관리 | **Web Security** | 웹 트래픽, 웹 애플리케이션 보안 |

---

## SECaaS vs CASB 비교

| 구분 | SECaaS | CASB |
|:-----|:-------|:-----|
| **목적** | 보안 서비스 전체 제공 | 클라우드 접근 보안 중점 |
| **범위** | 광범위한 보안 서비스 | 클라우드 서비스 접근 제어 |
| **형태** | 클라우드 기반 보안 서비스 | 클라우드 접근 중개 보안 |

---

## 연계 토픽

- [CASB](/docs/sec/01-cloud/casb)
- [SASE](/docs/sec/01-cloud/sase)
- [Zero Trust](/docs/sec/12-security-solution/zero-trust)

---

## 학습 체크리스트

- [ ] SECaaS의 주요 서비스 카테고리 이해
- [ ] SECaaS vs CASB 차이점 파악
- [ ] 클라우드 보안 서비스 트렌드 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료

