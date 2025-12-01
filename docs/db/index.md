---
layout: default
title: DB (데이터베이스)
nav_order: 7
has_children: true
permalink: /docs/db
---

# DB (데이터베이스)

데이터베이스 관련 학습 자료입니다. 총 **73개** 항목

---

## 1. 빅데이터 (16개)

| 구분 | 토픽 |
|:-----|:-----|
| 1.1 빅데이터 개념 | [빅데이터 3V/6V](/docs/db/01-bigdata/bigdata-3v-6v) \| [빅데이터 시각화](/docs/db/01-bigdata/bigdata-visualization) \| [빅데이터 분석도구 선택 원칙](/docs/db/01-bigdata/bigdata-analysis-tool) \| [데이터 라벨링 & 어노테이션](/docs/db/01-bigdata/data-labeling-annotation) |
| 1.2 처리·플랫폼 | [Hadoop 3.0](/docs/db/01-bigdata/hadoop-3) \| [Lambda/Kappa 아키텍처](/docs/db/01-bigdata/lambda-kappa) \| [Apache Kafka](/docs/db/01-bigdata/apache-kafka) \| [데이터 웨어하우스](/docs/db/01-bigdata/data-warehouse) \| [Data Lake](/docs/db/01-bigdata/data-lake) \| [Data Fabric](/docs/db/01-bigdata/data-fabric) |
| 1.3 분석 기법 | [배깅·부스팅](/docs/db/01-bigdata/bagging-boosting) \| [랜덤 포레스트](/docs/db/01-bigdata/random-forest) \| [앙상블 학습](/docs/db/01-bigdata/ensemble-learning) \| [상관·인과 관계](/docs/db/01-bigdata/correlation-causation) \| [분석 모델 평가 방법](/docs/db/01-bigdata/analysis-model-evaluation) |
| 1.4 빅데이터 보안 | [Big Data 보안](/docs/db/01-bigdata/bigdata-security) |

---

## 2. 데이터베이스 기본 (9개)

| 구분 | 토픽 |
|:-----|:-----|
| 2.1 DB 유형 | [NoSQL](/docs/db/02-db-basics/nosql) \| [CAP 이론](/docs/db/02-db-basics/cap-theorem) \| [PACELC 이론](/docs/db/02-db-basics/pacelc) \| [NewSQL](/docs/db/02-db-basics/newsql) \| [분산 DB](/docs/db/02-db-basics/distributed-db) \| [기타 데이터베이스](/docs/db/02-db-basics/other-databases) |
| 2.2 DB 구조 | [3단계 DB 구조](/docs/db/02-db-basics/three-level-architecture) \| [데이터 모델링](/docs/db/02-db-basics/data-modeling) \| [차원 모델링](/docs/db/02-db-basics/dimensional-modeling) |

---

## 3. 데이터 모델링 & 설계 (8개)

| 구분 | 토픽 |
|:-----|:-----|
| 3.1 정규화 | [함수적 종속성](/docs/db/03-modeling-design/functional-dependency) \| [정규화](/docs/db/03-modeling-design/normalization) \| [반정규화](/docs/db/03-modeling-design/denormalization) \| [이상현상](/docs/db/03-modeling-design/anomaly) |
| 3.2 무결성 | [무결성 제약조건](/docs/db/03-modeling-design/integrity-constraints) \| [릴레이션 무결성](/docs/db/03-modeling-design/relation-integrity) \| [무결성 유지방법](/docs/db/03-modeling-design/integrity-maintenance) |
| 3.3 KEY | [Primary Key / Foreign Key / Candidate Key](/docs/db/03-modeling-design/keys) |

---

## 4. 트랜잭션 (3개)

| 토픽 |
|:-----|
| [ACID](/docs/db/04-transaction/acid) \| [트랜잭션 상태 전이](/docs/db/04-transaction/transaction-state) \| [격리성(Isolation Level)](/docs/db/04-transaction/isolation-level) |

---

## 5. 동시성 제어 (6개)

| 토픽 |
|:-----|
| [Locking](/docs/db/05-concurrency/locking) \| [Two Phase Locking(2PL)](/docs/db/05-concurrency/two-phase-locking) \| [Timestamp Ordering](/docs/db/05-concurrency/timestamp-ordering) \| [MVCC](/docs/db/05-concurrency/mvcc) \| [Validation(낙관적 검증)](/docs/db/05-concurrency/validation) \| [동시성 제어 시 문제점](/docs/db/05-concurrency/concurrency-problems) |

---

## 6. 데이터 회복 (5개)

| 토픽 |
|:-----|
| [로그 기반 회복](/docs/db/06-recovery/log-based-recovery) \| [체크포인트](/docs/db/06-recovery/checkpoint) \| [그림자 페이지](/docs/db/06-recovery/shadow-paging) \| [ARIES](/docs/db/06-recovery/aries) \| [버퍼 관리 정책](/docs/db/06-recovery/buffer-management) |

---

## 7. 데이터 품질 (8개)

| 토픽 |
|:-----|
| [데이터 품질 관리(DQM)](/docs/db/07-data-quality/dqm) \| [데이터 프로파일링](/docs/db/07-data-quality/data-profiling) \| [데이터 클렌징](/docs/db/07-data-quality/data-cleansing) \| [데이터 결측값](/docs/db/07-data-quality/missing-data) \| [데이터 이상값](/docs/db/07-data-quality/outlier) \| [데이터 거버넌스](/docs/db/07-data-quality/data-governance) \| [메타데이터 관리](/docs/db/07-data-quality/metadata-management) \| [데이터 가공 절차](/docs/db/07-data-quality/data-processing) |

---

## 8. 공공데이터 (3개)

| 토픽 |
|:-----|
| [공공데이터 정의](/docs/db/08-public-data/public-data-definition) \| [Linked Open Data](/docs/db/08-public-data/linked-open-data) \| [마이데이터](/docs/db/08-public-data/mydata) |

---

## 9. DB 성능 (11개)

| 토픽 |
|:-----|
| [DB 튜닝](/docs/db/09-db-performance/db-tuning) \| [데이터베이스 성능 개선](/docs/db/09-db-performance/performance-improvement) \| [Optimizer](/docs/db/09-db-performance/optimizer) \| [샤딩](/docs/db/09-db-performance/sharding) \| [Partitioning](/docs/db/09-db-performance/partitioning) \| [Query Offloading](/docs/db/09-db-performance/query-offloading) \| [조인](/docs/db/09-db-performance/join) \| [서브쿼리](/docs/db/09-db-performance/subquery) \| [리팩터링](/docs/db/09-db-performance/refactoring) \| [인덱스 종류](/docs/db/09-db-performance/index-types) \| [Scan 방식](/docs/db/09-db-performance/scan-methods) |

---

## 10. 정책·데이터 활용 (4개)

| 토픽 |
|:-----|
| [디지털 플랫폼 정부](/docs/db/10-data-policy/digital-platform-government) \| [블록체인 산업 진흥 전략](/docs/db/10-data-policy/blockchain-strategy) \| [데이터옵스](/docs/db/10-data-policy/dataops) \| [데이터 중립성](/docs/db/10-data-policy/data-neutrality) |

