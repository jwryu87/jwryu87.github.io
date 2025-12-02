---
layout: default
title: 파이프라인
parent: 8. 파이프라인
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 1
---

# 파이프라인 (Pipeline)
{: .fs-8 }

8.1 파이프라인
{: .label .label-purple }

---

## 핵심 키워드

`IF` `ID` `EX` `MEM` `WB` `병렬 처리`

---

## 정의/개념

**파이프라인(Pipeline)**은 CPU 명령어 실행을 여러 단계로 나누어 **동시에 여러 명령어를 처리**하는 기법입니다.

---

## 파이프라인 단계 (5단계)

| 단계 | 약어 | 설명 |
|:-----|:-----|:-----|
| **명령어 인출** | IF (Instruction Fetch) | 메모리에서 명령어 가져오기 |
| **명령어 해독** | ID (Instruction Decode) | 명령어 분석 및 레지스터 읽기 |
| **실행** | EX (Execute) | ALU 연산 수행 |
| **메모리 접근** | MEM (Memory Access) | 메모리 읽기/쓰기 |
| **쓰기** | WB (Write Back) | 결과를 레지스터에 저장 |

---

## 파이프라인 성능

- **이상적 속도 향상**: 단계 수(k)배
- **실제**: 해저드로 인한 성능 저하

---

## 연계 토픽

- [파이프라인 해저드](/docs/caos/08-pipeline/pipeline-hazard)

---

## 학습 체크리스트

- [ ] 5단계 파이프라인 이해
- [ ] 각 단계 역할

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

