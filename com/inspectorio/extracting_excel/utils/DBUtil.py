import psycopg2
from django.conf import settings


def init_connection():
    # Open database connection
    config = settings.DATABASES['default']
    db = psycopg2.connect(host=config['HOST'], user=config['USER'],
                          password=config['PASSWORD'], dbname=config['NAME'])

    return db


def insert(sql, args):
    # Open database connection
    db = init_connection()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    id_of_new_row = None
    try:
        # Execute the SQL command
        cursor.execute(sql, args)
        id_of_new_row = cursor.fetchone()[0]
        # Commit your changes in the database
        db.commit()
    except Exception as ex:
        print('Error: ', ex)
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    cursor.close()
    db.close()
    return id_of_new_row


def insert_many(sql, list_args):
    # Open database connection
    db = init_connection()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # Execute the SQL command
        cursor.executemany(sql, list_args)
        # Commit your changes in the database
        db.commit()
    except Exception as ex:
        print('Error: ', ex)
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    cursor.close()
    db.close()


def execute(sql):
    # Open database connection
    db = init_connection()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Execute sql
    cursor.execute(sql)

    results = []
    for item in cursor:
        results.append(item)
    # disconnect from server
    cursor.close()
    db.close()
    return results