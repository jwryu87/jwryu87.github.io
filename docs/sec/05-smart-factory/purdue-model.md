---
layout: default
title: 퍼듀(Purdue) 모델
parent: 스마트공장 보안
grand_parent: 보안
nav_order: 2
---

# 퍼듀(Purdue) 모델
{: .fs-8 }

5.2 스마트공장 보안
{: .label .label-purple }

---

## 핵심 키워드

`ISA-99` `PERA` `IT` `OT망` `IDMZ` `ICS 보안`

---

## 정의/개념

ISA-99 제정, PERA 기반, 제조 보안 최적화, **네트워크 계층 기반**, IT, OT망 기반 모델 **ICS 보안 참조 모델**

---

## 계층

### 퍼듀 모델의 계층 구조

```
┌─────────────────────────────────────────────────────────────────────┐
│ Level 5 │     Enterprise Network                    │  Enterprise  │
├─────────┼───────────────────────────────────────────┤    Zone      │
│ Level 4 │  E-mail, Internet, Logistics Network      │              │
├─────────┼───────────────────────────────────────────┼──────────────┤
│         │           Firewall                         │              │
│         │  Terminal, Patch Mgmt, Web, App, AV       │    IDMZ      │
│         │           Firewall                         │              │
├─────────┼───────────────────────────────────────────┼──────────────┤
│ Level 3 │   Site Manufacturing, Operations          │Manufacturing │
├─────────┼───────────────────────────────────────────┤    Zone      │
│ Level 2 │      Area Supervisory Control             │              │
├─────────┼───────────────────────────────────────────┼──────────────┤
│ Level 1 │         Basic Control                     │  Cell/Area   │
├─────────┼───────────────────────────────────────────┤    Zone      │
│ Level 0 │           Process                         │              │
└─────────┴───────────────────────────────────────────┴──────────────┘
```

- Level 0 ~ 5의 6단계로 구성되며 Level 3단계와 4단계 사이에 IDMZ 구성으로 시스템 접근 제어 구현

---

## 구성요소

### 퍼듀 모델의 계층별 특징

| 계층 | 계층별 특징 | Zone |
|:-----|:-----------|:-----|
| **Level 5** | - Enterprise Network<br>- ICS 네트워크와 연결을 기반으로 공장 설비 상태, 재고, 수요 등을 파악하여 비즈니스 결정을 내리는 데 필요한 데이터를 제공하는 영역 | Enterprise Zone |
| **Level 4** | - 사이트 비즈니스 및 물류<br>- 생산정보 통계 보고, 주문 등 비즈니스 데이터를 ICS/OT 시스템에 분배<br>- DB, 어플리케이션 서버, 파일서버, 이메일 클라이언트, 감독자 Desktop 등 위치 | Enterprise Zone |
| **IDMZ** | - Industrial Demilitarized Zone<br>- IT와 OT시스템의 정보공유 계층으로 직접적인 통신 대신 중계/분리 계층 역할<br>- 터미널 서비스, 웹 서비스 운영 서버, 어플리케이션 서버, 보안솔루션 등이 위치 | IDMZ |
| **Level 3** | - Site Manufacturing Operation and Control<br>- 시설 전체의 제어기능과 모니터링을 담당하는 시스템 위치<br>- 도메인 컨트롤러 서버, 웹 프록시 서버, DB 복제 서버 등이 위치 | Manufacturing Zone |
| **Level 2** | - Area Supervisory Control Zone<br>- HMI(Human Machine Interface), EWS(Engineering Workstation)을 이용한 모니터링 및 관리 | Cell/Area Zone |
| **Level 1** | - Basic Control Zone<br>- 배치 제어, 분산 제어, 연속 프로세스 제어 등 기본적인 제어 영역 | Cell/Area Zone |
| **Level 0** | - Process Zone<br>- 센서, 액츄에이터, 펌프, 로봇 등 프로세스를 수행하는 장비들이 위치하는 영역 | Cell/Area Zone |

- 산업제어시스템(ICS) 보안 강화를 위한 퍼듀 모델과 IEC 62443, 62351 등 보안 표준 존재

---

## 퍼듀 모델의 주요 특징

| 특징 | 설명 |
|:-----|:-----|
| **계층적 구조** | 6개 계층으로 명확한 역할 분리 |
| **IDMZ** | IT/OT 네트워크 분리를 위한 완충 영역 |
| **방화벽 배치** | 계층 간 방화벽으로 트래픽 통제 |
| **최소 권한** | 필요한 통신만 허용하는 원칙 |

---

## 연계 토픽

- [IEC 62443](/docs/sec/05-smart-factory/iec-62443)
- [스마트공장 취약점](/docs/sec/05-smart-factory/smart-factory-security)
- [스마트 공장](/docs/ds/05-smart-factory/)

---

## 학습 체크리스트

- [ ] 퍼듀 모델 6개 계층(Level 0~5) 이해
- [ ] IDMZ의 역할 및 위치 이해
- [ ] Zone별 구성요소 파악

---

## 참고자료

- 정보관리기술사 보안 학습자료
- ISA-99 / IEC 62443

