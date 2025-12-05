---
layout: default
title: 📝 기출문제
parent: DS (Digital Service)
has_children: true
nav_order: 99
permalink: /docs/ds/exam
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
/* 회차, 정/컴, 교시, 번호 컬럼 - 폭 최소화 */
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
  padding: 0.3rem 0.5rem;
}
/* 문제 컬럼 */
#examTable td:nth-child(5) {
  white-space: normal;
  min-width: 300px;
}
/* 관련토픽 컬럼 */
#examTable td:nth-child(6) {
  white-space: nowrap;
  width: 1%;
}
/* 암기법 컬럼 - 폭 넓게 */
#examTable td:nth-child(7),
#examTable th:nth-child(7) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 180px;
  white-space: nowrap;
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
tr.has-page td:first-child::before {
  content: "✅ ";
}
</style>

# DS 기출문제
{: .fs-9 }

DS(Digital Service) 관련 기출문제 모음입니다. **검색, 정렬, 필터링**이 가능합니다.
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
<tr class="has-page"><td>137</td><td>관리</td><td>1</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-1-1-streaming-protocol">멀티미디어 스트리밍 프로토콜의 종류</a></td><td>스트리밍기술</td><td>RT-P/CP/SP H-D-C-LL</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>1</td><td>3</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-1-3-modbus">MODBUS 프로토콜을 설명하시오</a></td><td>스마트 그리드</td><td>R-A-T-O C-D-I-H</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>1</td><td>9</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-1-9-ab-testing">A/B 테스팅을 설명하시오</a></td><td>모바일 마케팅</td><td>C-V-R-S C-C-A-R</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>4</td><td>3</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-4-3-kubernetes">쿠버네티스(Kubernetes) 가. 개념 및 특징 나. 주요 컴포넌트 다. HPA</a></td><td>도커</td><td>A-S-C-E P-K-K-C 클상배서</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>1</td><td>3</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-1-3-intelligent-edge-computing">지능형 엣지 컴퓨팅</a></td><td>클라우드 컴퓨팅</td><td>디게서네클 디전지클앱</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-3-1-cloud-service-types">클라우드 컴퓨팅 서비스 유형 가. IaaS 나. PaaS 다. SaaS 라. FaaS</a></td><td>XaaS</td><td>물확비유 개다소 타유 이서자</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>4</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-4-1-video-compression">영상압축기법 가. 무손실 나. 손실 다. 혼합</a></td><td>압축기술</td><td>R-H-A-L D-I-V-W J-J-M-H</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>4</td><td>2</td><td><a href="{{ site.baseurl }}/docs/ds/exam/137-4-2-aiaas">AIaaS(AI as a Service)</a></td><td>XaaS</td><td>응엑요클학 온복통API 기빌운업</td></tr>

<!-- 136회 -->
<tr class="has-page"><td>136</td><td>관리</td><td>1</td><td>9</td><td><a href="{{ site.baseurl }}/docs/ds/exam/136-1-9-serverless-computing">서버리스 컴퓨팅(Serverless Computing)</a></td><td>XaaS</td><td>S-W-A-R B-C-F-E</td></tr>

<!-- 135회 -->
<tr><td>135</td><td>관리</td><td>2</td><td>6</td><td>AI디지털교과서에 대하여 다음을 설명하시오. 가. 개념 및 특징 나. 플랫폼 구조 다. 기능 및 핵심 서비스</td><td>e-pub</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>3</td><td>3</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-3-3-multicloud">멀티클라우드(MultiCloud) 가. 개념 및 필요성 나. 시스템 요구사항 다. 주요 기술</a></td><td>클라우드 컴퓨팅</td><td>단벤페서 인서앱통개</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-1-1-intellectual-property-rights">지식재산권의 종류</a></td><td>지식재산권</td><td>특실디상 반영데컴</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>2</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-1-2-soap-rest">SOAP vs REST 비교</a></td><td>Open API</td><td>유기데보대캐페 R-S-W-U-W</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>6</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-1-6-multicloud">멀티클라우드(Multicloud)</a></td><td>클라우드 컴퓨팅</td><td>인서앱통 개CLI웹</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-2-2-smart-city">지속 가능한 스마트시티(Smart City)</a></td><td>스마트시티</td><td>주에교환인 데컴센드 재데표윤</td></tr>
<tr><td>135</td><td>컴시응</td><td>3</td><td>1</td><td>데이터처리의 효율성과 속도를 높이기 위한 엣지 컴퓨팅(Edge Computing)에 대하여 아래 사항을 설명하시오. 가. 클라우드 환경에서의 엣지 컴퓨팅 나. 엣지 컴퓨팅을 활용한 자율 주행 차량 아키텍처 다. 해양 자율이동체에서의 엣지 컴퓨터</td><td>클라우드 컴퓨팅</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>3</td><td>2</td><td>『안티드론 시스템 프레임워크(정보통신단체표준, TTAK,KO-10.1460)」에 대하여 아래 사항을 설명하시오. 가. 안티드론 시스템 참조구조 나. 기술적 조치 참조구조</td><td>드론</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>3</td><td>5</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-3-5-blockchain-network-types">블록체인(Blockchain)의 네트워크 종류와 차이점</a></td><td>블록체인</td><td>퍼프컨 관참거속익</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>4</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/135-4-1-cbdc">중앙은행 디지털 화폐(CBDC) 설계를 위한 고려사항</a></td><td>블록체인</td><td>아인접연 익이보이</td></tr>
<tr><td>135</td><td>컴시응</td><td>4</td><td>2</td><td>스마트시티 데이터 거버넌스(Smart City Data Governance)에 대하여 설명하시오</td><td>스마트시티</td><td>-</td></tr>

<!-- 134회 -->
<tr class="has-page"><td>134</td><td>관리</td><td>1</td><td>9</td><td><a href="{{ site.baseurl }}/docs/ds/exam/134-1-9-intermittent-computing">인터미턴트 컴퓨팅(Intermittent Computing)</a></td><td>IoT</td><td>에메인프 초에비비</td></tr>
<tr class="has-page"><td>134</td><td>관리</td><td>1</td><td>10</td><td><a href="{{ site.baseurl }}/docs/ds/exam/134-1-10-storage-virtualization">스토리지 가상화(Storage Virtualization) 유형별 특징</a></td><td>가상화</td><td>블파오 F-S-H</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>1</td><td>국가기관, 지방자치단체 및 공공기관이 안전하고 효율적으로 SaaS를 이용하기 위해 공공부문 SaaS 이용 가이드라인을 발표하였다. 가. 클라우드 서비스 위험 관리원칙 및 기준 나. 보안대책 수립 및 보안성 검토 다. 서비스 수준 협약</td><td>XaaS</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>4</td><td>대규모 AI 서비스를 위한 데이터센터 구축 기술에 대하여 설명하시오. 가. 저지연 기술과 스케일링 확보 기술 나. DCI(Data Center Interconnect) 기술</td><td>컨버지드 인프라</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>3</td><td>6</td><td>일부 오픈소스 라이선스가 개방형(예: MIT, BSD 등)에서 폐쇄형(예: SSPL, BSL 등)으로 변화하고 있다. 이러한 오픈소스 라이선스 정책 변경의 배경 및 소프트웨어 산업에 미치는 영향에 대하여 설명하시오</td><td>OSS</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>4</td><td>4</td><td>개방형 API(Open API)에 대하여 설명하시오. 가. 정의 및 특징 나. SOAP 및 REST 구성요소 다. 취약점 및 대응 방안</td><td>Open API</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>컴시응</td><td>1</td><td>4</td><td><a href="{{ site.baseurl }}/docs/ds/exam/134-1-4-tactile-internet">촉각 인터넷(Tactile Internet)</a></td><td>IoT</td><td>5G엣SDN 햅AR로AI</td></tr>
<tr class="has-page"><td>134</td><td>컴시응</td><td>1</td><td>10</td><td><a href="{{ site.baseurl }}/docs/ds/exam/134-1-10-cloud-service-safety">「클라우드 컴퓨팅 서비스 이용 기준 및 안전성 확보 고시」의 서비스 운영 분야 안전성 검토 항목</a></td><td>클라우드 컴퓨팅</td><td>자비실장계</td></tr>

<!-- 133회 -->
<tr class="has-page"><td>133</td><td>관리</td><td>1</td><td>1</td><td><a href="{{ site.baseurl }}/docs/ds/exam/133-1-1-rest-api">REST API(REpresentational State Transfer API)</a></td><td>Open API</td><td>자행표 클무캐유계코</td></tr>
<tr class="has-page"><td>133</td><td>관리</td><td>1</td><td>12</td><td><a href="{{ site.baseurl }}/docs/ds/exam/133-1-12-kubernetes">쿠버네티스(Kubernetes)</a></td><td>도커</td><td>A-S-C-E P-K-K-C</td></tr>
<tr><td>133</td><td>관리</td><td>2</td><td>2</td><td>'디지털 정부서비스 UI/UX 가이드라인'(2024.2, 행정안전부)에 대하여 설명하시오. 가. 목적 및 주요특징 나. 가이드라인의 구조(구성요소) 다. 적용대상 및 기준 라. 가이드라인의 활용방법</td><td>UI/UX</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>3</td><td>3</td><td>슈퍼앱에 대하여 다음을 설명하시오. 가. 슈퍼앱의 정의와 주요요소 나. 슈퍼앱과 멀티앱의 비교 다. 슈퍼앱상 구동 서비스 미니앱 라. 슈퍼앱의 사례와 전망 및 이슈사항</td><td>모바일 콘텐츠</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>4</td><td>1</td><td>다자간 계산(Multi-Party Computation; MPC)에 대하여 설명하시오. 가. MPC 개념, 원리, 특징 나. MPC 기술 종류 다. MPC 기반 인증서비스</td><td>블록체인</td><td>-</td></tr>

<!-- 132회 -->
<tr class="has-page"><td>132</td><td>관리</td><td>1</td><td>12</td><td><a href="{{ site.baseurl }}/docs/ds/exam/132-1-12-storage-types">블록스토리지, 파일스토리지, 오브젝트스토리지 데이터 접근방식</a></td><td>오픈스택 프로젝트</td><td>블파오 FC-SMB-HTTP</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>3</td><td>2</td><td><a href="{{ site.baseurl }}/docs/ds/exam/132-3-2-cloud-management-platform">클라우드 관리 플랫폼의 정의 및 필요성, 필수기능, 선정기준, 기대효과</a></td><td>클라우드 컴퓨팅</td><td>정필선기 인운인클자인 표자거워지</td></tr>
<tr class="has-page"><td>132</td><td>컴시응</td><td>1</td><td>8</td><td><a href="{{ site.baseurl }}/docs/ds/exam/132-1-8-digital-literacy">디지털 리터러시(Digital Literacy)</a></td><td>디지털 리터러시</td><td>연비창디의기 윤능적</td></tr>
<tr class="has-page"><td>132</td><td>컴시응</td><td>1</td><td>12</td><td><a href="{{ site.baseurl }}/docs/ds/exam/132-1-12-zero-knowledge-proof">영지식 증명(Zero Knowledge Proof)</a></td><td>블록체인</td><td>완건영 SNARK-STARK</td></tr>
<tr class="has-page"><td>132</td><td>컴시응</td><td>1</td><td>13</td><td><a href="{{ site.baseurl }}/docs/ds/exam/132-1-13-super-app">슈퍼앱(Super APP)</a></td><td>모바일 콘텐츠</td><td>검금주OTT F-B-D-A-C</td></tr>
<tr><td>132</td><td>컴시응</td><td>2</td><td>2</td><td>사물인터넷은 일상생활에서 AI와 융합되어 지능형 IoT로 진화하고 있다. 가. AIoT 개념 나. AIoT의 보안 취약점 다. AIoT 디바이스 보안기술 3가지</td><td>IoT</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>3</td><td>1</td><td>앰비언트 컴퓨팅(Ambient Computing)에 대하여 설명하시오. 가. 앰비언트 컴퓨팅의 개념 나. 개념도 및 기술요소 다. 앰비언트 컴퓨팅과 IoT 비교</td><td>핀테크</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>3</td><td>2</td><td>가상머신(Virtual Machine)과 컨테이너(Container)에 대하여 구체적으로 설명하고, 공통점과 차이점을 상세히 설명하시오</td><td>가상화</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>4</td><td>3</td><td>디지털 트윈 기술을 이용한 제조에 대하여 설명하시오. 가. 제조를 위한 디지털 트윈 기술 개념 나. 제조 디지털 트윈 프레임워크 다. 액터 정보 테이블의 항목 및 항목값</td><td>인더스트리 4.0</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "쿠버네티스", "블록체인", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링
- **1교시형 모아보기**: "1교시 (단답형)" 버튼 클릭

---

<!-- jQuery & DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    // DataTables 초기화
    var table = $('#examTable').DataTable({
        pageLength: 50,
        lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "전체"]],
        order: [[0, 'desc'], [2, 'asc'], [3, 'asc']], // 회차 내림차순, 교시 오름차순, 번호 오름차순
        language: {
            search: "🔍 검색:",
            lengthMenu: "_MENU_ 개씩 보기",
            info: "총 _TOTAL_개 중 _START_ - _END_",
            infoEmpty: "데이터 없음",
            infoFiltered: "(전체 _MAX_개에서 필터됨)",
            paginate: {
                first: "처음",
                last: "마지막",
                next: "다음",
                previous: "이전"
            },
            zeroRecords: "일치하는 결과가 없습니다"
        },
        columnDefs: [
            { orderable: true, targets: [0,1,2,3,5,6] },
            { orderable: false, targets: [4] } // 문제 컬럼은 정렬 제외
        ],
    });

    // 빠른 필터 버튼 이벤트
    $('.filter-btn').click(function() {
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        
        var filter = $(this).data('filter');
        
        // 기존 검색 초기화
        table.search('').columns().search('').draw();
        
        if (filter === 'all') {
            table.draw();
        } else if (filter === 'has-page') {
            // 학습페이지 있는 항목만 (링크가 있는 행)
            $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
                return $(table.row(dataIndex).node()).hasClass('has-page');
            });
            table.draw();
            $.fn.dataTable.ext.search.pop();
        } else if (filter === 'has-mnemonic') {
            // 암기법 있는 항목만
            table.column(6).search('^(?!-$).*$', true, false).draw();
        } else {
            // 교시 필터 (1, 2, 3, 4)
            table.column(2).search('^' + filter + '$', true, false).draw();
        }
    });

    // 학습페이지 있는 행 필터를 위한 커스텀 필터 (has-page 버튼용)
    var hasPageFilter = false;
    
    $('.filter-btn[data-filter="has-page"]').click(function() {
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        
        table.search('').columns().search('').draw();
        
        $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
            return $(table.row(dataIndex).node()).hasClass('has-page');
        });
        table.draw();
        $.fn.dataTable.ext.search.pop();
    });
});
</script>
