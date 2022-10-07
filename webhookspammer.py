import os, time, threading, requests
os.system("title Webhook spammer made by hellboy;")
os.system("cls")
def spammer():
    web_url=input("Insert ur url webhook: ")
    r = requests.get(web_url)
    name=input("insert username: ")
    message=input("message to spam: ")
    amount=int(input("amount: "))
    for i in range(amount):
        r=requests.post(web_url, json={"content" : message, "username": name})
        requests.session={200, 204}
        if r.status_code in requests.session:
            print("message sent")
            #that's threads you can modify
            for i in range(100):
                threading.Thread(target=spammer, args=(message,web_url,)).start
        elif r.status_code==429:
            print("rate limited")
            time.sleep(r.json()["retry_after"] / 1000)
spammer()
