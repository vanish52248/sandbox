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
cur.execute("SELECT * FROM persons")
print(cur.fetchall())

# UPDATE
cur.execute("UPDATE persons SET name = 'Michel' WHERE name  = 'Mike'")
conn.commit()

# DELETE
cur.execute("DELETE FROM persons WHERE name = 'Michel'")
conn.commit()

# 後処理
cur.close()
conn.close()
