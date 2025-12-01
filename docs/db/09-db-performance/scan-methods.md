---
layout: default
title: Scan 방식
parent: 9. DB 성능
grand_parent: DB (데이터베이스)
nav_order: 10
---

# 데이터베이스 인덱스의 스캔(Scan) 방식
{: .fs-8 }

9.10 스캔 유형
{: .label .label-yellow }

---

## 핵심 키워드

`Index Range Scan` `Index Full Scan` `Index Unique Scan` `Index Skip Scan` `Index Range Scan Descending`

---

## 정의/개념

데이터베이스에서 레코드를 검색하기 위한 다양한 스캔 방식

---

## 스캔 방식별 특성

| 스캔(Scan) 방식 | 스캔 방식 개념도 | 설명 |
|:----------------|:----------------|:-----|
| **Index Range Scan** | 인덱스 루트 블록에서 리프 블록까지 수직적으로 탐색한 후에 리프 블록을 필요한 범위만 스캔하는 방식 | 생성된 결과집합은 인덱스 컬럼 순으로 정렬 상태이므로 sort order by, min/max 값을 빠르게 추출 가능 |
| **Index Full Scan** | 인덱스 리프 블록을 처음부터 끝까지 수평적으로 탐색하는 방식(최적화의 인덱스가 없을 때 차선) | 인덱스 선두 칼럼이 조건절에 없을 때 옵티마이저는 우선 Table Full Scan을 고려함 |
| **Index Unique Scan** | 수직적 탐색만으로 데이터를 찾는 스캔 방식 | = 조건으로 탐색하는 경우에 작동 |
| **Index Skip Scan** | 선두 칼럼이 조건절에 빠졌도 활용할 수 있는 스캔 방식 | 루트 or 브랜치 블록에서 읽은 칼럼 값 정보를 이용해 조건에 부합하는 레코드를 포함할 가능성 있는 하위 블록만 골라 액세스 하는 방식 |
| **Index Range Scan Descending** | Index Range Scan과 기본적으로 동일 | 인덱스 뒤쪽에서부터 앞쪽으로 스캔하기 때문에 내림차순으로 정렬된 결과집합 획득 |

---

## Full Table Scan vs Index Scan

| 구분 | Full Table Scan | Index Scan |
|:-----|:----------------|:-----------|
| **특징** | 테이블 전체를 읽음 | 인덱스를 통해 접근 |
| **사용 상황** | 인덱스가 없거나 비효율적일 때 | 조건에 맞는 인덱스가 있을 때 |
| **I/O** | 많음 | 상대적으로 적음 |

---

## 참고

- 인덱스 트리 구조를 무시하고 인덱스 세그먼트 전체를 Multiblock Read 방식으로 스캔하는 Index Fast Full Scan도 존재

---

## 연계 토픽

- [인덱스 종류](/docs/db/09-db-performance/index-types)
- [Optimizer](/docs/db/09-db-performance/optimizer)
- [DB 튜닝](/docs/db/09-db-performance/db-tuning)

---

## 학습 체크리스트

- [ ] 각 스캔 방식별 특징 이해
- [ ] Index Range Scan과 Full Scan 차이 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료

