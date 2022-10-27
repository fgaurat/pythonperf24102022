
from pprint import pprint
import requests
from multiprocessing.pool import ThreadPool

def download(url):
    response = requests.get(url)
    logfile = url.split('/')[-1]
    print(logfile)
    with open(logfile,'w') as f:
        print(response.text,file=f)


def main():
    urls = [f"https://logs.eolem.com/apache_logs_{i:02d}.log" for i in range(1,11)]
    pprint(urls)


    with ThreadPool(5) as th:
        th.map(download,urls)

if __name__=='__main__':
    main()
