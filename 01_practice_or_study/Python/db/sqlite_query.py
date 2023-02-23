import sqlite3

# ローカルに作成したDBとの接続情報
# conn = sqlite3.connect("develop.db")

# ★インメモリDBとの接続情報（ 接続が閉じられると、データベースは削除される）
conn = sqlite3.connect(':memory:')

cur = conn.cursor()

# DB作成
cur.execute("CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")
conn.commit()

# CREATE
cur.execute("INSERT INTO persons(name) VALUES('Mike')")
conn.commit()

# READ
name = "Mike"
cur.execute("SELECT * FROM persons WHERE name = '{}'".format(name))
conn.commit()
print(cur.fetchall())

# UPDATE
name2 = "Mimi"
cur.execute("UPDATE persons SET name = '{}' WHERE name = '{}'".format(name2, name))
conn.commit()

# DELETE
cur.execute("DELETE FROM persons WHERE name = '{}'".format(name2))
conn.commit()

# 後処理
cur.close()
conn.close()
