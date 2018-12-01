import sqlite3

con = sqlite3.connect('sales.db')
query = """  CREATE TABLE IF NOT EXISTS sales( 
              mbr VARCHAR(10), 
                product VARCHAR(10), 
               amount NUMBER
               ); 
       
          """
con.execute(query)
con.commit()

data = [('lee', 'phone', 50),
        ('kim', 'TV', 100),
        ('park', 'phone2', 20),
        ('song','running', 80)
        ]
stmt = "INSERT INTO sales VALUES(?,?,?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
row_counter = 0
for i in rows:
    print(i)
    row_counter += 1
print("회원 수 {}".format(row_counter))





