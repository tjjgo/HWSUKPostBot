def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = sqlite3.connect(db_file)
    return conn

 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sqltab = """ CREATE TABLE IF NOT EXISTS links (
id text PRIMARY KEY,
reply text
); """
database = "snapshill.sqlite3"
import sqlite3
conn = create_connection(database)
create_table(conn, sqltab)
