---
layout: default
title: 📝 기출문제
parent: SEC (정보보안)
has_children: true
nav_order: 99
permalink: /docs/sec/exam
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
#examTable td:nth-child(1),
#examTable td:nth-child(2),
#examTable td:nth-child(3),
#examTable td:nth-child(4),
#examTable th:nth-child(1),
#examTable th:nth-child(2),
#examTable th:nth-child(3),
#examTable th:nth-child(4) {
  width: 1%;
  white-space: nowrap;
  text-align: center;
  padding: 0.1rem 0.1rem;
  font-size: 0.7rem;
}
#examTable td:nth-child(5) {
  white-space: normal;
  min-width: 300px;
}
#examTable td:nth-child(6) {
  white-space: nowrap;
  width: 1%;
}
#examTable td:nth-child(7),
#examTable th:nth-child(7) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 180px;
  white-space: nowrap;
}

.completed { background-color: #d4edda !important; }

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
.filter-btn:hover { background: #e9ecef; }
.filter-btn.active {
  background: #0d6efd;
  color: white;
  border-color: #0d6efd;
}

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

#examTable a { color: #0d6efd; text-decoration: none; }
#examTable a:hover { text-decoration: underline; }

tr.has-page td:first-child::before { content: "✅ "; }
</style>

# SEC 기출문제
{: .fs-9 }

SEC(정보보안) 관련 기출문제 모음입니다. **검색, 정렬, 필터링**이 가능합니다.
{: .fs-6 .fw-300 }

---

## 🔍 빠른 필터

<div class="filter-buttons">
  <button class="filter-btn active" data-filter="all">전체</button>
  <button class="filter-btn" data-filter="1">1교시 (단답형)</button>
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
  <th>회차</th>
  <th>정/컴</th>
  <th>교시</th>
  <th>번호</th>
  <th>문제</th>
  <th>관련토픽</th>
  <th>암기법</th>
</tr>
</thead>
<tbody>
<!-- 137회 -->
<tr><td>137</td><td>관리</td><td>1</td><td>2</td><td><a href="/docs/sec/exam/137-1-2-artifact">디지털 포렌식에서 아트팩트(Artifact)를 설명하시오</a></td><td>디지털 포렌식</td><td><code>시응파메</code> <code>E-V-W-C</code></td></tr>
<tr><td>137</td><td>관리</td><td>1</td><td>4</td><td><a href="/docs/sec/exam/137-1-4-ciphertext-attack">암호문 공격(Ciphertext Attack)을 설명하시오</a></td><td>암호화 알고리즘</td><td><code>암알선선</code> <code>예탐대개</code></td></tr>
<tr><td>137</td><td>관리</td><td>1</td><td>6</td><td><a href="/docs/sec/exam/137-1-6-ai-governance">AI 거버넌스(Artificial Intelligence Governance)를 설명하시오</a></td><td>디지털윤리</td><td><code>가조프검</code> <code>사편규</code></td></tr>
<tr><td>137</td><td>관리</td><td>3</td><td>6</td><td>국가 망 보안체계(N2SF)에 대하여 개념, 적용 절차, 고려사항을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>4</td><td>1</td><td>BPFdoor 악성코드에 대하여 개념 및 기존 백도어와의 차이점, 위협 요소, 대응 방안을 설명하시오</td><td>APT</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>11</td><td><a href="/docs/sec/exam/137-1-11-ai-vulnerability">인공지능 시스템의 취약점</a></td><td>융합보안</td><td><code>PEIM</code> <code>적결탐쿼D</code></td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>12</td><td><a href="/docs/sec/exam/137-1-12-cloud-native-security">클라우드 네이티브 보안</a></td><td>클라우드 보안</td><td><code>4C</code> <code>동Dev제</code> <code>3R</code></td></tr>
<tr><td>137</td><td>컴시응</td><td>2</td><td>1</td><td>공공 마이데이터 활용 방안에 대하여 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>3</td><td>3</td><td>OPC UA에 대하여 등장배경, OPC와 비교, 활용분야를 설명하시오</td><td>산업제어시스템보안</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>3</td><td>5</td><td>샌드박스와 화이트박스의 목적, 적용 방법 및 예시를 설명하시오</td><td>Hacking</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>4</td><td>5</td><td>침입차단시스템(Firewall), IDS, IPS 및 VPN에 대하여 설명하시오</td><td>IDS/IPS</td><td>-</td></tr>

<!-- 136회 -->
<tr><td>136</td><td>관리</td><td>1</td><td>10</td><td><a href="/docs/sec/exam/136-1-10-safe-zone-comparison">개인정보 안심구역과 데이터안심구역 비교</a></td><td>디지털 발자국</td><td><code>법운목대이보</code></td></tr>
<tr><td>136</td><td>관리</td><td>1</td><td>11</td><td>CC(Common Criteria)</td><td>CC</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>1</td><td>12</td><td>타원곡선 암호(ECC)</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>2</td><td>6</td><td>TLS에 대하여 프로토콜 구조와 핸드셰이크 과정, TLS 1.2 취약점과 TLS 1.3 개선 사항을 설명하시오</td><td>SSL</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>4</td><td>4</td><td>공급망 보안을 설명하고, 제로트러스트 기반 공급망 보안 아키텍처를 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>4</td><td>5</td><td>OWASP LLM Top 10에 대하여 배경과 주요 특징, 주요 보안 위협, 대응방안을 설명하시오</td><td>OWASP</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>4</td><td>6</td><td>소프트웨어 보안 품질에 대하여 정의와 중요성, 자동화 기술과 도구, 구현방안, 기대효과를 설명하시오</td><td>시큐어 코딩</td><td>-</td></tr>

<!-- 135회 -->
<tr><td>135</td><td>관리</td><td>1</td><td>5</td><td>SIEM & SOAR 비교</td><td>ESM</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>1</td><td>7</td><td>개인정보 안심구역</td><td>디지털 발자국</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>3</td><td>4</td><td>양자 암호 기술에 대하여 QKD, PQC, QKD와 PQC 비교를 설명하시오</td><td>양자암호화</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>3</td><td>6</td><td>딥페이크에 대하여 개념 및 핵심 기술, 문제점, 대응방안을 설명하시오</td><td>융합보안</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>4</td><td>6</td><td>경계 기반 보안과 제로 트러스트 성숙도모델 2.0 비교, 제로 트러스트 아키텍처 도입 시 고려사항을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>2</td><td>3</td><td>접근통제 정책(MAC, DAC, RBAC, ABAC)에 대하여 개념, 정책 비교, MAC+ABAC 융합 정책을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>3</td><td>3</td><td>제로트러스트 가이드라인 2.0에 대하여 정의 및 핵심 원칙, 구성요소, 성숙도 수준 4단계, 도입 절차를 설명하시오</td><td>보안모델</td><td>-</td></tr>

<!-- 134회 -->
<tr><td>134</td><td>관리</td><td>1</td><td>11</td><td>개인정보 보호 강화기술(PET)</td><td>PIA</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>2</td><td>다크패턴(Dark Pattern)의 세부 유형 및 대응 방안을 설명하시오</td><td>랜섬웨어</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>3</td><td>3</td><td>SBOM에 대하여 오픈소스 소프트웨어 취약점, SBOM 기반 관리 방안을 설명하시오</td><td>Hacking</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>2</td><td>제로데이(Zero Day) 취약점</td><td>Hacking</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>5</td><td>제로 트러스트(Zero Trust)</td><td>보안모델</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>6</td><td>동적 WEP 키(Dynamic WEP Key)</td><td>무선랜보안</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>7</td><td>SBOM(Software Bill of Materials)</td><td>Hacking</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>2</td><td>3</td><td>ISMS-P 간편인증에 대하여 목적, 대상, 기준을 설명하시오</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>2</td><td>4</td><td>스푸핑 공격에 대하여 개념, ARP/IP/DNS 스푸핑 공격 방법과 보안 대책을 설명하시오</td><td>ARP Spoofing</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>3</td><td>6</td><td>웹방화벽, IDS, IPS의 개념과 기능을 설명하시오</td><td>IDS/IPS</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>4</td><td>4</td><td>PET에 대하여 개념, 주요 유형, 적용 사례를 설명하시오</td><td>PIA</td><td>-</td></tr>

<!-- 133회 -->
<tr><td>133</td><td>관리</td><td>1</td><td>4</td><td>전자봉투 생성절차와 개봉절차를 설명하시오</td><td>PKI</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>1</td><td>5</td><td>동형암호의 동작원리와 유형을 설명하시오</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>1</td><td>10</td><td>딥페이크(Deepfake)에 대하여 설명하시오</td><td>융합보안</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>2</td><td>5</td><td>PbD(Privacy by Design)에 대하여 7대 원칙, 8대 전략, 개인정보보호법과의 비교를 설명하시오</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>3</td><td>1</td><td>안티포렌식에 대하여 배경 및 기술, 컴플라이언스 시스템의 구축 프로세스를 설명하시오</td><td>디지털 포렌식</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>4</td><td>3</td><td>접근제어에 대하여 개념과 정책, 절차, 구현 매커니즘을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>4</td><td>6</td><td>VPN에 대하여 개념 및 특징, IPSec VPN과 SSL VPN, 기술요소를 설명하시오</td><td>VPN</td><td>-</td></tr>

<!-- 132회 -->
<tr><td>132</td><td>관리</td><td>1</td><td>4</td><td>대칭 암호화와 비대칭 암호화</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>5</td><td>ISA/IEC 62443</td><td>산업제어시스템보안</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>6</td><td>큐싱(Qshing)</td><td>Phishing</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>8</td><td>TPM(Trusted Platform Module)</td><td>생체인식시스템</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>2</td><td>4</td><td>마이데이터 전송 보안 안내서에 대하여 보호책임자 지정, 접근 관리, 재해재난 대비 조치를 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>3</td><td>5</td><td>APEC CBPR에 대하여 프라이버시 9원칙, 주요 인증기준을 설명하시오</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>4</td><td>1</td><td>FIPS 140-2에 대하여 레벨 분류, 암호화 시스템 설계 시 고려사항, 보안 요소, 위협 대응 전략을 설명하시오</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>4</td><td>6</td><td>정보보안 체계 수립에 대하여 정책의 개념, 시점별 보안 활동, 전문가의 역할과 역량을 설명하시오</td><td>CPO</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>10</td><td>만리장성 모델(Chinese Wall Model, Brewer-Nash Model)</td><td>보안모델</td><td>-</td></tr>

<!-- 131회 -->
<tr><td>131</td><td>관리</td><td>1</td><td>10</td><td>크리덴셜 스터핑(Credential stuffing)</td><td>Hacking</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>1</td><td>13</td><td>SBOM(Software Bill of Material)</td><td>Hacking</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>2</td><td>3</td><td>인공지능 윤리와 거버넌스 모형에 대하여 설명하시오</td><td>디지털윤리</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>2</td><td>4</td><td>제로 트러스트 보안모델의 보안원리, 핵심원칙, 적용분야를 트러스트 보안 모델과 비교하여 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>3</td><td>6</td><td>ISMS와 ISMS-P에 대하여 차이점, ISMS 의무 대상 기준을 설명하시오</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>4</td><td>2</td><td>개인정보의 안전성 확보조치 기준에 대하여 내부관리계획 수립·이행, 암호화 적용방안을 설명하시오</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>12</td><td>CBPR(Cross Border Privacy Rule)</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>13</td><td>CSRF(Cross-Site Request Forgery)</td><td>OWASP</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>1</td><td>적대적 예제(Adversarial Example)에 대하여 White-box/Black-box 공격 비교, 방어기법을 설명하시오</td><td>융합보안</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>2</td><td>개인정보 비식별 처리에 대하여 유형, 위험 요인을 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>5</td><td>공공기관 정보화 사업 추진 시 국가정보원 보안성 검토 절차를 설명하시오</td><td>정보보호 인증제도</td><td>-</td></tr>

<!-- 130회 -->
<tr><td>130</td><td>정</td><td>1</td><td>6</td><td>블록 암호화 알고리즘</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>2</td><td>4</td><td>개인정보보호법 개정안에 대하여 주요 내용, 처리 흐름, 전송요구권과 자동화 의사결정 대응권을 설명하시오</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>2</td><td>5</td><td>메타버스 윤리원칙에 대하여 3대 지향가치와 8대 실천원칙, 윤리 비교를 설명하시오</td><td>디지털윤리</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>2</td><td>6</td><td>디지털 역기능에 대하여 개념과 사례, 3대 이슈, 대응방안을 설명하시오</td><td>디지털윤리</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>3</td><td>4</td><td>인공지능 보안 위협에 대하여 적대적 공격 4가지와 방어기법, 생성형 언어모델 보안취약점을 설명하시오</td><td>융합보안</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>4</td><td>2</td><td>디지털 포렌식에 대하여 개념, 유형과 절차, 기술 및 활용분야를 설명하시오</td><td>디지털 포렌식</td><td>-</td></tr>
<tr><td>130</td><td>정</td><td>4</td><td>3</td><td>클라우드 서비스 도입 시 고려해야 할 보안 요소를 설명하시오</td><td>클라우드 보안</td><td>-</td></tr>

<!-- 129회 -->
<tr><td>129</td><td>정</td><td>1</td><td>2</td><td>인공지능의 3대 기본원칙 및 10대 핵심요건</td><td>디지털윤리</td><td>-</td></tr>
<tr><td>129</td><td>정</td><td>1</td><td>11</td><td>정보보호 제품 신속 확인 제도</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>129</td><td>정</td><td>2</td><td>2</td><td>접근 제어의 통제정책과 LDAP의 인증흐름에 대하여 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>129</td><td>정</td><td>4</td><td>1</td><td>인포스틸러(InfoStealer) 개념과 공격 절차, 대응방안을 설명하시오</td><td>Hacking</td><td>-</td></tr>
<tr><td>129</td><td>컴</td><td>1</td><td>2</td><td>CSAP (Cloud Security Assurance Program)</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>129</td><td>컴</td><td>1</td><td>3</td><td>웹 애플리케이션 방화벽(WAF)</td><td>Firewall</td><td>-</td></tr>
<tr><td>129</td><td>컴</td><td>3</td><td>4</td><td>양자 컴퓨터에 대하여 Qubit, 양자 우월성, 양자 결잃음, 구현 방법을 설명하시오</td><td>양자암호화</td><td>-</td></tr>
<tr><td>129</td><td>컴</td><td>4</td><td>3</td><td>디스크 이미징에 대하여 용도, Disk to Disk와 Disk to File 방식, 증거수집 방법을 설명하시오</td><td>디지털 포렌식</td><td>-</td></tr>

<!-- 128회 -->
<tr><td>128</td><td>정</td><td>1</td><td>10</td><td>개인정보의 가명 익명처리 기술에 대하여 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>
<tr><td>128</td><td>정</td><td>1</td><td>12</td><td>랜섬웨어와 RaaS에 대하여 설명하시오</td><td>랜섬웨어</td><td>-</td></tr>
<tr><td>128</td><td>정</td><td>1</td><td>13</td><td>큐비트(Qubit)에 대하여 설명하시오</td><td>양자암호화</td><td>-</td></tr>
<tr><td>128</td><td>정</td><td>2</td><td>4</td><td>데이터 3법과 마이데이터사업에 대하여 개정 배경, 개념 및 제공정보 범위, 활성화 방안을 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>
<tr><td>128</td><td>정</td><td>4</td><td>4</td><td>양자암호통신에 대하여 암호키 분배방식, 주요기술, 취약점을 설명하시오</td><td>양자암호화</td><td>-</td></tr>
<tr><td>128</td><td>정</td><td>4</td><td>6</td><td>식별과 인증에 대하여 정의 및 차이점, 보안 요구사항, 인증 방식 4가지 유형을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>128</td><td>컴</td><td>1</td><td>6</td><td>DRM, DLP 비교</td><td>DRM</td><td>-</td></tr>
<tr><td>128</td><td>컴</td><td>1</td><td>12</td><td>디피-헬만 알고리즘(Diffie-Hellman Algorithm)</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>128</td><td>컴</td><td>2</td><td>4</td><td>융합보안관제에 대하여 필요성, 구축 시 고려사항과 활용기술, 시스템 구축요소를 설명하시오</td><td>ESM</td><td>-</td></tr>
<tr><td>128</td><td>컴</td><td>3</td><td>3</td><td>디지털 포렌식 증거 수집에 대하여 네트워크, 시스템, 응용 프로그램 증거 수집 방법을 설명하시오</td><td>디지털 포렌식</td><td>-</td></tr>

<!-- 127회 -->
<tr><td>127</td><td>정</td><td>1</td><td>5</td><td>메시지 인증 코드(Message Authentication Code)</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>127</td><td>정</td><td>1</td><td>9</td><td>변조(Modification)와 위조(Fabrication)</td><td>보안모델</td><td>-</td></tr>
<tr><td>127</td><td>정</td><td>2</td><td>5</td><td>개인정보 안전성 확보조치 기준에 명시된 내부관리계획에 대해 설명하시오</td><td>개인정보보호법</td><td>-</td></tr>
<tr><td>127</td><td>정</td><td>2</td><td>6</td><td>접근 통제 보안 모델에 대하여 벨 라파듈라, 비바, Clark and Wilson 모델을 설명하시오</td><td>보안모델</td><td>-</td></tr>
<tr><td>127</td><td>정</td><td>3</td><td>6</td><td>SOAR에 대하여 설명하시오</td><td>ESM</td><td>-</td></tr>
<tr><td>127</td><td>정</td><td>4</td><td>6</td><td>블록 암호 모드에 대하여 ECB, CBC, CFB, OFB 모드를 설명하시오</td><td>암호화 알고리즘</td><td>-</td></tr>

<!-- 126회 -->
<tr><td>126</td><td>정</td><td>1</td><td>13</td><td>파일슬랙(File Slack)</td><td>디지털 포렌식</td><td>-</td></tr>
<tr><td>126</td><td>정</td><td>4</td><td>4</td><td>VPN과 Tor에 대하여 설명하시오</td><td>세이프 네트워크</td><td>-</td></tr>
<tr><td>126</td><td>정</td><td>4</td><td>5</td><td>RSA 알고리즘과 DSA를 비교하여 설명하시오</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>126</td><td>정</td><td>4</td><td>6</td><td>파일 카빙에 대하여 개념, 4종류 기법의 특징을 설명하시오</td><td>디지털 포렌식</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>1</td><td>3</td><td>샌드박스의 주요 구성요소 및 활용분야</td><td>Hacking</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>1</td><td>6</td><td>ISMS-P</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>1</td><td>11</td><td>양자키분배(Quantum Key Distribution) 기술</td><td>양자암호화</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>2</td><td>4</td><td>스마트 팩토리의 보안위협과 보안 요구사항, 보안대책에 대하여 설명하시오</td><td>산업제어시스템보안</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>3</td><td>1</td><td>소프트웨어 개발 보안 가이드에 대하여 정의, 대상 범위, 보안기준 개념 및 보안대책을 설명하시오</td><td>시큐어 코딩</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>3</td><td>2</td><td>ISO/IEC 29100 프라이버시 11원칙과 ISO/IEC 27701에 대하여 설명하시오</td><td>정보보호 인증제도</td><td>-</td></tr>
<tr><td>126</td><td>컴</td><td>3</td><td>5</td><td>마이데이터 서비스에 대하여 절차, 인증 방식, 보안 문제점 및 개선 방안을 설명하시오</td><td>개인정보 비식별화</td><td>-</td></tr>

<!-- 125회 -->
<tr><td>125</td><td>정</td><td>1</td><td>1</td><td>SECaaS(Security as a Service)</td><td>클라우드 보안</td><td>-</td></tr>
<tr><td>125</td><td>정</td><td>1</td><td>2</td><td>동형암호(Homomorphic Encryption)</td><td>암호화 알고리즘</td><td>-</td></tr>
<tr><td>125</td><td>정</td><td>1</td><td>9</td><td>포스트 양자 암호(Post-Quantum Cryptography)</td><td>양자암호화</td><td>-</td></tr>
<tr><td>125</td><td>정</td><td>2</td><td>4</td><td>TOCTOU에 대하여 정의와 개념, 문제 상황과 보안대책, 코드 실행 시 문제점과 해결 방안을 설명하시오</td><td>시큐어 코딩</td><td>-</td></tr>
<tr><td>125</td><td>정</td><td>2</td><td>5</td><td>EMP공격에 대하여 정의와 구분, HEMP의 원리, 위협별 방호방안을 설명하시오</td><td>부채널 공격</td><td>-</td></tr>
<tr><td>125</td><td>정</td><td>4</td><td>6</td><td>산업제어시스템의 퍼듀 모델에 대하여 개념, 계층과 계층별 특징을 설명하시오</td><td>산업제어시스템보안</td><td>-</td></tr>
<tr><td>125</td><td>컴</td><td>1</td><td>13</td><td>디바이스 DNA</td><td>PKI</td><td>-</td></tr>
<tr><td>125</td><td>컴</td><td>2</td><td>1</td><td>망분리시스템에 대하여 개념 및 원칙, 구축 유형 비교, 장단점을 설명하시오</td><td>망분리</td><td>-</td></tr>
<tr><td>125</td><td>컴</td><td>2</td><td>6</td><td>DDoS 공격에 대하여 공격기법 개념, 공격기법, 보안 대책을 설명하시오</td><td>DDOS</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "암호화", "포렌식", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링
- **1교시형 모아보기**: "1교시 (단답형)" 버튼 클릭

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 11개 |
| 136회 | 7개 |
| 135회 | 7개 |
| 134회 | 11개 |
| 133회 | 7개 |
| 132회 | 9개 |
| 131회 | 11개 |
| 130회 | 7개 |
| 129회 | 8개 |
| 128회 | 10개 |
| 127회 | 6개 |
| 126회 | 11개 |
| 125회 | 9개 |
| **합계** | **114개** |

---

<!-- jQuery & DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    var table = $('#examTable').DataTable({
        pageLength: 50,
        lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "전체"]],
        order: [[0, 'desc'], [2, 'asc'], [3, 'asc']],
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
            table.column(6).search('^(?!-$).*$', true, false).draw();
        } else {
            table.column(2).search('^' + filter + '$', true, false).draw();
        }
    });
});
</script>
