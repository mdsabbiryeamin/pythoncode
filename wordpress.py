from requests import get,post 
import json
import base64
server_url ='https://mobile-phone-server.vercel.app/phones'
res = get(server_url)
if res.status_code == 200:
    data =res.json()
    phones =data.get('RECORDS')

wp_user ='yeaminsabbir'
wp_pass ='6FOs 3HbE C0PG OJ2r CmkC xCdR'
wp_credential = f'{wp_user}:{wp_pass} '
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}





def post_titel(titel):
    pastitel=f'<!-- wp:heading --><h2>{titel}</h2><!-- /wp:heading -->'    
    return pastitel 

def media_from_url(picture,name ):
    cods = f'<!-- wp:image {{"align":"center","width":257,"height":341,"sizeSlug":"large"}} -->'\
           f'<figure class="wp-block-image aligncenter size-large is-resized"><img src="{picture}" alt="{name}" width="257" height="341"/></figure><!-- /wp:image -->'
 
    return cods    

def wp_table(dictionary):
    codes='<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for name, namber in dictionary.items():
        tr_td_data =f'<tr><td>{name}</td><td>{namber}</td></tr>'
        codes +=tr_td_data  
    codes +='</tbody></table></figure><!-- /wp:table -->'
    return codes


def wp_paragraph(text):
    codes =f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'  
    return codes


def content_string(*args):
        final =''
        for arg in args:
            final +=arg
        return final    
def sluggify(name):
    code =name.replace(' ','-')
    return code

def create_wp_post(title,content,slug):
    api_url='https://bestperfumefragrance.com/wp-json/wp/v2/posts'        
                  
    post_data = {
    'title':title,
    'content':content,
    'categories':'3',
    'slug':slug,
    'status':'draft'
    }
    response =post(api_url,wp_headers,json=post_data)

for phone in phones:
    name = phone.get('name').title()
    released = phone.get('released_at').lower().replace("Released ",'')
    chipsaet =phone.get('chipset')
    body =phone.get('body')
    os = phone.get('os')
    picture =phone.get('picture')

    dictionary= {
        'name':name,
        'released':released,
        'chipset':chipsaet,
        'body':body
         
    }
  
    fist_paragr =f'{name} has been {released}.'\
                 f'It comes with {chipsaet} chipset. The body of this mobile is {body}'\
                 f'{os} is the built in android version.'
             

    post_titels=post_titel(name)
    img =media_from_url(picture,name)
    article_paragraph =wp_paragraph(fist_paragr)      
    phone_table =wp_table(dictionary)           

##specifications section ...//
    specifications_string = phone.get('specifications')
    specifications = json.loads(specifications_string)
    secont_table = wp_table(specifications)

    content =content_string(post_titels,img,article_paragraph,phone_table,secont_table)

    create_wp_post(name,content,sluggify(name))

