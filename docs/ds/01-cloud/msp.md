---
layout: default
title: MSP
parent: 1. 클라우드
grand_parent: DS (Digital Service)
nav_order: 9
---

# CSP, MSP
{: .fs-8 }

1.4 클라우드 운영
{: .label .label-yellow }

---

## 핵심 키워드

| 구분 | 키워드 |
|:-----|:-------|
| **CSP** | `AWS` `Azure` `Google` |
| **MSP** | `메가존` `베스핀 글로벌` |

---

## 정의/개념

| 구분 | 정의 |
|:-----|:-----|
| **CSP** | 클라우드 인프라 기반, **IaaS, PaaS, SaaS 제공** 클라우드 서비스 기업 |
| **MSP** | 클라우드 인프라 없이, **시스템 구축/이전 운영 컨설팅 제공** 클라우드 서비스 기업 |

---

## 개념도

```
                "On Demand"              "클라우드 요구사항"
                    │                          │
    ┌───────────────▼───────────────┐   ┌──────▼──────┐
    │             CSP               │   │    고객      │
    │  ┌───────────────────────┐    │   └──────┬──────┘
    │  │        IaaS           │    │          │
    │  ├───────────────────────┤    │   "맞춤형 클라우드
    │  │        PaaS           │◄───┼─── 서비스 제공"
    │  ├───────────────────────┤    │          │
    │  │        SaaS           │    │   ┌──────▼──────┐
    │  └───────────────────────┘    │   │     MSP     │
    │      "Pay per Use"            │   │ "클라우드    │
    └───────────────────────────────┘   │  서비스      │
                                        │  파트너"     │
                                        └─────────────┘
```

---

## CSP와 MSP 상세 비교

| 비교 항목 | CSP | MSP |
|:---------|:----|:----|
| **목적** | Public 클라우드 환경 제공 | 고객 환경에 최적화된 맞춤형 클라우드 상품 제공 |
| **역할** | 클라우드 서비스 제공 | 클라우드 매니지드 제공 |
| **인프라** | 클라우드 인프라 보유 | 클라우드 인프라 미보유 (일부 보유한 사례도 존재) |
| **서비스** | IaaS, PaaS, SaaS | 컨설팅, 마이그레이션, 운영 |
| **핵심역량** | - Cloud Virtualization<br>- Cloud Portal<br>- Cloud Measured Service(과금)<br>- SASE(Secure Access Service Edge)<br>- SECaaS(Security as a Service) | - Cloud Rehost, Replatform, Refactoring<br>- Cloud Management Tool<br>- CSP의 Cloud 서비스의 이해<br>- 고객 비즈니스 도메인의 이해 |
| **업체** | AWS, Azure, GCP | 베스핀글로벌, 메가존, SDS, CNS |

---

## 참고

최근 보안 업계에서도 **MSSP(Managed Security Service Provider)** 사업 분야도 활발하게 추진중

---

## 관련 개념

- [클라우드 컴퓨팅](/docs/ds/01-cloud/클라우드-컴퓨팅)
- [XaaS (IaaS/PaaS/SaaS)](/docs/ds/01-cloud/xaas-iaas-paas-saas-daas-secaas)

---

## 학습 체크리스트

- [ ] CSP vs MSP 정의 구분
- [ ] 각 역할과 핵심역량 이해
- [ ] 대표 업체 숙지

---

## 참고자료

- 정보관리기술사 DS 학습자료
