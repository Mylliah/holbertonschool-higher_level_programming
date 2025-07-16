#!/usr/bin/node

const redHeaderButton = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderButton.addEventListener('click', function () {
  headerElement.classList.add('red');
});
