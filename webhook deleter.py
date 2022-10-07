import requests,os
os.system("cls")
os.system("title Webhook deleter made by hellboy;")
web_url1=input("Insert webhook to delete: ")
detele=requests.get(web_url1)
requests.delete(web_url1)
print("webhook deleted")