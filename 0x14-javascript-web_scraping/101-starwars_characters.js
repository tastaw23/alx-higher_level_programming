#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;
  const charactersPromises = [];

  charactersUrls.forEach(characterUrl => {
    const promise = new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(`Error: ${response.statusCode}`);
          return;
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
    charactersPromises.push(promise);
  });

  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => console.error(error));
});
