#!/usr/bin/node

const characterElement = document.querySelector('#character');
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    characterElement.textContent = `name : ${characterName}`;
  });
