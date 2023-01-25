import requests
import base64
wp_user ='attarstorebd'
wp_pass ='ePFC AdLT OUis Hyrk 1SKZ m1cn'
wp_credential = f'{wp_user}:{wp_pass} '
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

def postfancon(paragraph,h1line):
    code =f' <!-- wp:heading --><h1>{h1line}</h1><!-- /wp:heading --><!-- wp:paragraph --><p>{paragraph}</p><!-- /wp:paragraph -->'
    return code

title_content='How is attar different from perfume'
h1line='How is attar different from perfume'
paragraph_content='Attar and perfume are both types of fragrant products used to enhance the scent of the body or environment. However, there are some key differences between the two.Attar, also known as essential oil perfume, is made by distilling botanical materials, such as flowers, herbs, and spices, in a base of vegetable or animal oils. The resulting attar is a concentrated, natural fragrance that contains the essential oils extracted from the botanicals.'
post_data = {
    'title':title_content,
    'content':postfancon(paragraph_content,h1line),
    'categories':'3',
    'slug':'How is attar different from perfume',
    'status':'publish'
    }
wp_post_url = 'https://localhost/newsitepy/wp-json/wp/v2/posts'

res = requests.post(wp_post_url, data=post_data, headers=wp_headers, verify=False)
print(res.status_code)
print(res.json())
