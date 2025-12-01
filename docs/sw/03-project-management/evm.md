---
layout: default
title: EVM (Earned Value Management)
parent: 3. 프로젝트 관리
grand_parent: SW (소프트웨어공학)
nav_order: 8
---

# EVM (Earned Value Management)
{: .fs-8 }

3.1 일정/범위/위험 관리
{: .label .label-purple }

---

## 핵심 키워드

`PV` `EV` `AC` `SV` `CV` `SPI` `CPI` `ETC` `EAC` `VAC` `TCPI`

---

## 정의/개념

사업의 업무 범위, 일정 및 비용에 대한 개발 성과를 통합 관리 함으로써, 프로젝트의 최종 사업 일정과 비용을 예측하여 Risk를 사전에 조치할 수 있는 관리 기법

---

## 지표

### 계획 요소

| 구성 지표 | 설명 |
|:---------|:-----|
| **BAC (Budget At Completion)** | 완료 시점 예산으로 PV를 누적한 예산이며, 전체 프로젝트에 할당된 총 예산 |
| **PV (Planned Value)** | 계획상 현 시점까지 소요 예정이었던 예상 비용 |

### 측정 요소

| 구성 지표 | 설명 |
|:---------|:-----|
| **EV (Earned Value)** | 현재 실제로 달성된 작업까지 계획상의 예상 비용(획득 가치) |
| **AC (Actual Cost)** | 현재까지 실제 수행한 작업까지 실제 사용한 총 비용 |

### 분석 요소

| 구성 지표 | 설명 |
|:---------|:-----|
| **SV (Schedule Variance)** | 완료된 일의 가치와 계획된 가치의 차이<br>SV = EV - PV |
| **CV (Cost Variance)** | 완료된 일의 가치와 실제 원가의 차이<br>CV = EV - AC |
| **SPI (Schedule Performance Index)** | 완성된 작업에 대해 일정 측면 효율성을 측정하기 위한 지수<br>SPI = EV / PV |
| **CPI (Cost Performance Index)** | 완성된 작업에 대해 원가 측면 효율성을 측정하기 위한 지수<br>CPI = EV / AC |

### 예측 요소

| 구성 지표 | 설명 |
|:---------|:-----|
| **ETC (Estimating To Completion)** | 프로젝트를 완료하기 위해 예상되는 추가 원가<br>- ETC = BAC - EV (남은 작업 기반 산정, 향후 CPI = 1, SPI = 1)<br>- ETC = (BAC - EV) / CPI (CPI 향후 지속 가정)<br>- ETC = (BAC - EV) / (CPI × SPI) (CPI 및 SPI 향후 지속 가정) |
| **EAC (Estimating At Completion)** | 프로젝트를 완료하기 위해 예상되는 전체 원가<br>- EAC = AC + (BAC - EV) (예산 기준 완료 가정, 향후 CPI = 1, SPI = 1)<br>- EAC = AC + (BAC - EV) / CPI = BAC / CPI (CPI 향후 지속 가정)<br>- EAC = AC + (BAC - EV) / (누적 CPI × 누적 SPI) (CPI 및 SPI 향후 지속 가정) |
| **VAC (Variance At Completion)** | 실행 예산과 기준 되는 시점에서 예측되는 실제 총비용의 차이<br>VAC = BAC - EAC |

### 완료 성과 지수

| 구성 지표 | 설명 |
|:---------|:-----|
| **TCPI (To-complete Performance Index)** | 계획 가치(PV)를 실현하기 위해 현재부터 완료 시점까지 프로젝트에서 유지해야 하는 CPI 지수<br>- TCPI = (BAC - EV) / (BAC - AC) (BAC 기준 산출)<br>- TCPI = (BAC - EV) / (EAC - AC) (EAC 기준 산출) |

---

## 연계 토픽

- [CPM](/docs/sw/03-project-management/cpm)
- [프로젝트 위험관리](/docs/sw/03-project-management/risk-management)
- [프로젝트 일정관리](/docs/sw/03-project-management/schedule-management)

---

## 학습 체크리스트

- [ ] 계획/측정/분석/예측 요소별 지표 이해
- [ ] PV, EV, AC 개념 이해
- [ ] SV, CV, SPI, CPI 계산 방법 이해
- [ ] ETC, EAC, VAC, TCPI 계산 방법 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

