---
layout: default
title: NB-IoT
parent: 8. IoT
grand_parent: DS (Digital Service)
nav_order: 2
---

# NB-IoT (Narrowband IoT)
{: .fs-8 }

8. IoT
{: .label .label-purple }

---

## 핵심 키워드

`Standalone` `Guard-band` `In-band` `LPWA` `3GPP` `LTE`

---

## 정의/개념

**LPWA 네트워크 실현**, 15km 커버리지, 200KHz 대역폭, 100kbps 속도 **IoT 기술**

- Low Power Wide Area (LPWA) 네트워크를 실현하는 대표적인 IoT 통신 기술
- 기존 LTE 인프라를 활용하여 저전력, 광역 커버리지 제공

---

## 스펙

| 항목 | 사양 |
|:-----|:-----|
| **Coverage** | ~15Km (기존 GSM 대비 20dB 향상요구) |
| **배터리 수명** | ~10년 목표 (AA 건전지 사용, PSM, eDRX지원) |
| **디바이스 수용** | 5만개 이상의 디바이스 수용 |
| **표준화** | 3GPP Rel. 13, 2016년 2분기 |
| **주파수 대역** | 면허대역 (LTE) |
| **대역폭** | 200 KHz |
| **통신속도** | ~100kbps |
| **상용화 시기** | 2017년 2분기 (KT) |

---

## 운영모드

| 동작 모드 | 개념도 | 설명 |
|:-----|:-----|:-----|
| **Standalone Mode** | LTE-NB + Non-LTE Wireless Channels (e.g. GSM) | NB-IoT를 위한 **단독 서비스 주파수** 사용 |
| **Guard-band Mode** | Single LTE Band + LTE-NB + Another Single LTE Band | LTE밴드들 사이에 정의되어 있는 **가드대역내 사용하지 않는 지원블록**을 이용 |
| **In-band Mode** | LTE-NB within Single LTE Band | LTE밴드 내에서 **일부를 자원블록으로 할당**하여 이용 |

---

## 특징

| 구분 | 내용 |
|:-----|:-----|
| **저전력** | PSM(Power Saving Mode), eDRX 지원으로 배터리 수명 10년 목표 |
| **광역 커버리지** | 기존 GSM 대비 20dB 향상, 최대 15km 커버리지 |
| **대용량** | 셀당 5만개 이상 디바이스 수용 가능 |
| **저비용** | 기존 LTE 인프라 활용, 저렴한 모듈 비용 |
| **면허대역** | LTE 면허대역 사용으로 간섭 없는 안정적 통신 |

---

## LPWA 기술 비교

| 구분 | NB-IoT | LoRa | Sigfox |
|:-----|:-----|:-----|:-----|
| **주파수** | 면허대역 | 비면허대역 | 비면허대역 |
| **커버리지** | ~15km | ~15km | ~50km |
| **속도** | ~100kbps | ~50kbps | ~100bps |
| **표준** | 3GPP | LoRa Alliance | Sigfox |

---

## 연계 토픽

- [IoT](/docs/ds/08-iot/iot)
- [5G](/docs/ds/01-cloud/5g)
- [스마트팩토리](/docs/ds/05-smart-factory/)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 스펙 (커버리지, 배터리, 속도 등) 암기
- [ ] 3가지 운영모드 (Standalone, Guard-band, In-band) 암기
- [ ] LPWA 기술 비교 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
