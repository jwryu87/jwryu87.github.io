---
layout: default
title: IaC
parent: 23. 인프라스트럭처
grand_parent: DS (Digital Service)
nav_order: 1
---

# 코드형 인프라스트럭처 (IaC)
{: .fs-8 }

23. 인프라스트럭처
{: .label .label-purple }

---

## 핵심 키워드

`CI/CD` `DevOps` `Repository` `Code Review` `Deploy` `부트스트랩` `설정` `오케스트레이션` `CLI` `Chef` `Puppet` `Ansible` `Terraform` `Saltstack`

---

## 정의/개념

인프라 구성을 마치 소프트웨어를 프로그래밍하는 것처럼 **스크립트를 사용하여 처리하는 방식**

- 인프라를 코드로 통제하여 시스템의 가독성이 높아지고, TDD처럼 코드화된 인프라 테스트하며 멱등성 제공
- 오류 발생시 빠르게 수정하여 개선된 코드를 통해 지속적으로 인프라 관리 가능

---

## 메커니즘

```
① code → ② Version Control → ③ code review → ④ integrate → ⑤ deploy
                  ↓
              Repository
```

| 단계 | 설명 |
|:-----|:-----|
| **code** | 인프라 구성을 코드로 작성 |
| **Version Control** | 작성된 코드를 버전 관리 시스템에 저장 |
| **code review** | 코드 리뷰를 통한 품질 검증 |
| **integrate** | 통합 및 테스트 |
| **deploy** | 인프라에 배포 |

---

## 구성요소

| 구분 | 구성 기술 | 설명 |
|:-----|:-----|:-----|
| **Bootstrap** | Vagrant | 가상 머신 리소스 및 초기 스크립트 수행 |
| | Docker | 어플리케이션 구동 필요 설정 및 파일 관리 |
| | CLI | 기 구성 클라우드 인프라를 코드 형태로 Export |
| **Configuration** | Chef | 레시피, playbook 등을 통한 멱등성 제공 |
| | Puppet | agent 방식과 SSH 기반 non-agent 방식 제공 |
| | Ansible | 운영 환경 필요 설정 관련 사항 파일로 관리 |
| | Mcollective | 각 노드의 요청, 응답 관리 |
| **Orchestration** | SaltStack | 마스터에서 ZeroMQ를 사용, 다수 노드 관리 |
| | Jenkins+Fabric | Fabric 실행 결과를 Jenkins에 연동 관리 가능 |

---

## 구성요소별 역할

| 구분 | 역할 | 주요 도구 |
|:-----|:-----|:-----|
| **Bootstrap** | 초기 인프라 구성, 가상화 환경 설정 | Vagrant, Docker, CLI |
| **Configuration** | 서버 설정 및 구성 관리, 멱등성 보장 | Chef, Puppet, Ansible |
| **Orchestration** | 다수 노드 관리, 배포 자동화 | SaltStack, Jenkins+Fabric |

---

## 연계 토픽

- [YAML](/docs/ds/23-infra/yaml)
- [가상화](/docs/ds/07-virtualization/)
- [DevOps](/docs/ds/23-infra/devops)
- [컨테이너](/docs/ds/07-virtualization/container)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 메커니즘 (code → deploy 흐름) 이해
- [ ] 구성요소 3가지 (Bootstrap, Configuration, Orchestration) 암기
- [ ] 주요 도구별 특징 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료
