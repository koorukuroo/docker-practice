from locust import HttpUser, task, between, events
import time

class FastAPIUser(HttpUser):
    """
    FastAPI 애플리케이션 성능 테스트용 Locust 사용자 클래스

    각 가상 사용자는 1-3초 사이의 대기 시간을 가지며,
    정의된 태스크를 무작위로 실행합니다.
    """

    # 요청 간 대기 시간 (1-3초 사이 랜덤)
    wait_time = between(1, 3)

    @task(5)
    def get_root(self):
        """
        메인 엔드포인트 테스트 (가중치: 5)
        가장 자주 호출되는 엔드포인트
        """
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")

    @task(2)
    def get_health(self):
        """
        헬스체크 엔드포인트 테스트 (가중치: 2)
        모니터링 시스템이 주기적으로 호출
        """
        with self.client.get("/health", catch_response=True) as response:
            if response.status_code == 200 and response.json().get("status") == "healthy":
                response.success()
            else:
                response.failure("Health check failed")

    @task(3)
    def get_items(self):
        """
        API 엔드포인트 테스트 (가중치: 3)
        파라미터를 포함한 실제 API 호출 시뮬레이션
        """
        item_id = self.environment.runner.user_count % 100 + 1  # 1-100 사이 ID
        with self.client.get(f"/api/items/{item_id}?q=test", catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if "item_id" in data:
                    response.success()
                else:
                    response.failure("Invalid response format")
            else:
                response.failure(f"Got status code {response.status_code}")

    def on_start(self):
        """
        각 사용자가 시작될 때 한 번 실행되는 메서드
        로그인이나 초기 설정이 필요한 경우 여기에 작성
        """
        print(f"User {self.environment.runner.user_count} started")

    def on_stop(self):
        """
        각 사용자가 종료될 때 한 번 실행되는 메서드
        정리 작업이 필요한 경우 여기에 작성
        """
        print(f"User stopped")


# 이벤트 훅: 테스트 시작 시
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("=" * 50)
    print("성능 테스트를 시작합니다!")
    print(f"대상 호스트: {environment.host}")
    print("=" * 50)


# 이벤트 훅: 테스트 종료 시
@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("=" * 50)
    print("성능 테스트가 완료되었습니다!")
    print("=" * 50)


class NginxUser(HttpUser):
    """Nginx 프록시 테스트용 (포트 80)"""
    host = "http://localhost"
    wait_time = between(1, 2)

    @task
    def test_nginx(self):
        self.client.get("/")


class CaddyUser(HttpUser):
    """Caddy 프록시 테스트용 (포트 8080)"""
    host = "http://localhost:8080"
    wait_time = between(1, 2)

    @task
    def test_caddy(self):
        self.client.get("/")
