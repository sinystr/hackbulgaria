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

    # --- CINEMA BASIC FUNCTIONALITY ---

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
        print("Projections for movie '{}':".format(movie_name))

        active_projections = self.projections.get_projections(id, date)
        for movie in active_projections:
            id = movie['id']
            type = movie['type']
            date = movie['date']
            time = movie['time']
            res_count = self.reservations.get_movie_reseravtions(str(id))
            template = "[{}] - {} {} ({}) - {} spots available"
            print(template.format(id, date, time, type, res_count))

    # --- VALIDATION FUNCTIONS ---

    def __name_is_valid(self, name):
        is_not_empty = len(name) > 0
        contains_only_letters = re.match("^[a-zA-Z]*$", name)

        return is_not_empty and contains_only_letters

    def __num_tickets_valid(self, num_tickets):
        valid_range = False
        contains_only_digits = re.match('^[0-9]$', num_tickets)
        if contains_only_digits:
            valid_range = 0 < int(num_tickets) < 100

        return valid_range

    def __projection_valid(self, proj_id, movie_id):
        return self.projections.projection_is_for_movie(proj_id, movie_id)

    # --- CHOOSE FUNCTIONS ---

    def _choose_name(self):
        name = input("Step 1 (User): Choose name>")
        while not self.__name_is_valid(name):
            print("Ivalid name!")
            name = input("Step 1 (User): Choose name>")
        return name

    def _choose_number_of_tickets(self):
        num_of_tickets = input("Step 1 (User): Choose number of tickets>")

        while not self.__num_tickets_valid(num_of_tickets):
            print("Invalid number of tickets!")
            num_of_tickets = input("Step 1 (User): Choose number of tickets>")

        return num_of_tickets

    def _choose_movie(self):
        self.show_movies()
        movie_id = input("Step 2 (Movie): Choose a movie>")

        while not self.movies.movie_exists(movie_id):
            print("Invalid movie number!")
            self.show_movies()
            movie_id = input("Step 2 (Movie): Choose a movie>")
        return movie_id

    def _choose_projection(self, movie_id):
        self.show_projections(movie_id)
        projection_id = input("Step 3 (Projection): Choose a projection>")

        while not self.__projection_valid(projection_id, movie_id):
            print("Projection number is invalid!")
            self.show_projections(movie_id)
            projection_id = input("Step 3 (Projection): Choose a projection>")

        return projection_id

    # --- STEPS STRUCTURE FUNCTIONS ---

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

