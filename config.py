import pymysql.cursors

DB = {'host': 'dbairline.cjqsdkeisvcl.us-west-2.rds.amazonaws.com', 'port': 3306,
                         'user':'root',
                         'password':'deyairline',
                         'db':'airline',
                         'charset': 'utf8',
                         'cursorclass': pymysql.cursors.DictCursor}
