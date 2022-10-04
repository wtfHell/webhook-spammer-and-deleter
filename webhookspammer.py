from dhooks import Webhook
import time

wbhk=input("insert ur webhook: ")
message=input("insert ur message: ")

while True:
    time.sleep(0)
    wbhk.send(message)
    print("done!")
