import csv

def add_movie_to_db(
    movies, title: str, genre: str, year: int) -> None:
    # print("\n\nClient: Adding a Movie to database.")
    movies.append(locals())

if __name__ == "__main__":
    movies_db = []
    with open('movies.csv') as csv_movies:
        reader = csv.reader(csv_movies, delimiter=',')
        for row in reader:
            if row:
                add_movie_to_db(movies_db, *row)

    print(len(movies_db))

