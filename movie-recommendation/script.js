const API_KEY = 'YOUR_TMDB_API_KEY'; // Replace with your TMDb API key
const API_URL = 'https://api.themoviedb.org/3/discover/movie';

async function getMovieRecommendation() {
    const genre = document.getElementById('genre').value;
    const rating = document.getElementById('rating').value;
    
    const response = await fetch(`${API_URL}?api_key=${API_KEY}&with_genres=${genre}&vote_average.gte=${rating}`);
    const data = await response.json();

    displayMovie(data.results[0]);
}

function displayMovie(movie) {
    if (!movie) {
        document.getElementById('movie-title').textContent = 'No movie found.';
        document.getElementById('movie-overview').textContent = '';
        return;
    }

    document.getElementById('movie-title').textContent = movie.title;
    document.getElementById('movie-overview').textContent = movie.overview;
}
