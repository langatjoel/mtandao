
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const MovieDetails = () => {
    const { movieId } = useParams();
    const [movie, setMovie] = useState(null);

    useEffect(() => {
        fetch(`/api/movies/${movieId}`)
            .then(response => response.json())
            .then(data => setMovie(data))
            .catch(error => console.error('Error fetching movie details:', error));
    }, [movieId]);

    if (!movie) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{movie.title}</h1>
            <p>{movie.description}</p>
            <img src={movie.poster_url} alt={movie.title} />
        </div>
    );
};

export default MovieDetails;
