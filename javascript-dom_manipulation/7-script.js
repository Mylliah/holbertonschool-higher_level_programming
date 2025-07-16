#!/usr/bin/node

const movieElement = document.querySelector('#list_movies');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const movies = data.results;

    for (const movie of movies) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      movieElement.appendChild(li);
    }
  });
