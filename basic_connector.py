from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import datetime

DB_NAME='random_name'
TABLES={}


TABLES['social'] = (
    "CREATE TABLE `social` ("
    "  `id` char(4) NOT NULL,"
    "  `platform` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`id`), UNIQUE KEY `platform` (`platform`)"
    ") ENGINE=InnoDB")

try:
    cnx = mysql.connector.connect(
        user='gabi_remo',
        password='Eva1Japo2',
        host='176.126.172.208',
        database='gabi_remote'
    )

    cursor = cnx.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connected to database:", cursor)


    # CREATE A DATABASE
    # try:
    #     cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    # except mysql.connector.Error as err:
    #     print("Failed creating database: {}".format(err))
    #     exit(1)


    
    #CREATE A TABLE
    # for table_name in TABLES:
    #     tables_description = TABLES[table_name]
    #     try:
    #         print("Creating table {}: ".format(table_name), end='')
    #         cursor.execute(tables_description)
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #          print("already exists.")
    #         else:
    #           print(err.msg)
    #     else:
    #       print("OK")

    # cursor.close()
    # cnx.close()


    #INSERT DATA, INSERT INTO users
    # user = ("INSERT INTO users" 
    #         "(name, first_name)"
    #         "values (%s, %s)")
    
    # data_user = ('test', 'test')
    # try:
    #     cursor.execute(user, data_user)
    #     cnx.commit()
    #     print("OK")
    # except mysql.connector.Error as err:
    #     print(err)
    # finally:    
    #     cnx.close()
    #     cursor.close()


    #QUERYING DATA 
    # query = ("SELECT first_name, name, id FROM users "
    #          "WHERE id BETWEEN %s AND %s")

    # id_start = 1
    # id_end = 3

    # try:
    #     cursor.execute(query, (id_start, id_end))

    #     for (first_name, name, id) in cursor:
    #         print("ID: {}, Name: {}, First Name: {}".format(id, name, first_name))
    

    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your user name or password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    # cursor.close()
    # cnx.close()