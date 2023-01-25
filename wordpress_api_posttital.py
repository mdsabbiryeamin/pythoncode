from httpx import get
from pprint import  pprint
base_url = 'https://carcareguider.com/wp-json/wp/v2'

page_api = f'{base_url}/pages'
r = get(page_api)
api_data = r.json()

for page in api_data:
    try:
       print(page.get('link'))
   
    except:
        print('Page Not Found')
  
### new file open and new text add...///
   
for pagelink in api_data:
    file=open('sitePagelink','a+')
    file.writelines(pagelink.get('link')+'\n')
    file.close() 