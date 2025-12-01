---
layout: default
title: 무결성 제약조건
parent: 3. 데이터 모델링 & 설계
grand_parent: DB (데이터베이스)
nav_order: 5
---

# 데이터베이스 무결성
{: .fs-8 }

3.2 무결성
{: .label .label-yellow }

> 암기: **개참속사키도**

---

## 핵심 키워드

`정확성` `일관성` `유효성 유지` `제약조건`

---

## 정의/개념

데이터의 정확성, 일관성, 유효성이 유지되는 것을 의미

---

## 유형

| 구분 | 설명 | 제약 조건 |
|:-----|:-----|:---------|
| **개체 무결성<br>(Entity Integrity)** | - 기본키는 반드시 값을 가짐<br>- 기본키는 유일성을 보장하는 최소 집합 | - Primary Key<br>- Not Null |
| **참조 무결성<br>(Referential Integrity)** | - 외래키 속성은 참조 불가 값을 지닐 수 없음<br>- 외래키 값은 그 외래키가 기본키로 사용된 릴레이션의 기본키 값이거나 NULL 값일 것 | - Foreign Key |
| **속성 무결성<br>(Attribute Integrity)** | - 컬럼은 지정된 데이터 형식 만족하는 값만 포함 | Character, Date,<br>LONG, VARCHAR2,<br>NUMBER |
| **사용자 정의<br>무결성** | - 모든 데이터는 Business Rule을 준수해야 함 | Trigger, Check,<br>User Define Data Type,<br>DEFAULT Value |
| **키 무결성<br>(Key Integrity)** | - 한 릴레이션에 동일 키값인 튜플 허용 불가 | Primary Key +<br>Unique Index |
| **도메인 무결성<br>(Domain Integrity)** | - 속성 값은 미리 정의된 도메인 범위에 속해야 함 | CHECK, Default |

---

## 제약조건

| 구분 | 세부 |
|:-----|:-----|
| **선언적 방법** | - Primary Key<br>- Foreign Key<br>- Unique<br>- Check<br>- Data Type<br>- Default |
| **절차적 방법** | - Trigger<br>- Stored Procedure<br>- Application |

---

## 무결성 관계도

```
┌─────────────────┐        ┌─────────────────┐
│   개체무결성      │        │   참조무결성      │
├─────────────────┤        ├─────────────────┤
│ 고객번호(PK)     │◀───────│ 주문번호(PK)     │
│ 고객명           │        │ 고객번호(FK)     │
│ 성별             │        │                 │
└─────────────────┘        └─────────────────┘
        │
        └────────────────────┐
                             │
                    ┌────────┴────────┐
                    │   속성무결성      │
                    └─────────────────┘
```

---

## 연계 토픽

- [데이터베이스 정합성](/docs/db/03-modeling-design/relation-integrity)
- [정규화](/docs/db/03-modeling-design/normalization)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
