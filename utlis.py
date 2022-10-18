import csv


def filling_table(cursor):
    with open('animals.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 1
        for line in reader:
            print(f'Заполняется строка {count}')
            count += 1
            subtype = line['outcome_subtype']
            req_subtype = f"""
                INSERT INTO subtype (name_subtype)
                VALUES ('{subtype}');
            """
            cursor.execute(req_subtype)

            out_type = line['outcome_type']
            req_out_type = f"""
                INSERT INTO out_type (name_out_type)
                VALUES ('{out_type}')
            """
            cursor.execute(req_out_type)

            an_type = line['animal_type']
            req_an_type = f"""
                INSERT INTO an_type (animal_name)
                VALUES ('{an_type}')
            """
            cursor.execute(req_an_type)

            breed = line['breed']
            req_breed = f"""
                INSERT INTO breed (name_breed)
                VALUES ('{breed}')
            """
            cursor.execute(req_breed)

            colour1 = line['color1']
            colour2 = line['color2']
            req_colour = f"""
                INSERT INTO colour (name_colour_1, name_colour_2)
                VALUES ('{colour1}', '{colour2}')
            """
            cursor.execute(req_colour)

            id_animal = line['animal_id']
            name_animal = [line['name'] if "'" not in line['name'] else line['name'].replace("'", '-')]
            date_of_birth = line['date_of_birth']
            req_animal = f"""
                INSERT INTO animal (id_animal, name_animal, date_of_birth)
                VALUES ('{id_animal}', '{name_animal[0]}', '{date_of_birth}')
            """
            cursor.execute(req_animal)

            id_shelter = line['index']
            outcome_month = line['outcome_month']
            outcome_year = line['outcome_year']
            age_upon_outcome = line['age_upon_outcome']
            req_shelter = f"""
                INSERT INTO shelter (id_shelter, outcome_month, outcome_year, age_upon_outcome)
                VALUES ('{id_shelter}', '{outcome_month}', '{outcome_year}', '{age_upon_outcome}')
            """
            cursor.execute(req_shelter)

