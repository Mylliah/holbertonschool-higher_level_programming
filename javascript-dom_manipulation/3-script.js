#!/usr/bin/node

const toggleHeaderButton = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

toggleHeaderButton.addEventListener('click', function () {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
