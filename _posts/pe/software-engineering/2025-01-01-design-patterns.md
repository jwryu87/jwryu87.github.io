---
layout: post
title: (PE) 디자인 패턴 - 생성 패턴
date: 2025-01-01 11:00:00 +09:00
categories: pe
tags: [pe, software-engineering, design-pattern]
comments: true
---

# 디자인 패턴 - 생성 패턴 (Creational Patterns)

## 개념

생성 패턴은 객체 생성 메커니즘을 다루며, 상황에 적합한 방식으로 객체를 생성하는 패턴입니다.

<!-- more -->

## 주요 생성 패턴

### 1. 싱글톤 패턴 (Singleton Pattern)

**목적:** 클래스의 인스턴스가 오직 하나만 존재하도록 보장

**사용 시기:**
- 시스템 전체에서 하나의 인스턴스만 필요한 경우
- 예: 로거, 설정 관리자, 커넥션 풀

**구현 예시:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**장점:**
- 메모리 절약
- 전역 접근점 제공
- 지연 초기화 가능

**단점:**
- 멀티스레드 환경에서 주의 필요
- 테스트 어려움
- 전역 상태 관리로 인한 결합도 증가

### 2. 팩토리 메서드 패턴 (Factory Method Pattern)

**목적:** 객체 생성을 서브클래스에 위임

**사용 시기:**
- 생성할 객체의 타입을 미리 알 수 없는 경우
- 객체 생성 로직을 캡슐화하고 싶은 경우

**구현 예시:**
```python
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type == "card":
            return CardPayment()
        elif payment_type == "cash":
            return CashPayment()
        elif payment_type == "mobile":
            return MobilePayment()
```

### 3. 추상 팩토리 패턴 (Abstract Factory Pattern)

**목적:** 관련된 객체들의 그룹을 생성하는 인터페이스 제공

**사용 시기:**
- 여러 제품군 중 하나를 선택해야 하는 경우
- 예: UI 테마 (Light/Dark), DB 드라이버 (MySQL/PostgreSQL)

### 4. 빌더 패턴 (Builder Pattern)

**목적:** 복잡한 객체의 생성 과정을 단계별로 분리

**사용 시기:**
- 생성자 매개변수가 많은 경우
- 객체 생성 과정이 복잡한 경우

**구현 예시:**
```python
class QueryBuilder:
    def __init__(self):
        self.query = {}
    
    def select(self, fields):
        self.query['select'] = fields
        return self
    
    def where(self, condition):
        self.query['where'] = condition
        return self
    
    def build(self):
        return Query(self.query)

# 사용
query = QueryBuilder().select('*').where('id > 10').build()
```

### 5. 프로토타입 패턴 (Prototype Pattern)

**목적:** 기존 객체를 복제하여 새 객체 생성

**사용 시기:**
- 객체 생성 비용이 큰 경우
- 비슷한 객체를 여러 개 만들어야 하는 경우

## 패턴 선택 가이드

| 상황 | 추천 패턴 |
|------|----------|
| 인스턴스 하나만 필요 | Singleton |
| 생성 로직이 복잡 | Factory Method |
| 관련 객체 그룹 생성 | Abstract Factory |
| 많은 옵션 조합 | Builder |
| 복제가 효율적 | Prototype |

## 실무 적용 사례

### 1. Configuration Manager (Singleton)
```python
class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.config = {}
        return cls._instance
```

### 2. Logging Factory (Factory Method)
```python
class LoggerFactory:
    @staticmethod
    def get_logger(log_type):
        if log_type == "file":
            return FileLogger()
        elif log_type == "console":
            return ConsoleLogger()
        elif log_type == "remote":
            return RemoteLogger()
```

## 주의사항

1. **과도한 사용 금지**: 단순한 경우 일반 클래스 사용
2. **상황에 맞는 선택**: 모든 상황에 맞는 만능 패턴은 없음
3. **유지보수성 고려**: 코드 복잡도와 이득의 균형

## 관련 개념

- SOLID 원칙
- 의존성 주입 (Dependency Injection)
- IoC 컨테이너

---

**학습 체크리스트:**
- [ ] 각 패턴의 목적과 사용 시기 이해
- [ ] 실제 코드로 구현 가능
- [ ] 패턴 간 차이점 설명 가능
- [ ] 실무 적용 사례 파악


