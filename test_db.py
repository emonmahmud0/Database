import pymysql

try:
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',  # put your password here if needed
        database='library_management'
    )
    print("✅ Connection successful!")
    con.close()
except pymysql.MySQLError as e:
    print(f"❌ MySQL error: {e}")
