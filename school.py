import sqlite3
conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()



def students_from_city(db, city):
    query = "SELECT first_name FROM students WHERE birth_city = ?"
    db.execute(query, (city,))
    students = db.fetchall()
    return students









# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
#
# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
 #db = conn.cursor()
print(students_from_city(db, 'London'))
