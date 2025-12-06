---
layout: default
title: UML 4+1 View
parent: 5. UML
grand_parent: SW (소프트웨어공학)
nav_order: 2
---

# UML 4+1 View
{: .fs-8 }

5.1 UML 기본
{: .label .label-purple }

> 암기: **ULIPD(유리피디)**

---

## 핵심 키워드

`UseCase View` `Logic View` `Process View` `Deployment View` `Implementation View`

---

## 정의/개념

아키텍처 시스템, 이해자 관점, **4+1 분류 뷰 모델**

---

## 구성도

```
                    ┌─────────────────────┐
                    │   Implementation    │
                    │       View          │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   │   Logical   │◄───│  UseCase    │───►│   Process   │
   │    View     │    │    View     │    │    View     │
   └─────────────┘    └─────────────┘    └─────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Deployment        │
                    │       View          │
                    └─────────────────────┘
```

---

## 수직적 단편화 (정적 단편화)

- **문제영역인 Usecase View** 는 기능적인 요소를 설명
- **문제영역에 대한 해결방법**을 Logical, Process, Implementation, Deployment View 로 **4 개의 관점으로 분류**해 아키텍처측면의 해결방법을 제시
- **4+1 뷰 모델**은 Siemens, RUP 등 에서 제시한 5 개의 뷰 모델이 가장일반적으로 사용됨
- 뷰 모델을 구성하는 각각의 뷰는 **UML 등의 다양한 다이어그램의 형태로 가시화** 됨

---

## 구성요소 설명

| 구분 | 뷰 | 설명 |
|:-----|:---|:-----|
| **요구명세** | **Usecase View** | - 시스템이 제공하는 기능 관점 시스템 표현, 요구사항 명세<br>- Usecase Diagram |
| **분석/설계** | **Logical View** | - 시스템 내부모듈간의 논리적인 구조를 표현<br>- Class Diagram |
| | **Process View** | - 기능을 수행할 때 시스템의 순차적인 흐름을 표현<br>- Activity Diagram |
| | **Deployment View** | - 실행되는 시스템 하드웨어와 소프트웨어의 관계를 정의<br>- Deployment Diagram |
| **구현** | **Implementation View** | - 독립적으로 실행되는 컴포넌트와 이들 간의 관계를 정의<br>- Component Diagram |

---

## 4+1 View와 UML 다이어그램 매핑

| View | 목적 | 주요 다이어그램 |
|:-----|:-----|:--------------|
| **Use Case View** | 시스템 기능 요구사항 | Use Case Diagram |
| **Logical View** | 시스템 논리 구조 | Class Diagram, Object Diagram |
| **Process View** | 시스템 동작 흐름 | Activity Diagram, Sequence Diagram |
| **Deployment View** | 물리적 배치 | Deployment Diagram |
| **Implementation View** | 컴포넌트 구조 | Component Diagram, Package Diagram |

---

## 4+1 View 활용

| 이해관계자 | 관심 View |
|:----------|:---------|
| **최종 사용자** | Use Case View |
| **개발자** | Logical View, Implementation View |
| **시스템 통합자** | Process View |
| **시스템 엔지니어** | Deployment View |

---

## 연계 토픽

- [UML 개요](/docs/sw/05-uml/uml-overview)
- [소프트웨어 아키텍처](/docs/sw/04-architecture/sw-architecture)
- [ISO 42010](/docs/sw/04-architecture/iso-42010)

---

## 학습 체크리스트

- [ ] 4+1 View 5가지 뷰 암기 (ULIPD - 유리피디)
- [ ] 각 View의 목적과 대응 UML 다이어그램 이해
- [ ] 이해관계자별 관심 View 파악

---

## 참고자료

- 정보관리기술사 SW 학습자료
- Philippe Kruchten, "The 4+1 View Model of Architecture"




