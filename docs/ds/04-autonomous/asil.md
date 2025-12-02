---
layout: default
title: ASIL
parent: 4. 스마트카/자율주행
grand_parent: DS (Digital Service)
nav_order: 10
---

# ASIL (Automotive Safety Integrity Level)
{: .fs-8 }

4.3 차량 표준 및 안전
{: .label .label-purple }

---

## 정의

ISO 26262에서 정의한 자동차 기능 안전 시스템의 **안전 무결성 등급**

---

## ASIL 등급

| 등급 | 안전 수준 | 설명 | 예시 |
|:-----|:---------|:-----|:-----|
| **ASIL D** | 최고 | 가장 엄격한 안전 요구사항 | 브레이크 시스템, 조향 시스템 |
| **ASIL C** | 높음 | 높은 안전 요구사항 | 에어백 제어 |
| **ASIL B** | 중간 | 중간 안전 요구사항 | 헤드라이트 제어 |
| **ASIL A** | 낮음 | 낮은 안전 요구사항 | 도어락 제어 |
| **QM** | 품질관리 | 안전 요구사항 없음 | 인포테인먼트 |

---

## ASIL 결정 요소

| 요소 | 설명 | 등급 |
|:-----|:-----|:-----|
| **Severity (S)** | 피해의 심각도 | S0 ~ S3 |
| **Exposure (E)** | 위험 상황 노출 빈도 | E0 ~ E4 |
| **Controllability (C)** | 운전자의 제어 가능성 | C0 ~ C3 |

---

## ASIL 결정 매트릭스

| Severity | Exposure | C1 | C2 | C3 |
|:---------|:---------|:---|:---|:---|
| **S1** | E1 | QM | QM | QM |
| | E2 | QM | QM | QM |
| | E3 | QM | QM | A |
| | E4 | QM | A | B |
| **S2** | E1 | QM | QM | QM |
| | E2 | QM | QM | A |
| | E3 | QM | A | B |
| | E4 | A | B | C |
| **S3** | E1 | QM | QM | A |
| | E2 | QM | A | B |
| | E3 | A | B | C |
| | E4 | B | C | D |

---

## 관련 개념

- [ISO 26262](/docs/ds/04-autonomous/iso-26262)
- [ISO/PAS 21448](/docs/ds/04-autonomous/iso-pas-21448)

---

## 학습 체크리스트

- [ ] ASIL 정의 이해
- [ ] 5가지 등급 (ASIL D/C/B/A, QM) 구분
- [ ] 결정 요소 3가지 (S, E, C) 이해
- [ ] ASIL 결정 매트릭스 활용법 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
- ISO 26262 
