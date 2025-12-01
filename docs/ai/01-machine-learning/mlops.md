---
layout: default
title: MLOps
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 4
---

# 기계학습 운영화(MLOps)
{: .fs-8 }

1.1 기계학습 기초
{: .label .label-purple }

---

## 핵심 키워드

`DataOps` `ModelOps` `CI/CD` `ML 파이프라인`

---

## 정의/개념

DataOps와 ModelOps 결합, CI/CD 사용, ML 파이프라인 사용 ML 운영 방법론

---

## 프로세스

```
        기계 학습 운영화 프로세스

 Data → ML → DEV → OPS → Configure
        ↓     ↓      ↓
     Create  Plan  Release
        ↓     ↓      ↓
     Model  Verify Package
        ↓     ↓      ↓
        ←← Monitor ←←
```

| 단계 | 주요 활동 |
|:-----|:---------|
| **Experiment (ML)** | 데이터 수집, 비즈니스 분석, 초기 모델링 |
| **DEV** | 모델링 + 테스트, CI/CD |
| **OPS** | Continuous Delivery, Data Feedback Loop |

### 상세 설명

- **Experiment (ML)**: 데이터 소스와 데이터 소스에서 생성된 데이터 셋트
- **DEV**: 개발자나 Data scientist가 ML code를 repository에 push
- **사용 내역(history)과 특성(attributes)이 대기된 AI 모델 래파지토리(repository)**
- **라이프사이클을 통해 데이터 셋트, 모델과 실험을 관리하는 자동 ML 파이프라인**
- **OPS**: 모니터링을 통해 지속적인 검증 및 정애/정확성 확인

> MLOps 프로세스를 성공적으로 기업에 적용하기 위해선 단계별 구축 전략이 필요

---

## 생명주기 (ML Ops LifeCycle)

| 절차 | 주요 활동 | 설명 |
|:-----|:---------|:-----|
| **계획 수립** | 비즈니스 목표 설정 | 비즈니스 실행 식별, 프로젝트 실행범위/타당성여부 경가항목 정의, 타당성 검토 |
| | 접근방식 스케치 | 소규모 프로젝트 구현으로 유효성 및 신뢰성 점검 |
| **데이터 준비** | Feature Engineering | 데이터 마이닝 통한 특징 추출, 선택, 자원 축소 수행 및 ML 모델링 성능 개선 |
| | 데이터 품질 | 데이터 완전성, 유효성, 무결성 및 일관성 점검, 품질 차원에서 데이터 평가/검증 및 관리 |
| | 데이터 통찰 | 고객 경험개선 및 비즈니스 가치 향상 위한 개인화, 추천 서비스 수행 |
| **분석/관리** | 증강 데이터 관리 | 자동 데이터 수집/분석, 데이터 과학 민주화 지원 |
| | 데이터 라벨링 | 데이터 자동/합성 라벨링, 가이드 라벨링, 데이터 스키마 검증 |
| **기계학습** | 모델 학습/튜닝/평가 | 파라미터 최적화, 결함/오류 검증, 모델 성능/유효성 평가 |
| | 모델 배포 | 학습 모델 게보 관리 및 모델 유효성 검사, 배포 형식 패키징 |
| **배포/생산** | 생산적용 | 모델-인프라 호환성 검증, 모델 성능 실험, 롤아웃/배 최종 결정 지원 |
| **플 스택 지원** | 클라우드 연동 | 클라우드 호스팅, 고성능 컴퓨팅(GPU, TPU) 서비스 지원 |
| | LifeCycle 관리 | 파이프라인 오케스트레이션, 전체 프로젝트 통합관리 |

> ML 프로덕션환경 및 프로세스 성숙도 측정 위해 MLOps 성숙도 모델 메트릭 활용

---

## 연계 토픽

- [DataOps](/docs/ai/08-ml-process/ml-pipeline)
- [ModelOps](/docs/ai/01-machine-learning/modelops)
- [DSML](/docs/ai/01-machine-learning/dsml)

---

## 학습 체크리스트

- [ ] MLOps의 정의와 프로세스 이해
- [ ] DataOps, ModelOps와의 관계 이해
- [ ] 생명주기 각 단계별 활동 파악
- [ ] CI/CD와 ML 파이프라인 개념 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
