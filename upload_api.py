import requests
import urllib
import json

class UploadAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def upload_one_file(self, local_path, path, overwrite, autorename, operation_ids):
        print("단일 파일 업로드 API")

        req_url = self._get_url()
        req_url += 'images?'
        print("url : " + req_url)

        req_header = self._get_request_header()
        req_header['Content-Type'] = 'application/octet-stream'
        print(req_header)

        operation_str = ''                      # 리스트를 string ','로 구분
        for id in operation_ids:
            operation_str += id + ','           # 요소 마다 ',' 추가
        operation_str = operation_str[:-1]      # 마지막 ',' 삭제

        req_params={}
        req_params['path'] = path
        req_params['overwrite'] = overwrite
        req_params['autorename'] = autorename
        req_params['operationIds'] = operation_str

        file = open(local_path, 'rb').read()    # 해당 파일을 바이너리로 업로드

        req_query = urllib.parse.urlencode(req_params).replace('%2F', '/')      # '/' 자동 인코딩으로 인한 변경
        print("query : " + req_query)

        req_session = requests.Session()
        req = requests.Request(method='PUT', headers=req_header, url=req_url, data=file)

        prep = req.prepare()
        prep.url = req_url + req_query

        result = req_session.send(prep)
        return result

    def upload_multi_file(self, local_paths, basepath, overwrite, autorename, operation_ids, callback_url):
        print("다중 파일 업로드 API")

        req_url = self._get_url()
        req_url += 'images'
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        files = []                                              # 파일 리스트를 배열에 담아 업로드
        for file_path in local_paths:
            files.append(('files', open(file_path, 'rb')))

        params = {}
        params['basepath'] = basepath
        params['overwrite'] = overwrite
        params['autorename'] = autorename
        params['operationIds'] = operation_ids
        params['callbackUrl'] = callback_url

        data = {}
        data['params'] = (params, 'multipart/form-data')        # json 객체를 multipart 형태에 맞게 전송
        print(data)

        return requests.post(url=req_url, headers=req_header, files=files, data=data)

if __name__ == '__main__':

    # git 올릴때 삭제 후 commit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    IMAGE_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'
    APP_KEY = {APP_KEY}
    SECRET_KEY = {SECRET_KEY}
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    upload_api = UploadAPI(IMAGE_URL, APP_KEY, SECRET_KEY)

    path = '/sample.jpg'                    # (필수) 단일 업로드할 경로 + 파일명!!
    local_path = './sample.jpg'             # (필수) 단일 업로드할 실제 파일 경로

    base_path = '/'                                 # (필수) 다중 업로드할 경로
    local_paths = ['./sample.png', './sample.jpg']  # (필수) 다중 업로드할 실제 파일 경로 리스트

    overwrite = 'false'                         # (선택) 같은 이름이 있을 경우 덮어쓰기 여부
    autorename = 'true'                         # (선택) 같은 이름이 있을 경우 "이름(1).확장자" 형식으로 파일명 변경 여부
    operation_ids = ['ddd']                     # (선택) 이미지 오퍼레이션 ID 리스트
    callback_url = ''                           # (선택) 처리 결과를 통보받을 콜백 Url 경로

    # 단일 파일 업로드 API
    result = upload_api.upload_one_file(local_path, path, overwrite, autorename, operation_ids)
    print(result.json())
    print()

    # 다중 파일 업로드 API
    result = upload_api.upload_multi_file(local_paths, base_path, overwrite, autorename, operation_ids, callback_url)
    print(result.json())
    print()