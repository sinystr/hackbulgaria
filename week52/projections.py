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
