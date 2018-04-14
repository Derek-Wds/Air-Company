import pymysql.cursors
from functools import wraps


def query_mod(sql, config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # Insert a new record
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


def query_fetch(sql, config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchone()
        connection.commit()
    finally:
        connection.close()
    return result


def fetch_all(sql, config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # Read all records
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.commit()
    finally:
        connection.close()
    return result


def customer_login_required(f):
    pass





