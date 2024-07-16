#!/usr/bin/env python3
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from models import db, User, Movie, Review

watcher_bp = Blueprint('watcher', __name__)
api = Api(watcher_bp)

# Request parser for User data
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

# Request parser for Review data
review_parser = reqparse.RequestParser()
review_parser.add_argument('rating', type=int, required=True, help='Rating is required')
review_parser.add_argument('comment', type=str, required=True, help='Comment is required')
review_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
review_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return jsonify({'id': user.id, 'username': user.username})
            return {'message': 'User not found'}, 404
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username} for user in users])

    def post(self):
        args = user_parser.parse_args()
        new_user = User(username=args['username'], password=args['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'id': new_user.id}, 201

    def put(self, user_id):
        args = user_parser.parse_args()
        user = User.query.get(user_id)
        if user:
            user.username = args['username']
            user.password = args['password']
            db.session.commit()
            return {'message': 'User updated'}, 200
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}, 200
        return {'message': 'User not found'}, 404

class MovieResource(Resource):
    def get(self, movie_id=None):
        if movie_id:
            movie = Movie.query.get(movie_id)
            if movie:
                return jsonify({'id': movie.id, 'title': movie.title, 'description': movie.description, 'poster_url': movie.poster_url})
            return {'message': 'Movie not found'}, 404
        movies = Movie.query.all()
        return jsonify([{'id': movie.id, 'title': movie.title, 'description': movie.description, 'poster_url': movie.poster_url} for movie in movies])

class GetAllMovies(Resource):
    def get(self):
        movies = Movie.query.all()
        return jsonify([{'id': movie.id, 'title': movie.title, 'description': movie.description, 'poster_url': movie.poster_url} for movie in movies])

class ReviewResource(Resource):
    def post(self):
        args = review_parser.parse_args()
        new_review = Review(rating=args['rating'], comment=args['comment'], user_id=args['user_id'], movie_id=args['movie_id'])
        db.session.add(new_review)
        db.session.commit()
        return {'message': 'Review created', 'id': new_review.id}, 201

    def put(self, review_id):
        args = review_parser.parse_args()
        review = Review.query.get(review_id)
        if review:
            review.rating = args['rating']
            review.comment = args['comment']
            review.user_id = args['user_id']
            review.movie_id = args['movie_id']
            db.session.commit()
            return {'message': 'Review updated'}, 200
        return {'message': 'Review not found'}, 404

    def delete(self, review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return {'message': 'Review deleted'}, 200
        return {'message': 'Review not found'}, 404

class GetAllReviews(Resource):
    def get(self):
        reviews = Review.query.all()
        return jsonify([{'id': review.id, 'rating': review.rating, 'comment': review.comment, 'user_id': review.user_id, 'movie_id': review.movie_id} for review in reviews])

api.add_resource(GetAllMovies, '/movies/all')
api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(MovieResource, '/movies', '/movies/<int:movie_id>')
api.add_resource(ReviewResource, '/reviews', '/reviews/<int:review_id>')
api.add_resource(GetAllReviews, '/reviews/all')
