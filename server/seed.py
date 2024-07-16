#!/usr/bin/env python3

from app import app, db
from models import User, Movie, Review, Genre, MovieGenre

if __name__ == '__main__':
    with app.app_context():
        # Drop all tables and create new ones
        db.drop_all()
        db.create_all()

        print("Seeding genres...")
        genres = [
            Genre(name="Action"),
            Genre(name="Comedy"),
            Genre(name="Drama"),
            Genre(name="Horror"),
            Genre(name="Thriller")
        ]
        for genre in genres:
            db.session.add(genre)
        db.session.commit()

        print("Seeding movies...")
        movies = [
            Movie(
                title="Inception",
                description="A thief who steals corporate secrets through the use of dream-sharing technology.",
                poster_url="https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p7825626_p_v8_ae.jpg"
            ),
            Movie(
                title="The Matrix",
                description="A computer hacker learns from mysterious rebels about the true nature of his reality.",
                poster_url="https://images.bauerhosting.com/legacy/empire-tmdb/films/603/images/7u3pxc0K1wx32IleAkLv78MKgrw.jpg?ar=16:9&fit=crop&crop=top"
            ),
            Movie(
                title="Interstellar",
                description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVVazaukDPzzzl1gMZ4_0EVjGXVMlqk5VpaA&s"
            ),
            Movie(
                title="Pulp Fiction",
                description="The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                poster_url="https://cdn.britannica.com/66/141066-050-36AB089D/John-Travolta-Samuel-L-Jackson-Pulp-Fiction.jpg"
            ),
            Movie(
                title="The Dark Knight",
                description="When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
                poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ekE6Hhz9gvIbiFSUPxt-FyAh4zXTXX0bjQ&s"
            ),
            Movie(
                title="The Godfather",
                description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                poster_url="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg"
            ),
            Movie(
                title="Forrest Gump",
                description="The presidencies of Kennedy and Johnson, the Vietnam War, the civil rights movement, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
                poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvxY-v3jqcL0Z01G-KuVR_3h1sxRPUctyrKg&s"
            ),
            Movie(
                title="Fight Club",
                description="An insomniac office worker and a soap salesman build a global organization to help vent male aggression.",
                poster_url="https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg"
            ),
            Movie(
                title="The Shawshank Redemption",
                description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                poster_url="https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg"
            ),
            Movie(
                title="Gladiator",
                description="A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
                poster_url="https://m.media-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
            ),
            Movie(
                title="Joker",
                description="In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral that leads him to become the infamous Joker.",
                poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP7TzsGto_FJI2I9IibPV1GWd--ki-_NAAYQ&s"
            ),
        ]
        for movie in movies:
            db.session.add(movie)
        db.session.commit()

        print("Seeding users...")
        users = [
            User(username='john_doe', password='password123'),
            User(username='admin_user', password='adminpassword'),
        ]
        for user in users:
            db.session.add(user)
        db.session.commit()

        print("Seeding reviews...")
        reviews = [
            Review(user_id=1, movie_id=1, comment="Amazing movie!", rating=9),
            Review(user_id=2, movie_id=2, comment="A true classic.", rating=8.5),
            Review(user_id=1, movie_id=3, comment="A mind-bending journey through space.", rating=8.8),
            Review(user_id=2, movie_id=4, comment="Tarantino's best work!", rating=9.2),
            Review(user_id=1, movie_id=5, comment="The best Batman movie ever.", rating=9.5),
            Review(user_id=2, movie_id=6, comment="A masterpiece of crime cinema.", rating=9.3),
            Review(user_id=1, movie_id=7, comment="A heartwarming and profound story.", rating=8.7),
            Review(user_id=2, movie_id=8, comment="A dark and gritty look at modern masculinity.", rating=8.9),
            Review(user_id=1, movie_id=9, comment="An intense and moving film.", rating=9.0),
            Review(user_id=2, movie_id=10, comment="A powerful and disturbing character study.", rating=8.4),
        ]
        for review in reviews:
            db.session.add(review)
        db.session.commit()

        print("Seeding movie genres...")
        movie_genres = [
            MovieGenre(movie_id=1, genre_id=1),
            MovieGenre(movie_id=2, genre_id=1),
            MovieGenre(movie_id=3, genre_id=4),
            MovieGenre(movie_id=4, genre_id=3),
            MovieGenre(movie_id=5, genre_id=1),
            MovieGenre(movie_id=6, genre_id=3),
            MovieGenre(movie_id=7, genre_id=3),
            MovieGenre(movie_id=8, genre_id=2),
            MovieGenre(movie_id=9, genre_id=3),
            MovieGenre(movie_id=10, genre_id=1),
            MovieGenre(movie_id=11, genre_id=4),
        ]
        for movie_genre in movie_genres:
            db.session.add(movie_genre)
        db.session.commit()

        print("Seeding complete.")
