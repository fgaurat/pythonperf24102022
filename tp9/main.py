import requests
from bs4 import BeautifulSoup
import glob
import re

def main():
    log_files =glob.glob('*.log')
    
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                m = re.findall(r'\"\s(\d{3})\s',line)
                if '404' in m:
                    print(line)



def main_download():
    url = 'https://logs.eolem.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = [a['href']
             for a in soup.find_all('a') 
             if a['href'].endswith('.log')]

    for filename in links:
        url_log = f"{url}{filename}"
        response = requests.get(url_log)
        with open(filename,'w') as f:
            print(response.text,file=f)
            

if __name__ == '__main__':
    main()
