---
layout: default
title: 소프트웨어 안전 위험 분석
parent: 1. 소프트웨어 안전
grand_parent: SW (소프트웨어공학)
nav_order: 1
---

# 소프트웨어 안전 위험 분석
{: .fs-8 }

1.1 소프트웨어 안전 개념
{: .label .label-purple }

---

## 핵심 키워드

`FTA` `FMEA` `HAZOP` `ETA` `STPA` `순차적 사고 기반` `시스템 이론 기반`

---

## 정의/개념

| 구분 | 핵심 | 개념 | 키워드 |
|:-----|:-----|:-----|:------|
| **순차적 사고 기반** | FTA | 고장 유발 원인 | 정상사상, 기본사상, 통상사상, And, Or, Gate |
| | FMEA | 고장 모드 영향 | RPN(심각도, 발생도, 검출도) |
| | HAZOP | 이탈상황 | 가이드워드, 파라미터 |
| | ETA | 이벤트 발생 확률 계산 | 귀납분석, 초기 오류 대처 |
| **시스템 이론 기반** | STPA | STAMP 기반, 시스템 간 상호작용 | Control Structure, Unsafe Control Action(UCA) |

---

## 기법별 비교

| 비교 | FTA | FMEA | HAZOP | ETA | STPA |
|:-----|:----|:-----|:------|:----|:-----|
| **절차** | 1. 분석 대상 및 범위 정의<br>2. 고장/위험 정의<br>3. Fault Tree 전개<br>4. Fault Tree 분석 | 1. 분석 대상 및 범위 정의<br>2. 고장모드 도출<br>3. 고장모드 분석<br>4. 영향 분석<br>5. 권고사항 도출 | 1. 분석 대상 및 범위 정의<br>2. 이탈상황 도출<br>3. 영향 및 발생원인 분석<br>4. 위험도 평가 및 개선사항 도출 | 1. 분석 대상 및 범위 정의<br>2. 시스템 위험 또는 사고 정의<br>3. 초기 이벤트 정의<br>4. Event Tree 전개<br>5. 결과(Outcome) 분석 | 1. 사고 및 위험정의<br>2. Control Structure 도식화<br>3. Unsafe Control Action 도출<br>4. 원인 시나리오 도출 |
| **절차두음** | 범고전분 | 범도분영권 | 범이영위 | 범사이트결 | 사컨언원 |

---

## 연계 토픽

- [FTA (결함 수 분석)](/docs/sw/01-safety/fta)
- [FMEA (고장 모드 영향 분석)](/docs/sw/01-safety/fmea)
- [HAZOP (위험 및 운전성 분석)](/docs/sw/01-safety/hazop)
- [IEC 61508](/docs/sw/01-safety/iec-61508)

---

## 학습 체크리스트

- [ ] 순차적 사고 기반 vs 시스템 이론 기반 차이 이해
- [ ] 각 기법별 절차 및 절차두음 암기
- [ ] 핵심 키워드 암기

---

## 참고자료

- 정보관리기술사 SW 학습자료

