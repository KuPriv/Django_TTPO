from locust import HttpUser, TaskSet, task, between


class WebsiteTasks(TaskSet):
    @task
    def view_vaccination_schedule_list(self):
        self.client.get("/Privivki/")


class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    wait_time = between(1, 3)