import json
import requests
import urllib

class FolderAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def create(self, create_path):
        req_url = self._get_url()
        req_url += 'folders'
        print(req_url)

        req_header = self._get_request_header()
        req_header['Content-Type'] = 'application/json; charset=utf-8'
        print(req_header)

        req_data = {'path': create_path}
        print(req_data)

        return requests.post(req_url, headers=req_header, json=req_data)

    def get_file(self, create_path, created_by, file_name, page_num, row_num, sort):
        req_url = self._get_url()
        req_url += 'folders'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params={}
        req_params['basepath'] = create_path
        req_params['createdBy'] = created_by
        req_params['name'] = file_name
        req_params['page'] = page_num
        req_params['rows'] = row_num
        req_params['sort'] = sort

        return requests.get(req_url, headers=req_header, params=req_params)

    def get_folder(self):
        req_url = self._get_url()
        req_header = self._get_request_header()
        return requests.put(req_url, headers=req_header)


if __name__ == '__main__':
    FOLDER_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'

    folder_api = FolderAPI(FOLDER_URL, APP_KEY, SECRET_KEY)

    # 폴더 생성
    base_path = '/'
    folder_name = ''
    create_path = base_path + folder_name

    created_by = 'U'
    file_name = 'sample.png'
    page_num = 1
    row_num = 100
    sort = "name:asc"

    result = folder_api.create(create_path)
    print(result.json())

    result = folder_api.get_file(create_path, created_by, file_name, page_num, row_num, sort)
    print(result.url)
    print(result.json())

    #folder_api.get_folder(create_path)