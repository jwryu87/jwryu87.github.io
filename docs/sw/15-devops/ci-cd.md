---
layout: default
title: CI/CD
parent: 15. DevOps / TDD / SRE
grand_parent: SW (소프트웨어공학)
nav_order: 2
---

# CI/CD
{: .fs-8 }

DevOps
{: .label .label-purple }

---

## 핵심 키워드

- **CI**: Jenkins, SVN, GIT
- **CD**: Chef, ansible, puppet, YAML

---

## 정의/개념

- **CI (Continuous Integration)**: 애플리케이션에 대한 새로운 코드 변경사항이 정기적으로 빌드 및 테스트되어 공유 저장소에 병합되는 자동화된 프로세스
- **CD (Continuous Delivery/Deployment)**: 소프트웨어의 변경사항을 리포지토리에서 프로덕션 환경까지 자동으로 릴리즈 하는 프로세스

---

## 구성도

```
    ┌──────────┐
    │   📝     │
    │  CODE    │
    └────┬─────┘
         │
         ▼
    ┌──────────┐     ┌─────────────────────────────────────────────┐
    │  < / >   │     │                                             │
    │  COMMIT  │────►│    ┌─────────┐  ┌─────────┐  ┌───────────┐ │
    └──────────┘     │    │  BUILD  │  │  UNIT   │  │INTEGRATION│ │
                     │    │         │  │  TESTS  │  │   TESTS   │ │
                     │    └─────────┘  └─────────┘  └───────────┘ │
    ┌──────────┐     │                CI PIPELINE                  │
    │    >_    │     └─────────────────────────────────────────────┘
    │ RELATED  │                         │
    │   CODE   │                         ▼
    └──────────┘     ┌─────────────────────────────────────────────┐
                     │    ┌─────────┐  ┌─────────┐  ┌───────────┐ │
                     │    │ REVIEW  │  │ STAGING │  │PRODUCTION │ │
                     │    │         │  │         │  │           │ │
                     │    └─────────┘  └─────────┘  └───────────┘ │
                     │                CD PIPELINE                  │
                     └─────────────────────────────────────────────┘
```

{: .note }
> 개발환경과 운영환경까지 파이프라인이 설치되어 있음 개발환경에서 코드변경사항을 자동으로 빌드, 테스트, 통합되고 운영환경으로 실시간으로 배포 가능

---

## 구성요소 상세

### CI (Continuous Integration) 구성기술

| 구분 | 구성기술 | 세부기술 및 설명 |
|:-----|:---------|:----------------|
| **CI Server** | - CI Server | Jenkins, Travis CI, CruiseControl.NET, TeamCity |
| | - SCM | SVN, GIT, GITLAB, CVS, Mercurial로 형상관리 수행 |
| | - Build Tools | Maven, ant, Gradle, Make, MSBuild 소스코드 컴파일 지원 |
| | - Test Tools | Junit, sonacube, PMD, Selenium를 통한 정적분석 |
| | - Coverage Tools | Emma, Cobertura, TestCocoon로 소스코드 커버리지 테스트 |
| | - Inspection Tools | CheckStyle, Findbugs, Cppcheck, Valgrind |

### CD (Continuous Delivery) 구성기술

| 구분 | 구성기술 | 세부기술 및 설명 |
|:-----|:---------|:----------------|
| **CD 구성기술** | - app 설치 | Chef, ansible, puppet, vagrant를 통해 개발환경 및 인프라 구성 자동화 |
| | - 개발환경 구성 | |
| | - 공개키/개인키 | Ssh-keygen을 통해 배포서버의 공개키 등록 |
| | - 스크립트 | YAML Recipe, playbook 등을 통해 자동화 스크립트 구성 |

---

## CI/CD 도구

| 구분 | 도구 |
|:-----|:-----|
| **CI Server** | Jenkins, Travis CI, CircleCI, GitHub Actions, GitLab CI |
| **SCM** | Git, SVN, Mercurial |
| **Build** | Maven, Gradle, npm, Make |
| **Test** | JUnit, Selenium, Jest, pytest |
| **CD/Deployment** | Ansible, Chef, Puppet, Terraform, ArgoCD |
| **Container** | Docker, Kubernetes |

---

## CI/CD 효과

{: .highlight }
> CI/CD 기술을 통해 SW의 비가시성을 극복하고, 생산성 향상에 기여가능

---

## 연계 토픽

- [DevOps](/docs/sw/15-devops/devops)
- [Agile 방법론](/docs/sw/06-methodology/agile)

---

## 학습 체크리스트

- [ ] CI vs CD 개념 차이 이해
- [ ] CI 구성기술 6가지 파악
- [ ] CD 구성기술 파악
- [ ] 주요 CI/CD 도구 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

