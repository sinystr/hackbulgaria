class Reservations():

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def get_movie_reseravtions(self, id):
        self.cursor.execute('''SELECT COUNT(*)
        FROM Reservations WHERE projection_id = ?''', id)
        return 100 - self.cursor.fetchone()[0]
