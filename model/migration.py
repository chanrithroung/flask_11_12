import db_connect
def createTable():
    sql = """
        CREATE TABLE users(
            id INT(11) AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
        """
    
    connection = db_connect.db_connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()
    print("table usre create success")


if __name__ == '__main__':
    createTable()