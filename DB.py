import sqlite3

class DataBase:
    def __init__(self):
        self.connect = None
        self.cursor = None # 설명해주는 아이 데터베이스에 내가 만든 내용 번역해주는 아이 

        self.initDb()
        self.initTable_member()
        self.initTable_list()
        self.initTable_video()

        self.result = None
        self.video = None

    def initDb(self):
        self.connect = sqlite3.connect("src/stageus.db")  # 데이터 베이스 연결 ( 만약에 없다면, 생성하고 연결 )
        self.cursor = self.connect.cursor()

    def initTable_member(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS member (sequence INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, pw TEXT, name TEXT,phonenumber INTEGER); ")

    def initTable_list(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS list (sequence INTEGER PRIMARY KEY AUTOINCREMENT, listname TEXT, user INTEGER); ")

    def initTable_video(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS video (sequence INTEGER PRIMARY KEY AUTOINCREMENT, videourl TEXT, listnum INTEGER); ")

    def insertData(self,table,colum,value):
        sql = "INSERT INTO " + table + "("
        for index in range(0,len(colum)):
            sql += colum[index]
            if index >= 0 and index + 1 != len(colum):
                sql += ","
        sql += ") VALUES("
        for index in range(0,len(value)):
            sql += "?"
            if index >= 0 and index + 1 != len(value):
                sql += ","
        sql += ");"
        self.cursor.execute(sql,value)
        self.connect.commit()

    def deleteData(self,table,colum,value):
        sql = "DELETE FROM " + table
        if len(colum) != 0:
            sql +=" WHERE "
            for index in range(0, len(colum)):
                sql += colum[index] + "=" + "?"
                if index >= 0 and index + 1 != len(colum):
                    sql += " and "
                if index + 1 == len(colum):
                    sql += ";"
        print(sql)
        self.cursor.execute(sql,value) #WHERE 뒤에는 조건이다. 
        self.connect.commit()

    def readData(self,table,colum,value):
        sql = "SELECT * FROM " + table
        if len(colum) != 0:
            sql +=" WHERE "
            for index in range(0, len(colum)):
                sql += colum[index] + "=" + "?"
                if index >= 0 and index + 1 != len(colum):
                    sql += " and "
                if index + 1 == len(colum):
                    sql += ";"

        self.cursor.execute(sql,value)
        self.result = self.cursor.fetchall()

        if len(self.result) == 0:
            return False
        else:
            return True

    def readDataVideoList(self,_listNum): #List페이지에서 result값이 변하면 안되기 때문에 넣었음 
        memberData = [_listNum]
        self.cursor.execute("SELECT sequence, videourl FROM video WHERE listnum=?;", memberData)
        self.video = self.cursor.fetchall()

        if len(self.video) == 0:
            print(2)
            return False
        else:
            print(3)
            return True












    #     self.cursor.execute(sql)
    #     # self.cursor.execute("SELECT * FROM member WHERE id=? and pw=?;") # *는 전체컬럼값 , 일부만 가져오고 싶으면 id,pw를 쓰면 아이디와 패스워드가 가져와진다. 
    #     self.result = self.cursor.fetchall() # 모든 것을 우리가 볼 수 있는 단어로 패치하겠다는 문구 
    #     # print(result[0][0]) # 가져오는 것은 이차원 리스트라고 생각하면 됨 , 첫번째는 로우 값, 0,0은 아이디, 0,1은 비밀번호가 될 것이다. 

    #     if len(self.result) == 0: #로그인 실패
    #         return False
    #     else:
    #         return True



