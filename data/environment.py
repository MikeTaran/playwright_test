import os


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://admin.websitewizard.ru/',
        PROD: 'https://admin.websitewizard.ru/'
    }

    def __init__(self):
        self.env = os.getenv('ENV') or self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Environment()
