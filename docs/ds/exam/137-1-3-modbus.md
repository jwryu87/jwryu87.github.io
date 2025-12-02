---
layout: default
title: 137회-1교시-3번 MODBUS 프로토콜
parent: 📝 기출문제
grand_parent: DS (Digital Service)
nav_order: 2
permalink: /docs/ds/exam/137-1-3-modbus
---

# MODBUS 프로토콜
{: .fs-8 }

137회 정보관리기술사 1교시 3번
{: .label .label-blue }

네트워크 / 난이도: 상
{: .label .label-purple }

---

## 📚 목차

1. [고딩 수준 설명](#-고딩-수준-설명)
2. [기술사 수준 설명](#-기술사-수준-설명)

---

# 🎓 고딩 수준 설명
{: .fs-7 }

> 고등학생도 이해할 수 있게 설명합니다

---

## 🔑 핵심 키워드 3개

| 키워드 | 설명 |
|:------|:-----|
| **Master-Slave** | 사장님(Master)이 지시하면 직원(Slave)이 응답하는 구조 |
| **산업용 통신** | 공장 기계들끼리 대화하는 언어 |
| **오픈 프로토콜** | 누구나 무료로 사용 가능, 로열티 없음 |

---

## 📖 등장배경

```
🏭 1979년, 공장에 자동화 기계들이 늘어남

💡 문제: "기계들끼리 어떻게 대화하지? 각자 다른 언어를 쓰네..."

✅ 해결: Modicon 회사에서 MODBUS 개발!
   → 공장 기계들의 "공용어" 탄생
   → 센서, PLC, 컴퓨터가 모두 같은 언어로 소통
   → 무료 공개해서 전 세계 표준이 됨!
```

---

## 📝 개념 정의

> **MODBUS**란?
> 
> 🏭 공장의 **기계들(PLC, 센서, 컴퓨터)이 서로 통신**하기 위한  
> 📡 **산업용 표준 프로토콜**  
> 💰 **무료**로 사용 가능!

### 쉬운 비유

| 일반 대화 | MODBUS 통신 |
|:---------|:-----------|
| 👨‍💼 사장: "3번 직원, 온도 알려줘" | Master → Slave ID 3: "레지스터 값 읽기" |
| 👷 직원: "25도입니다" | Slave 3 → Master: "0x0019 (25)" |
| 사장이 물어봐야 직원이 대답 | Master가 요청해야 Slave가 응답 |

---

## 🏗️ 기술요소 (2가지 그룹)

### 그룹 1: 프로토콜 유형 (통신 방식)

| 유형 | 특징 | 사용처 |
|:----|:----|:------|
| **Modbus RTU** | 빠름, 바이너리 형식 | RS-232/RS-485 시리얼 통신 |
| **Modbus ASCII** | 느림, 사람이 읽기 쉬움 | 디버깅, 테스트 |
| **Modbus TCP** | 이더넷 사용, 502번 포트 | 네트워크 연결 장비 |

**활용**: 공장 자동화, 빌딩 관리, 에너지 모니터링

### 그룹 2: 데이터 모델 (저장 공간)

| 데이터 타입 | 크기 | 읽기 | 쓰기 | 쉬운 설명 |
|:-----------|:----|:----:|:----:|:---------|
| **Coils** | 1bit | ✅ | ✅ | 💡 전등 ON/OFF 스위치 |
| **Discrete Inputs** | 1bit | ✅ | ❌ | 🚨 센서 상태 (읽기만) |
| **Input Register** | 16bit | ✅ | ❌ | 🌡️ 온도 센서 값 (읽기만) |
| **Holding Register** | 16bit | ✅ | ✅ | ⚙️ 설정값 (읽기/쓰기) |

---

## ⭐ 차별점 키워드 (답안지 가산점!)

{: .highlight }
> **ICS/SCADA 보안 취약점**
> 
> MODBUS는 **인증·암호화가 없는** 1979년 설계 프로토콜
> 
> - 🔓 평문 전송 → 패킷 스니핑 가능
> - 🎭 인증 없음 → 스푸핑 공격 가능
> - 🏭 산업제어시스템(ICS) 해킹의 주요 타겟
> - 💡 Modbus/TCP Security 확장 필요

---

## 🔗 프로토콜 유형 관계

```
┌────────────────────────────────────────────────────┐
│                    MODBUS 프로토콜                  │
├────────────────────────┬───────────────────────────┤
│     시리얼 기반         │        이더넷 기반         │
├────────────────────────┼───────────────────────────┤
│  ┌──────────────────┐  │  ┌─────────────────────┐  │
│  │   Modbus RTU     │  │  │    Modbus TCP       │  │
│  │   (바이너리)      │  │  │    (502 port)       │  │
│  └──────────────────┘  │  └─────────────────────┘  │
│  ┌──────────────────┐  │  ┌─────────────────────┐  │
│  │   Modbus ASCII   │  │  │  Modbus over TCP    │  │
│  │   (문자 기반)     │  │  │  (RTU+TCP 혼합)     │  │
│  └──────────────────┘  │  └─────────────────────┘  │
├────────────────────────┼───────────────────────────┤
│  RS-232, RS-422,       │     Ethernet              │
│  RS-485                │                           │
└────────────────────────┴───────────────────────────┘
```

---

## 📋 6하원칙 요약

| 구분 | 내용 |
|:-----|:----|
| **누가(Who)** | Modicon(현 Schneider Electric), 1979년 개발 |
| **언제(When)** | 1979년 개발 → 2004년 Modbus Organization 이관 |
| **어디서(Where)** | 공장, 발전소, 빌딩, IoT 환경 |
| **무엇을(What)** | PLC, RTU, 센서 간 데이터 통신 |
| **왜(Why)** | 산업 자동화 기기 간 표준 통신 필요 |
| **어떻게(How)** | Master-Slave 구조, 시리얼/이더넷 전송 |

---

# 🎯 기술사 수준 설명
{: .fs-7 }

> 정보관리기술사 수준으로 설명합니다

---

## 🔑 핵심 키워드 3개

| 키워드 | 기술 의미 |
|:------|:---------|
| **Master-Slave Architecture** | 요청-응답 기반 폴링 통신 구조 |
| **Application Layer Protocol** | OSI 7계층 응용 계층 메시징 프로토콜 |
| **ICS/SCADA Integration** | 산업제어시스템 표준 통신 프로토콜 |

---

## 📖 등장배경

| 배경 | 설명 |
|:----|:-----|
| **산업 자동화 확산** | 1979년 공장 자동화로 디바이스 간 통신 표준 필요 |
| **ICS 보안 이슈 부각** | 인증·암호화 부재로 SCADA/IoT 환경 보안 위협 증가 |

---

## 📝 개념 정의 (22자 이내)

> **산업용 Master-Slave 응용계층 통신규약**

---

## 🏗️ 구성요소 (2그룹 × 4항목)

### 그룹 1: 프로토콜 유형 (Protocol Variants)

| 구성요소 | 전송방식 | 특징 | 인터페이스 |
|:--------|:--------|:-----|:----------|
| **Modbus RTU** | Binary | CRC 체크, 고속 전송 | RS-232, RS-485 |
| **Modbus ASCII** | ASCII | LRC 체크, 가독성 높음 | RS-232, RS-485 |
| **Modbus TCP** | TCP/IP | MBAP 헤더, 502 port | Ethernet |
| **Modbus over TCP** | TCP/IP | RTU 프레임+TCP 캡슐화 | Ethernet |

### 그룹 2: 데이터 모델 (Data Model)

| 구성요소 | 크기 | Master 접근 | Slave 접근 |
|:--------|:----|:-----------|:-----------|
| **Coils** | 1bit | Read/Write | Read/Write |
| **Discrete Inputs** | 1bit | Read Only | Read/Write |
| **Input Register** | 16bit | Read Only | Read/Write |
| **Holding Register** | 16bit | Read/Write | Read/Write |

---

## 🧠 암기법 (Mnemonic)

{: .note }
> ### 그룹 1: **"R-A-T-O"** (RTU → ASCII → TCP → Over TCP)
> 
> | 암기 | 프로토콜 | 키포인트 |
> |:-----|:--------|:--------|
> | **R** | RTU | **R**aw Binary, 가장 빠름 |
> | **A** | ASCII | **A**SCII 문자, 사람이 읽기 쉬움 |
> | **T** | TCP | **T**CP/IP, 502 port |
> | **O** | Over TCP | RTU **O**ver TCP 캡슐화 |
>
> 💡 **"RATO"** — 시리얼(R,A) → 이더넷(T,O) 순서로 진화

{: .note }
> ### 그룹 2: **"C-D-I-H"** (1bit → 16bit, Read Only → Read/Write)
> 
> | 암기 | 데이터 모델 | 크기 | 특징 |
> |:-----|:-----------|:----|:-----|
> | **C** | **C**oils | 1bit | 출력, R/W |
> | **D** | **D**iscrete Inputs | 1bit | 입력, RO |
> | **I** | **I**nput Register | 16bit | 입력, RO |
> | **H** | **H**olding Register | 16bit | 저장, R/W |
>
> 💡 **"CDIH"** — Coils/Discrete(1bit) → Input/Holding(16bit)

---

## 📊 프레임 구조 비교

| 구분 | Modbus RTU/ASCII | Modbus TCP |
|:----|:-----------------|:-----------|
| **헤더** | Slave ID | MBAP (Transaction ID, Protocol ID, Length, Unit ID) |
| **PDU** | Function Code + Data | Function Code + Data |
| **에러체크** | CRC(RTU) / LRC(ASCII) | TCP 체크섬 (하위 계층) |
| **프레임 구분** | 공백(RTU) / CR,LF(ASCII) | TCP 세그먼트 |

```
[Modbus RTU/ASCII Frame - ADU]
┌──────────┬───────────────┬────────┬─────────────┐
│ Slave ID │ Function Code │  Data  │ CRC/LRC     │
│ (1byte)  │   (1byte)     │(N byte)│ (2byte)     │
└──────────┴───────────────┴────────┴─────────────┘
  Addressing      └────── PDU ──────┘  Error Check

[Modbus TCP Frame - ADU]
┌────────────────────────────┬───────────────┬────────┐
│         MBAP Header        │ Function Code │  Data  │
│ (Trans ID, Proto, Len, UID)│   (1byte)     │(N byte)│
└────────────────────────────┴───────────────┴────────┘
        Addressing           └────── PDU ──────┘
```

---

## ⭐ 차별점 키워드 (답안 가산점!)

{: .important }
> **Modbus Security (TLS 기반 보안 확장)**
> 
> - 기존 Modbus의 **인증·암호화 부재** 문제 해결
> - **Modbus/TCP Security**: TLS 1.2+ 기반 암호화
> - **Role-Based Access Control**: 역할 기반 접근 제어
> - **X.509 인증서**: 디바이스 인증
> - ICS/SCADA 보안 강화를 위한 **IEC 62443** 연계

---

## 🔗 Modbus 프로토콜 체계

```
┌─────────────────────────────────────────────────────────────┐
│                    MODBUS 프로토콜 체계                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   OSI 7 Layer                      Modbus Stack             │
│   ┌─────────────┐                 ┌─────────────────┐       │
│   │ Application │ ◄─────────────► │ Modbus Protocol │       │
│   ├─────────────┤                 │ (Function Code) │       │
│   │ Presentation│                 └─────────────────┘       │
│   ├─────────────┤                         │                 │
│   │   Session   │                         │                 │
│   ├─────────────┤                         ▼                 │
│   │  Transport  │ ◄────────────► ┌─────────────────┐       │
│   ├─────────────┤                │   TCP / Serial  │       │
│   │   Network   │                └─────────────────┘       │
│   ├─────────────┤                         │                 │
│   │  Data Link  │                         ▼                 │
│   ├─────────────┤                ┌─────────────────┐       │
│   │  Physical   │ ◄─────────────►│ Ethernet/RS-485 │       │
│   └─────────────┘                └─────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 6하원칙 요약

| 구분 | 내용 |
|:----|:-----|
| **누가(Who)** | Modicon(현 Schneider Electric), Modbus Organization |
| **언제(When)** | 1979년 개발 → 2004년 Modbus Org 이관 → 현재 ICS 표준 |
| **어디서(Where)** | ICS/SCADA, 스마트 팩토리, 빌딩 자동화, IoT/IIoT |
| **무엇을(What)** | PLC, RTU, HMI 간 제어·상태 데이터 통신 |
| **왜(Why)** | 산업 자동화 표준화, 벤더 독립적 통신 |
| **어떻게(How)** | Master-Slave 폴링, ADU(PDU+주소+에러체크) 구조 |

---

## 📈 상위 토픽 계층도

```
최상위: IT 서비스
    │
    ├── 산업 IT (Industrial IT)
    │       │
    │       ├── ICS (Industrial Control System)
    │       │       │
    │       │       ├── SCADA (Supervisory Control and Data Acquisition)
    │       │       │       │
    │       │       │       └── 🎯 MODBUS 프로토콜
    │       │       │               ├── Modbus RTU/ASCII (시리얼)
    │       │       │               └── Modbus TCP (이더넷)
    │       │       │
    │       │       ├── PLC (Programmable Logic Controller)
    │       │       │
    │       │       └── DCS (Distributed Control System)
    │       │
    │       └── IIoT (Industrial IoT)
    │               └── 스마트 팩토리
    │
    └── 네트워크 기술
            ├── 시리얼 통신 (RS-232/422/485)
            └── 산업용 이더넷
```

---

## 🔮 향후 전망

### 기술적 전망

| 전망 | 설명 |
|:----|:-----|
| **Modbus Security 확산** | TLS 기반 암호화, X.509 인증 적용 확대 |
| **OPC UA 연계** | Modbus + OPC UA 게이트웨이 통합 |
| **Time-Sensitive Networking** | TSN 기반 결정적 통신 연계 |

### 서비스/산업 전망

| 전망 | 설명 |
|:----|:-----|
| **스마트 팩토리 확대** | Industry 4.0 환경에서 레거시 연동 |
| **IIoT 게이트웨이** | Modbus → MQTT/REST 변환 |
| **에너지 관리** | 스마트 그리드, EMS 연계 지속 |

### 보안/표준화 전망

| 전망 | 설명 |
|:----|:-----|
| **IEC 62443 적용** | ICS 보안 표준 기반 Modbus 보안 강화 |
| **제로 트러스트** | 산업 환경 제로 트러스트 아키텍처 적용 |
| **폐쇄망 + 암호화** | 물리적 분리 + Modbus Security 병행 |

---

## 📚 참고자료

- ITPE 서브노트
- Modbus Organization Specification
- IEC 62443 (Industrial Cybersecurity)
- NIST SP 800-82 (Guide to ICS Security)

---

## ✅ 학습 체크리스트

- [ ] Master-Slave 구조 이해
- [ ] RTU/ASCII/TCP 유형 차이 파악
- [ ] 데이터 모델 4가지(Coils, DI, IR, HR) 암기
- [ ] 프레임 구조(ADU = PDU + 주소 + 에러체크) 이해
- [ ] ICS/SCADA 보안 취약점 인지
- [ ] Modbus Security 확장 개념 파악

---

*Last Updated: 2025-12-02*

