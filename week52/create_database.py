import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    Movies(
        id INTEGER PRIMARY KEY,
        name TEXT,
        rating REAL
    )
''')

movies = [("The Hunger Games: Catching Fire", 7.9),
          ("Wreck-It Ralph", 7.8),
          ("Her", 8.3)]

cursor.executemany('''
    INSERT INTO Movies(name, rating)
    VALUES(?,?)''', movies)

db.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    Projections(
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        type TEXT,
        date TEXT,
        time TEXT,
        FOREIGN KEY(movie_id) REFERENCES Movies(id)
    )
''')

projections = [(1, "3D", "2014-04-01", "19:10"),
               (1, "2D", "2014-04-01", "19:00"),
               (1, "4DX", "2014-04-02", "21:00"),
               (3, "2D", "2014-04-05", "20:20"),
               (2, "3D", "2014-04-02", "22:00"),
               (2, "2D", "2014-04-02", "19:30")]

cursor.executemany('''
    INSERT INTO Projections(movie_id, type, date, time)
    VALUES(?,?,?,?)''', projections)

db.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    Reservations(
        id INTEGER PRIMARY KEY,
        username TEXT,
        projection_id INTEGER,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY(projection_id) REFERENCES Projections(id)
    )
''')

reservations = [("RadoRado", 1, 2, 1),
                ("RadoRado", 1, 3, 5),
                ("RadoRado", 1, 7, 8),
                ("Ivo", 3, 1, 1),
                ("Ivo", 3, 1, 2),
                ("Mysterious", 5, 2, 3),
                ("Mysterious", 5, 2, 4)]

cursor.executemany('''
    INSERT INTO Reservations(username, projection_id, row, col)
    VALUES(?,?,?,?)''', reservations)

db.commit()

db.close()
