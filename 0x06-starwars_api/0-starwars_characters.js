#!/usr/bin/node
/**
 * a script that prints all characters of a star wars movie
 * in the order they appear from the api
 * Usage: ./100-starwars_characters id
 */
if (process.argv.length < 3) process.exit();
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, res, body) {
  if (error) { console.log(error); } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    const fetchCharacters = async () => {
      for (const characterUrl of characters) {
        const promise = new Promise((resolve, reject) => {
          request(characterUrl, (error, res, body) => {
            if (error) {
              reject(error);
            } else {
              const karacter = JSON.parse(body);
              resolve(karacter.name);
            }
          });
        });
        const response = await promise;
        console.log(response);
      }
    };
    fetchCharacters();
  }
});
