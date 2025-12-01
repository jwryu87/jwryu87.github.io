---
layout: default
title: 메타데이터 관리
parent: 7. 데이터 품질
grand_parent: DB (데이터베이스)
nav_order: 7
---

# 메타데이터 (ISO/IEC 11179)
{: .fs-8 }

7.7 메타데이터 표준
{: .label .label-yellow }

---

## 핵심 키워드

`기술 메타데이터` `구조 메타데이터` `관리 메타데이터` `Marc` `Dublin Core` `RDF` `Ontology`

---

## 정의/개념

데이터에 관한 구조화된 데이터로, 데이터에 대한 여러 가지 정보는 물론 데이터 분류를 손쉽게 하기 위해 요약한 데이터

---

## 개념 및 유형

```
┌─────────────────────────────────────────────────────────┐
│  employee_id  first_name  last_name    nn    department_id   │
├─────────────────────────────────────────────────────────┤
│      44          Simon     Martinez   NN 45 09 73 D     1    │
│      45          Thomas    Goldeen    SA 75 35 42 B     2    │
│      46          Eugene    Corneleen  NE 22 63 82       2    │
│      ...                                                     │
└─────────────────────────────────────────────────────────┘
                         Data
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                      Metadata                           │
├─────────────┬────────────────┬─────────────────────────┤
│   Column    │   Data Type    │      Description        │
├─────────────┼────────────────┼─────────────────────────┤
│ employee_id │      int       │ Primary key of a table  │
│ first_name  │  nvarchar(50)  │ Employee first name     │
│ last_name   │  nvarchar(50)  │ Employee last name      │
│ nn          │  nvarchar(15)  │ National Identification │
│ position    │  nvarchar(50)  │ Current position title  │
│department_id│      int       │ Employee department ref │
│ gender      │    char(1)     │ M=Male, F=Female        │
│employment_  │      date      │ Start date of employment│
│start_date   │                │                         │
│employment_  │      date      │ Employment end date     │
│end_date     │                │                         │
└─────────────┴────────────────┴─────────────────────────┘
```

---

## 유형별 설명

| 구분 | 항목 | 설명 |
|:-----|:-----|:-----|
| **유형** | 기술 메타데이터 | 정보자원의 검색을 목적으로 한 메타데이터<br>기술 대상 기록을 검색할 수 있도록 해 줌 |
| | 구조 메타데이터 | 복합적인 디지털 객체들을 함께 묶어주기 위한 메타데이터<br>개별 기록 단위에서 전체를 구성하는 각각의 부분과의 관계를 보여줌 |
| | 관리 메타데이터 | 자원의 관리를 어떻게든 용이하게 하기 위한 메타데이터<br>어떤 객체가 언제 어떻게 작성되었나, 주 내용에 대한 접근을 관리하는 등의 책임은 누가 가지며, 접근이나 이용에 대한 어떤 제약이 적용될 수 있는지를 포함 |
| **종류** | Marc | 도서 레코드를 위한 기계 가독형 목록 |
| | Dublin Core | ISO 15836으로 표준화된 메타데이터 요소 집합 |
| | RDF | 기계가 이해할 수 있는 메타데이터 |
| | Ontology | 용어 사이의 관계를 정의하는 일종의 사전 |
| | URN | 정보자원의 고유한 이름 |
| | XMI | MOF에서 XML로 매핑하기 위한 표준 사항 |

---

## 메타데이터 관리 목적

| 목적 | 설명 |
|:-----|:-----|
| **데이터 검색 지원** | 데이터 검색 중 데이터를 찾고, 분석 도구가 빅데이터를 정확하게 해석하고 사용할 수 있도록 실행 |
| **데이터 이해도 향상** | 데이터의 의미, 구조, 품질에 대한 정보 제공 |
| **데이터 품질 관리** | 데이터의 출처, 변환 이력 등을 추적하여 품질 관리 가능 |
| **시스템 통합 지원** | 이기종 시스템 간 데이터 통합 시 표준화된 정보 제공 |

---

## 연계 토픽

- [다크 데이터](/docs/db/01-bigdata/data-lake)
- [데이터 거버넌스](/docs/db/07-data-quality/data-governance)
- [데이터 품질관리(DQM)](/docs/db/07-data-quality/dqm)

---

## 학습 체크리스트

- [ ] 메타데이터 정의 및 개념 이해
- [ ] 유형 3가지 (기술/구조/관리) 암기
- [ ] 종류별 특징 파악 (Marc, Dublin Core, RDF, Ontology, URN, XMI)

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료

