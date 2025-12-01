---
layout: default
title: 접근제어
parent: 3. 네트워크 기본
grand_parent: NW (네트워크)
nav_order: 2
---

# 접근제어
{: .fs-8 }

3.1 네트워크 기본
{: .label .label-purple }

---

## 핵심 키워드

`CSMA/CD` `CSMA/CA` `충돌 감지` `충돌 회피`

---

## 정의/개념

LAN에서 하나의 통신 회선을 여러 단말장치들이 원활하게 공유할 수 있도록 해주는 **통신 회선 접근 방식**

---

## CSMA/CD vs CSMA/CA 비교

| 구분 | CSMA/CD | CSMA/CA |
|:-----|:--------|:--------|
| **개념** | 송신 노드에서 회선에 전송한 신호의 충돌 감지(Collision Detection) 시 일정 시간 후 재전송하는 방식으로 회선을 제어하는 접근제어 기법 | 송신 노드에서 전송 전 매체의 유휴상태를 체크하여 충돌을 회피(Collision Avoidance)하는 방식으로 회선을 제어하는 접근제어 기법 |
| **특징** | 충돌 감지: Jamming 신호에 따른 Back-Off 처리<br>유선 환경에 적용 (IEEE 802.3 표준) | 충돌 회피: RTS/CTS Frame, SIFS/DIFS Wait<br>무선 환경에 적용 (IEEE 802.11 표준) |
| **용도** | LAN의 Ethernet | Wireless |
| **표준** | IEEE 802.3 | IEEE 802.11 |
| **토폴로지** | 버스형, 트리형 | 무선 |
| **원리** | 전송 후, 충돌을 감지하여 충돌 발생 시 일정시간 이후 재전송 | 전송 전, 사용을 확인하고 일정시간 대기한 후 전송/확인 |
| **장점** | 구현이 쉽고 가격이 저렴<br>한 장비가 고장나도 통신 영향 적음 | 충돌 패킷을 재전송 하는데 사용되는 대역폭 낭비를 줄임<br>회피를 통한 에러제어가 가능 |
| **단점** | 거리의 제약<br>통신량 증가 시 충돌 많아지는 문제 | 고속의 LAN에 적합하지 않음<br>매체 접근 속도가 느림<br>Station이 증가할수록 전송 효율이 떨어짐 |

---

## 동작 원리

### CSMA/CD 동작
```
     송신 대기
         |
         v
    +----------+
    | 회선확인 |
    +----------+
         |
    Busy |     Idle
         v         v
   Back-Off     송신
     Wait         |
         |     충돌?
         v    Yes |  No
    Retry <---+    v
              Jamming    송신 완료
              Signal
```

### CSMA/CA 동작
```
     송신 대기
         |
         v
    +----------+
    | 회선확인 |
    +----------+
         |
    Busy |     Idle
         v         v
    IFS Wait    송신
         |         |
         v         v
    회선확인    ACK?
    Idle |    Yes |  No
         v         v    v
    Back-Off   송신   Back-Off
      Wait     완료     Wait
         |              |
         v              v
       송신          Retry
```

{: .note }
> 물리적으로 공유하는 회선이나 매체에서 충돌을 감지 또는 회피하여 안정적으로 프레임을 전송

---

## 연계 토픽

- [회선제어](/docs/nw/03-fundamentals/line-control)
- [다원접속·다중접속](/docs/nw/03-fundamentals/multiple-access)

---

## 학습 체크리스트

- [ ] CSMA/CD와 CSMA/CA 차이 이해
- [ ] 각 방식의 적용 환경(유선/무선) 구분
- [ ] 동작 원리 및 장단점 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


