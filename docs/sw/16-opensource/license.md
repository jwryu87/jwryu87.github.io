---
layout: default
title: 오픈소스 라이선스
parent: 16. 오픈소스
grand_parent: SW (소프트웨어공학)
nav_order: 2
---

# 오픈소스 (특징, 라이선스)
{: .fs-8 }

오픈소스
{: .label .label-green }

---

## 핵심 키워드

`MPL` `EPL` `GPL` `BSD` `Apache 2.0` `MIT`

---

## 정의/개념

오픈소스 소프트웨어 개발자와 이용자 간에 **사용방법 및 조건 범위 명시**한 오픈소스 소프트웨어 계약서

---

## 오픈소스의 특징 (OSI 10대 원칙)

| 번호 | 원칙 | 설명 |
|:-----|:-----|:-----|
| 1 | **Free Redistribution** | 자유로운 재배포 |
| 2 | **Source Code** | 소스코드의 제공 |
| 3 | **Derived Works** | 수정 · 개작의 허용 |
| 4 | **Integrity of The Author's Source Code** | 원저작자 정보삭제 금지 |
| 5 | **No Discrimination Against Persons or Groups** | 사람의 차별금지 |
| 6 | **No Discrimination Against Fields of Endeavor** | 영역의 차별금지 |
| 7 | **Distribution of License** | 라이선스의 제공 |
| 8 | **License Must Not Be Specific to a Product** | 보편적인 라이선스 |
| 9 | **License Must Not Restrict Other Software** | 동일한 조건의 라이선스 |
| 10 | **License Must Be Technology-Neutral** | 기술중립적인 라이선스 |

---

## 라이선스 분류 체계

```
                    SW에 대한 지식재산권으로 보호
                  (저작권, 특허권, 상표권, 영업비밀)
                              │
                         소프트웨어 (Software)
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
       비 FOSS 라이선스                  FOSS 라이선스
         (사유 SW)                            │
              │                   ┌───────────┴───────────┐
    ┌─────────┼─────────┐         ▼                       ▼
    ▼         ▼         ▼    변형 의무                반환 불필요
  특허      비특허     공유불가능  (Reciprocal)         (Permissive)
   SW        SW        SW          │                       │
    │         │         │    ┌─────┴─────┐           ┌─────┴─────┐
    ▼         ▼         ▼    ▼           ▼           ▼           ▼
 상용 SW   Freeware   특허조항     제약        무제약
 (EULA)   (EULA)                    │            │
                               ┌────┴────┐   ┌───┴───┬───────┐
                               ▼         ▼   ▼       ▼       ▼
                              EPL       MPL AGPL    GPL     LGPL
                                            3.0     3.0     2.1
                                                    GPL     Apache
                                                    2.0      2.0
                                                    BSD      MIT
```

---

## 주요 라이선스 비교

| 라이선스 | 유형 | 소스 공개 의무 | 수정 배포 시 | 특징 |
|:---------|:-----|:--------------|:-------------|:-----|
| **GPL 3.0** | Reciprocal | 전체 공개 | 동일 라이선스 | 가장 강력한 Copyleft |
| **GPL 2.0** | Reciprocal | 전체 공개 | 동일 라이선스 | 리눅스 커널 적용 |
| **LGPL 2.1** | Reciprocal (약함) | 수정 부분만 | 동일 라이선스 | 라이브러리용 |
| **AGPL 3.0** | Reciprocal | 네트워크 서비스 포함 | 동일 라이선스 | 서버 SW에 강력 적용 |
| **MPL** | Reciprocal (약함) | 파일 단위 | 파일별 적용 | Mozilla 재단 |
| **EPL** | Reciprocal (약함) | 모듈 단위 | 모듈별 적용 | Eclipse 재단 |
| **Apache 2.0** | Permissive | 의무 없음 | 자유롭게 | 특허권 명시 |
| **BSD** | Permissive | 의무 없음 | 자유롭게 | 매우 관대 |
| **MIT** | Permissive | 의무 없음 | 자유롭게 | 가장 간단 |

---

## 라이선스 선택 가이드

| 상황 | 권장 라이선스 |
|:-----|:-------------|
| 완전 자유로운 사용 허용 | MIT, BSD |
| 특허권 보호 필요 | Apache 2.0 |
| 수정 시 소스 공개 강제 | GPL |
| 라이브러리만 공개 | LGPL |
| 네트워크 서비스 포함 | AGPL |

---

## 연계 토픽

- [오픈소스 거버넌스](/docs/sw/16-opensource/opensource-governance)
- [SBOM](/docs/sw/17-etc/sbom)
- [라이선스 호환성](/docs/sw/16-opensource/license-compatibility)

---

## 학습 체크리스트

- [ ] OSI 10대 원칙 이해
- [ ] Reciprocal vs Permissive 구분
- [ ] GPL, Apache, MIT 차이점 암기

---

## 참고자료

- 정보관리기술사 SW 학습자료
