---
layout: post
title: jekyll 로컬에서 실행 시 `ERROR '/' not found.`
date: 2021-06-26 23:00:00 +09:00
tags: jekyll
comments: true
---

## jekyll 로컬에서 실행 시 ERROR 문제
- `$ jekyll serve` 로 로컬에서 `http://127.0.0.1:4000/` 실행 시 아래와 같은 오류 발생했을 시 해결 방범  
  ![error]({{ site.url }}/assets/notfound.png)
- `$ _config.yml` 파일에서 baseurl 을 주석처리 한다..    
  ![error2]({{ site.url }}/assets/notfound_2.png)

##  Reference
- https://stackoverflow.com/questions/56100280/how-to-fix-error-not-found-error-about-jekyll-in-localhost4000
