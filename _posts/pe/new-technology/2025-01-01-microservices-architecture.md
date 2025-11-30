---
layout: post
title: (PE) 마이크로서비스 아키텍처
date: 2025-01-01 12:00:00 +09:00
categories: pe
tags: [pe, architecture, microservices]
comments: true
---

# 마이크로서비스 아키텍처 (Microservices Architecture)

## 개념

마이크로서비스 아키텍처는 애플리케이션을 작고 독립적인 서비스들의 집합으로 구성하는 아키텍처 패턴입니다.

<!-- more -->

## 핵심 특징

### 1. 서비스 독립성
- 각 서비스는 독립적으로 배포 가능
- 독립적인 데이터베이스 소유
- 느슨한 결합 (Loose Coupling)

### 2. 비즈니스 중심 설계
- 비즈니스 도메인 단위로 분할
- 단일 책임 원칙 (SRP) 적용
- 명확한 경계 컨텍스트 (Bounded Context)

### 3. 분산 시스템
- 서비스 간 통신 (REST, gRPC, 메시지 큐)
- 서비스 디스커버리
- API 게이트웨이

## 모놀리식 vs 마이크로서비스

| 구분 | 모놀리식 | 마이크로서비스 |
|------|----------|---------------|
| 배포 | 전체 재배포 | 부분 배포 가능 |
| 확장성 | 수직 확장 | 수평 확장 |
| 기술 스택 | 단일 기술 | 다양한 기술 가능 |
| 개발 | 초기에 빠름 | 초기에 느림 |
| 복잡도 | 낮음 | 높음 |
| 장애 격리 | 어려움 | 용이 |

## 주요 패턴

### 1. API 게이트웨이 패턴

**역할:**
- 단일 진입점 제공
- 인증/인가
- 라우팅 및 로드밸런싱
- 요청/응답 변환

```
클라이언트 → API Gateway → 서비스 A
                        → 서비스 B
                        → 서비스 C
```

### 2. 서비스 디스커버리 패턴

**목적:** 동적으로 서비스 위치 탐색

**구현 방식:**
- Client-side Discovery (Eureka, Consul)
- Server-side Discovery (Kubernetes Service)

### 3. Circuit Breaker 패턴

**목적:** 장애 전파 방지

**동작:**
```
정상 (Closed) → 장애 감지 → 차단 (Open) → 복구 시도 (Half-Open)
```

### 4. SAGA 패턴

**목적:** 분산 트랜잭션 관리

**방식:**
- Choreography: 이벤트 기반
- Orchestration: 중앙 조정자

**예시:**
```
주문 생성 → 결제 → 재고 확인 → 배송
   ↓실패시
보상 트랜잭션 실행 (롤백)
```

## 데이터 관리

### Database per Service

**원칙:** 각 서비스가 자신만의 DB 소유

**장점:**
- 독립적 확장
- 기술 선택 자유도
- 장애 격리

**단점:**
- 분산 트랜잭션 복잡
- 데이터 일관성 문제
- 조인 쿼리 불가

### 이벤트 소싱 (Event Sourcing)

- 상태 변경을 이벤트로 저장
- 이벤트 재생으로 상태 복구
- 감사 추적(Audit Trail) 가능

### CQRS (Command Query Responsibility Segregation)

- 읽기/쓰기 모델 분리
- 읽기 최적화 가능
- 복잡도 증가 주의

## 통신 방식

### 1. 동기 통신

**REST API:**
```
GET /api/users/123
POST /api/orders
```

**gRPC:**
- 고성능 RPC 프레임워크
- Protocol Buffers 사용
- 양방향 스트리밍

### 2. 비동기 통신

**메시지 큐:**
- Kafka, RabbitMQ, SQS
- 느슨한 결합
- 부하 평준화

**이벤트 드리븐:**
```
Service A → Event Bus → Service B
                      → Service C
                      → Service D
```

## 배포 및 운영

### 컨테이너화
```dockerfile
FROM python:3.9
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### 오케스트레이션
- Kubernetes: 컨테이너 오케스트레이션
- Docker Swarm: 간단한 오케스트레이션

### 모니터링
- **분산 추적**: Jaeger, Zipkin
- **로그 집계**: ELK Stack, Splunk
- **메트릭**: Prometheus, Grafana

## 장점

1. **독립적 배포**: 서비스별 배포 주기
2. **기술 다양성**: 각 서비스에 적합한 기술 선택
3. **확장성**: 필요한 서비스만 스케일링
4. **장애 격리**: 한 서비스 장애가 전체에 영향 없음
5. **팀 자율성**: 작은 팀이 서비스 전체 관리

## 단점 및 고려사항

1. **복잡도 증가**
   - 분산 시스템 복잡성
   - 네트워크 지연
   - 데이터 일관성

2. **운영 오버헤드**
   - 여러 서비스 모니터링
   - 배포 자동화 필수
   - 인프라 비용

3. **개발 초기 비용**
   - 초기 설정 시간
   - 학습 곡선
   - 테스트 복잡도

## 도입 고려사항

### 마이크로서비스가 적합한 경우
- 대규모 시스템
- 빠른 배포 주기 필요
- 독립적인 팀 운영
- 확장성 요구사항

### 모놀리식이 적합한 경우
- 소규모 시스템
- 팀 규모가 작음
- 복잡도 감당 어려움
- 빠른 MVP 개발

## 실무 체크리스트

- [ ] 서비스 경계 정의 (Domain-Driven Design)
- [ ] API 게이트웨이 구성
- [ ] 서비스 간 통신 방식 결정
- [ ] 분산 트랜잭션 전략
- [ ] 모니터링/로깅 체계 구축
- [ ] CI/CD 파이프라인 자동화
- [ ] 보안 전략 (인증/인가)

## 관련 개념

- Domain-Driven Design (DDD)
- Event-Driven Architecture
- Service Mesh (Istio, Linkerd)
- Serverless Architecture

---

**학습 체크리스트:**
- [ ] 마이크로서비스 특징 설명 가능
- [ ] 주요 패턴 이해 및 적용 시나리오 파악
- [ ] 모놀리식과의 차이점 설명
- [ ] 실제 설계 경험 정리
- [ ] 장단점 트레이드오프 이해


