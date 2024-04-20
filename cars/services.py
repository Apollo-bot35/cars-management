import pymysql

class Carservices():
    def addcust(self,id,nm,ar,no):
        try:
            con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
            curs=con.cursor()
            curs.execute("insert into customers values(%d,'%s','%s',%d)" %(id,nm,ar,no))
            con.commit()
            stat="success"
        except:
            stat="failed"

        return stat
    

    def login2(self,id,pw):
        try:
            con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
            curs=con.cursor()
            curs.execute("insert into Users values('%s','%s')" %(id,pw))
            con.commit()
            stat="success"
        except:
            stat="failed"

        return stat


    def addca(self,id,mn,co,pr):
        try:
            con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
            curs=con.cursor()
            curs.execute("insert into cars values(%d,'%s','%s',%d)" %(id,mn,co,pr))
            con.commit()
            stat="success"
        except:
            stat="failed"

        return stat



    def getalldata(self):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from cars")
        data=curs.fetchall()
        return data