import requests
import urllib

class TaskAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def get_task(self, queue_id):
        # 작업 조회 API

        req_url = self._get_url()
        req_url += 'queues/'
        req_url += queue_id
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        return requests.get(req_url, headers=req_header)

if __name__ == '__main__':

    # git 올릴때 삭제 후 commit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    IMAGE_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'
    APP_KEY = {APP_KEY}
    SECRET_KEY = {SECRET_KEY}
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    task_api = TaskAPI(IMAGE_URL, APP_KEY, SECRET_KEY)

    queue_id = 'a66714dd-c80f-484b-b42c-5168e7baf4f5'   # (필수) 조회할 작업 고유 ID

    # 작업 조회 API
    result = task_api.get_task(queue_id)
    print(result.json())
    print()

