---
layout: default
title: ASIL
parent: 1. 소프트웨어 안전
grand_parent: SW (소프트웨어공학)
nav_order: 7
---

# ASIL (Automotive Safety Integrity Level)
{: .fs-8 }

1.2 안전 표준 & 기법
{: .label .label-yellow }

---

## 핵심 키워드

`IEC61508` `차량안전성` `잠재적 심각도` `노출 가능성` `통제 가능성`

---

## 정의/개념

전기전자 장치안전 표준(IEC 61508)의 안전성 보전등급(SIL)을 자동차에 맞게 개선 적용한 차량 안전성등급

---

## 차량안전성 보전등급 결정 요소 : SEC

| 구분 | 내용 |
|:-----|:-----|
| **S (Severity)** | 위험의 잠재적 심각도(Potential severity), S0 ~ S3 |
| **E (Exposure)** | 재난상황에 노출 가능성(Probability of exposure), E0 ~ E4 |
| **C (Controllability)** | 통제 가능성(Controllability), C0 ~ C3 |

---

## 세부구성

### 재난 요인 별 심각도 분석

| 등급(Class) | S0 | S1 | S2 | S3 |
|:------------|:---|:---|:---|:---|
| **설명** | 심각하지 않음 | 가벼운 위험적 결함 | 위험적 (생존 가능) | 위험적 (생존 불확실) |

### 재난 요인 별 노출 가능성 분석

| 등급(Class) | E0 | E1 | E2 | E3 | E4 |
|:------------|:---|:---|:---|:---|:---|
| **설명** | 거의 없음 | 매우 낮음 | 낮음 | 중간 | 높음 |

### 재난 요인 별 통제 가능성 분석

| 등급(Class) | C0 | C1 | C2 | C3 |
|:------------|:---|:---|:---|:---|
| **설명** | 일반적 설명 | 간단히 통제 | 정상 통제 | 어려운 통제 |

---

## ASIL 등급 정의

| ASIL Definition | C1 | C2 | C3 |
|:----------------|:---|:---|:---|
| **S1-E1** | QM | QM | QM |
| **S1-E2** | QM | QM | QM |
| **S1-E3** | QM | QM | A |
| **S1-E4** | QM | A | B |
| **S2-E1** | QM | QM | QM |
| **S2-E2** | QM | QM | A |
| **S2-E3** | QM | A | B |
| **S2-E4** | QM | A | B |
| **S3-E1** | QM | A | B |
| **S3-E2** | QM | A | B |
| **S3-E3** | A | B | C |
| **S3-E4** | A | B | D |

- QM(Quality Management): 기능안전과 무관

---

## 등급

| 등급 | 설명 |
|:-----|:-----|
| **ASIL A** | 기능안전등급 A (Low) |
| **ASIL B** | 기능안전등급 B |
| **ASIL C** | 기능안전등급 C |
| **ASIL D** | 기능안전등급 D (High) |

---

## 연계 토픽

- [ISO 26262](/docs/sw/01-safety/iso-26262)
- [IEC 61508](/docs/sw/01-safety/iec-61508)

---

## 학습 체크리스트

- [ ] ASIL 정의 및 개념 이해
- [ ] SEC (Severity, Exposure, Controllability) 이해
- [ ] ASIL A~D 등급별 특성 이해
- [ ] QM(Quality Management) 개념 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

