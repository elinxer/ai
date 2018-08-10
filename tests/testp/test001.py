from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    """ 脚步任务行为 """

    def on_start(self):
        self.client.post("/login", {
            "username": "test",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    """ 单个用户操作 """

    task_set = WebsiteTasks
    host = "http://debugtalk.com"
    min_wait = 1000
    max_wait = 5000
