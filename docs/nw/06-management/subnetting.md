---
layout: default
title: Supernetting·Subnetting
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 8
---

# Subnetting, Supernetting
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

### Subnetting
`IP 주소 비트 차용` `서브넷 마스크 생성` `네트워크 세그먼트` `서브넷 아이디` `호스트 아이디` `CIDR` `VLSM`

### Supernetting
`연속된 네트워크 병합` `서브넷 마스크 조정` `CIDR` `네트워크 집약`

---

## 정의/개념

- **Subnetting**: 하나 네트워크를 작은 서브 네트워크로 나누는 기법
- **Supernetting**: 연속된 서브 네트워크를 하나의 네트워크로 통합하는 기법

---

## Subnetting

| 항목 | 설명 |
|:-----|:-----|
| **Subnetting의 정의** | 하나 네트워크를 작은 서브 네트워크로 나누는 기법 |
| **Subnetting의 특징** | **Network ID**: 네트워크 ID 부분 확장, 네트워크 규모 축소<br>**Host ID**: Host ID 축소, 소속된 Host 수 감소<br>**Broadcast 감소**: Host 수 감소로 Broadcast Traffic 영향 감소 |

### Subnetting의 개념도

```
Default Subnet Mask: 1111111111111111111111110000000
                      └──── Network ID ────┘ └ Host ID ┘

Subnetting된 Subnet Mask: 111111111111111111111111110000000
                           └──── Network ID ────┘└──┘

서브넷마스크        255     255     255     192
```

{: .note }
> 할당된 네트워크 주소를 각 용도 및 필요에 따라 작은 규모로 나누어 사용 가능

---

## Supernetting

| 항목 | 설명 |
|:-----|:-----|
| **Supernetting의 정의** | 연속된 서브 네트워크를 하나의 네트워크로 통합하는 기법 |
| **Supernetting의 특징** | **Network ID**: 네트워크 ID 부분 축소, 네트워크 규모 확장<br>**Host ID**: Host ID 확장, 소속된 Host 수 증가<br>**라우팅 테이블**: 작은 네트워크 정보를 합쳐 큰 단위 네트워크로 통합 관리 가능 |

### Supernetting의 개념도

```
같은 비트마스크 사용 시 다른 네트워크로 구분되는 것

192  168   1    0      0 0 0 0 0 0 0 0
192  168   2    0
192  168   3    0      1 1 1 1 1 0 0 0
192  168   4    0          ↓
192  168   5    0
192  168   6    0          ↓
                     Supernetting된
                     Subnet Mask    255   255   248    0
                                                 ←──
```

{: .note }
> 작은 연속된 네트워크 통합을 통해 전송 또는 관리할 네트워크 정보의 양 감소 가능

---

## 연계 토픽

- [IPv4·IPv6](/docs/nw/07-osi-layer/ipv4-ipv6)
- [NAT](/docs/nw/03-fundamentals/nat)

---

## 학습 체크리스트

- [ ] Subnetting, Supernetting 개념 이해
- [ ] 서브넷 마스크 계산 방법 파악
- [ ] CIDR, VLSM 관계 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


