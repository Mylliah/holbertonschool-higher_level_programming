#!/usr/bin/node

// Attend que le DOM soit entièrement chargé
document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.querySelector('#hello');
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      const helloWord = data.hello;
      helloElement.textContent = helloWord;
    })
    .catch(error => {
      console.error('Erreur lors de la récupération du mot "hello" :', error);
    });
});
