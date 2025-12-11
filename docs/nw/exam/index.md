---
layout: default
title: 📝 기출문제
parent: NW (네트워크)
has_children: true
nav_order: 99
permalink: /docs/nw/exam
---

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/searchpanes/2.2.0/css/searchPanes.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/select/1.7.0/css/select.dataTables.min.css">

<style>
/* 페이지 전체 너비 확장 */
.main-content {
  max-width: 100% !important;
}
.main-content-wrap {
  max-width: 100% !important;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* 테이블 스타일 */
#examTable {
  width: 100% !important;
  font-size: 0.85rem;
}
#examTable th {
  background-color: #f8f9fa;
  white-space: nowrap;
  text-align: center;
}
#examTable td {
  vertical-align: middle;
}
/* 1열: 문제 (넓게) */
#examTable td:nth-child(1),
#examTable th:nth-child(1) {
  white-space: normal;
  min-width: 300px;
}
/* 2열: 암기법 (모노스페이스, 붉은 글씨) */
#examTable td:nth-child(2),
#examTable th:nth-child(2) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 150px;
}
/* 3-6열: 회차, 정/컴, 교시, 번호 (아주 좁게, 중앙정렬) */
#examTable td:nth-child(3),
#examTable td:nth-child(4),
#examTable td:nth-child(5),
#examTable td:nth-child(6),
#examTable th:nth-child(3),
#examTable th:nth-child(4),
#examTable th:nth-child(5),
#examTable th:nth-child(6) {
  width: 1%;
  white-space: nowrap;
  text-align: center;
  padding: 0.05rem 0.15rem;
  font-size: 0.7rem;
}
/* 7열: 관련토픽 (아주 좁게) */
#examTable td:nth-child(7),
#examTable th:nth-child(7) {
  white-space: nowrap;
  width: 1%;
  font-size: 0.7rem;
  padding: 0.05rem 0.15rem;
}

/* 학습완료 행 스타일 */
.completed {
  background-color: #d4edda !important;
}

/* 필터 버튼 스타일 */
.filter-buttons {
  margin-bottom: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.filter-btn {
  padding: 0.4rem 0.8rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  background: #fff;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}
.filter-btn:hover {
  background: #e9ecef;
}
.filter-btn.active {
  background: #0d6efd;
  color: white;
  border-color: #0d6efd;
}

/* DataTables 커스텀 */
.dataTables_wrapper .dataTables_filter input {
  padding: 0.5rem 1rem;
  border: 2px solid #dee2e6;
  border-radius: 20px;
  font-size: 0.9rem;
  width: 250px;
}
.dataTables_wrapper .dataTables_filter input:focus {
  border-color: #0d6efd;
  outline: none;
}
.dataTables_wrapper .dataTables_length select {
  padding: 0.3rem;
  border-radius: 4px;
}

/* 링크 스타일 */
#examTable a {
  color: #0d6efd;
  text-decoration: none;
}
#examTable a:hover {
  text-decoration: underline;
}

/* 학습 페이지 있는 행 표시 */
/* tr.has-page td:first-child::before {
  content: ""; */
}
</style>

# NW 기출문제
{: .fs-9 }

NW(네트워크) 관련 기출문제 모음입니다. **검색, 정렬, 필터링**이 가능합니다.
{: .fs-6 .fw-300 }

---

## 🔍 빠른 필터

<div class="filter-buttons">
  <button class="filter-btn active" data-filter="all">전체</button>
  <button class="filter-btn" data-filter="1">1교시 (단답형)</button>
  <button class="filter-btn" data-filter="essay">서술형 (2~4교시)</button>
  <button class="filter-btn" data-filter="2">2교시</button>
  <button class="filter-btn" data-filter="3">3교시</button>
  <button class="filter-btn" data-filter="4">4교시</button>
  <button class="filter-btn" data-filter="has-page">📄 학습페이지 있음</button>
  <button class="filter-btn" data-filter="has-mnemonic">🧠 암기법 있음</button>
</div>

---

## 📋 기출문제 목록

<table id="examTable" class="display compact">
<thead>
<tr>
  <th>문제</th>
  <th>암기법</th>
  <th>회차</th>
  <th>정/컴</th>
  <th>교시</th>
  <th>번호</th>
  <th>관련토픽</th>
</tr>
</thead>
<tbody>
<!-- 137회 -->
<tr class="has-page"><td><a href="/docs/nw/exam/137-1-1-igp-egp">동적 라우팅 프로토콜인 IGP와 EGP를 설명하시오</a></td><td><code>RIP-OSPF-EIGRP</code> <code>BGP</code></td><td>137</td><td>관리</td><td>1</td><td>1</td><td>라우팅 프로토콜</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/137-3-5-communication-protocol">통신 프로토콜에 대하여 설명하시오 (오류제어, 혼잡제어, 슬라이딩윈도우, 설계시 고려사항)</a></td><td><code>(오류제어) FB</code> <code>(혼잡제어) SCFR</code> <code>(고려사항) 호안성효</code></td><td>137</td><td>관리</td><td>3</td><td>5</td><td>OSI 7 Layer</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/137-4-4-dns">DNS(Domain Name System) 개요, 구성요소, 보안 취약점 및 대응 방안</a></td><td><code>도리존네리</code> <code>DNSSEC</code></td><td>137</td><td>컴시응</td><td>4</td><td>4</td><td>DNS</td></tr>

<!-- 136회 -->

<!-- 135회 -->
<tr class="has-page"><td><a href="/docs/nw/exam/135-1-4-ibn">IBN(Intent-Based Networking)</a></td><td><code>5N</code> <code>명번적모검</code> <code>NLES</code> <code>모VFC</code></td><td>✅ 135</td><td>관리</td><td>1</td><td>4</td><td>SDN</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/135-1-10-ieee-802-11bn">IEEE 802.11bn (Wi-Fi 8)</a></td><td><code>(특징) 적연전</code> <code>(PHY) DRU-UM-MCS</code> <code>(MAC) SR-MAC-NPCA-DPS</code></td><td>✅ 135</td><td>관리</td><td>1</td><td>10</td><td>차세대무선랜</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/135-2-4-6g">6G이동통신기술 서비스 특징, 성능 요구사항, 주파수 동향</a></td><td><code>지에프신</code> <code>초6</code></td><td>135</td><td>관리</td><td>2</td><td>4</td><td>6G 이동통신기술</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/135-1-7-shannon-capacity">채널용량(샤논 제3정리, Information Capacity Theorem)</a></td><td><code>C=Blog₂(1+S/N)</code> <code>CBSN</code></td><td>✅ 135</td><td>컴시응</td><td>1</td><td>7</td><td>전송기술</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/135-1-13-zsm">ETSI의 Zero-touch network and Service Management(ZSM)</a></td><td><code>(구성요소) 완E2AI</code> <code>(원칙) OICA</code> <code>(핵심기술) DNI</code></td><td>✅ 135</td><td>컴시응</td><td>1</td><td>13</td><td>SDN</td></tr>
<tr class="has-page"><td><a href="/docs/nw/exam/135-2-5-traffic-policing-shaping">트래픽 폴리싱과 트래픽 쉐이핑에 대하여 설명하시오</a></td><td><code>MMD</code> <code>CCEE</code> <code>LTH</code></td><td>135</td><td>컴시응</td><td>2</td><td>5</td><td>OSI 7 Layer</td></tr>
<tr><td>서버 이중화 구성 방안에 대하여 설명하시오. 가. L4스위치 기반 나. 소프트웨어 기반 다. 비교</td><td>-</td><td>135</td><td>컴시응</td><td>4</td><td>3</td><td>Internetworking</td></tr>

<!-- 134회 -->
<tr><td>RIP와 OSPF 비교</td><td>-</td><td>134</td><td>관리</td><td>1</td><td>8</td><td>라우팅 프로토콜</td></tr>
<tr><td>Wi-Fi 7</td><td>-</td><td>134</td><td>컴시응</td><td>1</td><td>1</td><td>차세대무선랜</td></tr>
<tr><td>PoE(Power of Ethernet)에 관하여 설명하시오. 가. 개념 나. IEEE 표준 다. 국내 기술기준</td><td>-</td><td>134</td><td>컴시응</td><td>2</td><td>1</td><td>PoE</td></tr>
<tr><td>OSI 7 계층에 대하여 계층별 기능, 프로토콜 종류, 데이터 종류, 주요 장비를 설명하시오</td><td>-</td><td>134</td><td>컴시응</td><td>2</td><td>6</td><td>OSI 7 Layer</td></tr>
<tr><td>디지털 계위에 관하여 PDH, SDH, SONET을 설명하시오</td><td>-</td><td>134</td><td>컴시응</td><td>3</td><td>3</td><td>전송기술</td></tr>
<tr><td>네트워크 프로토콜에 대하여 개념, 3가지 요소, 기능을 설명하시오</td><td>-</td><td>134</td><td>컴시응</td><td>3</td><td>5</td><td>Internetworking</td></tr>
<tr><td>HDLC 프로토콜의 기능, 프레임 구조, 동작모드를 설명하시오</td><td>-</td><td>134</td><td>컴시응</td><td>4</td><td>5</td><td>OSI 7 Layer</td></tr>

<!-- 133회 -->
<tr><td>TCP 프로토콜의 3-way handshake와 4-way handshake를 설명하시오</td><td>-</td><td>133</td><td>관리</td><td>1</td><td>13</td><td>TCP/IP</td></tr>
<tr><td>5G특화망을 위한 네트워크 구축 시 고려사항. 가. 안정성 및 신뢰성 확보 방안 나. 간섭회피 방안</td><td>-</td><td>133</td><td>관리</td><td>4</td><td>5</td><td>5G</td></tr>

<!-- 132회 -->
<tr><td>SCTP와 관련하여 개요와 특징, 프로토콜 구조 및 동작 방식을 설명하시오</td><td>-</td><td>132</td><td>관리</td><td>3</td><td>4</td><td>SCTP</td></tr>
<tr><td>전송 제어 프로토콜(TCP)의 4-way handshake</td><td>-</td><td>132</td><td>컴시응</td><td>1</td><td>5</td><td>TCP/IP</td></tr>
<tr><td>네트워크 실시간 측위(NRTK)</td><td>-</td><td>132</td><td>컴시응</td><td>1</td><td>9</td><td>위치 측위 기술</td></tr>
<tr><td>ICMP와 IGMP를 비교하여 설명하시오</td><td>-</td><td>132</td><td>컴시응</td><td>2</td><td>3</td><td>OSI 7 Layer</td></tr>
<tr><td>Open RAN에 대하여 개념, 구성요소, RAN과 비교를 설명하시오</td><td>-</td><td>132</td><td>컴시응</td><td>2</td><td>6</td><td>5G</td></tr>
<tr><td>맨체스터 코딩에 대하여 개념, 인코딩/디코딩, 차등 맨체스터 코딩과 비교를 설명하시오</td><td>-</td><td>132</td><td>컴시응</td><td>3</td><td>3</td><td>OSI 7 Layer</td></tr>
<tr><td>모바일 엣지 컴퓨팅에 대하여 개념, 플랫폼 구조 및 구성요소, 5G 적용 방안을 설명하시오</td><td>-</td><td>132</td><td>컴시응</td><td>4</td><td>6</td><td>5G</td></tr>

<!-- 131회 -->
<tr><td>소켓 통신과 관련하여 정의, 개념도 및 유형, TCP 소켓 및 Web 소켓 흐름, HTTP 통신 방식과 비교를 설명하시오</td><td>-</td><td>131</td><td>관리</td><td>2</td><td>5</td><td>TCP/IP</td></tr>
<tr><td>네트워크 인프라에 SDN을 이용하여 머신러닝 기법을 적용하는 이유와 강화학습 적용방안을 설명하시오</td><td>-</td><td>131</td><td>컴시응</td><td>2</td><td>4</td><td>SDN</td></tr>

<!-- 130회 -->
<tr><td>6G 이동통신</td><td>-</td><td>130</td><td>정</td><td>1</td><td>7</td><td>6G 이동통신기술</td></tr>
<tr><td>VXLAN(Virtual eXtensible LAN)</td><td>-</td><td>130</td><td>정</td><td>1</td><td>8</td><td>VLAN</td></tr>
<tr><td>네트워크 서브네팅과 관련하여 수퍼네팅/서브네팅 개념, 서브넷 분할 절차를 설명하시오</td><td>-</td><td>130</td><td>정</td><td>2</td><td>3</td><td>TCP/IP</td></tr>
<tr><td>TCP 혼잡제어 메커니즘의 구성요소, 혼잡상황 감지, 혼잡상황 제어, 혼잡 윈도우 크기를 설명하시오</td><td>-</td><td>130</td><td>정</td><td>3</td><td>3</td><td>OSI 7 Layer</td></tr>

<!-- 129회 -->
<tr><td>비직교 다중접속(NOMA)</td><td>-</td><td>129</td><td>정</td><td>1</td><td>12</td><td>5G</td></tr>
<tr><td>전송 부호화 기법의 소스코딩과 채널코딩을 비교하여 설명하시오</td><td>-</td><td>129</td><td>컴</td><td>1</td><td>8</td><td>OSI 7 Layer</td></tr>
<tr><td>네트워크 스위치와 관련하여 개요, OSI 레이어에 따른 스위치 유형, L4/L7 스위치 비교를 설명하시오</td><td>-</td><td>129</td><td>컴</td><td>3</td><td>2</td><td>Internetworking</td></tr>
<tr><td>이더넷 표준에 대하여 정의 및 특징, IEEE 802.3 프레임 구조, 최소 크기가 64바이트인 이유를 설명하시오</td><td>-</td><td>129</td><td>컴</td><td>3</td><td>5</td><td>Internetworking</td></tr>
<tr><td>TCP, UDP, SCTP에 대하여 설명하시오</td><td>-</td><td>129</td><td>컴</td><td>4</td><td>1</td><td>SCTP</td></tr>
<tr><td>Ad-hoc 라우팅 프로토콜에 대하여 개요, 유형, AODV를 설명하시오</td><td>-</td><td>129</td><td>컴</td><td>4</td><td>2</td><td>Ad hoc 네트워크</td></tr>

<!-- 128회 -->
<tr><td>6G 이동통신을 위한 위성-상공-지상 통합형 무선 네트워크(SATIN)를 설명하시오</td><td>-</td><td>128</td><td>정</td><td>4</td><td>3</td><td>6G 이동통신기술</td></tr>
<tr><td>네트워크에서 IP 주소, MAC 주소, Port 주소, 전자메일 주소의 개념과 구조를 설명하시오</td><td>-</td><td>128</td><td>컴</td><td>2</td><td>1</td><td>OSI 7 Layer</td></tr>
<tr><td>계층구조의 통신 프로토콜 설계 시 오류 제어, 흐름 제어, 데이터 전달 방식을 설명하시오</td><td>-</td><td>128</td><td>컴</td><td>3</td><td>1</td><td>OSI 7 Layer</td></tr>
<tr><td>TCP에 대하여 헤더, 제어 플래그의 종류를 설명하시오</td><td>-</td><td>128</td><td>컴</td><td>3</td><td>2</td><td>TCP/IP</td></tr>
<tr><td>5G와 6G 이동통신에 대한 특징과 발전 동향을 설명하시오</td><td>-</td><td>128</td><td>컴</td><td>4</td><td>2</td><td>6G 이동통신기술</td></tr>

<!-- 127회 -->
<tr><td>SDN에 대하여 SDN 제어 평면의 개요 및 구조의 특징, 오픈플로우 프로토콜을 설명하시오</td><td>-</td><td>127</td><td>정</td><td>3</td><td>5</td><td>SDN</td></tr>

<!-- 126회 -->
<tr><td>빅 엔디언과 리틀 엔디언</td><td>-</td><td>126</td><td>정</td><td>1</td><td>11</td><td>오류제어 알고리즘</td></tr>
<tr><td>네트워크 스캐닝(Network Scanning)</td><td>-</td><td>126</td><td>정</td><td>1</td><td>12</td><td>Internetworking</td></tr>
<tr><td>FANET (Flying Ad-Hoc Network)</td><td>-</td><td>126</td><td>컴</td><td>1</td><td>1</td><td>Ad hoc 네트워크</td></tr>
<tr><td>5G 특화망에 대하여 5G 이동통신과 비교, 네트워크 슬라이싱 기술, 활용분야를 설명하시오</td><td>-</td><td>126</td><td>컴</td><td>2</td><td>6</td><td>5G</td></tr>
<tr><td>5G특화망 구축에 있어 MPLS-TP 및 IP-MPLS 기술 개념 및 비교, 백홀망 구축 방안을 설명하시오</td><td>-</td><td>126</td><td>컴</td><td>4</td><td>6</td><td>MPLS</td></tr>

<!-- 125회 -->
<tr><td>WFQ(Weighted Fair Queuing)</td><td>-</td><td>125</td><td>정</td><td>1</td><td>10</td><td>QoS</td></tr>
<tr><td>5G 특화망(지역 5G)</td><td>-</td><td>125</td><td>정</td><td>1</td><td>11</td><td>5G</td></tr>
<tr><td>SDR(Software Defined Radio)</td><td>-</td><td>125</td><td>정</td><td>1</td><td>12</td><td>SDR</td></tr>
<tr><td>QoS 방식인 DiffServ와 IntServ를 설명하시오</td><td>-</td><td>125</td><td>정</td><td>3</td><td>3</td><td>QoS</td></tr>
<tr><td>정보이론과 샤논의 정리에 대하여 설명하시오</td><td>-</td><td>125</td><td>정</td><td>4</td><td>2</td><td>전송기술</td></tr>
<tr><td>IEEE 802.11ax와 IEEE 802.11be 비교</td><td>-</td><td>125</td><td>컴</td><td>1</td><td>1</td><td>차세대무선랜</td></tr>
<tr><td>TCP wrapper</td><td>-</td><td>125</td><td>컴</td><td>1</td><td>9</td><td>TCP/IP</td></tr>
<tr><td>해밍코드에 대하여 구성, 정정과정 및 정정방법, 활용 사례를 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>2</td><td>2</td><td>오류제어 알고리즘</td></tr>
<tr><td>전송계층 흐름제어에 대하여 개념, 개념도, Sliding Windows와 Slow Start 비교를 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>3</td><td>1</td><td>OSI 7 Layer</td></tr>
<tr><td>TCP 전송계층 프로토콜에 대하여 개념, 3-way/4-way handshake, TCP와 UDP 비교를 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>3</td><td>2</td><td>TCP/IP</td></tr>
<tr><td>CSMA/CD 개념과 동작원리, I-Persistent, P-Persistent, Non-Persistent 경합 프로토콜을 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>4</td><td>1</td><td>CSMA/CD</td></tr>
<tr><td>단말 간 직접통신(D2D)의 운용 시나리오와 활용분야를 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>4</td><td>2</td><td>무선 Lan</td></tr>
<tr><td>데이터링크 계층 오류제어에 대하여 개념과 종류, FEC와 ARQ 비교, ARQ 방식 3가지를 설명하시오</td><td>-</td><td>125</td><td>컴</td><td>4</td><td>3</td><td>오류제어 알고리즘</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "TCP", "5G", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링
- **1교시형 모아보기**: "1교시 (단답형)" 버튼 클릭

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 3개 |
| 135회 | 7개 |
| 134회 | 7개 |
| 133회 | 2개 |
| 132회 | 7개 |
| 131회 | 2개 |
| 130회 | 4개 |
| 129회 | 6개 |
| 128회 | 5개 |
| 127회 | 1개 |
| 126회 | 5개 |
| 125회 | 13개 |
| **합계** | **62개** |

---

<!-- jQuery & DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    var table = $('#examTable').DataTable({
        pageLength: 50,
        lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "전체"]],
        order: [[2, 'desc'], [3, 'asc'], [4, 'asc'], [5, 'asc']],
        language: {
            search: "🔍 검색:",
            lengthMenu: "_MENU_ 개씩 보기",
            info: "총 _TOTAL_개 중 _START_ - _END_",
            infoEmpty: "데이터 없음",
            infoFiltered: "(전체 _MAX_개에서 필터됨)",
            paginate: { first: "처음", last: "마지막", next: "다음", previous: "이전" },
            zeroRecords: "일치하는 결과가 없습니다"
        },
        columnDefs: [
            { orderable: true, targets: [0,1,2,3,5,6] },
            { orderable: false, targets: [4] }
        ],
    });

    $('.filter-btn').click(function() {
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        var filter = $(this).data('filter');
        table.search('').columns().search('').draw();
        
        if (filter === 'all') {
            table.draw();
        } else if (filter === 'has-page') {
            $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
                return $(table.row(dataIndex).node()).hasClass('has-page');
            });
            table.draw();
            $.fn.dataTable.ext.search.pop();
        } else if (filter === 'has-mnemonic') {
            table.column(1).search('^(?!-$).*$', true, false).draw();
        } else if (filter === 'essay') {
            // 서술형 (2, 3, 4교시)
            table.column(4).search('^[234]$', true, false).draw();
        } else {
            table.column(4).search('^' + filter + '$', true, false).draw();
        }
    });
});
</script>
