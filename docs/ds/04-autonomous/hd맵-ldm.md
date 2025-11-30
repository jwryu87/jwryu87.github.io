---
layout: default
title: HD맵/LDM
parent: 4. 스마트카/자율주행
grand_parent: DS (Digital Service)
nav_order: 3
---

# LDM (Local Dynamic Map)
{: .fs-8 }

4.1 자율주행
{: .label .label-yellow }

---

## 핵심 키워드

`데이터저장소` `정적/준정적/준동적/동적` `정밀전자지도` `C-ITS`

---

## 정의/개념

정보수집의 대상 범위 내에 있는 고정 물체(예: 노변 시설 및 장치) 또는 이동 물체(예: 차량, 보행자 등)에 관한 정적(static), 일시적(temporary), 동적(dynamic) 정보를 모두 관리할 수 있는 **동적인 공간 데이터 저장소**

---

## LDM 구성도

```
                    Information through V to X
Time frame    Linked layers    · surrounding vehicles
                              · pedestrians
              Link            · timing of traffic signals
                    
Dynamic (< 1 sec)              Traffic Information
                              · accidents
Semi-dynamic (< 1 min)         · congestion
                              · local weather
                    
Semi-static (< 1 hour)         Planned and forecast
                              · traffic regulations
Static (< 1 month)             · road works
                              · weather forecast
                    
Basic Map                      Basic Map Database
                              · Digital cartographic data
                              · Topological data with unique
                              · Road Facilities
```

---

## LDM 구성요소

| 조항 | Layer | 제공 정보 | 갱신주기 |
|:-----|:------|:---------|:---------|
| **정적 정보** | Layer 1 : 정밀 전자지도 (Static) | 도로, 실제 지형 정보 등 표현 | < month |
|  | Layer 2 : 계획 및 전망 (Semi Static) | 도로 시설물, 표지판, 공사/통제 정보, 휴게소 운영시간 등 표현 | < hour |
| **동적 정보** | Layer 3 : 교통정보 (Semi Dynamic) | 속성 정보 지도, 사고/도로 상황, 날씨 등 표현 | < min |
|  | Layer 4 : V2X 를 통한 정보 (Dynamic) | 기준 자동차 기반 인식 대상 지도, 주변 차량/보행자 등 표현 | < sec |

---

## 연계 토픽

- [C-ITS](/docs/ds/04-autonomous/)
- [자율주행 자동차](/docs/ds/04-autonomous/자율주행-자동차)
- [정밀지도](/docs/ds/04-autonomous/)

---

## 학습 체크리스트

- [ ] LDM 정의 이해
- [ ] 4개 Layer (Static → Semi Static → Semi Dynamic → Dynamic) 구분
- [ ] 각 Layer별 제공 정보 및 갱신주기 숙지
- [ ] C-ITS와 연계 이해

---

## 참고자료

- 정보관리기술사 DS 학습자료
