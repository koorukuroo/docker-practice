# 🚀 Docker Workshop - FastAPI with Reverse Proxy

<div align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=for-the-badge&logo=caddy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Locust](https://img.shields.io/badge/Locust-00B140?style=for-the-badge&logo=locust&logoColor=white)

**프로덕션급 FastAPI 애플리케이션과 리버스 프록시 설정을 위한 완벽한 Docker 워크샵 프로젝트**

[시작하기](#-빠른-시작) • [아키텍처](#-아키텍처) • [성능 테스트](#-성능-테스트) • [문서](#-api-문서)

</div>

---

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [아키텍처](#-아키텍처)
- [기술 스택](#-기술-스택)
- [빠른 시작](#-빠른-시작)
- [프로젝트 구조](#-프로젝트-구조)
- [API 문서](#-api-문서)
- [성능 테스트](#-성능-테스트)
- [설정 가이드](#-설정-가이드)
- [트러블슈팅](#-트러블슈팅)

---

## 🎯 프로젝트 소개

이 프로젝트는 **Docker 컨테이너 오케스트레이션**, **리버스 프록시 설정**, 그리고 **성능 테스팅**을 학습하기 위한 실전 워크샵 자료입니다. FastAPI 기반의 백엔드 애플리케이션을 Nginx 또는 Caddy를 통해 프록시하고, Locust를 활용한 부하 테스트까지 포함하고 있습니다.

### 🎓 학습 목표

- ✅ Docker Compose를 활용한 멀티 컨테이너 애플리케이션 구성
- ✅ Nginx와 Caddy 리버스 프록시 설정 및 비교
- ✅ FastAPI를 활용한 RESTful API 개발
- ✅ Locust를 이용한 성능 테스트 및 분석
- ✅ 컨테이너 헬스체크 및 모니터링
- ✅ 프로덕션 환경을 위한 베스트 프랙티스

---

## ✨ 주요 기능

### 🔥 FastAPI 애플리케이션
- **고성능 비동기 API**: Python 3.11 기반의 최신 FastAPI 프레임워크
- **자동 문서화**: Swagger UI 및 ReDoc을 통한 인터랙티브 API 문서
- **CORS 지원**: 크로스 오리진 리소스 공유 완벽 지원
- **헬스체크 엔드포인트**: 컨테이너 상태 모니터링

### 🌐 리버스 프록시
#### Nginx
- 고성능 웹 서버 및 리버스 프록시
- WebSocket 지원
- 커스텀 헤더 전달
- 포트: `80`

#### Caddy
- 자동 HTTPS 지원
- 모던한 설정 문법
- JSON 로깅
- 보안 헤더 자동 설정
- 포트: `8080`, `8443`

### 📊 성능 테스트
- **Locust 통합**: 웹 UI 기반의 부하 테스트
- **멀티 시나리오**: 다양한 엔드포인트 테스트
- **실시간 모니터링**: RPS, 응답시간, 에러율 등
- **확장 가능**: 분산 테스트 지원

---

## 🏗 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│                    Client Browser                        │
└──────────────────┬──────────────────┬───────────────────┘
                   │                  │
                   │                  │
          ┌────────▼────────┐  ┌─────▼──────────┐
          │  Nginx :80      │  │  Caddy :8080   │
          │  (Alpine)       │  │  (Alpine)      │
          └────────┬────────┘  └─────┬──────────┘
                   │                  │
                   │   ┌──────────────┘
                   │   │
            ┌──────▼───▼───────────────────────┐
            │    FastAPI Application :8000     │
            │    (Python 3.11 Slim)            │
            │                                   │
            │  • RESTful API                   │
            │  • Health Check                  │
            │  • Auto Documentation            │
            └──────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              Locust Load Testing                        │
│         (http://localhost:8089)                         │
└─────────────────────────────────────────────────────────┘
```

### 네트워크 구성
- **app-network**: 내부 브리지 네트워크로 모든 컨테이너 연결
- **포트 매핑**:
  - `80` → Nginx → FastAPI
  - `8080`, `8443` → Caddy → FastAPI
  - `8089` → Locust Web UI

---

## 🛠 기술 스택

### Backend
| 기술 | 버전 | 설명 |
|------|------|------|
| **Python** | 3.11 | 메인 프로그래밍 언어 |
| **FastAPI** | 0.109.0 | 모던 웹 프레임워크 |
| **Uvicorn** | 0.27.0 | ASGI 서버 |

### Infrastructure
| 기술 | 버전 | 설명 |
|------|------|------|
| **Docker** | Latest | 컨테이너 플랫폼 |
| **Docker Compose** | 3.8 | 멀티 컨테이너 오케스트레이션 |
| **Nginx** | Alpine | 리버스 프록시 (옵션 1) |
| **Caddy** | Alpine | 리버스 프록시 (옵션 2) |

### Testing
| 기술 | 버전 | 설명 |
|------|------|------|
| **Locust** | Latest | 부하 테스트 도구 |

---

## 🚀 빠른 시작

### 사전 요구사항

```bash
# Docker 설치 확인
docker --version
# Docker version 20.10.0 이상

# Docker Compose 설치 확인
docker-compose --version
# Docker Compose version 1.29.0 이상
```

### 1️⃣ Nginx 버전 실행

```bash
# 컨테이너 빌드 및 실행
docker-compose -f docker-compose.nginx.yml up --build

# 백그라운드 실행
docker-compose -f docker-compose.nginx.yml up -d

# 접속 테스트
curl http://localhost/
curl http://localhost/health
```

**접속 URL**: http://localhost

### 2️⃣ Caddy 버전 실행

```bash
# 컨테이너 빌드 및 실행
docker-compose -f docker-compose.caddy.yml up --build

# 백그라운드 실행
docker-compose -f docker-compose.caddy.yml up -d

# 접속 테스트
curl http://localhost:8080/
curl http://localhost:8080/health
```

**접속 URL**: http://localhost:8080

### 3️⃣ 성능 테스트 실행

```bash
# Locust 설치
cd performance
pip install -r requirements.txt

# Nginx 버전 테스트
locust -f locustfile.py --host=http://localhost

# Caddy 버전 테스트
locust -f locustfile.py --host=http://localhost:8080

# 웹 UI 접속: http://localhost:8089
```

### 4️⃣ 종료

```bash
# Nginx 버전 종료
docker-compose -f docker-compose.nginx.yml down

# Caddy 버전 종료
docker-compose -f docker-compose.caddy.yml down

# 볼륨까지 삭제
docker-compose -f docker-compose.nginx.yml down -v
```

---

## 📁 프로젝트 구조

```
lgcns/
├── 📄 README.md                          # 프로젝트 문서
├── 📄 docker-compose.nginx.yml           # Nginx 구성 파일
├── 📄 docker-compose.caddy.yml           # Caddy 구성 파일
├── 📄 Docker-Workshop-Complete.pdf       # 워크샵 완전 가이드
│
├── 📂 app/                                # FastAPI 애플리케이션
│   ├── 📄 main.py                        # 메인 애플리케이션 코드
│   ├── 📄 requirements.txt               # Python 의존성
│   └── 📄 Dockerfile                     # 애플리케이션 이미지 빌드 파일
│
├── 📂 nginx/                              # Nginx 설정
│   └── 📄 nginx.conf                     # Nginx 리버스 프록시 설정
│
├── 📂 caddy/                              # Caddy 설정
│   └── 📄 Caddyfile                      # Caddy 리버스 프록시 설정
│
└── 📂 performance/                        # 성능 테스트
    ├── 📄 locustfile.py                  # Locust 테스트 시나리오
    └── 📄 requirements.txt               # 테스트 도구 의존성
```

---

## 📚 API 문서

### 🌐 엔드포인트

#### `GET /`
메인 엔드포인트

**Response**:
```json
{
  "message": "Hello from FastAPI behind Nginx!"
}
```

#### `GET /health`
헬스체크 엔드포인트

**Response**:
```json
{
  "status": "healthy"
}
```

#### `GET /api/items/{item_id}`
아이템 조회 API

**Parameters**:
- `item_id` (path): 아이템 ID (integer)
- `q` (query, optional): 검색 쿼리 (string)

**Response**:
```json
{
  "item_id": 42,
  "q": "search query"
}
```

**Example**:
```bash
curl "http://localhost/api/items/42?q=test"
```

### 📖 인터랙티브 문서

FastAPI는 자동으로 API 문서를 생성합니다:

- **Swagger UI**:
  - Nginx: http://localhost/docs
  - Caddy: http://localhost:8080/docs

- **ReDoc**:
  - Nginx: http://localhost/redoc
  - Caddy: http://localhost:8080/redoc

---

## 📊 성능 테스트

### Locust 사용법

#### 웹 UI를 통한 테스트

1. Locust 실행:
```bash
cd performance
locust -f locustfile.py --host=http://localhost
```

2. 브라우저에서 접속: http://localhost:8089

3. 테스트 파라미터 설정:
   - **Number of users**: 동시 사용자 수 (예: 100)
   - **Spawn rate**: 초당 증가하는 사용자 수 (예: 10)
   - **Host**: 테스트 대상 URL

4. **Start swarming** 클릭하여 테스트 시작

#### CLI를 통한 테스트

```bash
# Headless 모드로 실행
locust -f locustfile.py \
  --host=http://localhost \
  --users=100 \
  --spawn-rate=10 \
  --run-time=1m \
  --headless

# CSV 리포트 생성
locust -f locustfile.py \
  --host=http://localhost \
  --users=100 \
  --spawn-rate=10 \
  --run-time=1m \
  --headless \
  --csv=results
```

### 테스트 시나리오

#### FastAPIUser 클래스
표준 성능 테스트 시나리오:

| 태스크 | 가중치 | 설명 |
|--------|--------|------|
| `get_root()` | 5 | 메인 페이지 접속 (가장 빈번) |
| `get_health()` | 2 | 헬스체크 호출 |
| `get_items()` | 3 | API 엔드포인트 호출 |

#### NginxUser 클래스
Nginx 프록시 전용 테스트 (포트 80)

#### CaddyUser 클래스
Caddy 프록시 전용 테스트 (포트 8080)

### 성능 메트릭

Locust는 다음 메트릭을 제공합니다:

- **RPS** (Requests Per Second): 초당 요청 수
- **Response Time**:
  - Average (평균)
  - Min/Max (최소/최대)
  - Median (중앙값)
  - 95th/99th Percentile
- **Failure Rate**: 실패율 (%)
- **Throughput**: 처리량 (requests/s)

---

## ⚙️ 설정 가이드

### Nginx 설정 커스터마이징

[nginx/nginx.conf](nginx/nginx.conf) 파일 수정:

```nginx
# 업스트림 서버 설정
upstream fastapi {
    server fastapi:8000;
    # 로드 밸런싱을 위한 여러 서버 추가 가능
    # server fastapi2:8000;
}

server {
    listen 80;
    server_name localhost;

    # 최대 업로드 크기 설정
    client_max_body_size 20M;

    # 프록시 설정
    location / {
        proxy_pass http://fastapi;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # 타임아웃 설정 (선택사항)
        # proxy_connect_timeout 60s;
        # proxy_send_timeout 60s;
        # proxy_read_timeout 60s;
    }
}
```

### Caddy 설정 커스터마이징

[caddy/Caddyfile](caddy/Caddyfile) 파일 수정:

```caddyfile
:8080 {
    # 리버스 프록시
    reverse_proxy fastapi:8000

    # JSON 로깅
    log {
        output stdout
        format json
        level INFO
    }

    # 보안 헤더
    header {
        X-Content-Type-Options "nosniff"
        X-Frame-Options "DENY"
        X-XSS-Protection "1; mode=block"
        # Strict-Transport-Security "max-age=31536000;"
    }

    # CORS 설정 (선택사항)
    # @cors {
    #     header Origin *
    # }
    # header @cors Access-Control-Allow-Origin "*"
}
```

### 환경 변수

[docker-compose.nginx.yml](docker-compose.nginx.yml) 또는 [docker-compose.caddy.yml](docker-compose.caddy.yml)에서 환경 변수 설정:

```yaml
services:
  fastapi:
    environment:
      - PYTHONUNBUFFERED=1
      - LOG_LEVEL=info
      - API_PREFIX=/api/v1
      # 추가 환경 변수...
```

---

## 🔍 모니터링

### 컨테이너 상태 확인

```bash
# 실행 중인 컨테이너 확인
docker-compose -f docker-compose.nginx.yml ps

# 로그 확인
docker-compose -f docker-compose.nginx.yml logs -f

# 특정 서비스 로그만 확인
docker-compose -f docker-compose.nginx.yml logs -f fastapi
docker-compose -f docker-compose.nginx.yml logs -f nginx
```

### 헬스체크

모든 서비스는 자동 헬스체크를 포함합니다:

```bash
# 헬스체크 상태 확인
docker inspect --format='{{json .State.Health}}' fastapi-app | jq
docker inspect --format='{{json .State.Health}}' nginx-proxy | jq

# 또는
curl http://localhost/health
```

### 리소스 사용량 모니터링

```bash
# 실시간 리소스 사용량
docker stats

# 특정 컨테이너만
docker stats fastapi-app nginx-proxy
```

---

## 🐛 트러블슈팅

### 포트가 이미 사용 중

**문제**: `Bind for 0.0.0.0:80 failed: port is already allocated`

**해결**:
```bash
# 포트 사용 중인 프로세스 확인 (Mac/Linux)
lsof -i :80

# 포트 사용 중인 프로세스 종료
kill -9 <PID>

# 또는 docker-compose.yml에서 포트 변경
ports:
  - "8080:80"  # 호스트 포트를 8080으로 변경
```

### 컨테이너가 시작되지 않음

**문제**: 컨테이너가 반복적으로 재시작됨

**해결**:
```bash
# 로그 확인
docker-compose logs -f

# 컨테이너 재빌드
docker-compose -f docker-compose.nginx.yml up --build --force-recreate

# 캐시 없이 빌드
docker-compose -f docker-compose.nginx.yml build --no-cache
```

### 502 Bad Gateway

**문제**: Nginx/Caddy에서 502 에러 발생

**해결**:
1. FastAPI 컨테이너가 정상 실행 중인지 확인
```bash
docker-compose ps
curl http://localhost:8000/health  # FastAPI 직접 접근
```

2. 네트워크 설정 확인
```bash
docker network ls
docker network inspect <network-name>
```

3. 업스트림 서버 이름 확인 (nginx.conf, Caddyfile)

### Permission Denied

**문제**: 볼륨 마운트 시 권한 오류

**해결**:
```bash
# SELinux 시스템에서
chcon -Rt svirt_sandbox_file_t ./nginx
chcon -Rt svirt_sandbox_file_t ./caddy

# 또는 docker-compose.yml에서
volumes:
  - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro,Z
```

---

## 📖 학습 자료

### 추천 읽을거리

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Docker 공식 문서](https://docs.docker.com/)
- [Nginx 프록시 가이드](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- [Caddy 문서](https://caddyserver.com/docs/)
- [Locust 문서](https://docs.locust.io/)

### 다음 단계

1. **데이터베이스 추가**: PostgreSQL, MongoDB 등 통합
2. **인증/인가**: JWT, OAuth2 구현
3. **CI/CD**: GitHub Actions, GitLab CI 설정
4. **모니터링**: Prometheus, Grafana 통합
5. **로깅**: ELK Stack, Loki 구성
6. **HTTPS**: Let's Encrypt 자동 인증서
7. **로드 밸런싱**: 여러 FastAPI 인스턴스 운영
8. **캐싱**: Redis 통합

---

## 🤝 기여하기

이 프로젝트는 교육 목적으로 제작되었습니다. 개선 사항이나 버그를 발견하시면 이슈를 등록해 주세요!

---

## 📄 라이센스

이 프로젝트는 교육 및 학습 목적으로 자유롭게 사용할 수 있습니다.

---

## 📞 문의

질문이나 피드백이 있으시면 언제든지 연락 주세요!

---

<div align="center">

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요! ⭐**

Made with ❤️ for Docker & FastAPI Learning

</div>
