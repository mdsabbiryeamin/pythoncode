import requests
import base64
wp_user ='attarstorebd'
wp_pass ='ePFC AdLT OUis Hyrk 1SKZ m1cn'
wp_credential = f'{wp_user}:{wp_pass} '
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

page_data={
    'title':'New Page',
    'content':'How is attar different from perfume',
    'slug':'How is attar different from perfume',
    'status':'publish'
}

wp_page_url = 'https://localhost/newsitepy/wp-json/wp/v2/pages'
res = requests.post(wp_page_url, data=page_data, headers=wp_headers, verify=False)
print(res.status_code)
print(res.json())