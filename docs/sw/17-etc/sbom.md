---
layout: default
title: SBOM (Software Bill of Materials)
parent: 17. 기타
grand_parent: SW (소프트웨어공학)
nav_order: 16
---

# SBOM (Software Bill of Materials)
{: .fs-8 }

기타
{: .label .label-yellow }

---

## 핵심 키워드

`Author Name` `Timestamp` `Version String` `SPDX` `CycloneDX` `SWID`

---

## 정의/개념

소프트웨어 컴포넌트 및 구성 요소를 식별할 수 있는 **메타데이터와 저작권 및 라이선스** 등으로 소프트웨어 콘텐츠에 대한 정보를 포함하는 **공식 SW 자재 명세서**

---

## 개념도

```
                    ┌──────────────┐
                    │ Bingo Buffer │
                    │    V2.2      │
                    └──────┬───────┘
                           │ Included in
                           ▼
                    ┌──────────────────┐
┌─────────────┐     │      Acme       │
│    Carol    │     │   Application   │
│ Compression │────▶│      V1.1      │
│    V3.1     │     └──────────────────┘
└─────────────┘              ▲
                             │ Included in
                    ┌────────┴───────┐
                    │  Bob Browser   │
                    │     V2.1       │
                    └────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Component Name │ Supplier │ Version │ Author │ Hash  │ UID │
├────────────────┼──────────┼─────────┼────────┼───────┼─────┤
│ Application    │ Acme     │ 1.1     │ Acme   │ 0x123 │ 234 │
│ ..Browser      │ Bob      │ 2.1     │ Bob    │ 0x223 │ 334 │
│ ..Compression  │ Carol    │ 3.1     │ Acme   │ 0x323 │ 434 │
│ ..Buffer       │ Bingo    │ 2.2     │ Acme   │ 0x423 │ 534 │
└─────────────────────────────────────────────────────────────┘
```

---

## 기술요소

### Baseline Attributes (기본 속성)

| 핵심 기술 | 설명 |
|:----------|:-----|
| **Author Name** | SW 작성자 정보 |
| **Timestamp** | SBOM이 마지막으로 업데이트된 날짜 및 시간 (ISO 8601) |
| **Supplier Name** | SW 공급업체의 이름 또는 기타 식별자 |
| **Component Name** | SW 구성요소 이름 또는 식별자 |
| **Version String** | SW Version 정보 (Semantic Versioning) |
| **Component Hash** | SW 컴포넌트 해시 값을 통한 무결성 증빙 |
| **Unique Identifier** | 고유한 Namespace 및 고유 식별자 생성 |
| **Relationship** | SBOM 구성 요소 간의 종속성 및 연간 관계 표현 |

### Formats (표준 포맷)

| 포맷 | 설명 |
|:-----|:-----|
| **SPDX** | - Software Package Data Exchange<br>- 리눅스 재단 오픈소스 저작권 및 라이선스 정보 교환 표준 |
| **CycloneDX** | - OWASP 재단 공급망 구성요소 보안 및 결함 SBOM 표준 |
| **SWID** | - Software Identification<br>- SW 정보에 대한 Tag 생성 및 오픈소스 SW 인벤토리 지원 |

---

## SBOM 활용 분야

| 분야 | 활용 내용 |
|:-----|:---------|
| **공급망 보안** | 서드파티 컴포넌트 취약점 파악 |
| **라이선스 컴플라이언스** | 오픈소스 라이선스 준수 확인 |
| **취약점 관리** | CVE 기반 보안 취약점 추적 |
| **자산 관리** | SW 구성요소 인벤토리 관리 |

---

## 연계 토픽

- [오픈소스 라이선스](/docs/sw/16-opensource/license)
- [오픈소스 거버넌스](/docs/sw/16-opensource/opensource-governance)

---

## 학습 체크리스트

- [ ] SBOM의 정의와 필요성 이해
- [ ] Baseline Attributes 항목 암기
- [ ] SPDX, CycloneDX, SWID 포맷 구분

---

## 참고자료

- 정보관리기술사 SW 학습자료
