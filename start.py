# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")

# else:2
#        print("b is not greater than a")

# my_list=['apple','banana','cherry']
# print(my_list)

# frist_name = input("Enter You frist name :")
# last_name = input('Enter Your last name :')
# full_name = frist_name +" "+ last_name
# print( full_name)


# usd =int(input( 'amount'))
# print(usd,type(usd))

# usd_namber =float(input( 'amount'))
# usd_namber1=usd_namber*100
# print(usd_namber1,type(usd_namber1))

# name=input('your name: ')
# age=input('Enter your age')
# cv=f'Hi, I am {name}. MY {age} old.'
# print(cv)


### Escape Character////
#  print('He says,"He is going to cox\"s Bazar')
#  fprint("Hara Gumbad Jo Dekhoge\n Zamana Bhool Jaoge Hara Gumbad\n\t Jo Dekhoge Zamana Bhool Jaoge ")   


### If Else Condition////
# namber= int(input('Enter Your Namber :'))
# if namber >=18:
#     print("YOU NID CARD  RESITSON")

# else:
#     print('YOU NID CARD NOT RESITSON')    



# name=input('Enter your name : ')
# roll_namber= int(input('Enter Your Roll namber : '))
# dip=input('Enter You Technology : ')
# session=int(input('Enter Your Session : ')) 



# name = input('Enter Your Name :')
# gender = input('Enter Your  Gender (m/f):')
# country=input('Enter Your Country Namer :')

# if gender =='m':
#     profession ='actor'
#     pronoun ='He'
#     known_as ='nayok'

#     # print(f'{name} is an {profession} of {country}.{pronoun} { known_as} ')
# else:    
#     profession ='actor'
#     pronoun ='She'
#     Known_as ='nayika'
    
# print(f'{name} is an {profession} of {country}.{pronoun} is {Known_as}')

#### And LOGICAL OPERATORS///
##Al condions must be true...
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

#### OR LOGICAL OPERATORS////

# marks =int(input('Enter Marks:'))
# weight=int(input('Enter weight:'))

# if marks >= 80 or weight <=20:
#     print('You will get a chocklet')
# else:
#     print('You get less marks and over weight')    


### OR LOGICAL OPERATORS////
### Any one condtion must be true...

# marks =int(input('Enter Marks:'))
# weight=int(input('Enter weight:'))

# if marks >= 80 or weight <=20:
#     print('You will get a chocklet')
# else:
#     print('You get less marks and over weight')  




#### Introduction to List ///
# jalanta=['jalanta Khalil',45,'nayok','Rain']

# name = jalanta[0]
# age = jalanta[1]
# profession = jalanta[2]
# nayika = jalanta[3]
# print(f'{name} is {profession} of {age} years who works with {nayika}')

### Len Function//// 
# list = [1,2,3,4,5,6,7,8,9,10]
# namber_list=len(list)
# print(namber_list)
# print(list[2:4])
# print(list[-1])
# print(list[2:])
# print(list[:7])
# print(type(list))

### Logical operators Example///

# salary= int(input('Enter your salary: '))
# years_of_services = float(input('Enter years of services:'))

# if years_of_services >= 5 and salary >=20000:
#     bonus = 0.05
#     net_salary = salary + salary * bonus
    
#     print('Your net salary with bonus',net_salary)

# else:
#      print('You get only your salary',salary,'USD')

 

### Change the Element of list///
# name = ['yeamin','sabbir','al amin','saimoon']
# name[1]='Tarek Aziz'
# print(name)
# name[0:2] =['MD YEAMIN SABBIR'] # list কয়েকটি আইটেম পরিবতন করতে হলে [] দিয়ে করতে হবে।   
# print(name)

### Adding Element to the list///
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# name = []
# name.append('MD')
# name.append('Yeamin')
# name.append('Sabbir')
# name.insert(2,'MD.') #insert =(index number,"object")
# print(name)

###Remove item///
# thisset = [1,2,3,4,5,6,7,8,9]
# thisset.remove(5)
# print(thisset)
# name = ['yeamin','sabbir','al-amin']
# name.pop()
# print(name)
# name_list =  ['yeamin','sabbir','al-amin']
# del name_list[1]
# print(name_list)


# namber= [1,2,3,4,5]
# namber_one = [6,7,8,9,10]
# namber.extend(namber_one)
# print(namber)
# ###list items by using a for loop///
# list =[1,2,3,4,5,6,7,8,9,10]
# for x in list:
#     print(x)
 
####  List Sorting and Joining///

# list_item =['Yeamin','Sabbir','Al-Amin','Saimoon']
# list_sum= ' + '.join(list_item)
# print(list_sum) 

# namber = [4,6,34,3,8,88,13,2,1,5,7,9,11,12,10,14,16,15]
# namber.sort()
# print(namber)
# namber.sort(reverse=True)
# print(namber)

#### While Loop

# number = int(input('Enter Number: '))
# start = 1
# while start <= 10:
#     print(number,'x',start,'=',number * start)
#     start = start + 1

 
# years = [1988.3214,2022,1956,1656]
# i =0
# while i < len(years):
#     if years[i] % 4 == 0:
#         print(years[i],'is leap year')
#     i=i+1



# number = [1,2,3,4,5,67,8,9,55,44,55]
# i = 0
# while i < len(number):
#     if number[i] % 2 == 0:
#         print(number[i], 'Event number')
#     i =i+1

### Login setup///

# name = input('Enter Your Name : ')
# pas = input('Enter Your password : ')
# f_name = ['20',
#           'Bangla',
#           'Bangladesh',
#           '01748078171'
        
#          ]

# yeamin= f' My Name {name.title()}.I am {f_name[0]} years old. My language {f_name[1]}.My Country {f_name[2]}.My mobile Namber {f_name[-1]} '
# if name == 'yeamin' and pas == '123':
#     print(yeamin)     

# sabbir=[  '30',
#           'English',
#           'Bangladesh',
#           '01914336754'
        
#          ]
# name_sabbir= f' My Name {name.title()}.I am {sabbir[0]} years old. My language {sabbir[1]}.My Country {sabbir[2]}.My mobile Namber {sabbir[-1]} '

# if name == 'sabbir' and pas == '444':
#     print(name_sabbir)
 

# namber = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20]
# ]
# i = 0
# while i < len(namber):
#      namber_list =namber[i]
#      name = namber_list[0]
#      gender = namber_list[1]
#      country =namber_list[2]
#      list = namber_list[3]
#      na_list   = namber_list[4]
    

#      print(name,gender,country,list,na_list,sep=" <=|=> ")
#      i+=1

### Add or Update  Dictionary Items///
# name ={
#     'fname':'MD Yeamin',
#     'age':20,
#     'fatherName':'Salam'
# }
# name['fname']='MD Yeamin Sabbir' 
# print(name)

# name.update({'age':22})
# print(name) 

# users =[
#     {
#         'name':'MD Yeamin Sabbir',
#         'password':12345,
#         'id':1,
#         'us':{
#             'fname':'sabbir',
#             'roll':12,
#             'classe':{
#                 'fist':4,
                
#                      },
#         },
#     }
# ]
# for user in users:
#     name=user.get('name')
#     pas=user.get('password')
#     ids=user.get('id')
#     use=user.get('us').get('fname')
#     rol=user.get('us').get('roll')
#     classer=user.get('us').get('classe').get('fist')
   
#     sentense=f'My Name {name}.MY FB password {pas}.User id {ids}.us Full Name {use}.My Roll Namber {rol}. My Class {classer}'
#     print(sentense)






# users_name = [
#     {
#         'name':'MD Al-Amin',
#         'password':12795,
#         'id':3,
#         'tital':{ 
#                  'h1':'MY Name Yeamin Sabbir',
#                  'h2':'MY Father Name Abdus Salam',
                
#                  'seo':{
#                         'one page':'best Contant post your site ',
#                         'off page':'off page seo'
#                        }
#         }   
#     }
    
# ]

# for name in users_name:
#     fname=name.get('name')
#     password=name.get('password')
#     id=name.get('id')
#     tital=name.get('tital').get('h1')
#     seo=name.get('tital').get('seo').get('one page')
#     seopage=name.get('tital').get('seo').get('off page')  

# user =f'My Name {fname}. FB password {password}. My id Namber {id}.Page tital {tital}.Best SEO Paktice {seo}.Best SEO {seopage}.'
# print(user)


### index Namber দিয়া elemanc  
# namber = [
#     {
#         'namber':12,
#         'fname': {
#             'name':'Yeamin'
#         }
#     }, n
#     {
#         'rol':21
#     }
# ]

# na=namber[0].get('namber')
# nam=namber[0].get('fname').get('name')
# sw=namber[1].get('rol')
# sen=f'Your Namber {na}.Your Name :{nam}.MY Roll Namber :{sw}'
# print(sen)





# user = [
#     {
#         'userName':'MD Yeamin Sabbir',
#         'password':1221,
#         'userData':{
#             'fristName':'MD Yeamin',
#             'lastName':'Sabbir',
#             'DPT':'AIDT',
#             'roll':580441,
#             'subject':['interior Desine-2', 'CAD-1','History of AIDT','Persoective Drawing','Business Organization','Basic Estimating Costing','Fundamental Constrction Process'],
#         },
#         'famileData':{
#             'fatherName':'MD Abdus Salam',
#             'motherName':'Parvin Aktar',
#             'batherName':[
#                 'MD Al-Amin parvis',
#                 'MD Saymoon'
#            ]
#         }
#     },
#     {
#         'userName':'MD Al-Amain',
#         'password':15641,
#         'userData':{
#             'fristName':'MD Amain',
#             'lastName':'Parvis',
#             'DPT':'Business',
#             'roll':125385,
#             'subject':['Business Organization','Math','English'],
#         },
#         'famileData':{
#             'fatherName':'MD Abdus Salam',
#             'matherName':'Parvin Aktar',
#             'batherName':[
#                  'MD Yeamin Sabbir',
#                  'MD Saymoon'
#             ]
#         }
#     } 
#  ]
# user_Name = user[0].get('userName')
# user_password = user[0].get('password')
# fristName = user[0].get('userData').get('fristName')
# lastName = user[0].get('userData').get('lastName')
# dpt= user[0].get('userData').get('DPT')
# rollNamber = user[0].get('userData').get('roll')
# subjectName = user[0].get('userData').get('subject')
# fatherName = user[0].get('famileData').get('fatherName')
# motherName = user[0].get('famileData').get('motherName')
# batherName = user[0].get('famileData').get('batherName')


# sentans = f'User Name {user_Name}.User Password {user_password} .Frist Name {fristName} and last name {lastName}. {user_Name}DPT Name : {dpt}.Roll Namber {rollNamber}. Subject Name {subjectName[:5]}.MY Father Name {fatherName} and Mother Name {motherName}.Bather Name {batherName[0]},{batherName[1]}.  '
# print(sentans)


#### String mathod////

# str1 = 'Python'
# str2 = 'PYTHON'
# str3 = ' '
# print(str1.istitle())
# print(str1.islower())
# print(str3.isspace())

# string1 = 'MD Yeamin Sabbir'
# print(string1.count('a')) #///output : a 2 bar ace.

### Strip Methods ///
# str1 = '------Yeamin Sabbir-----'
# print(str1.strip("-"))

# str2 = r'f:\Name yeamin Sabbir Roll:580411'
# print(str2)


### Center ,ljust,rjust expandtabs ,join methods ...///
# str1 = 'yeamin'
# str2 = 'md \t yeamin'
# str3 = ['sabbir' ,'yeamin']

# print(len(str1))
# print(str1.center(13,"*"))
# print(str1.ljust(14,"+"))

# print(str2.expandtabs(40))
# print(' - '.join(str3))



### String Method Exercise Convert String to URL...///

# def url_string(string):
#     stripped_string = string.strip()
#     lower_case = stripped_string.lower()
#     url = lower_case.replace(' ','-')
#     return url

# print(url_string('MD YEAMIN SABBIR'))    


# def slugtital(text):
#     slug =text.strip().lower().replace(' ','-')
#     while '--' in slug:
#         slug =slug.replace('--','-')

#     return slug

# tital = input('Enter Your Tital : ')
# slug21 =slugtital(tital)
# print(slug21)




#### Unlimited Argument passing...///

# def mulitple_add(*args):
#     total =0
#     for number in args:
#         total+= number
#     return total

# result =mulitple_add(1,2,3)
# print(result)        

#### Convert Tuple to List and item change ... List item convert Tuple ...///

# def number(a,b,c):
#     sum = a+b
#     sam = b+c
#     add =sum+sam
#     return sum,sam,add

# num=number(5,5,1)    

# listitem = list(num)
# listitem[1]=20
# tupleitem=tuple(listitem)
# print(tupleitem)





 #### wordpress post function...///

# def post1(postcontent,heading):
#      paragraph = f" <!-- wp:paragraph --><p>{postcontent} <!-- /wp:paragraph --></p>"
#      headingcode =f'<!-- wp:heading --><h2>{heading}</h2><!-- /wp:heading -->'

#      return paragraph,headingcode

# parag ="You can customise the sizes and color palette according to your preference. We love customised orders! Just let us know your vision and we will be happy to guide you through the process and curate a beautiful artpiece for you."
# heading_content = 'wordpress function'
# postdemo =post1(parag,heading_content) 
# print(postdemo)    

  