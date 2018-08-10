from locust import TaskSet, task, HttpLocust


class payStyle(TaskSet):

    @task(2)
    def pay(self):
        self.client.get(
            "http://47.75.200.170:51882/pay/get_pay_channel?pay_channel=android&accountId=10002537&appId=111115")

class userlogin(TaskSet):

    @task(3)
    def anyUserLogin(self):
        self.client.get(
            "http://47.75.200.170:51880/users/login?appid=111115&data=a6rPzhTBg-iMuWCGHwvszNtxRTDCSHu_WE7vLQSCze6RCB6W6GxG_pAGvrIOI8_im0d-QYpecPrN-A2uUqi0vSr1kTIgb7cUL_enZUDwsNY=")


class create(TaskSet):

    @task(5)
    def createAnyUser(self):
        self.client.get(
            "http://47.75.200.170:51880/users/createVisitorID?appid=111115&data=7pFmMQ-HLjf4-SN7s9XZVEm-pncr3i4ApNEzQWOY3FxNIk9vz8ruc9gPah7X_oIQHjoV2nTy3uPIrljL9JzmMA==")


class UserTask(TaskSet):

    def on_start(self):
        self.client.get("http://47.75.200.170/config/GAGameConfig.txt")
        pass

    tasks = {create: 15, userlogin: 12, payStyle: 5}
    pass


class User(HttpLocust):
    task_set = UserTask
    host = ""
    min_wait = 1000
    max_wait = 5000
