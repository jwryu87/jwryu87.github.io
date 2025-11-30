---
layout: page
title: 정보관리기술사
permalink: /pe/
---

# 정보관리기술사 학습 노트

이 섹션은 정보관리기술사 시험 준비를 위한 학습 자료를 정리하는 공간입니다.

## 📚 학습 카테고리

### 데이터베이스
- 데이터베이스 설계
- SQL 및 쿼리 최적화
- 트랜잭션 관리
- 분산 데이터베이스

### 소프트웨어공학
- 개발 방법론
- 설계 패턴
- 테스트 전략
- 품질 관리

### 시스템 아키텍처
- 클라우드 아키텍처
- 마이크로서비스
- 시스템 설계
- 성능 최적화

### 정보보안
- 보안 위협 및 대응
- 암호화
- 인증 및 접근제어
- 보안 아키텍처

### 신기술
- AI/ML
- 빅데이터
- 블록체인
- IoT

---

## 📝 최근 학습 내용

<div class="posts">
  {% for post in site.posts %}
    {% if post.categories contains 'pe' %}
      <article class="post">
        <h3>
          <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        </h3>
        
        <div class="post-meta">
          <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
          {% if post.tags %}
            <span class="post-tags">
              {% for tag in post.tags %}
                <a href="{{ site.baseurl }}/tags/#{{ tag }}">#{{ tag }}</a>
              {% endfor %}
            </span>
          {% endif %}
        </div>
        
        <div class="post-excerpt">
          {{ post.excerpt }}
        </div>
      </article>
    {% endif %}
  {% endfor %}
</div>

---

## 📊 학습 통계

- 전체 포스트: {{ site.posts | where: "categories", "pe" | size }}개
- 마지막 업데이트: {{ site.time | date: "%Y-%m-%d" }}

## 🎯 학습 목표

- [ ] 기출문제 분석 완료
- [ ] 핵심 개념 정리
- [ ] 모의고사 준비
- [ ] 실전 문제 풀이

