import requests



vk_token = 'vk1.a.sdQfQZSv3ft5tSlX95uhuWjJHSZ6E5G_6LAgJbcmGXPAy2eQflZxxt2xxGgWyCP4_C5yFnaqJ8W_o1sWDyLlj4DzhGa0bmn4hHEIL51l5wsXgvb5ATAbLJdwodMbKH8yZ_E9UWcb4SZUXGjvqoMQdg7OFsVpFJnR3KVn3tVeWA34GIMtcE9rTeWQO2ZKA_lG'
ya_token = 'y0_AgAAAABjgZOBAADLWwAAAAD6sb3HAADRT3aPS8xLu6KWlRpw7p3lqODjyg'
class VK:
    api_base_url = 'https://api.vk.com/method/'
    def __init__(self, token,user_id):
        self.token = token
        self.user_id = user_id

    def get_photos(self):
        photos = []
        response = requests.get(self.api_base_url + 'photos.get', params={
            'owner_id': self.user_id,
            'extended': 1,
            'access_token': self.token,
            'v': '5.199',
            'album_id': 'wall'})

        for j,i in enumerate(response.json()['response']['items']):
            photos.append((i['sizes'][-1]['url'],i['sizes'][-1]['type']))

            print(f'photo{j}.jpg - ',i['sizes'][-1]['type'])

        return photos

class YaDisk:
    api_base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    def __init__(self, token):
        self.token = token
        self.params = {'path': 'netology'}
    def create_folder(self):
        try:
            response = requests.put(self.api_base_url, params=self.params, headers={'Authorization': f'OAuth {self.token}'})
        except requests.exceptions.HTTPError:
            pass





    def upload_photos(self):


        for i,photo in enumerate(vk_client.get_photos()):
            print(f'Uploading photo{i}.jpg')
            url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            resp = requests.post(url_for_upload, params={'path': f'netology/photo{i}.jpg','url': photo[0]},headers={'Authorization': f'OAuth {ya_token}'})

            print(f'Photo {i} uploaded')


        return resp


vk_client = VK(vk_token,"465197045")
yd = YaDisk(ya_token)
yd.create_folder()
yd.upload_photos()









