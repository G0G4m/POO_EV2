import m_logic.base_method as bm
import sqlite3 as sql

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class user(bm.base_meth):

    def __init__(self,id_user = None,name_user = None, key_user = None):
        self.id_user = id_user
        self.name_user = name_user
        self.key_user = key_user

    def create(self):
        c.execute("INSERT INTO user (name_user,key_user) VALUES (?,?)",(
            self.name_user,
            self.key_user
        ))
        conn.commit()
        self.id_user = c.lastrowid
    
    def update(self):
        c.execute("UPDATE user SET name_user = ?, key_user = ? WHERE id_user = ?",(
            self.name_user,
            self.key_user,
            self.id_user
        ))
    
    