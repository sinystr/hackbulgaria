import movies
import projections
import reservations
import re

class Cinema():

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()
        self.movies = movies.Movies(db)
        self.projections = projections.Projections(db)
        self.reservations = reservations.Reservations(db)

    def show_movies(self):
        print("Current movies:")
        active_movies = self.movies.get_movies()
        for movie in active_movies:
            id = movie['id']
            name = movie['name']
            rating = movie['rating']
            print("[{}] - {} ({})".format(id, name, rating))

    def show_projections(self, id, date=None):
        movie_name = self.movies.get_movie_name(str(id))
        active_projections = self.projections.get_projections(id, date)
        print("Projections for movie '{}':".format(movie_name))
        for movie in active_projections:
            id = movie['id']
            type = movie['type']
            date = movie['date']
            time = movie['time']
            res_count = self.reservations.get_movie_reseravtions(str(id))
            print("[{}] - {} {} ({}) - {} spots available".format(id, date, time, type, res_count))

    # --- VALIDATIONS FUNCTIONS ---

    def __name_is_invalid(self, name):
        is_not_empty = len(name) > 0
        contains_only_letters = re.match('^[a-z][A-Z]$', name)
        return is_not_empty and contains_only_letters

    def ___num_tickets_valid(self, num_tickets):
        contains_only_digits = re.match('^[0-9]$', num_tickets)
        valid_range = 0 < int(num_tickets) < 100
        return contains_only_digits and valid_range

    # --- CHOOSE FUNCTIONS ---

    def _choose_name(self):
        name = input("Step 1 (User): Choose name>")
        while not self.__name_is_valid(name):
            print("Ivalid name!")
            name = input("Step 1 (User): Choose name>")
        return name

    def _choose_number_of_tickets(self):
        num_of_tickets = input("Step 1 (User): Choose number of tickets>")
        while __num_tickets_valid(num_of_tickets):
            print("Invalid number of tickets!")
            num_of_tickets = input("Step 1 (User): Choose number of tickets>")
        return num_of_tickets

    def _choose_movie(self):
        self.show_movies()
        chosen_movie_id = input("Step 2 (Movie): Choose a movie>")
        while not self.movies.movie_exists(chosen_movie_id):
            print("Invalid movie number!")
            self.show_movies()
            chosen_movie_id = input("Step 2 (Movie): Choose a movie>")
        return chosen_movie_id

    def _choose_projection(self, movie_id):
        self.show_projections(movie_id)
        chosen_movie_id = input("Step 3 (Projection): Choose a projection>")
        while not self.movies.movie_exists(chosen_movie_id):
            print("Projection number is invalid!")
            self.show_movies()
            chosen_movie_id = input("Step 2 (Movie): Choose a movie>")
        return chosen_movie_id

    def _step_one(self):
        return self._choose_name(), self._choose_number_of_tickets()

    def _step_two(self):
        return self._choose_movie()

    def _step_three(self, movie_id):
        self._choose_projection(movie_id)

    def make_reservation(self):
        name, tickets = self._step_one()
        movie_id = self._step_two()
        self._step_three(movie_id)
