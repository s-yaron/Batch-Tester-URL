import requests
import sys
import threading
import queue

list_name = sys.argv[1]
num = int(sys.argv[2])

quit = queue.Queue()
threading_num = num

url_list = open(list_name,'r')
lines = url_list.readlines()
url_list.close()
for line in lines:
    line = line.rstrip()
    quit.put(line)


def crawler():
    while not quit.empty():
        url = quit.get()
        try:
            requests.packages.urllib3.disable_warnings()
            content = requests.get(url, verify=False, allow_redirects=True, timeout=10)
            if content.status_code == 200:
                print (url,"alive")
        except requests.RequestException as e:
            print (url,"broken")

if __name__ == '__main__':
    for i in range(threading_num):
        t = threading.Thread(target=crawler)
        t.start()
