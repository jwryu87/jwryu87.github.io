---
layout: post
title: Blog start with Jekyll
date: 2021-06-11
tags: jekyll
comment: true
---

### 1. Ruby 설치

설치가 안되어 있다면 설치합니다.
(mac은 기존적으로 설치되어 있습니다)

```
ruby -v
```

### 2. Jekyll 설치

```
gem install jekyll
```

### 3. Jekyll 프로젝트 생성

```
jekyll new jwryu87.github.io
```

### 4. Jekyll 테마 적용

1. 원하는 테마를 찾아서 다운로드
2. 위 만들어진 디렉토리에 덮어쓰기한다.
3. http://jekyllthemes.org

### 5. 패키지 설치

해당 디렉토리로 이동 수 실행

```
source ~/.zshrc
bundle install
```

### 6. 로컬 서버 수행

```
jekyll serve
```

### 6. Github page로 웹호스팅하기

1. https://github.com/jwryu87 에 가서 레포지토리 생성
    1. GitHub Pages가 웹호스팅하는 기본 repository 이름 형식은 username.github.io 이다
    2. 따라서 jwryu87.github.io로 생성
2. 위에 생성한 디렉토리를 push
    1. 이 작업은 레포지토리 생성하면 방법이 나옴 -> 그대로 수행 (Quick setup)

### 7. Custom domain 설정하기
   