class Projections():

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def get_projections(self, id, date=None):
        if date is None:
            self.cursor.execute('''SELECT id, type, date, time
            FROM Projections WHERE movie_id = ?''', id)
            return self.cursor
        else:
            self.cursor.execute('''SELECT id, type, date, time
            FROM Projections WHERE movie_id = ? AND date = ?''', (id, date))
            return self.cursor

    def projection_is_for_movie(self, id, movie_id):
            self.cursor.execute('''SELECT COUNT(*)
            FROM Projections WHERE id = ? AND movie_id = ?''', (id, movie_id))
            if self.cursor.fetchone()[0] > 0:
                return True
            return False
