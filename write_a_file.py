import requests
text=input('Entrt Your Text : ')
file =open('yeamin.txt',"a+")
file.writelines(text+'\n')
file.close()