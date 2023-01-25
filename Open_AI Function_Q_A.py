import base64
import requests
import openai

wp_user ='yeaminsabbir'
wp_pass ='6FOs 3HbE C0PG OJ2r CmkC xCdR'
wp_credential = f'{wp_user}:{wp_pass} '
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

openai.api_key = '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'

def head(text):
    code =f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def parg(para_text):
    code =f'<!-- wp:paragraph --><p>{para_text}</p><!-- /wp:paragraph -->'
    return code

def media_upload (img):
    media_url = f'https://bestperfumefragrance.com/wp-json/wp/v2/media'
    file = {'file':open(img,'rb')}
    resp=requests.post(media_url,files=file,headers=wp_headers)
    print(resp.json())   


def opneaifun(prompt):
     response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0
    )
     output= response.get('choices')[0].get('text')
     return output
keyword = input('Enter your keyword ')
prompt =f'write three question about {keyword} '
content =parg(opneaifun(f'write short intro about {keyword}'))

questions =opneaifun(prompt)
questions_list =questions.strip().split('\n')
ent_line = 'write a paragraph about it'

qna={}
for qu in questions_list:
    command =f'{qu} {ent_line}'
    answer = opneaifun(command).strip().strip('\n')
    qna[qu]=answer


for key, value in qna.items():
    he = head(key) 
    ans = parg(value)
    temp = he+ans
    content = temp

### wordpass post 
tital=f'most popaler {keyword}  question '
data = {
    'tital':tital.title(),
    'content':content,
    'slug':keyword.replace(' ','-'),
    'status':'draft'
}
api_url='https://bestperfumefragrance.com/wp-json/wp/v2/posts'       
resp =requests.post(api_url,data=data,headers=wp_headers)


media_upload('img.jpq')
