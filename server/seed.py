# seed.py

from app import app, db, User, Movie, Review, Genre, MovieGenre

# Seed data
with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Create genres
    action = Genre(name="Action")
    comedy = Genre(name="Comedy")
    drama = Genre(name="Drama")
    
    db.session.add_all([action, comedy, drama])
    db.session.commit()

    # Create movies
    movie1 = Movie(title="Action Movie", description="An action-packed movie.", poster_url="http://example.com/poster1.jpg")
    movie2 = Movie(title="Comedy Movie", description="A hilarious comedy movie.", poster_url="http://example.com/poster2.jpg")
    movie3 = Movie(title="Drama Movie", description="A touching drama movie.", poster_url="http://example.com/poster3.jpg")
    
    db.session.add_all([movie1, movie2, movie3])
    db.session.commit()

    # Assign genres to movies
    movie_genre1 = MovieGenre(movie_id=movie1.id, genre_id=action.id)
    movie_genre2 = MovieGenre(movie_id=movie2.id, genre_id=comedy.id)
    movie_genre3 = MovieGenre(movie_id=movie3.id, genre_id=drama.id)
    
    db.session.add_all([movie_genre1, movie_genre2, movie_genre3])
    db.session.commit()

    # Create users
    user1 = User(username="john_doe", password="password1")
    user2 = User(username="jane_doe", password="password2")
    
    db.session.add_all([user1, user2])
    db.session.commit()

    # Create reviews
    review1 = Review(rating=5, comment="Amazing movie!", user_id=user1.id, movie_id=movie1.id)
    review2 = Review(rating=4, comment="Really funny!", user_id=user2.id, movie_id=movie2.id)
    review3 = Review(rating=3, comment="Very emotional.", user_id=user1.id, movie_id=movie3.id)
    
    db.session.add_all([review1, review2, review3])
    db.session.commit()

    print("Database seeded successfully!")
