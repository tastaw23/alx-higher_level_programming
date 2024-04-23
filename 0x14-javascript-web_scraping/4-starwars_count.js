#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // ID of Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    const charactersUrls = film.characters;
    if (charactersUrls.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });

  console.log(count);
});
