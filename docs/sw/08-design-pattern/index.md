---
layout: default
title: 8. 디자인 패턴
parent: SW (소프트웨어공학)
has_children: true
nav_order: 8
---

# 디자인 패턴
{: .fs-8 }

8.1 디자인 패턴 기본
{: .label .label-purple }

> 암기: **생구행**

---

## 핵심 키워드

`생성 패턴` `구조 패턴` `행위 패턴`

---

## 정의/개념

소프트웨어 설계에서 자주 발생하는 문제에 대한 **일반적으로 재사용이 가능한 해결책모음**

---

## 디자인 패턴 구성

```
                    구체적
                       │
                   ┌───────────┐
                   │  소스코드  │
                   └───────────┘
                       │
                       ▼
                   ┌───────────┐         ┌───────────┐
                   │ 디자인 패턴 │────────►│  생성 패턴  │
                   └───────────┘         ├───────────┤
                       │                 │  구조 패턴  │
                       ▼                 ├───────────┤
              ┌─────────────────┐        │  행위 패턴  │
              │ 객체지향 디자인 원칙 │       └───────────┘
              └─────────────────┘
                       │
                   추상적
```

---

## 디자인 패턴 유형

| 디자인 패턴 유형 | 설명 |
|:----------------|:-----|
| **생성 패턴** | - 객체들의 생성과 관련<br>- Factory method, Abstract Factory, Builder, Prototype, Singleton |
| **구조 패턴** | - 클래스, 객체의 정적인 구조와 관련<br>- Adaptor, Bridge, Composite, Decorator, Façade, Flyweight, Proxy |
| **행위 패턴** | - 클래스와 객체의 반응과 책임할당<br>- Interpreter, Template Method, Command, Mediator, Memento, Iterator, State, Strategy, Observer, Visitor |

{: .highlight }
> 생성패턴은 객체 생성에 대한 정의를 하고 있고, 무분별한 객체 생성을 통제하기 위해서 사용

---

## 패턴별 상세

### 생성 패턴 (Creational Patterns)

| 패턴 | 설명 |
|:-----|:-----|
| **Factory Method** | 객체 생성을 서브클래스에 위임 |
| **Abstract Factory** | 관련 객체군 생성을 위한 인터페이스 |
| **Builder** | 복잡한 객체를 단계별로 생성 |
| **Prototype** | 기존 객체를 복제하여 생성 |
| **Singleton** | 클래스의 인스턴스를 하나로 제한 |

### 구조 패턴 (Structural Patterns)

| 패턴 | 설명 |
|:-----|:-----|
| **Adapter** | 호환되지 않는 인터페이스 변환 |
| **Bridge** | 추상화와 구현 분리 |
| **Composite** | 객체를 트리 구조로 구성 |
| **Decorator** | 객체에 동적으로 기능 추가 |
| **Facade** | 복잡한 서브시스템에 단순 인터페이스 |
| **Flyweight** | 객체 공유로 메모리 절약 |
| **Proxy** | 다른 객체에 대한 대리자 |

### 행위 패턴 (Behavioral Patterns)

| 패턴 | 설명 |
|:-----|:-----|
| **Template Method** | 알고리즘 구조를 정의하고 일부 단계를 서브클래스에 위임 |
| **Strategy** | 알고리즘을 캡슐화하여 교체 가능 |
| **Observer** | 객체 상태 변경 시 종속 객체들에 알림 |
| **Command** | 요청을 객체로 캡슐화 |
| **State** | 객체 상태에 따라 행위 변경 |
| **Memento** | 객체 상태를 저장/복원 |

---

## 연계 토픽

- [리팩토링](/docs/sw/10-maintenance/refactoring)
- [SOLID 원칙](/docs/sw/07-oop/solid)

---

## 학습 체크리스트

- [ ] 디자인 패턴 3가지 분류 (생성/구조/행위) 암기
- [ ] 각 유형별 대표 패턴 파악
- [ ] GoF 23개 패턴 구분

---

## 참고자료

- 정보관리기술사 SW 학습자료
- GoF, "Design Patterns: Elements of Reusable Object-Oriented Software"

