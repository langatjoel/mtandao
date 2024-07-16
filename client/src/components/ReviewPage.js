
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const ReviewPage = () => {
    const { movieId } = useParams();
    const [reviews, setReviews] = useState([]);
    const [rating, setRating] = useState('');
    const [comment, setComment] = useState('');

    useEffect(() => {
        fetch('/api/reviews/all')
            .then(response => response.json())
            .then(data => setReviews(data.filter(review => review.movie_id === parseInt(movieId))))
            .catch(error => console.error('Error fetching reviews:', error));
    }, [movieId]);

    const handleSubmit = (e) => {
        e.preventDefault();

        const newReview = {
            rating: parseInt(rating),
            comment,
            user_id: 1, // Assuming user_id = 1 for simplicity; replace with actual user ID
            movie_id: parseInt(movieId),
        };

        fetch('/api/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newReview),
        })
        .then(response => response.json())
        .then(data => {
            setReviews([...reviews, data]);
            setRating('');
            setComment('');
        })
        .catch(error => console.error('Error adding review:', error));
    };

    const handleUpdate = (reviewId) => {
        const updatedReview = {
            rating: parseInt(rating),
            comment,
            user_id: 1,
            movie_id: parseInt(movieId),
        };

        fetch(`/api/reviews/${reviewId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedReview),
        })
        .then(response => response.json())
        .then(data => {
            setReviews(reviews.map(review => review.id === reviewId ? data : review));
            setRating('');
            setComment('');
        })
        .catch(error => console.error('Error updating review:', error));
    };

    const handleDelete = (reviewId) => {
        fetch(`/api/reviews/${reviewId}`, {
            method: 'DELETE',
        })
        .then(() => {
            setReviews(reviews.filter(review => review.id !== reviewId));
        })
        .catch(error => console.error('Error deleting review:', error));
    };

    return (
        <div>
            <h1>Reviews</h1>
            <form onSubmit={handleSubmit}>
                <input type="number" value={rating} onChange={(e) => setRating(e.target.value)} placeholder="Rating" required />
                <input type="text" value={comment} onChange={(e) => setComment(e.target.value)} placeholder="Comment" required />
                <button type="submit">Add Review</button>
            </form>
            <div>
                {reviews.map(review => (
                    <div key={review.id}>
                        <h2>Rating: {review.rating}</h2>
                        <p>{review.comment}</p>
                        <button onClick={() => handleUpdate(review.id)}>Update Review</button>
                        <button onClick={() => handleDelete(review.id)}>Delete Review</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ReviewPage;
