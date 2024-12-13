import sqlite3
#db file bilan python orasida connection yaratamiz:
connection = sqlite3.connect("C:\\Users\\Sabohat\\Downloads\\Telegram Desktop\\sample-database(2).db")
#va python dasturimiz ichida kod yoza olish uchun kursor yaratamiz:
cursor = connection.cursor()
#kod yozish:
cursor.execute("""
SELECT * FROM departments LIMIT 5;
""")
#koddan kelgan natijani olish yoki kodni run qilish:
natija = cursor.fetchall()
for i in natija:
    print(i)
cursor.close()
connection.close()
