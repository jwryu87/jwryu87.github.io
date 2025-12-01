---
layout: default
title: CCM (Critical Chain Method)
parent: 3. 프로젝트 관리
grand_parent: SW (소프트웨어공학)
nav_order: 3
---

# CCM (Critical Chain Method)
{: .fs-8 }

3.1 일정/범위/위험 관리
{: .label .label-purple }

> 암기: **프피자**

---

## 핵심 키워드

`프로젝트 버퍼` `피딩 버퍼` `자원 버퍼`

---

## 정의/개념

자원 가용성을 고려하여 일정 변경을 예상하고, 이를 토대로 활동 사이에 의존 관계 및 수행기간을 결정하는 일정관리 기법

---

## 개념

### Critical Chain Method의 개념 설명

| 구분 | 설명 |
|:-----|:-----|
| **개념** | 자원 가용성을 고려하여 일정의 변경을 예상하고, 이를 토대로 활동 사이에 의존 관계 및 수행기간을 결정하는 일정관리 방법 |
| **특징** | 과다하게 설정될 수 있는 여유시간을 줄여 통합된 버퍼로 책정하고 버퍼의 소진율을 모니터링하여 전체 프로젝트를 관리 |

### 개념도

```
Non-Critical Chain ──► A1 ──► [① Feeding Buffer]
                                     │
Critical Chain ──► B1 ──► [① Resource Buffer] ──► B2 ──► [① Project Buffer]
                                     │
Non-Critical Chain ──► C1 ──► [② Feeding Buffer]
```

---

## 버퍼 분류

### Critical Chain Method의 버퍼 분류

| 버퍼 분류 | 버퍼 개념도 | 설명 |
|:---------|:-----------|:-----|
| **① 프로젝트 버퍼<br>(Project Buffer)** | B1 → B2 → ① Project Buffer (전체 버퍼) | - Critical Chain상의 활동에서 확보한 버퍼를 Critical Chain 끝에 두어 관리<br>- 안전영역, 모니터 영역, 행동 영역으로 나누어 관리<br>• 안전 영역: 사용해도 안전한 버퍼<br>• 모니터링 영역: 버퍼 사용 추이 및 원인을 모니터링 하는 영역<br>• 행동 영역: 버퍼 통제를 위한 조치를 취하는 영역 |
| **② 피딩 버퍼<br>(Feeding Buffer)** | A1 → [Feeding Buffer]<br>↓<br>B1 → B2 | - Critical Chain에 연결되는 Non-Critical Chain의 끝에 두어 관리<br>- Critical Chain의 작업 착수 지연 방지 |
| **③ 자원 버퍼<br>(Resource Buffer)** | B1 → [Resource Buffer] → B2 | - Critical Chain상의 작업착수 전에 해당자원에게 수행시기를 알려줌<br>- 일종의 경보장치<br>- CCM과 CPM은 네트워크 및 일정 산출방식은 동일하지만, 각 활동의 여유시간을 빼 내어 필요 시 여유시간을 적절히 공급하는 방식으로 차이점이 존재함 |

---

## 연계 토픽

- [CPM (Critical Path Method)](/docs/sw/03-project-management/cpm)
- [프로젝트 일정관리](/docs/sw/03-project-management/schedule-management)

---

## 학습 체크리스트

- [ ] CCM 정의 및 개념 이해
- [ ] 3가지 버퍼(프로젝트, 피딩, 자원) 역할 이해
- [ ] CPM과 CCM의 차이점 이해
- [ ] 두음매직 "프피자" 암기

---

## 참고자료

- 정보관리기술사 SW 학습자료

