import requests
import urllib

class RealtimeAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def get_realtime(self):
        # 실시간 서비스 조회 API

        req_url = self._get_url()
        req_url += 'users'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        return requests.get(req_url, headers=req_header)

    def put_realtime(self, realtime_service):
        # 실시간 서비스 변경 API

        req_url = self._get_url()
        req_url += 'users'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}
        req_params['realtimeService'] = realtime_service

        return requests.put(req_url, headers=req_header, json=req_params)

if __name__ == '__main__':

    # git 올릴때 삭제 후 commit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    IMAGE_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'
    APP_KEY = {APP_KEY}
    SECRET_KEY = {SECRET_KEY}
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    realtime_api = RealtimeAPI(IMAGE_URL, APP_KEY, SECRET_KEY)

    realtime_service = 'false'              # (필수) 변경할 실시간 서비스 제공 여부 값

    # 실시간 서비스 조회 API
    result = realtime_api.get_realtime()
    print(result.json())
    print()

    # 실시간 서비스 변경 API
    result = realtime_api.put_realtime(realtime_service)
    print(result.json())
    print()