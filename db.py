import sqlite3

class DataBase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            code Integer,
            kmih Integer,
            price Integer,
            ml7ozat text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,code,kmih,price,ml7ozat):
        self.cur.execute(
            "insert into employees values (NULL,?,?,?,?)",
            (code,kmih,price,ml7ozat)
            )
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    
    def update(self,id,code,kmih,price,ml7ozat):
        self.cur.execute(
            "update employees set code=?,kmih=?,price=?,ml7ozat=? where id=?",
            (code,kmih,price,ml7ozat, id)
            )
        self.con.commit()
    