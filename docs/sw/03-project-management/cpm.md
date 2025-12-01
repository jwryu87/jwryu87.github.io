---
layout: default
title: CPM (Critical Path Method)
parent: 3. 프로젝트 관리
grand_parent: SW (소프트웨어공학)
nav_order: 2
---

# CPM (Critical Path Method)
{: .fs-8 }

3.1 일정/범위/위험 관리
{: .label .label-purple }

---

## 핵심 키워드

`ES` `EF` `진척률` `EVM` `Critical Path` `전진 계산` `후진 계산`

---

## 정의/개념

대규모 프로젝트의 일정을 계획 및 관리하기 위한 기법으로, 시간과 비용을 고려하여 프로젝트의 최소 시간을 결정하는 네트워크 분석기법

---

## 프로세스

### 주공정법 CPM 프로세스별 활동

| 구분 | 프로세스 | 설명 |
|:-----|:---------|:-----|
| **활동 정의** | 1) 활동 정의 | 범위 기준선에 있는 WBS의 직업 패키지를 활동이라는 더 작은 요소로 분할하는 프로세스 |
| | 2) 활동 순서 배열 | 선행 활동과 후행 활동의 다양한 논리적인 연관관계와 순서를 식별하는 프로세스 |
| | 3) 활동 기간 산정 | 연동 계약 같은 점진적 상세화를 통해 산정 기간의 정확성을 높이는 프로세스 |
| **경로 계산** | 4) 전진계산 | 빠른 개시일(ES), 빠른 종료일(EF)을 구함 |
| | 5) 후진계산 | 늦은 개시일(LS), 늦은 종료일(LF)을 구함 |
| **결과 도출** | 6) 주경로 분석 | 여유시간을 구한 다음 여유시간이 0인 경로를 구하면 주공정 경로가 만들어 진다. |
| | 7) 프로젝트 수행 기간 추정 | 주경로 분석을 통해 프로젝트의 수행 기간이 추정되고 지연인 경우 자원 최적화 적용한다. |

- **주공정법의 총여유(Total Float)**: 프로젝트 종료일을 지연시키지 않으면서 한 활동이 가질 수 있는 총 여유 시간
- **주공정법의 자유 여유(Free Float)**: 후행 활동의 빠른 개시일을 지연시키지 않으면서 현재(혹은 이전) 활동이 가질 수 있는 여유시간

---

## 메커니즘

### CPM 주경로 도출 방법

```
    ┌─────┬─────┬─────┐
    │  1  │  3  │  3  │
    │ ES  │ 기간 │ EF  │
    ├─────┴─────┴─────┤
    │    활동 이름     │
    ├─────┬─────┬─────┤
    │ LS  │여유기간│ LF  │
    │  3  │  2  │  5  │
    └─────┴─────┴─────┘
```

| 약어 | 설명 |
|:-----|:-----|
| **ES** | 빠른 개시일 (ES, Early Start Date) |
| **EF** | 빠른 종료일 (EF, Early Finish Date) |
| **LS** | 늦은 개시일 (LS, Late Start Date) |
| **LF** | 늦은 종료일 (LF, Late Finish Date) |
| **TF** | 여유 기간, 총 여유 (TF, Total Float) |
| **FF** | 자유 여유 (FF, Free Float) |

### 전진계산/후진계산

| 구분 | 항목 | 설명 |
|:-----|:-----|:-----|
| **전진계산<br>(Forward pass)** | ES (Early Start) | 빠른 개시일 (Early Start Date)<br>ES = 선행활동의 빠른 종료일(EF) + 1 |
| | EF (Early Finish) | 빠른 종료일 (Early Finish Date)<br>EF = 빠른 개시일(ES) + 기간 - 1<br>- 프로젝트 종료일 기준으로 시작일 도출하여 LS와 LF를 구하는 방식 |
| **후진계산<br>(Backward pass)** | LF (Late Finish) | 늦은 종료일 (Late Finish Date)<br>LF = 후행활동의 늦은 개시일(LS) - 1 |
| | LS (Late Start) | 늦은 개시일 (Late Start Date)<br>LS = 늦은 종료일(LF) - 기간 + 1<br>- 프로젝트 납기에 영향을 주지 않고 해당 활동에 주어진 여유시간 |
| **여유시간 계산<br>(Float)** | TF (Total Float) | 총 여유시간<br>TF = 늦은 종료일(LF) - 빠른 종료일(EF)<br>TF = 늦은 개시일(LS) - 빠른 개시일(ES)<br>- **프로젝트 종료일을 지연시키지 않으면서 한 활동이 가질 수 있는 총 여유시간** |
| | FF (Free Float) | 자유 여유 (Free Float)<br>FF = 후행 활동의 빠른 개시일(ES) - 빠른 종료일(EF) - 1<br>(1일 시작기준) |
| | CP | Critical Path: 여유기간이 '0'인 경로를 연결한 경로 |

---

## 연계 토픽

- [CCM (Critical Chain Method)](/docs/sw/03-project-management/ccm)
- [프로젝트 일정관리](/docs/sw/03-project-management/schedule-management)
- [EVM](/docs/sw/03-project-management/evm)

---

## 학습 체크리스트

- [ ] CPM 정의 및 개념 이해
- [ ] 7단계 프로세스 이해
- [ ] ES, EF, LS, LF, TF, FF 계산 방법 이해
- [ ] 전진계산/후진계산 이해
- [ ] Critical Path 개념 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

