---
layout: default
title: LiDAR
parent: 4. 스마트카/자율주행
grand_parent: DS (Digital Service)
nav_order: 6
---

# LiDAR
{: .fs-8 }

4.1 자율주행
{: .label .label-yellow }

---

## 핵심 키워드

`변조 방식` `구성 기술` `동작 기술`

---

## 정의/개념

**빛**, 적외선 광 펄스 **위치 거리 속도 측정 기술**

---

## LiDAR 메커니즘

```
신차 인식 → Source → Optic → Laser → 사물
  ↑                              ↓
  ← 대역 ← 신호처리신 ← 탐지 ←
```

---

## LiDAR 구성요소

| 구분 | 요소 | 설명 |
|:-----|:-----|:-----|
| **구성요소** | Source | - 광학계(Lens)로부터 균일한 레이저 빔을 발광<br>- Laser Diode, Illumination Board, 광학계 |
|  | Optic | - Source, Detector 간 시야 각 및 해상도 확보<br>- 광학 렌즈, 거울, 프리즘 등으로 구성 |
|  | Detector | - 반사되어 들어오는 레이저 점 군 인식<br>- Photodiode Array, 집광부, 신호처리부, 제어부 |
| **기술요소** | 변조 방식 | - **TOF(Time of Flight)** 방식 : 레이저 펄스가 물체에 반사되어 수신되어 도착한 시간 측정<br>- **PS(Phase Shift)** 방식 : 특정 주파수 레이저가 물체에 반사되는 신호 위상 변화 측정 |
|  | 구성 기술 | - **회전형** : 360도 회전체 내 레이저 탑재<br>- **어레이형** : 수광부 픽셀을 다수 배치하여 3차원 고해상도 영상 습득<br>- **STUD 방식** : Static Unitary Detector 320 x 240 픽셀 3차원 영상습득 |
|  | 동작 기술 | - **Raman LiDAR** : 분자 에너지 따른 주파수변화<br>- **DIAL** : 각 레이저 파장 별 흡수 차이<br>- **Resonance Fluorescence LiDAR** : 긴 파장 및 방출 특성 이용<br>- **Doppler LiDAR** : 레이저 빔 미세한 주파수 변화<br>- **Imaging LiDAR** : 거리정보 포함 공간영상 모델링 |

---

## 빛을 통한 감지와 빛을 이용해 거리 측정 수행

---

## 연계 토픽

- [RADAR](/docs/ds/04-autonomous/radar)
- [SLAM](/docs/ds/04-autonomous/)
- [자율주행 자동차](/docs/ds/04-autonomous/자율주행-자동차)

---

## 학습 체크리스트

- [ ] LiDAR 정의 이해
- [ ] 구성요소 3가지 (Source, Optic, Detector) 숙지
- [ ] 변조 방식 (TOF, Phase Shift) 이해
- [ ] 구성 기술 (회전형, 어레이형, STUD) 이해
- [ ] 동작 기술 5가지 숙지

---

## 참고자료

- 정보관리기술사 DS 학습자료
