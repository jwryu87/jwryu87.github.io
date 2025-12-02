---
layout: default
title: IoT
parent: 8. IoT
grand_parent: DS (Digital Service)
nav_order: 1
---

# IoT (Internet of Things)
{: .fs-8 }

8. IoT
{: .label .label-purple }

---

## 핵심 키워드

`센서` `유무선 네트워크` `인터페이스` `센싱기술` `WiFi` `Bluetooth` `NB-IoT` `미들웨어`

---

## 정의/개념

센서, 네트워크, 인터페이스 **모든 사물 연결 제공 기술**

- IoT 3대 핵심 기술 중 유무선 통신 사용시 LTE 망에서 서비스되는 NB-IoT가 많이 활용되고 있음

---

## 메커니즘

```
IoT 디바이스 → IoT 네트워크 → IoT 플랫폼 → IoT 서비스
```

| 계층 | 구성요소 | 설명 |
|:-----|:-----|:-----|
| **IoT 서비스** | 헬스케어, 스마트홈, 스마트공장, 스마트농업, 스마트그리드, 환경감시, 원격관제 | IoT 서비스 프레임워크<br>IoT 기반 플랫폼 |
| **IoT 플랫폼** | 앱스, 연결, 제조, 헬싱, 해킹, 기타 | IoT 서비스 인터페이스 기술 |
| **IoT 네트워크** | Bluetooth, LoRa, 인터넷(Internet), lte 5G, Sigfox, 유선망 | 유무선 통신 및 네트워크 인프라 기술 |
| **IoT 디바이스** | 센서, 게이트, 렌서, 기기, 디바이스 플랫폼, 해킹, 포로그, 신발, S카 | 센싱 기술<br>실제 사물(Physical Thing) / 가상적 사물(Virtual Thing) |

---

## 3대 핵심 기술

| 핵심 기술 | 설명 |
|:-----|:-----|
| **센싱기술** | - 유형 사물과 주변 환경으로부터 정보를 얻는 기술<br>- 온습도/조도/온도 센서, 원격 감지, 레이더, 영상센서 |
| **유무선 통신** | - IoT Device간 또는 IoT Device와 G/W, 서버 간의 통신 기술<br>- WiFi, 4G/LTE, Bluetooth, NB-IoT, Sigfox |
| **IoT 서비스<br>인터페이스 기술** | - 정보를 센싱, 가공/추출/처리, 저장, 판단, 상황인식, 보안/프라이버시 보호, 인증/인가<br>- 응용 서비스와 연동하는 역할 수행<br>- 미들웨어, 오픈 플랫폼, 데이터 마이닝 기술 등 서비스 수행을 위한 인터페이스 역할 |

---

## IoT 아키텍처

| 구분 | 설명 |
|:-----|:-----|
| **디바이스 계층** | 물리적 사물(센서, 액추에이터) 및 가상 사물 |
| **네트워크 계층** | 유무선 통신 인프라 (WiFi, LTE, LoRa 등) |
| **플랫폼 계층** | 데이터 수집, 처리, 저장, 분석 |
| **서비스 계층** | 응용 서비스 제공 (스마트홈, 스마트팩토리 등) |

---

## RFID (Radio Frequency IDentification)

> 암기: **이리사오피** (Tag, Reader, Savant Server, ONS, PML)

### RFID 구성요소

| 구성요소 | 설명 |
|:---------|:-----|
| **Tag (EPC)** | 전자 제품 코드가 저장된 태그 |
| **Reader** | 태그 정보를 읽는 장치 |
| **Savant Server** | 대량의 EPC 데이터 필터링/처리 |
| **ONS** | EPC → URL 변환 (Object Name Service) |
| **PML** | 제품 정보 기술 언어 (Physical Markup Language) |
| **PML Server** | PML 데이터 저장/관리 서버 |

### RFID 동작 흐름

```
Tag(EPC) → Reader → Savant Server → ONS(EPC→URL) → PML Server
```

---

## 연계 토픽

- [NB-IoT](/docs/ds/08-iot/nb-iot)
- [IoT Matter](/docs/ds/08-iot/iot-matter)
- [스마트팩토리](/docs/ds/05-smart-factory/)
- [스마트그리드](/docs/ds/06-smart-grid/)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 3대 핵심 기술 암기 (센싱, 유무선 통신, 서비스 인터페이스)
- [ ] IoT 아키텍처 계층 이해
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료
