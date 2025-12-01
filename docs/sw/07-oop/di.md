---
layout: default
title: 의존성 주입 (DI)
parent: 7. 객체지향(OOP)
grand_parent: SW (소프트웨어공학)
nav_order: 6
---

# 의존성 주입 (Dependency Injection)
{: .fs-8 }

7.2 OOP 설계 원리
{: .label .label-yellow }

---

## 핵심 키워드

`의존관계 컨테이너 자동 연결` `Bean Definition 정보 기반` `Setter` `Constructor` `Method`

---

## 정의/개념

어떤 객체가 다른 객체를 사용해야 할 때, 그 사용하는 객체를 외부에서 직접 생성하는 대신 **외부에서 만들어진 객체를 주입 받아 사용하는 디자인 패턴**

---

## IoC 구현 방법 구성도

```
                            ┌──────────────────────────────────────────┐
                            │                IoC 분류                   │
                            └────────────────────┬─────────────────────┘
                                                 │
         ┌───────────────────────────────────────┼───────────────────────────────────────┐
         │                                       │                                       │
         ▼                                       ▼                                       ▼
    ┌─────────┐                            ┌─────────┐                             ┌─────────┐
    │   EJB   │                            │   IoC   │  IoC: Inversion of Control  │  Spring │
    │  Spring │                            │         │  DI: Dependency Injection   │         │
    └────┬────┘                            └────┬────┘  DL: Dependency Lookup      └────┬────┘
         │                                      │                                       │
         ▼                                      ▼                                       ▼
    ┌─────────┐                           ┌─────────┐                             ┌─────────┐
    │   DL    │                           │   DI    │  의존관계를                  │  Spring │
    └─────────┘                           └────┬────┘  연결시키는                   └─────────┘
                                               │      방법에 따른 분류
                                               │
                          ┌────────────────────┼────────────────────┐
                          │                    │                    │
                          ▼                    ▼                    ▼
                   ┌─────────────┐     ┌─────────────────┐   ┌─────────────┐
                   │   Setter    │     │   Constructor   │   │   Method    │
                   │  Injection  │     │   Injection     │   │  Injection  │
                   └─────────────┘     └─────────────────┘   └─────────────┘
```

---

## 의존성 주입의 방법

| 구분 | 설명 |
|:-----|:-----|
| **생성자 사용<br>(Constructor Injection)** | - 필요한 의존성을 모두 포함하는 클래스의 생성자를 만들고 그 생성자를 통해 의존성을 주입한다. |
| **세터(Setter)를 통한 주입<br>(Method(Setter) Injection)** | - 의존성을 입력받는 Setter 메소드를 만들고 이를 통해 의존성을 주입한다. |
| **인터페이스(Interface)를 통한 주입<br>(Field Injection)** | - 의존성을 주입하는 함수를 포함한 인터페이스를 작성하고 이 인터페이스를 구현하도록 함으로써 실행시에 이를 통하여 의존성을 주입한다. |

{: .note }
> 마틴 파울러는 위와 같은 세가지 의존성 주입 패턴을 제시

---

## DI 장점

| 장점 | 설명 |
|:-----|:-----|
| **느슨한 결합** | 객체 간 의존성 감소 |
| **테스트 용이** | Mock 객체 주입으로 단위 테스트 용이 |
| **재사용성 향상** | 컴포넌트 재사용성 증가 |
| **유연성** | 런타임에 의존성 교체 가능 |

---

## DI 구현 예시 (Java/Spring)

### Constructor Injection (권장)

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

### Setter Injection

```java
@Service
public class UserService {
    private UserRepository userRepository;
    
    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

### Field Injection

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
}
```

---

## 연계 토픽

- [IoC](/docs/sw/07-oop/ioc-di)
- [SOLID 원칙](/docs/sw/07-oop/solid)

---

## 학습 체크리스트

- [ ] DI 3가지 방법 (Constructor, Setter, Interface) 이해
- [ ] DI 장점 파악
- [ ] Spring에서 DI 구현 방법 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료
- Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern"


