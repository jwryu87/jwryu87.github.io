---
layout: default
title: IDS/IPS
parent: 탐지/대응
grand_parent: 보안
nav_order: 1
---

# 침입탐지시스템(IDS), 침입방지시스템(IPS)
{: .fs-8 }

19.1 탐지/대응
{: .label .label-purple }

---

## 핵심 키워드

`IDS` `IPS` `Mirroring` `Positive` `Reactive` `시그니처 DB` `침입차단` `Active` `Proactive`

---

## 정의/개념

### IDS (Intrusion Detection System)

비인가된 사용자가 자원의 **무결성(integrity), 기밀성(confidentiality), 가용성(availability)**을 저해하는 일련의 행동들과 보안 정책을 위반하는 행위, 즉 **침입(intrusion)**을 **실시간으로 탐지**하는 시스템

### IPS (Intrusion Prevention System)

침입탐지 시스템의 오판(False Positive)과 미탐(Miss Detection)의 문제 해결을 위해 등장한 정보 시스템으로, **네트워크에서의 침입탐지와 방어가 가능한 시스템**

---

## 정의 비교

| 구분 | 침입탐지시스템(IDS) | 침입방지시스템(IPS) |
|:-----|:-----------------|:-----------------|
| **정의** | 비인가된 사용자가 자원의 무결성(integrity), 기밀성(confidentiality), 가용성(availability)을 저해하는 일련의 행동들과 보안 정책을 위반하는 행위, 즉 침입(intrusion)을 실시간으로 탐지하는 시스템 | 침입탐지 시스템의 오판(False Positive)과 미탐(Miss Detection)의 문제 해결을 위해 등장한 정보 시스템<br>- 네트워크에서의 침입탐지와 방어가 가능한 시스템 |

---

## 개념도

### IDS 개념도

```
                 ① 내부망 침입
    인터넷 ───────────────────▶ Firewall ──────────▶ 내부망
                                    │
                               ② Mirroring
                                    │
                                    ▼
                    IDS ◀─────── Switch
                    │
                ③ 침입 탐지
                    │
                ④ Event Alarm
                    │
                    ▼
              Management
                Server
```

**특징**: Positive, Reactive 탐지 / 선 패턴 등록 후 반응

### IPS 개념도

```
                 ① 내부망 침입
    인터넷 ───────────────────▶ Firewall ──────────▶ 내부망
                                    │
                               ② 침입 차단
                                    │
                                    ▼
                                  IPS
                                    │
                            ④ Event Alarm
                                    │
                                    ▼
                              Management
                                Server ──────▶ Switch
```

**특징**: Active, Proactive 대응 / 공격전 사전 차단

---

## IDS와 IPS의 탐지/차단 측면 개념 비교

| 구분 | 침입탐지시스템(IDS) | 침입방지시스템(IPS) |
|:-----|:-----------------|:-----------------|
| **목적** | 침입 여부 탐지 | 침입탐지, 탐지 후 적극적 대응 |
| **분석방법** | 시그니처 DB기반 패턴 매칭방법<br>알려진 공격패턴 감지(CVE) | Rule DB 기반<br>비정상 행위 방지(머지도 학습) |
| **패킷공격<br>Zero-Day Attack** | 첫번째 패킷 공격의 방어 어려움 | 공격 방지 가능 |
| **차단방법** | Reset Signal, 방화벽 연동 | 자체 차단 |
| **One-Way Attack** | 탐지 | 탐지/차단 |
| **DDoS, DoS차단** | 탐지 | 탐지/차단 |
| **Worm Virus** | 탐지 | 탐지/차단 |
| **Ransomware** | 탐지 | 탐지/차단 |
| **암호화 트래픽** | 암호화 트래픽 분석 제한<br>복호화 트래픽 장비 연동 | 암호화 트래픽 분석 가능<br>사설 인증서 적용 |

---

## IDS와 IPS의 구축/운영 측면 개념 비교

| 구분 | 침입탐지시스템(IDS) | 침입방지시스템(IPS) |
|:-----|:-----------------|:-----------------|
| **연결 방법** | Mirroring<br>Out of Path | In-Line<br>TAP(Test Access Point) |
| **설치 위치** | 코어 네트워크 스위치 | 관문 방화벽 상/하단 |
| **서비스 전환** | IDS Monitoring 및 트래픽 학습<br>오탐 패턴 탐지 예외 | IDS Mode Monitoring<br>오탐 패턴 차단 예외 |
| **대응 방법** | 관리자에게 경고<br>통합보안관리시스템을 통해 방화벽 Rule변경 | 알려지지 않은 공격 탐지<br>자원 접근 차단 |
| **서비스 중단 시<br>장애극복** | 서비스 영향 없음 | FoD(Fail over Device)를 통한 장애대응<br>Bypass Mode |
| **시스템 부하** | 시스템 부하 영향 없음 | 트래픽 처리 지연 발생 |
| **장점** | 모든 패킷에 대해 자체 탐지 모듈 지원으로 네트워크 이상 경고<br>방화벽과 연동 방어를 통한 차단 기능(독립적 제한적) | 모든 패킷에 대해 자체 탐지 및 차단 모듈을 지원으로 네트워크 보호<br>Transparent mode로 운영되며 NAT등 방화벽 고유 기능지원 불가 |
| **단점** | 방화벽과 연동 방어를 통한 차단 기능(독립적 제한적) | 방화벽 고유 기능지원 불가 |

- IDS는 탐지, IPS는 차단 기능을 제공하며 방화벽과 유사한 기능을 제공하나 차이점 존재

---

## 탐지 방식 비교

| 탐지 방식 | IDS | IPS |
|:---------|:----|:----|
| **시그니처 기반** | ✅ | ✅ |
| **이상탐지 기반** | ✅ | ✅ |
| **행위 기반** | ⭕ | ✅ |
| **AI/ML 기반** | ⭕ | ✅ |

---

## 오탐/미탐 유형

| 유형 | 설명 |
|:-----|:-----|
| **True Positive (TP)** | 실제 공격을 공격으로 탐지 (정상) |
| **True Negative (TN)** | 정상을 정상으로 판단 (정상) |
| **False Positive (FP)** | 정상을 공격으로 탐지 (오탐) |
| **False Negative (FN)** | 실제 공격을 정상으로 판단 (미탐) |

---

## 연계 토픽

- [방화벽](/docs/sec/16-network-security/)
- [XDR](/docs/sec/12-security-solution/xdr)
- [SIEM](/docs/sec/12-security-solution/)
- [사이버 디셉션](/docs/sec/12-security-solution/cyber-deception)

---

## 학습 체크리스트

- [ ] IDS와 IPS의 정의 및 차이점 이해
- [ ] 탐지/차단 측면 비교 항목 파악
- [ ] 구축/운영 측면 비교 항목 파악
- [ ] 오탐/미탐 유형 구분

---

## 참고자료

- 정보관리기술사 보안 학습자료


