---
layout: default
title: 샤딩
parent: 9. DB 성능
grand_parent: DB (데이터베이스)
nav_order: 3
---

# 데이터베이스 샤딩 (Sharding)
{: .fs-8 }

9.3 데이터 분산
{: .label .label-purple }

> 암기: **VRKD**

---

## 핵심 키워드

`Shard Key` `Shard DB` `Vertical` `Range` `Key` `Directory`

---

## 정의/개념

물리적으로 다른 데이터베이스에 Shard 사용, 수평 분할 방식 분산 저장 기법

---

## 구성요소

| # | 구성요소 | 핵심 |
|:--|:---------|:-----|
| 1 | **Shard DB** | 분할된 테이블, 데이터 포함 |
| 2 | **Shard Metadata** | 샤드 동작 위한 설정 정보 |
| 3 | **Shard Key** | Shard 선택 식별자 칼럼 |
| 4 | **Shard Key Data** | 질의 중 Shard 식별 위한 힌트에 해당하는 Shard Key 값 |
| 5 | **Shard ID** | Shard DB 식별자 |
| 6 | **Proxy** | 해석된 힌트와 Shard Metadata 이용, Shard DB로 요청 전달 |

---

## 분할방법

| # | 분할 방법 | 핵심 |
|:--|:----------|:-----|
| 1 | **Vertical** | 테이블별 서버 분할 방식 |
| 2 | **Range Based** | 테이블 점점 거대해지는 경우 서버 분리 방식 |
| 3 | **Key Based** | 엔티티를 해시함수에 넣어서 나오는 값을 이용해서 서버 정하는 방식 |
| 4 | **Directory Based** | 파티셔닝 메커니즘 제공 추상화된 서비스 생성 |

---

## 샤딩 vs 파티셔닝 비교

| 구분 | 샤딩 | 파티셔닝 |
|:-----|:-----|:---------|
| **분산 위치** | 여러 물리적 서버 | 단일 서버 내 |
| **확장성** | Scale-out | Scale-up |
| **복잡도** | 높음 | 상대적으로 낮음 |

---

## 연계 토픽

- [파티셔닝](/docs/db/09-db-performance/partitioning)
- [쿼리오프로딩](/docs/db/09-db-performance/query-offloading)
- [분산 DB](/docs/db/02-db-basics/distributed-db)

---

## 학습 체크리스트

- [ ] 샤딩 구성요소 이해
- [ ] 분할방법 4가지 암기 (VRKD)
- [ ] 샤딩과 파티셔닝 차이점 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료

