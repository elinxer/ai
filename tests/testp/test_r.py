"""

接口压测

author Elinx

"""

from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    GameConfig = ''

    def on_start(self):
        # self.client.get("/login", {
        #     "username": "test",
        #     "password": "123456"
        # })

        self.client.get("http://47.75.200.170/config/GAGameConfig.txt")
        pass

    @task(2)
    def anyUserLogin(self):
        self.client.get(
            "http://47.75.200.170:51880/users/login?appid=111115&data=a6rPzhTBg-iMuWCGHwvszNtxRTDCSHu_WE7vLQSCze6RCB6W6GxG_pAGvrIOI8_im0d-QYpecPrN-A2uUqi0vSr1kTIgb7cUL_enZUDwsNY=")

    @task(1)
    def createAnyUser(self):
        self.client.get(
            "http://47.75.200.170:51880/users/createVisitorID?appid=111115&data=7pFmMQ-HLjf4-SN7s9XZVEm-pncr3i4ApNEzQWOY3FxNIk9vz8ruc9gPah7X_oIQHjoV2nTy3uPIrljL9JzmMA==")

    @task(1)
    def payStyle(self):
        self.client.get(
            "http://47.75.200.170:51882/pay/get_pay_channel?pay_channel=android&accountId=10002537&appId=111115")


class WebsiteUser(HttpLocust):
    """ 单个用户操作 """

    task_set = WebsiteTasks
    # host = "http://47.75.200.170"
    host = ""
    min_wait = 1000
    max_wait = 5000
