---
layout: default
title: RAN-Sharing
parent: 4. 네트워크 구축
grand_parent: NW (네트워크)
nav_order: 5
---

# RAN-Sharing
{: .fs-8 }

4.1 네트워크 구축
{: .label .label-purple }

---

## 핵심 키워드

`MORAN` `MOCN` `GWCN`

---

## 정의/개념

이동통신망에서 서로 다른 사업자가 동일한 주파수 사용시 발생되는 간섭 문제 해결을 위해 기지국, 코어망, Gateway를 공유 사용하며 **MOCN, MORAN, GWCN 기술 활용하는 무선 인프라 공유 기술**

---

## 기술 방식

### MOCN (Multi-Operator Core Network)

```
"이통사 A"  →  Service Platform  →  Core  →  컨트롤러    →  기지국     →  Spectrum
                                           (Shared)      (Shared)     (Shared)
"이통사 B"  →  Service Platform  →  Core  ──────────┘
```

- 기지국, 컨트롤러, 스펙트럼 공유
- 각 사업자별 Core 망 분리 운영

### MORAN (Multi-Operator Radio Access Network)

```
"이통사 A"  →  Service Platform  →  Core  →  컨트롤러    →  기지국     →  Spectrum
                                           (Shared)      (Shared)
"이통사 B"  →  Service Platform  →  Core  ──────────┘               →  Spectrum
```

- 기지국, 컨트롤러 공유
- 스펙트럼은 각 사업자별 분리 사용

### GWCN (Gateway Core Network)

```
"이통사 A"  →  Service Platform  →  Core(MME)  →  컨트롤러    →  기지국     →  Spectrum
                                  (Shared)      (Shared)      (Shared)     (Shared)
"이통사 B"  →  Service Platform  ────────┘
```

- Core(MME), 기지국, 컨트롤러, 스펙트럼 모두 공유
- 가장 높은 수준의 인프라 공유

---

## 연계 토픽

- [O-RAN](/docs/nw/04-infrastructure/o-ran)
- [5G 특화망](/docs/nw/04-infrastructure/5g-private-network)

---

## 학습 체크리스트

- [ ] RAN-Sharing 개념 이해
- [ ] MOCN, MORAN, GWCN 차이 구분
- [ ] 각 방식별 공유 범위 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


