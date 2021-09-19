import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file = path_to_file[(path_to_file.rfind('/')+1):]
        headers = {'Accept': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': file_path + file}
        url = 'https://cloud-api.yandex.net/post/v1/disk/resources/upload'
        response = requests.get(url, headers=headers, params=params)
        href = response.json().get('href')
        response_load = requests.put(href, data=open(path_to_file, 'rb'))
        print(response_load)


if __name__ == '__main__':
    path_to_file = 'files_list/2.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload('/1001/')
