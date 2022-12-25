from flask import Flask, render_template,request,url_for,redirect
import cx_Oracle
import random




app = Flask(__name__)

# =======For rendering the index.html files=================
@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")

# =========For rendering the admin form page================
@app.route("/admin")
def adminpage():
    return render_template("admin.html")

# ===============for inserting the data into database from createform file========
@app.route("/add3", methods=['POST'])
def adminform():
    #======making connection with oracle database============
    conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
    cur = conn.cursor()


    aregno = request.form['aregno']
    name = request.form['name']
    gender = request.form['gender']
    Department = request.form['Department']
    email = request.form['email']
    
    datatuple3 = (aregno,name,gender,Department,email)
    datatuple3 = tuple(datatuple3)
    data3 = []
    data3.append(datatuple3)

    cur.executemany( """INSERT INTO "SYSTEM"."ADMIN"(aregno, name, gender, Department, email) VALUES (:1, :2, :3, :4, :5)""",data3)

    conn.commit()

    return "Your Data inserted successfully!"
    

# =======For rendering the createform.html files=================
@app.route("/createform")
def cform():
    return render_template("createform.html")


# ===============for inserting the data into database from createform file========
@app.route("/add", methods=['POST'])
def studentform():
    #======making connection with oracle database============
    conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
    cur = conn.cursor()


    regno = request.form['regno']
    name = request.form['name']
    gender = request.form['gender']
    dob = request.form['dob']
    city = request.form['city']
    state = request.form['state']
    country = request.form['country']
            

    datatuple = (regno,name,gender,dob,city,state,country)
    datatuple = tuple(datatuple)
    data = []
    data.append(datatuple)

    cur.executemany( """INSERT INTO "SYSTEM"."STUDENT"(regno, name, gender, dob, city, state, country) VALUES (:1, :2, :3, :4, :5, :6, :7)""",data)

    conn.commit()

    return "Your Data inserted successfully!"
    

# =======For rendering the hosteldetails.html files=================
@app.route("/HostelDetail")
def hostelform():
    return render_template("HostelDetail.html")

# ===============for inserting the data into database from createform file========
@app.route("/add2", methods=['POST'])
def hostelsubmit():
    #======making connection with oracle database============
    conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
    cur = conn.cursor()

# ==========for Hostel table=====================
    regno = request.form['regno']
    year = request.form['year']
    branch = request.form['branch']

    

    

    # creating the random number which is unique in certain range
    # list1 = []
    # for i in range(111,500):
    #     hid = random.randint(111,500)
    #     if hid not in list1:
    #         list1.append(hid)

    # for hid in list1:
    #     if hid not in list1:
    #         return hid

# =========creating list and tuples to insert the data in table hostel=================
    datatuple1 = (regno,year,branch)
    datatuple1 = tuple(datatuple1)
    data1 = []
    data1.append(datatuple1)

    cur.executemany( """INSERT INTO "SYSTEM"."HOSTEL"(regno, year,branch) VALUES (:1, :2, :3)""",data1)
    conn.commit()

# ==========for block table=====================
    # noofyear = request.form['year']
    # list2 = []
    # for i in range(1,57):
    #     if noofyear == 1:
    #         roomno = random.randint(1,15)
    #         if roomno not in list2:
    #             list2.append(roomno)
    #     elif noofyear ==2:  
    #         roomno = random.randint(15,30)
    #         if roomno not in list2:
    #             list2.append(roomno)  
    #     elif noofyear ==3:  
    #         roomno = random.randint(30,45) 
    #         if roomno not in list2:
    #             list2.append(roomno) 
    #     elif noofyear ==4:  
    #         roomno = random.randint(45,57)
    #         if roomno not in list2:
    #             list2.append(roomno)  

    #     for roomno in list2:
    #         if roomno not in list2:
    #             return roomno

    roomno = random.randint(1,15)

# =========creating list and tuples to insert the data in table block=================
    datatuple2 = (branch,year,roomno,regno)
    datatuple2 = tuple(datatuple2)
    data2 = []
    data2.append(datatuple2)

    cur.executemany( """INSERT INTO "SYSTEM"."BLOCK"(bname,floor,roomno,regno) VALUES (:1, :2, :3, :4)""",data2)

    conn.commit()

    return "Your Data inserted successfully!"
    

# ================Fetching data from different tables=================

# ================for student table==========================



@app.route("/showdata")
def tabledata():
    conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
    cur = conn.cursor()
# ====for fetching datafrom student table==========
    sql_fetch = """
        SELECT * FROM STUDENT
       """
    cur.execute(sql_fetch)
    sdata = cur.fetchall()
    
# ====for fetching datafrom hostel table==========
    sql_fetch1 = """
        SELECT * FROM HOSTEL
       """
    cur.execute(sql_fetch1)
    sdata1 = cur.fetchall()

# ====for fetching student room , floor and block==========
    sql_fetch2 = """
        SELECT * from BLOCK
       """
    cur.execute(sql_fetch2)
    sdata2 = cur.fetchall()

# ====for fetching Admin details========== 
    sql_fetch3 = """
        SELECT * from ADMIN
       """
    cur.execute(sql_fetch3)
    sdata3 = cur.fetchall()

    return render_template("showdata.html", sdata=sdata, sdata1=sdata1, sdata2=sdata2, sdata3=sdata3)

# =============================Different HTML pages =====================
@app.route("/block")
def blockpage():
    return render_template("block.html")


@app.route("/about")
def aboutpage():
    return render_template("about.html")


@app.route("/services")
def servicespage():
    return render_template("services.html")



# ======================for runnin the server========================
if __name__ == "__main__":
    app.run(debug=True)


# ========================for testing the syntax=========================

