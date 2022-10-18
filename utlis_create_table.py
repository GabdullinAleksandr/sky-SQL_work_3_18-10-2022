import psycopg2


def connect_bd():
    """
    Подключает БД
    :return:
    """
    try:
        connection = psycopg2.connect(user="postgres", password="99493876", host="127.0.0.1",
                                      port="5432", database="sky-SQL_work_2")
        connection.autocommit = True
        print('Connection DONE')
        return connection
    except:
        print('Connection FAILED')
        return False


def create_table(cursor):
    create_table_colour(cursor)
    create_table_breed(cursor)
    create_table_an_type(cursor)
    create_table_animal(cursor)
    create_table_subtype(cursor)
    create_table_out_type(cursor)
    create_table_shelter(cursor)


def create_table_colour(cursor):
    req = f"""
        CREATE TABLE IF NOT EXISTS colour (
            id_colour SERIAL PRIMARY KEY,
            name_colour_1 VARCHAR(25),
            name_colour_2 VARCHAR(25)
        )
    """
    try:
        cursor.execute(req)
        print('create colour DONE')
    except:
        print('create colour FAILED')


def create_table_breed(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS breed (
        id_breed SERIAL PRIMARY KEY,
        name_breed VARCHAR(255)
    )
    """
    try:
        cursor.execute(req)
        print('create breed DONE')
    except:
        print('create breed FAILED')


def create_table_an_type(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS an_type (
        id_type SERIAL PRIMARY KEY,
        animal_name VARCHAR(25)
    )
    """
    try:
        cursor.execute(req)
        print('create an_type DONE')
    except:
        print('create an_type FAILED')


def create_table_animal(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS animal (
        id_an SERIAL PRIMARY KEY,
        id_animal TEXT,
        fk_animal_type SERIAL,
        name_animal VARCHAR(25),
        fk_breed SERIAL,
        fk_colour_1 SERIAL,
        fk_colour_2 SERIAL,
        date_of_birth DATE,
        FOREIGN KEY (fk_animal_type) REFERENCES an_type (id_type),
        FOREIGN KEY (fk_breed) REFERENCES breed (id_breed),
        FOREIGN KEY (fk_colour_1) REFERENCES colour (id_colour),
        FOREIGN KEY (fk_colour_2) REFERENCES colour (id_colour)
        )
    """
    try:
        cursor.execute(req)
        print('create animal DONE')
    except:
        print('create animal FAILED')


def create_table_subtype(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS subtype (
        id_subtype SERIAL PRIMARY KEY,
        name_subtype VARCHAR(25)
    )
    """
    try:
        cursor.execute(req)
        print('create subtype DONE')
    except:
        print('create subtype FAILED')


def create_table_out_type(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS out_type (
        id_out_type SERIAL PRIMARY KEY,
        name_out_type VARCHAR(25)
    )
    """
    try:
        cursor.execute(req)
        print('create out_type DONE')
    except:
        print('create out_type FAILED')


def create_table_shelter(cursor):
    req = """
    CREATE TABLE IF NOT EXISTS shelter (
        id_shelter INTEGER PRIMARY KEY,
        fk_animal SERIAL,
        fk_output_subtype SERIAL,
        outcome_month INTEGER,
        outcome_year INTEGER,
        fk_outcome_type SERIAL,
        age_upon_outcome TEXT,
        FOREIGN KEY (fk_animal) REFERENCES animal (id_an),
        FOREIGN KEY (fk_output_subtype) REFERENCES subtype (id_subtype),
        FOREIGN KEY (fk_outcome_type) REFERENCES out_type (id_out_type)
    )
    """
    try:
        cursor.execute(req)
        print('create shelter DONE')
    except:
        print('create shelter FAILED')

