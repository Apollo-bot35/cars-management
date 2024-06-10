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
    
    def getdata(self):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from customers")
        data=curs.fetchall()
        return data
    
    
    def searchresult(self,nm):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from cars where modelnm='%s'" %nm)
        data=curs.fetchone()
        car={}

        if data:
            car['carid']=data[0]
            car['company']=data[2]
            car['price']=data[3]
        else:
            car['carid']='not found'
            car['company']='not found'
            car['price']=0
        con.close()

        return car
    
    def searchresults(self,ne):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from customers where custname='%s'" %ne)
        data=curs.fetchone()
        customer={}

        if data:
            customer['custid']=data[0]
            customer['address']=data[2]
            customer['phoneno']=data[3]
        else:
            customer['custid']='not found'
            customer['address']='not found'
            customer['phoneno']='not found'
        con.close()

        return customer

        
    def changecarpri(self,nm,pri):
        try:
            con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
            curs=con.cursor()
            curs.execute("update cars set price=%.2f where modelnm='%s'" %(pri,nm))
            con.commit()
            stat='success'
        except:
            stat='failed'

        return stat
    

    def changephn(self,nm,no):
        try:
            con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
            curs=con.cursor()
            curs.execute("update customers set phoneno=%d where custname='%s'" %(no,nm))
            con.commit()
            stat='success'
        except:
            stat='failed'

        return stat



