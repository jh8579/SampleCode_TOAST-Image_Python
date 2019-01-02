import requests
import urllib

class ImageOperationAPI:
    def __init__(self, folder_url, app_key, secret_key):
        self.folder_url = folder_url
        self.app_key = app_key
        self.secret_key = secret_key

    def _get_url(self):
        return self.folder_url + self.app_key + '/'

    def _get_request_header(self):
        return {'Authorization': self.secret_key}

    def create_operation(self, operation_id, description, realtime_service, delete_thumbnail, data):
        print("이미지 오퍼레이션 생성 및 수정 API")

        req_url = self._get_url()
        req_url += 'operations/'
        req_url += operation_id
        print("url : " + req_url)

        req_header = self._get_request_header()
        req_header['Content-Type'] = 'application/json'
        print(req_header)

        req_params = {}
        req_params['description'] = description
        req_params['realtimeService'] = realtime_service
        req_params['deleteThumbnail'] = delete_thumbnail
        req_params['data'] = data

        return requests.put(headers=req_header, url=req_url, json=req_params)

    def get_operation(self, name, page, rows, sort, template):
        print("이미지 오퍼레이션 목록 조회 API")

        req_url = self._get_url()
        req_url += 'operations?'
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}
        req_params['name'] = name
        req_params['page'] = page
        req_params['rows'] = rows
        req_params['sort'] = sort
        req_params['template'] = template

        req_query = urllib.parse.urlencode(req_params).replace('%3A', ':')  # ':' 자동 인코딩으로 인한 변경
        print("query : " + req_query)

        req_session = requests.Session()
        req = requests.Request(method='GET', headers=req_header, url=req_url)

        prep = req.prepare()
        prep.url = req_url + req_query

        result = req_session.send(prep)
        return result

    def get_detail_operation(self, operation_id):
        print("이미지 오퍼레이션 상세 조회 API")

        req_url = self._get_url()
        req_url += 'operations/'
        req_url += operation_id
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        return requests.get(headers=req_header, url=req_url)

    def delete_operation(self, operation_id, delete_thumbnail):
        print("이미지 오퍼레이션 삭제 API")

        req_url = self._get_url()
        req_url += 'operations/'
        req_url += operation_id
        print("url : " + req_url)

        req_header = self._get_request_header()
        req_header['Content-Type'] = 'application/json'
        print(req_header)

        req_params = {}
        req_params['deleteThumbnail'] = delete_thumbnail

        return requests.delete(headers=req_header, url=req_url)

    def exceute_operation(self, basepath, filepaths, operation_ids, callback_url):
        print("이미지 오퍼레이션 실행 API")

        req_url = self._get_url()
        req_url += 'operations-exec'
        print("url : " + req_url)

        req_header = self._get_request_header()
        print(req_header)

        req_params = {}
        req_params['basepath'] = basepath
        req_params['filepaths'] = filepaths
        req_params['operationIds'] = operation_ids
        req_params['callbackUrl'] = callback_url

        return requests.post(headers=req_header, url=req_url, json=req_params)

if __name__ == '__main__':

    # git 올릴때 삭제 후 commit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    IMAGE_URL = 'https://api-image.cloud.toast.com/image/v2.0/appkeys/'
    APP_KEY = {APP_KEY}
    SECRET_KEY = {SECRET_KEY}
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    image_operation_api = ImageOperationAPI(IMAGE_URL, APP_KEY, SECRET_KEY)

    operation_id = '100x100'            # (필수) 생성 및 수정할 오퍼레이션 이름

    description = '100x100으로 변경'    # (선택) 오퍼레이션 설명
    realtime_service = 'false'          # (선택) 실시간 서비스 제공 여부
    delete_thumbnail = 'true'           # (선택) 기존에 해당 오퍼레이션으로 생성된 썸네일을 삭제할지 여부
    data = [                            # (선택) 오퍼레이션 작업 목록
        {
            "templateOperationId": "resize_max_fit",
            "option": {
                "resizeType": "max_fit",
                "width": 100,
                "height": 100,
                "quality": 80,
                "upDownSizeType": "downOnly"
            }
        }
    ]

    name = '100x100'                    # (필수) 검색할 오퍼레이션 이름
    page = 1                            # (선택) 페이지 번호
    rows = 100                          # (선택) 조회 개수
    sort = "name:asc"                   # (선택) 정렬 방식 (정렬대상 : name or date, 정렬방식 : asc or desc)
    template = 'false'                  # (선택) 목록 조회 대상 (true: 기본 오퍼레이션, false: 사용자 생성 오퍼레이션)

    basepath = '/'                                  # (필수) 기준이 되는 폴더의 절대 경로
    filepaths = ['/sample.png', '/sample.jpg']      # (필수) 실행할 절대 경로의 폴더 및 파일 리스트
    operation_ids = ['100x100']                     # (필수) 실행할 오퍼레이션 ID 리스트
    callback_url = ''                               # (선택) 처리 결과를 통보받을 URL 경로


    # 이미지 오퍼레이션 생성 API
    result = image_operation_api.create_operation(operation_id, description, realtime_service, delete_thumbnail, data)
    print(result.json())
    print()

    # 이미지 오퍼레이션 목록 조회 API
    result = image_operation_api.get_operation(name, page, rows, sort, template)
    print(result.json())
    print()

    # 이미지 오퍼레이션 상세 조회 API
    result = image_operation_api.get_detail_operation(operation_id)
    print(result.json())
    print()

    # 이미지 오퍼레이션 실행 API
    result = image_operation_api.exceute_operation(basepath, filepaths, operation_ids, callback_url)
    print(result.json())
    print()

    # 이미지 오퍼레이션 삭제 API
    result = image_operation_api.delete_operation(operation_id, delete_thumbnail)
    print(result.json())
    print()
