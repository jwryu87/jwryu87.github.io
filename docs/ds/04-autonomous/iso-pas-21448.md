---
layout: default
title: ISO/PAS 21448
parent: 4. 스마트카/자율주행
grand_parent: DS (Digital Service)
nav_order: 9
---

# ISO/PAS 21448 (SOTIF)
{: .fs-8 }

4.2 자율주행 표준
{: .label .label-purple }

> 암기: **기연트줄/VKU배**

---

## 핵심 키워드

`Verification` `Validation`

---

## 정의/개념

**의도된 기능**이 한계로 인해 위험 발생 시, **위험 최소화 기술**

SOTIF = Safety Of The Intended Functionality

---

## 프로세스

| 구분 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **절차** | 5 | 기능 및 시스템 사양 |
|  | 6 | SOTIF 연관 위험식별과 위험평가 |
|  | 7 | 트리거 이벤트에 대한 식별 및 평가 |
|  | 8 | SOTIF 위험 줄이기 위한 기능 수정 |
|  | 9 | Verification 과 Validation 전략의 정의 |
|  | 10 | SOTIF Verification: Known 시나리오 평가 |
|  | 11 | SOTIF Validation: Unknown 시나리오 평가 |
|  | 12 | SOTIF 배포위한 방법론과 기준 |
| **위험 요인** | 시스템 | - E/E 시스템 고장: ISO 26262<br>- 성능 부족이나 상황인지 오류: ISO/PAS 21448<br>- 사용자 오사용 및 HMI 오류: ISO/PAS 21448, ISO 26262<br>- 외부공격에 대한 보안 취약성: ISO 21434/SAE J3061 |
|  | 외부 요소 | - 인프라 동작 오류(차량 통신, 외부 시스템, 클라우드 서비스): ISO 20077 / ISO 26262<br>- 환경 요소 반영 미흡(기후, 자기 간섭, 다른 차량): ISO/PAS 21448 |

---

## 메커니즘

```
                    ⑨ Verification과 Validation 전략의 정의
                              ↓
Item 정의 → ⑤ → ⑥ → ⑦ → ⑧ → SOTIF 식별과 검증 → ⑪ Vehicle Validation Test
    ↓                              ↓
  HARA                    SOTIF 감기사 및 분석
    ↓                              ↓
   FSC                    SOTIF Verification → ⑩ Vehicle Verification Test
    ↓                    (Known 시나리오검증)
   TSC
    ↓                              ⑫
H/W and S/W Development      SOTIF 배포 위한
                            방법론과 기준
```

---

## 참고사항

- UNECE(유엔 유럽 경제 위원회)에서는 급격하게 성장하고 있는 차량 산업의 보안 위험을 우려해 UNECE Cyber Security Regulation 를 수립하여 OEM 및 부품공급업체는 차량 사이버보안 관리체계를 구축 및 인증을 받게 함

**용어:**
- HARA: Hazard Assessment by Risk Analysis
- TSC: Technical Safety Concept
- FSC: Functional Safety Concept

---

## 연계 토픽

- [ISO 26262](/docs/ds/04-autonomous/iso-26262)
- [ISO/SAE 21434](/docs/ds/04-autonomous/iso-sae-21434)

---

## 학습 체크리스트

- [ ] SOTIF 정의 이해
- [ ] 절차 5~12 단계 숙지
- [ ] ISO 26262와 SOTIF 차이점 이해
- [ ] 위험 요인 (시스템/외부 요소) 구분

---

## 참고자료

- 정보관리기술사 DS 학습자료
