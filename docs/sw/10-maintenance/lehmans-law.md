---
layout: default
title: 레만의 SW 변화 원리
parent: 10. 유지보수
grand_parent: SW (소프트웨어공학)
nav_order: 3
---

# 레만의 SW 변화 원리
{: .fs-8 }

유지보수
{: .label .label-purple }

> 암기: **계자조친/피지증감**

---

## 핵심 키워드

`E-Type` `계속적 변경` `자가 규제` `조직적 안정화` `친근성 유지` `피드백 시스템` `지속적 성장` `증가 복잡도` `감소하는 품질`

---

## 정의/개념

소프트웨어는 요구에 의해 계속적으로 변경되며, 변경에 따른 복잡성, 프로그램의 고유한 변경 추세, SW조직 생산성의 일관성, 소프트웨어 각 버전의 변화에 대한 일관성을 제시한 **SW 변화 원리**

---

## Lehman SW 변화 원리 분류 (Category)

| 구분 | 관점 | 설명 |
|:-----|:-----|:-----|
| **S-type**<br>(Static) | Specification and solutions<br>(명세) | - 정해진 명세에 따라 정확히 동작하는 S/W (계산기프로그램) |
| **P-type**<br>(Practical) | Procedures<br>(절차) | - 절차나 실행 입력 값에 따라 다르게 수행되는 S/W (체스게임) |
| **E-type**<br>(Embedded) | Environment<br>(환경) | - 실 세계의 환경적 상황과 밀접하게 연관되어 동작하는 S/W<br>(엘리베이터 센서, Tax시스템) |

> 리만은 위의 분류 중 **E-Type**에 대한 변화 원리를 제시

---

## Lehman 소프트웨어 변화의 원리 상세

| 원리 | 설명 | 적용방안 |
|:-----|:-----|:---------|
| **계속적 변경**<br>(Continuing Change) | - SW는 요구사항에 의해 계속 변경 | - 요구관리프로세스<br>- 변경관리프로세스 |
| **자가 규제**<br>(Self-Regulation) | - SW 진화 과정은 단계별 피드백, 자가규제 적용 | - 통제 프로세스<br>- 변경 영향도 분석 |
| **조직적 안정화**<br>(Organizational Stability) | - 작업량 분배, 개발 생산성은 자원 변경에 민감하지 않음 | - 변경통제위원회(CAB)<br>- 형상통제위원회(CCB) |
| **친근성 유지**<br>(Conservation Familiarity) | - SW 각 버전 변화는 일정, 기존 사용자를 만족시키는 방향으로 진화되는 경향이 있음 | - 형상관리시스템<br>- SVN, Git |
| **피드백 시스템**<br>(Feedback System) | - 중요한 SW 제품 개선을 달성하기 위해 Feedback 시스템으로 구성(제품개선 도출) | - Baseline<br>- CMDB |
| **지속적 성장**<br>(Continuing Growth) | - 사용자 만족 위해 지속적 기능 추가 | - CI/CD<br>- DevOps, SRE |
| **증가 복잡도**<br>(Increasing Complexity) | - 변경이 가해질수록 SW구조는 복잡해짐 | - 3R (Reverse Engineering,<br>  Reengineering, Reuse) |
| **감소하는 품질**<br>(Declining Quality) | - 엄격한 관리·운영 환경에 적응하지 않는 한 품질이 감소 | - 리팩토링(Refactoring)<br>- 회귀테스트 |

---

## 적용 포인트

- 소프트웨어 변화의 특성을 이해하고 **유지보수, 변경관리, 형상관리, 품질통제**의 중요 모델로 반영
- E-Type 소프트웨어의 특성에 맞는 체계적인 관리 필요

---

## 연계 토픽

- [유지보수 개념](/docs/sw/10-maintenance/maintenance-concept)
- [리팩토링](/docs/sw/10-maintenance/refactoring)
- [3R](/docs/sw/10-maintenance/3r)
- [형상관리](/docs/sw/02-quality/configuration-management)

---

## 학습 체크리스트

- [ ] E-Type, P-Type, S-Type 분류 이해
- [ ] 8가지 변화 원리 암기 (계자조친/피지증감)
- [ ] 각 원리별 적용방안 숙지

---

## 참고자료

- 정보관리기술사 SW 학습자료
