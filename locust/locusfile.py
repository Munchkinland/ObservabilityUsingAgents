from locust import HttpUser, task, between

class LoadTestingUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def heavy_task(self):
        self.client.get("/heavy-task")
