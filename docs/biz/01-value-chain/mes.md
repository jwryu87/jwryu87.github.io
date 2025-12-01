---
layout: default
title: MES
parent: 1. 가치사슬 (Value Chain)
grand_parent: BIZ (경영)
nav_order: 3
---

# MES (Manufacturing Execution System)
{: .fs-8 }

1.3 MES
{: .label .label-purple }

---

## 핵심 키워드

`생산관리` `실적관리` `POP` `APS` `MESA`

---

## 정의/개념

생산 환경 실시간 모니터링, 추적 관리, 불량 파악 **통합생산관리 시스템**

---

## 메커니즘

### MES 시스템 구조

```
┌────────────────────────────────────────┐
│              MES 시스템                │
├────────────────────────────────────────┤
│ 기준관리 │ 영업관리 │ 구매관리 │ 재고관리 │
│ 설비관리 │ 품질관리 │ 생산관리 │        │
└────────────────────────────────────────┘
                    │
              ┌─────┴─────┐
              │           │
         ┌────┴────┐ ┌────┴────┐
         │POP 시스템│ │ 모니터링 │
         ├─────────┤ └─────────┘
         │ 현장관리 │
         │ 작업지시 │
         │ 생산실적 │
         └─────────┘
```

### POP 시스템 구성

| 구분 | 설명 |
|:-----|:-----|
| **생산관리** | 생산 계획 및 실행 |
| **작업지시** | 현장 작업 지시서 |
| **생산실적** | 실적 데이터 수집 |
| **설비가동정보** | 설비 상태 모니터링 |
| **불황정보** | 불량 발생 추적 |

---

## ISA 기능분류

ISA(Instrumentation, Systems, and Automation Society): 자동화 시스템 비영리 표준화 단체

### Level별 기능 분류

| Level | 설명 | 내용 |
|:------|:-----|:-----|
| **Level 0** | Batch Control | 실제 생산 공정 |
| **Level 1** | Continuous Control | 생산공정 센싱 및 조작 |
| **Level 2** | Discrete Control | 생산공정을 관리 감독하며, 자동화 설비를 이용 |
| **Level 3** | Manufacturing Operations Management | 제품을 생산하기 위하여 작업흐름을 단계별로 제어하며 생산공정을 최적화하고 기록을 유지 |
| **Level 4** | Business Planning & Logistics | 기본적인 공장 스케줄 생성 (생산, 자재사용, 배송), 적정재고 수준 결정 |

---

## 연계 토픽

- [POP](/docs/biz/01-value-chain/pop)
- [APS](/docs/biz/01-value-chain/ahp)
- MESA

---

## 학습 체크리스트

- [ ] MES 정의 및 목적 이해
- [ ] ISA 기능분류 Level 0~4 암기
- [ ] POP 시스템 구성요소 파악

---

## 참고자료

- 정보관리기술사 경영 학습자료
- MESA International

