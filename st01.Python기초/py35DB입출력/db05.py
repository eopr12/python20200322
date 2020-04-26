
import sqlite3
import os


def getDbFileName(currentDir, fileName):
    dbFile = None

    try:
        # SQLite3 Database 파일 경로 설정
        dbFile = os.path.normpath(currentDir + os.path.join("/", fileName))
        print(dbFile)
    except Exception as ex:
        pass
    finally:
        pass

    return dbFile


def OrderFunc(str1, str2):  # 대소문자 구별 없이 정렬하는 함수
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1 > s2) - (s1 < s2)


def main():

    # 현재 실행되는 스크립트파일의 절대경로를 구하려면
    currentDir = os.path.dirname(os.path.abspath(__file__))
    print(currentDir)

    # SQLite3 Database 파일 경로 설정
    dbFile = getDbFileName(currentDir, "phonebook.db3")

    # 데이터베이스 연결
    # 실제 파일을 이용한 Connection 객체 생성
    con = sqlite3.connect(dbFile)   # 파일 디비 ==> 영구적

    cur = con.cursor()

    # DROP문 수행 : Cursor.execute 메서드를 이용하여 SQL문을 수행
    cur.execute("DROP TABLE IF EXISTS PhoneBook;")

    # CREATE문 수행 : Cursor.execute 메서드를 이용하여 SQL문을 수행
    cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")

    # INSERT문 수행
    cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")

    # INSERT문 수행 : 인자를 전달하여 SQL문을 수행
    name = "Someone"
    phoneNumber = '010-5678-1234'
    cur.execute("INSERT INTO PhoneBook VALUES(?, ?);", (name, phoneNumber))

    # INSERT문 수행 : 사전을 이용한 인자 전달
    dict = {"inputName": "Jack", "inputNum": "111-2222-3333"}
    cur.execute("INSERT INTO PhoneBook VALUES(:inputName, :inputNum);", dict)

    # INSERT문 수행 : 동일한 문장을 매개변수만 바꾸며 연속적으로 수행하는 경우
    datalist = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
    cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", datalist)

    # 레코드 조회
    # fetch를 이용한 레코드 조회 방법
    # 실행 예시
    #   ('Derick', '010-1234-5678')
    #   ('Someone', '010-5670-2343')
    #   ('Tom', '010-543-5432')
    #   ('DSP', '010-123-1234')
    cur.execute("SELECT * FROM PhoneBook;")
    for row in cur:
        print(row)

    # 레코드 조회
    # fetchone를 이용한 레코드 조회 방법
    # 실행 예시 >> ('Derick', '010-1234-5678')
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchone())

    # 레코드 조회
    # fetchmany를 이용한 레코드 조회 방법
    # 실행 예시 >> [('Derick', '010-1234-5678'), ('Someone', '010-5678-1234')]
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchmany(2))

    # 레코드 조회
    # fetchall를 이용한 레코드 조회 방법
    # 실행 예시 >> [('Derick', '010-1234-5678'), ('Someone', '010-5678-1234'), ('Jack', '111-2222-3333'), ('Tom', '010-543-5432'), ('DSP', '010-123-1234')]
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchall())

    # 레코드 정렬
    # ORDER BY 사용 예제
    # 실행 예시 >> [('DSP', '010-123-1234'), ('Derick', '010-1234-5678'), ('Jack', '111-2222-3333'), ('Someone', '010-5678-1234'), ('Tom', '010-543-5432')]
    cur.execute("SELECT * FROM PhoneBook ORDER BY Name")
    print(cur.fetchall())

    # 실행 예시 >> [('Tom', '010-543-5432'), ('Someone', '010-5678-1234'), ('Jack', '111-2222-3333'), ('Derick', '010-1234-5678'), ('DSP', '010-123-1234')]
    cur.execute("SELECT * FROM PhoneBook ORDER BY Name DESC")
    print(cur.fetchall())

    # 레코드 정렬
    # 사용자 함수를 사용하여 정렬 방식을 변경하는 경우
    con.create_collation('myordering', OrderFunc)  # SQL 구문에서 호출할 이름과 함수를 등록
    cur.execute("SELECT Name FROM PhoneBook ORDER BY Name COLLATE myordering")

    # 실행 예시 >> ['DSP', 'Jack', 'Someone', 'Tom']
    print(cur.fetchone())
    for row in cur:
        print(row[0])
    print()

    # 트랜잭션 처리
    # 작업한 내용이 커밋되지 않는 예제

    dbFile = getDbFileName(currentDir, "test.db3")
    con = sqlite3.connect(dbFile)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneBook;")
    cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
    cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchall())

    # 트랜잭션 처리
    # 작업한 내용이 커밋되지 않는 결과 확인

    dbFile = getDbFileName(currentDir, "test.db3")
    con = sqlite3.connect(dbFile)
    cur = con.cursor()
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchall())

    # 트랜잭션 처리
    # 작업한 내용을 커밋하는 예제
    dbFile = getDbFileName(currentDir, "commit.db3")
    con = sqlite3.connect(dbFile)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneBook;")
    cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
    cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
    con.commit()

    # 트랜잭션 처리
    # 작업한 내용을 커밋한 내용을 확인하는 예제

    dbFile = getDbFileName(currentDir, "commit.db3")
    con = sqlite3.connect(dbFile)
    cur = con.cursor()
    cur.execute("SELECT * FROM PhoneBook;")
    print(cur.fetchall())

    # 데이터베이스 덤프 만들기
    # 데이터베이스 덤프 예제 코드
    # 실행 결과 예시 >>
    #   BEGIN TRANSACTION;
    #   CREATE TABLE PhoneBook(Name text, PhoneNum text);
    #   INSERT INTO "PhoneBook" VALUES('Derick','010-1234-5678');
    #   INSERT INTO "PhoneBook" VALUES('Tom','010-543-5432');
    #   INSERT INTO "PhoneBook" VALUES('DSP','010-123-1234');
    #   COMMIT;

    # 메모리를 이용한 Connection 객체 생성
    con = sqlite3.connect(":memory:")  # 메모리 디비 ==> 임시적
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneBook;")
    cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
    cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
    list = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
    cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", list)
    con.commit()

    for l in con.iterdump():
        print(l)


main()
