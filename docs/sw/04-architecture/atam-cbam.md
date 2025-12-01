---
layout: default
title: SW 아키텍처 평가모델
parent: 4. 아키텍처
grand_parent: SW (소프트웨어공학)
nav_order: 3
---

# SW 아키텍처 평가모델
{: .fs-8 }

4.1 아키텍처 기본
{: .label .label-purple }

---

## 핵심 키워드

`SAAM` `ATAM` `CBAM` `EATAM` `ADR` `ARID`

---

## 정의/개념

소프트웨어 아키텍처 품질 속성 충족 아키텍처 평가 기법

---

## 구성도

```
                    계승/발전
        SAAM ─────────────────► ATAM ─────────────► ADR
         │                        │                   │
  - Modifiability            - Performance        - 응집도 평가
  - Functionality            - Reliability        - 설계기반
                                  │
                            경제성                ATAM과 ADR
                            평가보강              혼합
                                  │                   │
                                  ▼                   ▼
        EATAM ◄──────────── CBAM ──────────────► ARID
           │                   │                     │
  - Product Line평가      - 경제성평가            - 품질요소 집중
  - 스테이지 기반         - ROI                   - 조기검토
           │                   │
     시나리오 기반        설계/혼합 기반
       평가모델            평가모델
```

---

## 구성요소

### 소프트웨어 아키텍처 평가 모델 설명

| 구분 | 평가모델 | 목표 | 설명 |
|:-----|:---------|:-----|:-----|
| **시나리오 기반 평가모델** | SAAM | 수정 가능성과 기능성에 집중 | - Software Architecture Analysis Method<br>- 수정 가능성과 기능 분석 중심의 최초의 아키텍처 평가 방법 |
| | ATAM | SAAM 계승, 품질 요소간 Trade-Off 평가 | - Architecture Tradeoff Analysis Method<br>- 품질목표 간에 Trade off가 있는지 파악 가능한 아키텍처 평가방법 |
| | CBAM | 편익 분석을 통해 투자가치 판단 | - Cost Benefit Analysis Method<br>- ATAM의 평가를 보완하여 시스템 구축 시 경제성 평가까지 하여 수익이 최대가 될 수 있도록 의사 결정을 도와주는 SW아키텍처 평가모델 |
| | EATAM | Product Line 확장 평가 | - Extending Architecture Trade off Analysis Method<br>- 개별 평가모델의 확장, 스테이지 기반 모델을 통한 Product Line 아키텍처 평가 수행 |
| **설계/혼합 기반 평가모델** | ADR | ATM과 ARID 혼합 | - Active Design Review<br>- 설계기반 아키텍처 구성요소 간 응집도 평가 |
| | ARID | 특정 부분의 품질 요소 집중 | - Active Reviews for Intermediate Designs<br>- 조기에 일부 설계만 완료되었더라도 쉽게 평가하 도록 하여 조기 발생 가능성 위험 감소<br>- 시나리오 중심의 ATAM, SAAM과 설계 검토 방법인 ARD를 혼합 |

---

## 연계 토픽

- [SW 아키텍처 패턴/스타일](/docs/sw/04-architecture/architecture-pattern)
- [ISO 42010](/docs/sw/04-architecture/iso-42010)

---

## 학습 체크리스트

- [ ] 시나리오 기반 평가모델 (SAAM, ATAM, CBAM, EATAM) 이해
- [ ] 설계/혼합 기반 평가모델 (ADR, ARID) 이해
- [ ] 각 평가모델의 목표 및 특징 이해
- [ ] ATAM과 CBAM의 관계 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

