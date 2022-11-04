import sqlite3


def f_addPersontodb(name, surname, age, year, info, path_photo):
    # функция добаляет информацию о человеке в базу данных (таблица person)

    con = sqlite3.connect('../person_db.sqlite')
    cur = con.cursor()
    cur.execute(f"""INSERT INTO person(name, surname, age, year, information, photo)
    VALUES('{name}', '{surname}', {age}, DATE('{year}'), '{info}', '{path_photo}')""")
    con.commit()

    res = cur.execute('''select * from person''').fetchall()
    print(res)

    con.close()


def f_addVideotodb(datetime, peoples, not_known, video_path):
    # функция добавляет записанное видео и информацию о нем в базу данных (таблица videos)

    date = datetime.toString('yyyy-MM-dd')
    time = datetime.toString('hh:mm:ss')

    a = list(peoples)
    if not not_known:
        a.append(f'неизвестные: {not_known}')
    people = ', '.join(a)

    con = sqlite3.connect('../person_db.sqlite')
    cur = con.cursor()
    cur.execute(f"""INSERT INTO videos(data, time, people, video)
        VALUES(DATE('{date}'), TIME('{time}'), '{people}', '{video_path}')""")
    con.commit()
    con.close()
