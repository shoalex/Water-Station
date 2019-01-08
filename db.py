import sqlite3
from datetime import datetime
import queue
class dbconnect:
    def __init__(self,dbname):
        self.dbname=dbname
    def connect(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cmd = """
        CREATE TABLE IF NOT EXISTS station_status (
        	station_id INT,
        	last_date TEXT,
        	alarm1 INT,
        	alarm2 INT,
        	PRIMARY KEY(station_id)
        );
        """
        cur.execute(cmd)
        conn.commit()
        conn.close()


    def insert(self,id,alarm1,alarm2):
        myqueue = queue.Queue()
        self.select(id,myqueue)
        myqueue=myqueue.get()
        if myqueue:
            del myqueue
            self.update(id, alarm1, alarm2)

        else:
            conn = sqlite3.connect(self.dbname)
            cur = conn.cursor()
            #sql = "INSERT INTO station_status VALUES ({},\"{}\",{},{})".format(id, str(datetime.now()), alarm1, alarm2)
            #print(sql)
            cur.execute(
                "INSERT INTO station_status VALUES ({},\"{}\",{},{})".format(id, str(datetime.now()), alarm1, alarm2))
            conn.commit()
            conn.close()

    def update(self, id, alarm1, alarm2):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #sql="update station_status set last_date=\"{}\" , alarm1={},alarm2={} where station_id={}".format(str(datetime.now()),alarm1,alarm2,id)
        #print(sql)
        cur.execute("update station_status set last_date=\"{}\" , alarm1={},alarm2={} where station_id={}".format(str(datetime.now()),alarm1,alarm2,id))
        conn.commit()
        conn.close()

    def select(self,id,myqueue):
            conn = sqlite3.connect(self.dbname)
            cursor = conn.execute("SELECT * FROM 'station_status' where station_id={}".format(id,))
            queue.Queue.put(myqueue,cursor.fetchall())
            conn.close()


    
