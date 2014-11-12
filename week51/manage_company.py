import sqlite3


def list_employees(db, cursor):
    cursor.execute('''SELECT id, name, position
                      FROM company_members''')
    for row in cursor:
        id = row['id']
        name = row['name']
        position = row['position']
        print('{0} - {1} - {2}'.format(id, name, position))


def add_employee(db, cursor):
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")
    cursor.execute('''
    INSERT INTO company_members(name, monthly_salary, yearly_bonus, position)
           VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
    db.commit()


def update_employee(db, cursor, id):
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")
    cursor.execute('''UPDATE company_members
    SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
    WHERE id = ? ''', (name, monthly_salary, yearly_bonus, position, id))
    db.commit()


def delete_employee(db, cursor, id):

    cursor.execute('''SELECT name FROM company_members
                      WHERE id=?''', (id))
    db.commit()
    user = cursor.fetchone()

    cursor.execute('''DELETE FROM company_members WHERE id = ? ''', (id))
    db.commit()
    print('{} was deleted!'.format(user['name']))


def monthly_spending(db, cursor):
    cursor.execute('''SELECT monthly_salary
                      FROM company_members''')
    money_spend = 0
    for row in cursor:
        money_spend += row['monthly_salary']
    print('The company is spending ${} every month!'.format(money_spend))


def yearly_spending(db, cursor):
    cursor.execute('''SELECT yearly_bonus, monthly_salary
                      FROM company_members''')
    money_spend = 0
    for row in cursor:
        salaries = row['monthly_salary'] * 12
        bonus = row['yearly_bonus']
        money_spend += salaries + bonus
    print('The company is spending ${} every year!'.format(money_spend))


def main():
    db = sqlite3.connect("company.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    command = input("command> ")
    command_properties = command.split(' ')

    if command_properties[0] == "list_employees":
        list_employees(db, cursor)
    elif command_properties[0] == "monthly_spending":
        monthly_spending(db, cursor)
    elif command_properties[0] == "yearly_spending":
        yearly_spending(db, cursor)
    elif command_properties[0] == "delete_employee":
        delete_employee(db, cursor, command_properties[1])
    elif command_properties[0] == "add_employee":
        add_employee(db, cursor)
    elif command_properties[0] == "update_employee":
        update_employee(db, cursor, command_properties[1])
    else:
        print('Invalid Command')
    main()

if __name__ == '__main__':
    main()
