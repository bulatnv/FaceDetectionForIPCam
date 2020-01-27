import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()


def select_user_sql(username):
    result = cur.execute(f"""SELECT * FROM users
                        WHERE name = \"{username}\"""").fetchall()
    con.close()
    return result


def add_user_sql(username, passwd):
    cur.execute(f"""INSERT INTO users(name, pass)
                VALUES(\"{username}\", \"{passwd}\")""")
    con.commit()
    con.close()


def remove_user_sql(username):
    cur.execute(f"""DELETE from users WHERE
                name = \"{username}\"""")
    con.commit()
    con.close()