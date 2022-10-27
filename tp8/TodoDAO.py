import sqlite3

from Todo import Todo



class TodoDAO:
    
    def __init__(self,db_file):
        self._con = sqlite3.connect(db_file)

    def getAll(self):
        cur = self._con.cursor()
        res = cur.execute("SELECT * FROM todos_tbl")
        for id,user_id,title,completed in res.fetchall():
            todo = Todo(id=id,userId=user_id,title=title,completed=completed)
            yield todo

    def save(self,todo):
        cur = self._con.cursor()
        query = f"""
        INSERT INTO todos_tbl(user_id,title,completed) 
        VALUES ({todo.userId},'{todo.title}',{todo.completed})
        """
        cur.execute(query)
        self._con.commit()

    def __del__(self):
        self._con.close()



