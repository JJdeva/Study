import MySQLdb
# db연결
conn = MySQLdb.connect(host="localhost", user="myuser", password='qwer1234', db='hanbitDB', charset='utf8')
print(conn)
# 커서 생성
cur = conn.cursor()
print(cur)
# 테이블 생성
# cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)")

# 데이터 입력
# cur.execute("INSERT INTO userTable VALUES ('john', 'John Bann', 'john@naver.com', 1990)")
# cur.execute("INSERT INTO userTable VALUES ('kim', 'kim Chi', 'kim@daum.net', 1992)")
# cur.execute("INSERT INTO userTable VALUES ('lee', 'Lee Pal', 'lee@paran.com', 1988)")
# cur.execute("INSERT INTO userTable VALUES ('park', 'Park Su', 'park@gmail.com', 1980)")


# 데이터 커밋
# conn.commit()

# db 연결 끊기
# conn.close()

# select
print(cur.execute("SELECT * FROM userTable;"))

