---
layout: default
title: UML 개요
parent: 5. UML
grand_parent: SW (소프트웨어공학)
nav_order: 1
---

# UML (Unified Modeling Language)
{: .fs-8 }

5.1 UML 기본
{: .label .label-purple }

---

## 핵심 키워드

`가시화/구체화/명세화/문서화` `자동화` `SOA/MDA 지원` `M0~3 UML 4계층 구조` `구조, 행동, 상호작용 등 13개 다이어그램` `명칭` `일반화` `실체화` `의존` `연관`

---

## 정의/개념

특정 언어나 공정에 종속되지 않고 보다 수준 높은 자동화 기반의 **소프트웨어 시스템 아키텍처를 묘사하기 위한 표준 모델링 언어**

---

## UML 다이어그램 유형

```
                            ┌─────────────────┐
                            │    Diagram      │   행위 다이어그램
                            │                 │
                            └────────┬────────┘
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
            ┌────────────────┐              ┌────────────────┐
            │   Structure    │              │   Behavior     │
            │    Diagram     │              │   Diagram      │
            └────────┬───────┘              └────────┬───────┘
     ┌───────┬───────┼───────┬───────┐              │
     ▼       ▼       ▼       ▼       ▼              │
  ┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐         │
  │Class ││Compo-││Object││Compo-││Deploy-│         │
  │      ││nent  ││      ││site  ││ment   │         │
  │      ││      ││      ││Struct││       │         │
  └──────┘└──────┘└──────┘└──────┘└──────┘         │
                                                    │
                            ┌───────────────────────┴─────────┐
                            │                                 │
              ┌─────────────┼─────────────┐                   │
              ▼             ▼             ▼                   ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐        ┌───────────────┐
        │ Activity │ │ Use Case │ │  State   │        │  Interaction  │
        │ Diagram  │ │ Diagram  │ │ Machine  │        │   Diagram     │
        └──────────┘ └──────────┘ │ Diagram  │        └───────┬───────┘
                                  └──────────┘                │
                                               ┌──────────────┼──────────────┐
                                               ▼              ▼              ▼
                                        ┌──────────┐  ┌──────────┐  ┌──────────┐
                                        │ Sequence │  │ Communi- │  │  Timing  │
                                        │ Diagram  │  │ cation   │  │ Diagram  │
                                        └──────────┘  └──────────┘  └──────────┘
```

---

## UML 다이어그램 분류

### 1) 구조 다이어그램 (Structure Diagram)

| 다이어그램 | 설명 |
|:----------|:-----|
| **Class** | 클래스와 클래스 간의 관계를 기술 |
| **Component** | 컴포넌트의 구조와 연관관계를 기술 |
| **Object** | 특정 시점의 객체의 snapshot 을 기술 |
| **Composite Structure** | 하나의 클래스의 실행시의 내부 구조를 기술 |
| **Deployment** | 시스템의 물리적인 배치를 기술 |
| **Package** | 시스템의 컴파일시의 계층적인 구조를 기술 |

### 2) 행동 다이어그램 (Behavior Diagram) - 정적

| 다이어그램 | 설명 |
|:----------|:-----|
| **Activity** | 절차적이고 병렬적인 행위를 기술 |
| **Use Case** | 사용자가 상호작용하는 시스템의 모습을 기술 |
| **State Machine** | 객체의 상태에 따른 작업과 event 에 따른 상태의 변화 기술 |

### 3) 상호작용 다이어그램 (Interaction Diagram) - 동적

| 다이어그램 | 설명 |
|:----------|:-----|
| **Sequence** | 객체들간의 상호작용을 순서에 초점을 맞춰 기술 |
| **Interaction Overview** | Sequence 와 Activity diagram 의 결합 |
| **Communication** | 객체들간의 상호작용을 연결에 초점을 맞춰 기술 |
| **Timing** | 객체들간의 상호작용을 시간 제약에 초점을 맞춰 기술 |

---

## 다이어그램 요약

| 구분 | 다이어그램 |
|:-----|:----------|
| **구조** | Class, Component, Object, Composite Structure, Deployment, Package |
| **행동(정적)** | Activity, Use Case, State Machine |
| **상호작용(동적)** | Sequence, Interaction Overview, Communication, Timing |

---

## 연계 토픽

- [UML 4+1 View](/docs/sw/05-uml/4plus1-view)
- [클래스 다이어그램](/docs/sw/05-uml/class-diagram)
- [시퀀스 다이어그램](/docs/sw/05-uml/sequence-diagram)

---

## 학습 체크리스트

- [ ] UML 13개 다이어그램 종류 암기
- [ ] 구조/행동/상호작용 다이어그램 분류 이해
- [ ] 각 다이어그램의 목적과 특징 파악

---

## 참고자료

- 정보관리기술사 SW 학습자료
- OMG UML 2.5 Specification

