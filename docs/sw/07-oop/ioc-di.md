---
layout: default
title: IoC/DI
parent: 7. 객체지향(OOP)
grand_parent: SW (소프트웨어공학)
nav_order: 4
---

# IoC (Inversion of Control)
{: .fs-8 }

7.2 OOP 설계 원리
{: .label .label-yellow }

---

## 핵심 키워드

`DL` `DI`

---

## 정의/개념

기존의 모든 제어를 클라이언트 코드가 가지도록 구현하던 것에서, **프레임워크가 제어를 나누어 진행하는 프로그래밍 기법**

---

## IoC 분류

```
                                ┌──────────────────────────────┐
                                │         IoC 분류              │
                                └──────────────┬───────────────┘
                                               │
        ┌──────────────────────────────────────┼──────────────────────────────────────┐
        │                                      │                                      │
        ▼                                      ▼                                      ▼
   ┌─────────┐                           ┌─────────┐                            ┌─────────┐
   │   EJB   │                           │   IoC   │◄── IoC: Inversion of Control │  Spring │
   │  Spring │                           │         │    DI: Dependency Injection  │         │
   └────┬────┘                           └────┬────┘    DL: Dependency Lookup     └────┬────┘
        │                                     │                                        │
        │                               ┌─────┴─────┐                                  │
        │                               │           │                                  │
        ▼                               ▼           ▼                                  ▼
   ┌─────────┐                    ┌─────────┐  ┌─────────┐                      ┌─────────┐
   │   DL    │                    │   DI    │  │         │ 의존관계를            │  Spring │
   └─────────┘                    └────┬────┘  │ Setter  │ 연결시키는            └─────────┘
                                       │      │Injection│ 방법에 따른 분류
                                       │      └─────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
             ┌─────────────┐   ┌─────────────────┐  ┌─────────────┐
             │   Setter    │   │   Constructor    │  │   Method    │
             │  Injection  │   │   Injection      │  │  Injection  │
             └─────────────┘   └─────────────────┘  └─────────────┘
```

---

## 호출방식 비교

### 사례를 통한 기존 클래스 호출 방식과 IoC 호출 방식의 차이점

| 호출 방식 | 개념도 | 상세 설명 |
|:---------|:-------|:---------|
| **일반적 Class 간 호출** | `A Class` → 사용/생성/호출 → `B Class` | - 클래스 내에 선언과 구현이 하나이기 때문에 다양한 형태로 변화 불가능 |
| **Interface Class 호출** | `Class` → 사용 → `Interface` → 생성/호출 → `Concrete Class` | - 클래스를 인터페이스와 구현으로 분리<br>- 구현(Concrete) 클래스 교체 용이해 다양한 형태로 변화가 가능하지만 구현 클래스 교체 시 호출 클래스의 소스를 수정 |
| **Factory Pattern 호출** | `Class` → 호출 → `Interface`<br>`Class` → 생성 → `Concrete Class` | - 팩토리 방식은 팩토리가 구현클래스를 생성하므로 클래스는 팩토리를 호출하는 코드로 충분<br>- 구현클래스 변경 시 호출 클래스에는 영향을 미치지않고, 팩토리만 수정하면 됨 |
| **IoC 이용 호출** | `Class` → 사용 → `Interface`<br>`조립기` → 의존성 삽입(DI) → 구현 → `Concrete Class` | - 팩토리의 장점을 더해 어떤 것에도 의존하지 않는 형태로 구성 가능<br>- 실행 시점에 클래스 간의 관계가 형성 |

---

## DI (Dependency Injection) 유형

| 유형 | 설명 |
|:-----|:-----|
| **Setter Injection** | Setter 메소드를 통해 의존성 주입 |
| **Constructor Injection** | 생성자를 통해 의존성 주입 |
| **Method Injection** | 메소드 호출 시 의존성 주입 |

---

## IoC/DI 장점

| 장점 | 설명 |
|:-----|:-----|
| **느슨한 결합** | 클래스 간 의존성 감소 |
| **테스트 용이** | Mock 객체 주입 가능 |
| **재사용성** | 컴포넌트 교체 용이 |
| **유지보수성** | 변경 영향 최소화 |

---

## 연계 토픽

- [DI](/docs/sw/07-oop/solid)
- [디자인 패턴](/docs/sw/08-design-pattern/index)

---

## 학습 체크리스트

- [ ] IoC 개념 및 정의 이해
- [ ] DL vs DI 차이 파악
- [ ] 3가지 DI 유형 (Setter, Constructor, Method Injection) 이해
- [ ] IoC 호출 방식 비교 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료
- Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern"

