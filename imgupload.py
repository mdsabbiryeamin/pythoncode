import base64
import requests


wp_user ='yeamin'
wp_pass ='2wXc 79Og ElzL gVek S327 JYeX'
wp_credential = f'{wp_user}:{wp_pass} '
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}




def media_upload(image):
    media_url = 'https://attar.local/wp-json/wp/v2/media'
    files = {'file':open(image,'rb')}
    resp=requests.post(media_url,files=files,headers=wp_headers,verify=False)
    print(resp.json())

  
media_upload('img1.jpq')