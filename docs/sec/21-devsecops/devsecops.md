---
layout: default
title: DevSecOps
parent: DevSecOps
grand_parent: 보안
nav_order: 1
---

# DevSecOps
{: .fs-8 }

21.1 DevSecOps
{: .label .label-green }

---

## 핵심 키워드

`개발과 운영에 보안 통합` `CI/CD` `Security as Code` `Shift Left`

---

## 정의/개념

**개발(Development)과 운영(Operation)의 융합과 협업**의 개발 주기에 **보안(Security) 측면을 포함**한 개발 방법론

---

## 메커니즘

```
                            ┌─────── Sec ───────┐
                            │                   │
             Dev            │       Ops         │
        ┌─────────────────┐ │  ┌─────────────┐ │
        │                 │ │  │             │ │
        │    Create       │ │  │   Prevent   │ │   Detect
        │      │          │ │  │      │      │ │     │
        │      ▼          │ │  │      ▼      │ │     ▼
        │  ┌───────────┐  │ │  │ ┌─────────┐ │ │  ┌─────────┐
        │  │Continuous │◀─┼─┼──│ │Continuous││ │  │Continuous│
        │  │Integration│  │ │  │ │Configura-│ │ │  │Monitoring│
        │  │           │──┼─┼──▶ │tion      │ │ │  │         │
        │  └─────┬─────┘  │ │  │ └────┬────┘ │ │  └────┬────┘
        │        │        │ │  │      │      │ │       │
        │        ▼        │ │  │      ▼      │ │       ▼
        │  ┌───────────┐  │ │  │ ┌─────────┐ │ │  ┌─────────┐
        │  │Continuous │  │ │  │ │Continuous││ │  │         │
        │  │Improvement│  │ │  │ │Learning  │ │ │  │ Respond │
        │  │           │  │ │  │ │         │ │ │  │         │
        │  └─────┬─────┘  │ │  │ └────┬────┘ │ │  └────┬────┘
        │        │        │ │  │      │      │ │       │
        │        ▼        │ │  │      ▼      │ │       ▼
        │  ┌───────────┐  │ │  │ ┌─────────┐ │ │  ┌─────────┐
        │  │Continuous │──┼─┼──▶ │Predict  │ │ │  │         │
        │  │Deployment │◀─┼─┼──│ │         │ │ │  │ Predict │
        │  │           │  │ │  │ └─────────┘ │ │  │         │
        │  └───────────┘  │ │  │             │ │  └─────────┘
        │                 │ │  │             │ │
        │    Verify       │ │  │   Preprod   │ │
        │                 │ │  │             │ │
        └─────────────────┘ │  └─────────────┘ │
                            │                   │
                            └───────────────────┘
                                     │
                                     ▼
                           Continuous Delivery
```

© 2017 Gartner, Inc.

---

## 동작방식

| 요소 | 작동 방식 설명 |
|:-----|:-------------|
| **DevOps** | 개발 팀과 운영 팀을 하나로 모아 개발 진행 |
| **CI/CD** | 자동화된 구축 및 테스트를 통해 신규 애플리케이션을 제공 |
| **DevSecOps** | CI/CD 프로세스 전반에 보안 평가를 통합하여 DevOps 방식에 보안 도입<br>- 개발팀: 코드 구현 전 보안 팀과 협업<br>- 운영팀: 배포 후 소프트웨어의 보안 문제를 모니터링 |

---

## 구현요소

| 요소 | 핵심 성공 요소 |
|:-----|:-------------|
| **문화** | 보안 조직의 조기 참여 |
| **프로세스** | 프로세스 초기에 보안 분석 및 테스트 |
| **자동화** | 코드 보안 관리 (Security as Code) |
| **도구** | 보안 점검 도구 |
| **성과 평가** | 보안코드 품질 점수 |

---

## 구현 도구/보안 기능

### 도구

| 구분 | SDLC | 기술 |
|:-----|:-----|:-----|
| **Code** | 형상관리, 코드 추적성 | Git, SVN |
| **Build** | 자동화된 코드 빌드 도구 | Jenkins, Maven |
| **Test** | 동적, 정적 커버리지 자동화 테스트 도구 | JUnit, Selenium |
| **Release** | 변경관리, 변경 승인, 릴리즈 계획 & 자동화 | Ansible, Chef |

### 보안기능

| 구분 | SDLC | 기술 |
|:-----|:-----|:-----|
| **Security Engineering** | 보안에 대한 공학적 접근 방법 및 자동화 도구 제공 | OWASP, SAST/DAST |
| **Security Operations** | 보안성 확보를 위한 지속적 모니터링, Detecting 제공 | SIEM, SOC |
| **Security Science** | 보안 모델에 대한 수립, 학습, 전파 및 예측성 제공 | AI/ML 기반 |

---

## Shift Left 개념

{: .note }
> 보안을 개발 초기 단계로 이동 (Shift Left)하여 취약점을 조기에 발견하고 수정 비용 최소화

```
전통적 방식:   요구사항 → 설계 → 개발 → 테스트 → [보안검토] → 배포
Shift Left:   [보안] → 요구사항 → [보안] → 설계 → [보안] → 개발 → [보안] → 테스트 → 배포
```

---

## 연계 토픽

- [공급망 공격](/docs/sec/18-attack/supply-chain-attack)
- [시큐어코딩](/docs/sec/)
- [CI/CD](/docs/sec/)

---

## 학습 체크리스트

- [ ] DevSecOps의 정의와 DevOps와의 차이점 이해
- [ ] 메커니즘 (Dev/Sec/Ops 영역) 이해
- [ ] 구현요소 (문화, 프로세스, 자동화, 도구, 성과평가) 이해
- [ ] Shift Left 개념 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료

