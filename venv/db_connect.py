import pymysql

def connect_to_db():
    pymysql.connect(db = "all_knowledge",
                    user = "***",
                    passwd = "*******",
                    unix_socket = "*******",
                    port = '*****')