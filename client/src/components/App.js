import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MoviePage from './MoviePage';
import MovieDetails from './MovieDetails';
import ReviewPage from './ReviewPage';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={MoviePage} />
                <Route path="/movies/:movieId" exact component={MovieDetails} />
                <Route path="/movies/:movieId/review" exact component={ReviewPage} />
            </Switch>
        </Router>
    );
};

export default App;
