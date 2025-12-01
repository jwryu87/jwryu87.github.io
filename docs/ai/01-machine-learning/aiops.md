---
layout: default
title: AIOps
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 5
---

# AIOps(Artificial Intelligence for IT Operations)
{: .fs-8 }

1.1 기계학습 기초
{: .label .label-purple }

---

## 핵심 키워드

`IT인프라 문제` `AI 활용` `분석 학습 엔진` `Infra Tools` `Event View`

---

## 정의/개념

빅데이터 분석과 머신 러닝(Machine Learning) 및 AI를 활용하여 IT 인프라(Infra)문제를 분석과 해결 방법을 제시하는 IT운영을 위한 인공지능

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│  Business Value    Operations Center      DevOps            │
│    Dashboard                                                │
├─────────────────────────────────────────────────────────────┤
│         Applications for IT and Business Users              │
├─────────────────────────────────────────────────────────────┤
│  Consume │  Presentation Layer (Visualization and NLP)      │
├──────────┼──────────────────────────────────────────────────┤
│          │  Analytical Learning                             │
│   API    │  (Pattern Discovery,     Deep Analysis  Real-Time│
│  Access  │   Anomaly Detection,                    Analysis │
│          │   Machine Learning, NLP)                         │
├──────────┼──────────────────────────────────────────────────┤
│  Provide │            Storage                               │
│          │         Data Collection                          │
├──────────┴──────────────────────────────────────────────────┤
│         Data Sources (Private and Public)                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 프로세스

| 프로세스 | 기반 기술 | 설명 |
|:--------|:---------|:-----|
| **데이터 수집** (Data Collection) | 빅데이터 플랫폼<br>데이터 수집기<br>스토리지(Storage) | Infra를 구성하는 각 장비와 프로그램에서 발생하는 이벤트(Event), 로그(Log), 티켓, 모니터링 등의 데이터와 기존 저장된 데이터를 저장 |
| **데이터 분석** (Data Analysis) | 분석 학습 엔진<br>규칙 & 패턴 분석<br>도메인 알고리즘 | 머신 러닝 알고리즘 및 기타 AI 기술로 데이터를 분석하여 정보를 연관시키고, 패턴을 발견하고, 이상을 감지하고, 근본 원인을 결정하고, 서버, 시스템 및 플랫폼 간의 인과 관계를 식별 |
| **자동 제어** (Automated Reaction) | API<br>Trigger<br>Infrastructure Tools | 분석 결과를 사용하여 작업을 자동화하고 조정하여 핵심 사항을 기반으로 작업을 트리거 |
| **가시화** (Visualization) | 대시 보드(Dashboard)<br>Event View<br>Slack | 관리자가 문제를 식별하고 환경 변경 사항을 추적하고 결정을 내리고 IT 인프라에 대한 일반적인 통찰력을 제공하는 데 도움이 되는 보고서 및 시각화를 생성 |

---

## 연계 토픽

- [MLOps](/docs/ai/01-machine-learning/mlops)
- [ModelOps](/docs/ai/01-machine-learning/modelops)

---

## 학습 체크리스트

- [ ] AIOps의 정의와 목적 이해
- [ ] 아키텍처 구성요소 파악
- [ ] 데이터 수집-분석-자동제어-가시화 프로세스 이해

---

## 참고자료

- 정보관리기술사 AI 학습자료
