import requests
page_url='https://developers.google.com'
api_url =f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={page_url}'
link =requests.get(api_url)
if link.status_code == 200:
   print(link.json())
else:
     print('no anser')

