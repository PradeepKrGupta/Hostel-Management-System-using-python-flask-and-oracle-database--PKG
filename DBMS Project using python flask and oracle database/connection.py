import cx_Oracle

conn = cx_Oracle.connect('system/sys@//LAPTOP-LL2H9RBK:1521/xe')
# print(conn.version)
print()
print("Your Database has been connected successfully")

cur = conn.cursor()
# Creating table into database..............
sql_create = """
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER
)
"""
# cur.execute(sql_create)
# print('table created successfully...')


# for inserting the data into database.......
sql_insert = """
INSERT INTO "SYSTEM"."CEO_DETAILS" (FIRST_NAME, LAST_NAME, COMPANY, AGE) VALUES (
    'bruce', 
    'banner', 
    'hulkindustry', 
    '65'
)
"""
# cur.execute(sql_insert)
# conn.commit()
# print("ROW INSERTED SUCCESSFULLY... ")

sql_fetch = """
SELECT * FROM CEO_DETAILS
"""
cur.execute(sql_fetch)
print("Your data is:")
print()
for i in cur:
    print(i)
