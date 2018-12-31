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

    def create(self, created_path):
        print("폴더 생성 API")

        req_url = self._get_url()
        req_url += 'folders'
        print(req_url)

        req_header = self._get_request_header()
        req_header['Content-Type'] = 'application/json; charset=utf-8'
        print(req_header)

        req_data = {'path': created_path}
        print(req_data)

        return requests.post(req_url, headers=req_header, json=req_data)

    def get_file(self, created_path, created_by, file_name, page_num, row_num, sort):
        req_url = self._get_url()
        req_url += 'folders'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params={}
        req_params['basepath'] = created_path
        req_params['createdBy'] = created_by
        req_params['name'] = file_name
        req_params['page'] = page_num
        req_params['rows'] = row_num
        req_params['sort'] = sort

        return requests.get(req_url, headers=req_header, params=req_params)

    def get_file1(self, created_path, created_by, file_name, page_num, row_num, sort):
        print("폴더 내 파일 목록 조회 API")

        req_url = self._get_url()
        req_url += 'folders?'
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params={}
        req_params['basepath'] = created_path
        req_params['createdBy'] = created_by
        req_params['name'] = file_name
        req_params['page'] = page_num
        req_params['rows'] = row_num
        req_params['sort'] = sort

        req_query = urllib.parse.urlencode(req_params).replace('%2F', '/')
        req_query = req_query.replace('%3A', ':')
        print("query : " + req_query)

        req_session = requests.Session()
        req = requests.Request(method='GET', headers=req_header, url=req_url)

        prep = req.prepare()
        prep.url = req_url + req_query

        result = req_session.send(prep)
        return result

    def get_folder(self, created_path):
        print("폴더 속성 조회 API")

        req_url = self._get_url()
        req_url += 'properties?'
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}
        req_params['path'] = created_path

        req_query = urllib.parse.urlencode(req_params).replace('%2F', '/')
        print("query : " + req_query)

        req_session = requests.Session()
        req = requests.Request(method='GET', headers=req_header, url=req_url)

        prep = req.prepare()
        prep.url = req_url + req_query

        result = req_session.send(prep)
        return result

if __name__ == '__main__':

    realtime_api = RealtimeAPI(FOLDER_URL, APP_KEY, SECRET_KEY)

    base_path = '/'                         # base 경로
    folder_name = 'jinho'                   # 폴더 이름
    created_path = base_path + folder_name  # (필수) 폴더 경로

    created_by = 'U'                        # (선택) 목록 조회 대상 생성 속성 지정
    file_name = 'sample.png'                # (선택) 목록 조회 대상 이름 지정
    page_num = 1                            # (선택) 목록 조회 페이지 수 지정
    row_num = 100                           # (선택) 목록 조회 열 수 지정
    sort = "name:asc"                       # (선택) 목로 조회 정렬 기준 지정

    # 폴더 생성 API
    result = realtime_api.create(created_path)
    print(result.json())
    print()

    # 폴더 내 파일 목록 조회 API
    #result = folder_api.get_file(created_path, created_by, file_name, page_num, row_num, sort)
    result = realtime_api.get_file1(created_path, created_by, file_name, page_num, row_num, sort)
    print(result.json())
    print()

    # 폴더 속성 조회 API
    result = realtime_api.get_folder(created_path)
    print(result.json())
    print()