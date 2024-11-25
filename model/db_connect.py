from pymysql import connect, MySQLError

def db_connect():
    db_name = "flask_crud"
    try:
        connection = connect(
            host="127.0.0.1",
            user="root",
            port=3307,
            database="flask_crud",
            ssl={'disable': True}
        )

        sql = f"""CREATE DATABASE IF NOT EXISTS {db_name};"""

        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.execute(f"USE {db_name}")
        return connection
    except MySQLError as e: 
        print(f"Fial connect database: {e}")


if __name__ == "__main__":
    db_connect()