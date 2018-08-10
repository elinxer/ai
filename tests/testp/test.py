
"""
上面是官方的示例demo，定义了针对http://example.com网站的测试场景：先模拟用户登录系统，
然后随机地访问index（/）和profile页面（/profile/），请求比例为2:1；并且，在测试过程中，两次请求的间隔时间为5~9秒间的随机值。

"""

from locust import HttpLocust, TaskSet
import time
import datetime


def login(l):
    l.client.post("/users/createVisitorID", {"ad_id": "0","machine_id": "1111", "timestamp": time.time()})


def index(l):
    l.client.get("/config/GAGameConfig.txt")


def profile(l):
    l.client.get("/users/login?appid=111115&data=a6rPzhTBg-iMuWCGHwvszNtxRTDCSHu_WE7vLQSCze6RCB6W6GxG_pAGvrIOI8_im0d-QYpecPrN-A2uUqi0vSr1kTIgb7cUL_enZUDwsNY=")


"""
行为
"""
class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

"""
启动
"""
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
