import requests
import argparse
import configparser
from Todo import Todo
from TodoDAO import TodoDAO

def main():
    parser = argparse.ArgumentParser(description="Un script vraiment bien ...")    
    conf = configparser.ConfigParser()
    parser.add_argument('-c','--config',help="configuration file",default="config.ini")
    args = parser.parse_args()

    print(args.config)
    conf.read(args.config)
    print(conf['DB']['db_file'])
    
    dao = TodoDAO(conf['DB']['db_file'])
    # todos =dao.getAll()
    # for todo in todos:
    #     print(todo.title)

    # t = Todo(title="Le titre",completed=True)
    # dao.save(t)


    response = requests.get(conf['API']['data_url'])
    data = response.json()

    for d in data:
        del d['id']
        d['completed'] = int(d['completed'])
        todo = Todo(**d)
        dao.save(todo)

if __name__=='__main__':
    main()
