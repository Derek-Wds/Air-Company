import pymysql.cursors

secret_key = '\x1b\x9d\xa8\x9b\xbbn\xa5\xfd\xd2\xa4\x16%{c\xba~\xd5\xb1\x11iy\x97=\x96'

DB = {'host': 'dbairline.cjqsdkeisvcl.us-west-2.rds.amazonaws.com', 'port': 3306,
                         'user':'root',
                         'password':'deyairline',
                         'db':'airline',
                         'charset': 'utf8',
                         'cursorclass': pymysql.cursors.DictCursor}
