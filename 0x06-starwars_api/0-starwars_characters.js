#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const arg = process.argv;
const movieId = arg[2];

request.get(url + movieId, (error, response, body) => {
  try {
    if (error) {
      throw new Error('An error occurred while making the request.');
    }

    const resp = JSON.parse(body);
    const characters = {};
    const characterIds = [];
    if (resp.characters.length) {
      const charLength = resp.characters.length;
      resp.characters.forEach(element => {
        request.get(element, (err, response, body) => {
          try {
            if (err) {
              throw new Error('An error occurred while making the character request.');
            }

            const urlArray = element.split('/');
            const id = urlArray[urlArray.length - 2];
            const json = JSON.parse(body);
            characters[id] = json.name;
            characterIds.push(Number(id));
            if (Object.keys(characters).length === charLength) {
              characterIds.sort((a, b) => {
                return a - b;
              });
              characterIds.forEach(element => {
                console.log(characters[element]);
              });
            }
          } catch (characterError) {
            console.error('Character Request Error:', characterError.message);
          }
        });
      });
    }
  } catch (requestError) {
    console.error('Movie Request Error:', requestError.message);
  }
});
