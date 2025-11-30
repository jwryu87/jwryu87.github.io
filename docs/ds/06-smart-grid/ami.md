---
layout: default
title: AMI
parent: 6. 스마트그리드/에너지
grand_parent: DS (Digital Service)
nav_order: 2
---

# AMI (Advanced Metering Infrastructure) 2.0
{: .fs-8 }

6.1 스마트그리드
{: .label .label-green }

---

## 핵심 키워드

`LWM2M` `SNMP v3` `보안 강화형 스마트 전력량계` `CAN` `Wi-SUN` `Mbed OS` `IoT-PLC`

---

## 정의/개념

수용가에서 소비되는 전력량 측정, 과거 소비량 기반 분석 통한 향후 소비량 예측 등을 위해 개발된 **AMI에 IoT 환경 통신 기술과 보안 성능을 강화**한 **차세대 AMI 기술**

---

## AMI 2.0 발전 메커니즘

| AMI | 요구 사항 | AMI 2.0 |
|:----|:---------|:--------|
| HAN | 보안 강화 | LWM2M |
| Smart Meter | 통신 성능 | SNMP v3 |
| MDMS | IoT | Mbed OS |

---

## AMI 2.0 구성요소

| 구분 | 구성 요소 | 설명 |
|:-----|:---------|:-----|
| **기존 기술** | 스마트 미터 | 양방향 통신 기반, 사용량 분석 통한 전력 수요 예측 기능 제공 |
|  | IHD | In-Home Display, 사용자와의 상호 작용을 위한 인터페이스 제공 |
|  | MDMS | 미터 데이터 관리 시스템, 이기종 미터링 시스템 데이터 수신 및 관리 |
|  | ESS | 자가 발전 등을 통해 생산된 에너지를 저장 하기 위한 기술 |
| **신규 기술** | IoT-PLC | IoT 기반에서 사용 가능 하도록 6LowPAN 기반 차세대 전력선 통신 기술 |
|  | LWM2M | 관리 기능을 제한적 자원, 성능 환경에서 운용 하기 위한 경량화 플랫폼 |
|  | SNMP v3 | 사용자 보안 모델과 뷰-기반 접근 제어를 정의한 프로토콜 |
|  | Secure DCU | 분산 데이터 수집 및 전송을 위한 DCU에 보안 기능이 강화된 형태 |

---

## AMI 2.0 아키텍처

```
Building
┌─────────────────┐                    ┌───────────────┐
│ 스마트가전      │                    │    MDMS      │
│   ESS          │     NAN            │    ERP       │
│   IHD          │  스마트  SNMP v3  │    OMS       │
│                │   미터  ─────→ WAN │  Dashboard   │
│ Mobile Device  │                    │    CIS       │
│  Mbed OS       │  Secure DCU       │    DR        │
│   PV    스마트 │    (Data          │              │
│  태양광  미터  │  Concentration    │              │
│  발전         │     Unit)          │  전력 회사   │
└─────────────────┘                    └───────────────┘
      수용가          배전전주
```

---

## 연계 토픽

- [스마트그리드](/docs/ds/06-smart-grid/스마트그리드)

---

## 학습 체크리스트

- [ ] AMI 2.0 정의 이해
- [ ] 기존 기술 4가지 (스마트미터, IHD, MDMS, ESS) 숙지
- [ ] 신규 기술 4가지 (IoT-PLC, LWM2M, SNMP v3, Secure DCU) 숙지
- [ ] AMI vs AMI 2.0 차이점 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
