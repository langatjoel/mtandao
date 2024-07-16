
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const MoviePage = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetch('/api/movies/all')
            .then(response => response.json())
            .then(data => setMovies(data))
            .catch(error => console.error('Error fetching movies:', error));
    }, []);

    return (
        <div>
            <h1>Movies</h1>
            <div>
                {movies.map(movie => (
                    <div key={movie.id}>
                        <h2>{movie.title}</h2>
                        <p>{movie.description}</p>
                        <Link to={`/movies/${movie.id}`}>View Details</Link>
                        <Link to={`/reviews/${movie.id}`}>Add/Update/Delete Review</Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MoviePage;
