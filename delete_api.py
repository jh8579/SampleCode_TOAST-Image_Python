import requests
import urllib

class DeleteAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def delete_one_file(self, folderId, fileId, includeThumbnail):
        print("단일 삭제(동기) API")

        req_url = self._get_url()
        req_url += 'images/'
        req_url += 'sync?'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}                               # folderId나 fileId 중 선택(폴더, 파일 동시에 삭제 불가!!!)
        # req_params['folderId'] = folderId           # 삭제 원하는 요소만 주석 해제!
        # req_params['fileId'] = fileId
        req_params['includeThumbnail'] = includeThumbnail

        return requests.delete(req_url, headers=req_header, params=req_params)

    def delete_multi_file(self, folderIds, fileIds, includeThumbnail):
        print("다중 삭제(비동기) API")

        req_url = self._get_url()
        req_url += 'images/'
        req_url += 'async?'
        print(req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}
        req_params['folderIds'] = ''                                        # 리스트를 string ','로 구분
        for i in folderIds:
            req_params['folderIds'] += i + ','                              # 요소 마다 ',' 추가
        req_params['folderIds'] = req_params['folderIds'][:-1]              # 마지막 ',' 삭제

        req_params['fileIds'] = ''                                          # 리스트를 string ','로 구분
        for i in fileIds:
            req_params['fileIds'] += i + ','                                # 요소 마다 ',' 추가
        req_params['fileIds'] = req_params['fileIds'][:-1]                  # 마지막 ',' 삭제

        req_params['includeThumbnail'] = includeThumbnail

        req_query = urllib.parse.urlencode(req_params).replace('%2C', ',')      # ',' 자동 인코딩으로 인한 변경
        print("query : " + req_query)

        req_session = requests.Session()
        req = requests.Request(method='DELETE', headers=req_header, url=req_url, params=req_params)

        prep = req.prepare()
        prep.url = req_url + req_query

        result = req_session.send(prep)
        return result

if __name__ == '__main__':

    # git 올릴때 삭제 후 commit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    IMAGE_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'
    APP_KEY = {APP_KEY}
    SECRET_KEY = {SECRET_KEY}
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    delete_api = DeleteAPI(IMAGE_URL, APP_KEY, SECRET_KEY)

    # (중요!) 단일 삭제 API로는 폴더와 파일 동시 삭제 불가
    folder_id = '71dfdd68-9443-4edb-bbab-7eff86513a02'      # (필수) 단일 삭제할 폴더 id
    file_id = '77cbb66d-5fdd-4b36-8918-5323ed16c0b5'        # (필수) 단일 삭제할 파일 id

    folder_ids = ['65b0faf3-d0a4-4b7a-b47f-8464c65ac7f3', '77cbb66d-5fdd-4b36-8918-5323ed16c0b5']   # (필수) 다중 삭제할 폴더 id
    file_ids = ['65b0faf3-d0a4-4b7a-b47f-8464c65ac7f3', '77cbb66d-5fdd-4b36-8918-5323ed16c0b5']     # (필수) 다중 삭제할 파일 id

    includeThumbnail = True                 # (선택) 목록 조회 대상 생성 속성 지정

    # 단일 삭제 API
    result = delete_api.delete_one_file(folder_id, file_id, includeThumbnail)
    print(result.json())
    print()

    # 다중 삭제 API
    result = delete_api.delete_multi_file(folder_ids, file_ids, includeThumbnail)
    print(result.json())
    print()

