---
layout: default
title: RTO/RPO
parent: 3. BCP·BCM
grand_parent: BIZ (경영)
nav_order: 2
---

# RTO, RPO
{: .fs-8 }

3.2 RTO/RPO
{: .label .label-red }

---

## 핵심 키워드

- RTO: `한계재정영향` `x축(재정적 영향)` `y축(업무중단기간)`
- RPO: `손실허용량` `x축(현시점과 복구시점 시간차)` `y축(데이터 손실)`

---

## 정의/개념

| 구분 | 정의 |
|:-----|:-----|
| **RTO (Recovery Time Objective)** | 업무가 중단된 시점으로부터 복구되어 **업무가 정상적으로 가능할 때까지의 목표 시간** |
| **RPO (Recovery Point Objective)** | 업무가 중단된 시점으로부터 **데이터 복구가 수행되어야 하는 목표 시점** |

---

## 개념도

### RTO (복구목표시간)

| 구분 | 내용 |
|:-----|:-----|
| **개념도** | 재정영향 ↗ Pain Threshold → 한계재정영향 → 업무중단기간 → **복구목표시간(RTO)** |
| **특징** | - 재해 시 목표복구 시간의 선정<br>- RTO 는 구축 비용에 반비례<br>- 재해 발생 시 손실에 비례 |

### RPO (복구목표시점)

| 구분 | 내용 |
|:-----|:-----|
| **개념도** | 데이터손실 ↗ Data Recovery Requirements → 복구목표시점(RPO) → 손실허용량 → 현시점과 복구시점의 시간차 → **복구목표시점(RPO)** |
| **특징** | - 데이터가 복구 되어야 하는 시점<br>- 특정 백업 시점 (전일 마감, 재해발생시점) |

---

## RTO와 RPO 관계

> RTO, RPO 는 **상호 연관 관계**를 가지고 있어 RTO 를 짧게 설정할수록 RPO 목표 수준은 높아짐.

---

## 연계 토픽

- [MBCO](/docs/biz/03-bcp-bcm/bcm-bcp)
- [MAO](/docs/biz/03-bcp-bcm/bcm-bcp)
- [MTPD](/docs/biz/03-bcp-bcm/bcm-bcp)

---

## 학습 체크리스트

- [ ] RTO와 RPO 정의 구분
- [ ] 각각의 특징 이해
- [ ] RTO/RPO 상호 관계 이해

---

## 참고자료

- 정보관리기술사 경영 학습자료

