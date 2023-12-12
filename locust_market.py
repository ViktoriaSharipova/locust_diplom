from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def product(self):
        self.client.get("/product/whitney-pullover")

    @task(3)
    def checkout(self):
        self.client.get("/checkout/information")
