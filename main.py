from utlis_create_table import *
from utlis import *


def main():
    conn = connect_bd()
    if conn:
        cursor = conn.cursor()
        create_table(cursor)
        filling_table(cursor)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
