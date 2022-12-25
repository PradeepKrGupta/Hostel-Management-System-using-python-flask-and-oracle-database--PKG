# import cx_Oracle
# import re
# from flask import Flask, render_template, request, url_for, redirect

# app = Flask(__name__)

# conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
# cur = conn.cursor()

# @app.route("/index")
# def home():
#     return render_template("index.html")
    

# @app.route('/createform')
# def edited():
#     conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
#     cur = conn.cursor()

# print(conn.version)
# print()
# print("Your Database has been connected successfully")

    

    # regno = request.form['regno']
    # name = request.form['name']
    # gender = request.form['gender']
    # dob = request.form['dob']
    # city = request.form['city']
    # state = request.form['state']
    # country = request.form['country']

    # sql_insert = """INSERT INTO "SYSTEM"."student" VALUES
    #             (regno, name, gender, dob, city, state, country)"""

    # cur.execute(sql_insert, {'regno': regno, 'name': name,
    #                         'gender': gender, 'dob': dob, 'city': city,'state': state,'country': country})
    # conn.commit()



# @app.route("/createform", methods=["GET", "POST"])
# def studentform():
#     return render_template("createform.html")


# @app.route('/createform', methods=['POST', 'GET'])
# def postdata():
#     return redirect(url_for('edited'))


# for inserting the data into database.......
# sql_insert = """
# INSERT INTO "SYSTEM"."CEO_DETAILS" (FIRST_NAME, LAST_NAME, COMPANY, AGE) VALUES (
#     'bruce', 
#     'banner', 
#     'hulkindustry', 
#     '65'
# )
# """
# cur.execute(sql_insert)
# conn.commit()
# print("ROW INSERTED SUCCESSFULLY... ")
# if __name__ == "__main__":
#     app.run(debug=True)


# =========================================================================


# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'd369342136ecd032f8b4a930b6bb2e0e'


# @app.route('/add')
# def edited():
#     connect = cx_Oracle.connect("********", "********", "******/XE")
#     cursor = connect.cursor()

#     cod_ed = request.form['cod_ed']
#     nome_ed = request.form['nome_ed']
#     endereco = request.form['endereco']
#     telefone = request.form['telefone']
#     cidade = request.form['cidade']
#     execute = """INSERT INTO editor VALUES
#             (:cod_ed, :nome_ed, :endereco, :telefone, :cidade)"""
#     cursor.execute(execute, {'cod_ed': cod_ed, 'nome_ed': nome_ed,
#                    'endereco': endereco, 'telefone': telefone, 'cidade': cidade})
#     connect.commit()


# @app.route('/', methods=['GET', 'POST'])
# def add_data():
#     return render_template('forms.html')


# @app.route('/post_data', methods=['GET', 'POST'])
# def post_data():
#     return redirect(url_for('edited'))


# if __name__ == "__main__":
#     app.run(host='localhost', port=8000, debug=True)
