# from flask import Flask, render_template,request,url_for,redirect

# app = Flask(__name__)

# # =======For rendering the index.html files=================
# @app.route("/index")
# @app.route("/")
# def home():
#     return render_template("index.html")

# # =======For rendering the createform.html files=================
# @app.route("/createform")
# def cform():
#     return render_template("createform.html")

# # =======For rendering the hosteldetails.html files=================
# @app.route("/HostelDetail")
# def hostelform():
#     return render_template("HostelDetail.html")

# if __name__ == "__main__":
#     app.run(debug=True)

import random

print(random.randint(0,100))



# # =========================================
# import random
# print("Hello this is my python prograam")
# l1 =[]
# l2=[]
# l3=[]

# for i in range(1,46):
#     if i not in range(1,15):
#         a = random.randint(1,15)
#         if a not in l1:
#             l1.append(a)
#     if i in range(15,29):
#         a = random.randint(16,29)
#         if a not in l2:
#             l2.append(a)
#     if i in range(29,45):
#         a = random.randint(30,44)
#         if a not in l3:
#             l3.append(a)
    
#     # break

# print("List 1: ",l1)
# print("List 2: ",l2)
# print("List 3: ",l3)

# import random
# l1 = []
# if i in range(111,500):
#    num = random.randint(i)
#    if num not in l1:
#     l1.append(num)

# print(l1)
