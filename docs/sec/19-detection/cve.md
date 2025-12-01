---
layout: default
title: CVE
parent: 탐지/대응
grand_parent: 보안
nav_order: 6
---

# CVE (Common Vulnerabilities and Exposures)
{: .fs-8 }

19.6 탐지/대응
{: .label .label-purple }

---

## 핵심 키워드

`MITRE` `SW 보안 취약점` `고유번호` `CVSS`

---

## 정의/개념

미국 MITRE 기관에서 일반적 SW에서 공통적으로 발생하는 **잠재적 보안취약점을 가리키는 고유번호**를 표준화한 체계

---

## 특징

| 구분 | 설명 |
|:-----|:-----|
| **개념** | 미국 비영리 회사인 MITRE 社에서 1999년 처음 만들어 운영하기 시작한 공개적으로 알려진 소프트웨어의 보안취약점을 가리키는 고유번호를 표준화한 체계 |
| **목적** | 보안 취약점 식별하기 위한 번호체계 |
| **분류기준** | 접두사, 발견연도, 취약점번호 |
| **선정기준** | MITRE 심사, 취약점 수집 및 평가(CVSS) |
| **체계내용** | 보안 취약점 명칭, 고유번호, 히스토리 |

---

## CVE 번호 체계

```
  CVE  -  2016  -  0000
   │        │        │
   │        │        └── 취약점번호
   │        │
   │        └── 발견연도
   │
   └── 접두사
```

---

## 주요 CVE 사례

| CVE 번호 | 취약점명 | 설명 |
|:---------|:---------|:-----|
| **CVE-2017-5753** | 스펙터 (Spectre) | CPU 취약점 |
| **CVE-2017-5754** | 멜트다운 (Meltdown) | CPU 취약점 |
| **CVE-2010-0249** | 0-Day 취약점 | Internet Explorer 취약점 |
| **CVE-2017-5638** | Apache Struts2 | RCE(Remote Code Execution) |
| **CVE-2021-44228** | Log4Shell | Log4j RCE |

{: .warning }
> CWE에서 CVE로 구체화될 때 연결을 끊는 방법으로 사이버 킬 체인 활용

---

## CVSS (Common Vulnerability Scoring System)

| 등급 | 점수 범위 | 설명 |
|:-----|:---------|:-----|
| **Critical** | 9.0 - 10.0 | 매우 심각 |
| **High** | 7.0 - 8.9 | 심각 |
| **Medium** | 4.0 - 6.9 | 중간 |
| **Low** | 0.1 - 3.9 | 낮음 |
| **None** | 0.0 | 없음 |

---

## 연계 토픽

- [CWE](/docs/sec/19-detection/cwe)
- [사이버 킬 체인](/docs/sec/19-detection/cyber-kill-chain)
- [취약점 스캐닝](/docs/sec/)

---

## 학습 체크리스트

- [ ] CVE의 정의와 번호 체계 이해
- [ ] 주요 CVE 사례 숙지
- [ ] CVSS 점수 체계 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료

