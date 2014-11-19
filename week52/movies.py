class Movies():

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def add_movie(self, name, rating):
        self.cursor.execute('''
            INSERT INTO Movies(name, rating)
            VALUES(?,?)''', [name, rating])

        self.db.commit()

    def get_movies(self):
        self.cursor.execute('''SELECT id, name, rating
        FROM Movies''')
        return self.cursor

    def get_movie_name(self, id):
        self.cursor.execute('''SELECT name
        FROM Movies WHERE id = ?''', id)
        return self.cursor.fetchone()['name']

    def movie_exists(self, id):
        self.cursor.execute('''SELECT COUNT(*)
        FROM Movies WHERE id = ?''', id)
        if self.cursor.fetchone()[0] > 0:
            return True
        return False
