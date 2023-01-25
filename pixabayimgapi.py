from requests import get
from pprint import pprint

pixabayapi ='https://pixabay.com/api/?key=32060522-a4b3e9b385e2d1d455624a8c5&q=yellow+flowers&image_type=photo&pretty=true'
text =get(pixabayapi)
jsonlike =text.json()
hits=jsonlike.get('hits')[0:]

### new file open and new img url add...///
for img in hits:
    img_url=img.get('largeImageURL')
    img =open('img_urlfile.txt','a+')
    img.writelines(img_url+'\n')
    img.close()


  