import sqlite3


count_users = 10
primary_balance = 1000
update_balance = 500
step_update = 2
step_delete = 3
select_age = 60
delete_user = 6

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )
    '''
    )

for i in range(1, count_users+1):
    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f'User{i}', f'example{i}@gmail.com', i*10, primary_balance)
        )

for i in range(1, count_users+1, step_update):
    cursor.execute(
        "UPDATE Users SET balance = ? WHERE id = ?", (update_balance, i)
        )

for i in range(1, count_users+1, step_delete):
    cursor.execute(
        "DELETE FROM Users WHERE id = ?", (i,)
        )

cursor.execute(
    "SELECT username, email, age, balance FROM Users WHERE age != ?", (select_age,)
    )
result = cursor.fetchall()
for user in result:
    print(
        f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}'
        )

cursor.execute(
    "DELETE FROM Users WHERE id = ?", (delete_user,)
    )

cursor.execute(
    "SELECT COUNT(*) FROM Users"
    )
total_users = cursor.fetchone()[0]

cursor.execute(
    "SELECT SUM(balance) FROM Users"
    )
all_balance = cursor.fetchone()[0]

print(
    f'Средний баланс всех пользователей: '
    f'{all_balance} / {total_users} = {all_balance / total_users}'
    )

connection.commit()
connection.close()