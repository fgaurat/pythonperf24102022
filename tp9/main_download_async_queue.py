from pprint import pprint
import asyncio
import threading
from requests_html import AsyncHTMLSession


async def download(q1,q2,worker_id):
    while True:
        data = await q1.get()
        url = data['url']
        print("download",url,worker_id,threading.current_thread().name)
        asession = AsyncHTMLSession()
        response = await asession.get(url)
        d = {'url':url,'text':response.text}
        q2.put_nowait(d)
        q1.task_done()


async def write_log(q2,worker_id):
    while True:
        data = await q2.get()
        url = data['url']
        text = data['text']
        print("write_log",url)
        logfile = url.split('/')[-1]
        logfile+="./logs/"
        with open(logfile,'w') as f:
            print(text,file=f)
        q2.task_done()


async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    urls = [f"https://logs.eolem.com/apache_logs_{i:02d}.log" for i in range(1,11)]

    # download_tasks=[download(url) for url in urls]
    # download_tasks = map(download,urls)

    download_tasks = [asyncio.create_task(download(q1,q2,worker_id)) for worker_id in range(len(urls))]
    writer_tasks = [asyncio.create_task(write_log(q2,worker_id)) for worker_id in range(len(urls))]


    for url in urls:
        d = {'url':url}
        q1.put_nowait(d)

    await q1.join()
    await q2.join()

    [task.cancel() for task in download_tasks]
    [task.cancel() for task in writer_tasks]

if __name__=='__main__':
    asyncio.run(main())
