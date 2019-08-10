import sqlite3


# you can pass in file
# inmemory db ':memory:'

conn = sqlite3.connect('employee.db')
c = conn.cursor()

'''c.execute("""Create Table employees(
        first text,
        last text,
        pay integer
        )""")'''

c.execute("INSERT INTO employees VALUES('maks','d','1')")
conn.commit()

# c.execute("insert into eployees values(?, ?, ?)",emp1.first, emp1.last, emp1.pay)
# c.commit()
# returns a dict :key_name
# c.execute("insert into eployees values(:first, :last, :pay)",emp1.first, emp1.last, emp1.pay)
# c.commit()

c.execute("Select * FROM employees")
# returns all with fetch all or fetchmany(amount here)
print(c.fetchall())
conn.commit()
conn.close()

def insert(emp):
    with conn:
        c.execute("insert into eployees values(:first, :last, :pay)",emp.first, emp.last, emp.pay)
        
        
def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=last",{'last':lastname})
    return c.fetchall()

def update_employee_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last """, {'first': emp.first, 'last': emp.last, 'pay':emp.pay})