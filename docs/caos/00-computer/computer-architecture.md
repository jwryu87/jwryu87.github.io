---
layout: default
title: Computer Architecture
parent: 0. Computer
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 2
---

# Computer Architecture
{: .fs-8 }

0. 기본 개념
{: .label .label-purple }

---

## 핵심 키워드

`ISA` `마이크로 아키텍처` `시스템 디자인` `폰노이만` `하버드` `CISC` `RISC`

---

## 정의/개념

**컴퓨터 아키텍처(Computer Architecture)**는 컴퓨터 시스템의 성능, 효율성, 확장성 등을 결정하는 중요한 요소로 **컴퓨터를 설계하고 구축**하는 데 필요한 **기본 원칙과 지침**입니다.

---

## 컴퓨터 아키텍처의 구성요소

| 구성요소 | 설명 |
|:--------|:-----|
| **명령어 집합 아키텍처 (ISA)** | Instruction Set Architecture - 컴퓨터가 실행할 수 있는 명령어들의 종류와 형식, 그리고 각 명령어가 어떻게 동작하는지를 정의함 |
| **마이크로아키텍처** | Microarchitecture - 컴퓨터 시스템 내부의 세부적인 구성 요소들(CPU, 메모리, 입출력 장치 등)과 이들 간의 데이터 흐름, 제어 방식 등을 정의함 |
| **시스템 디자인** | System Design - 여러 개의 프로세서, 메모리, 입출력 장치 등을 포함하는 복잡한 컴퓨터 시스템의 전체적인 구조와 상호 연결 방식을 정의함 |

---

## 컴퓨터 아키텍처의 분류

### 폰 노이만 vs 하버드 아키텍처

| 구분 | 폰 노이만 아키텍처 | 하버드 아키텍처 |
|:-----|:------------------|:---------------|
| **메모리 구조** | 프로그램과 데이터를 같은 메모리 공간에 저장 | 프로그램과 데이터를 별도의 메모리 공간에 저장 |
| **적용 분야** | 대부분의 현대 컴퓨터 | 임베디드 시스템, DSP(Digital Signal Processor) 등 특수 목적 컴퓨터 |
| **장점** | 구조 단순, 범용성 | 병렬 처리, 보안성 |
| **단점** | 병목 현상 | 하드웨어 복잡 |

### CISC vs RISC

| 구분 | CISC | RISC |
|:-----|:-----|:-----|
| **정의** | Complex Instruction Set Computer | Reduced Instruction Set Computer |
| **특징** | 복잡하고 다양한 명령어들을 제공 | 간단하고 핵심적인 명령어들만 제공 |
| **예시** | x86 | ARM |
| **명령어** | 다양하고 복잡 | 단순하고 고정 길이 |
| **사이클** | 명령어당 여러 사이클 | 명령어당 단일 사이클 |

### 병렬처리 아키텍처

| 구분 | 설명 |
|:-----|:-----|
| **SIMD** | Single Instruction Multiple Data - 하나의 명령어로 여러 데이터를 동시에 처리 (예: 벡터 연산, 이미지 처리) |
| **MIMD** | Multiple Instruction Multiple Data - 여러 개의 프로세서가 각각 다른 명령어를 실행하여 여러 데이터를 동시에 처리 (예: 슈퍼컴퓨터, 대규모 서버 시스템) |

---

## 연계 토픽

- [Computer](/docs/caos/00-computer/computer)
- [하버드/폰노이만 아키텍처](/docs/caos/13-cpu-gpu/harvard-von-neumann)
- [CPU, GPU, FPGA, ASIC](/docs/caos/13-cpu-gpu/cpu-gpu-fpga-asic)

---

## 학습 체크리스트

- [ ] ISA, 마이크로아키텍처, 시스템 디자인 이해
- [ ] 폰 노이만 vs 하버드 아키텍처 비교
- [ ] CISC vs RISC 비교
- [ ] SIMD vs MIMD 이해

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

