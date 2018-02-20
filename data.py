import pymysql

settings = {
    "host": "localhost",
    "port": 3306,
    "user": "mcbbs_admin",
    "passwd": "Default_PWD1",
    "database": "mcbbs",
    "charset": 'utf8'
}


def open_database():
    return pymysql.connect(**settings)


def init_database():
    create_table_sql = """CREATE TABLE IF NOT EXISTS Users(
    id INT UNSIGNED auto_increment,
    uid INT UNSIGNED UNIQUE NOT NULL,
    username varchar(50) UNIQUE NOT NULL,
    friend INT NOT NULL,
    comment INT NOT NULL,
    topic INT NOT NULL,
    online_time INT NOT NULL,
    reg_time DATETIME NOT NULL,
    point INT NOT NULL,
    popularity INT NOT NULL,
    gold_grain INT NOT NULL,
    gold_ingot INT NOT NULL,
    emerald INT NOT NULL,
    nether_star INT NOT NULL,
    contribution INT NOT NULL,
    assistance INT NOT NULL,
    diamond INT NOT NULL,
    PRIMARY KEY (id)
    )DEFAULT CHARSET=utf8"""
    cursor = database.cursor()
    cursor.execute(create_table_sql)
    database.commit()
    cursor.close()


def insert_user(**values):
    insert_sql = """INSERT INTO Users("""
    for column in values:
        insert_sql += (column + ', ')
    insert_sql = insert_sql[0:len(insert_sql) - 2]
    insert_sql += ') VALUES ('
    for value in values:
        insert_sql += ("'" + values[value] + "', ")
    insert_sql = insert_sql[0:len(insert_sql) - 2]
    insert_sql += ');'
    try:
        cursor = database.cursor()
        cursor.execute(insert_sql)
        database.commit()
        cursor.close()
    except:
        print(insert_sql)
        print(values['uid'] + ' Data Error Database\n')


database = open_database()
