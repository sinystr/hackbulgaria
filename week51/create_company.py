import sqlite3

db = sqlite3.connect("company.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    company_members(id INTEGER PRIMARY KEY, name TEXT,
    monthly_salary INTEGER, yearly_bonus INTEGER,
    position TEXT)
''')

users = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
         ("Rado Rado", 500, 0, "Technical Support Intern"),
         ("Ivo Ivo", 10000, 100000, "CEO"),
         ("Petar Petrov", 3000, 1000, "Marketing Manager"),
         ("Maria Georgieva", 8000, 10000, "COO")]

cursor.executemany('''
    INSERT INTO company_members(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', users)

db.commit()
db.close()
