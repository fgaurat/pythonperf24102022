import functools
from pprint import pprint
import requests
import asyncio
from multiprocessing.pool import ThreadPool
from requests_html import AsyncHTMLSession


async def download_without_async(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,functools.partial(requests.get,url))
    logfile = url.split('/')[-1]
    print(logfile)
    with open(logfile,'w') as f:
        print(response.text,file=f)


async def download(url):
    logfile = url.split('/')[-1]
    asession = AsyncHTMLSession()
    response = await asession.get(url)
    with open(logfile,'w') as f:
        print(response.text,file=f)


async def main():
    urls = [f"https://logs.eolem.com/apache_logs_{i:02d}.log" for i in range(1,11)]
    
    # download_tasks=[download(url) for url in urls]
    download_tasks = map(download,urls)


    r = await asyncio.gather(*download_tasks)



if __name__=='__main__':
    asyncio.run(main())
