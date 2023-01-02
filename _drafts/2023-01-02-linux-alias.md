---
layout: post
title: (linux) 영구적으로 alias 설정
date: 2023-01-02 12:00:00 +09:00
tags: Linux
comments: true
---

## Subject
- 현재 계정에 영구적으로 alias 설정
- `ls -rlt` 을 자주 사용하는데 `ll` 로 alias 로 등록하고자 한다.

## 방법
- bashrc (또는 zshrc 등 사용하는 쉘의 파일 ) 파일 맨 마지막 줄에 alias 별명="명령어 or 이름" 을 추가하면 된다.
- source로 동기화한다. 

```
vi ~/.bashrc
```

```   
alias ll=‘ls -rlt'
```

```
source ~/.bashrc
```   

