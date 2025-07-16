#!/usr/bin/node

const updateHeaderButton = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateHeaderButton.addEventListener('click', function () {
  headerElement.textContent = 'New Header!!!';
});
