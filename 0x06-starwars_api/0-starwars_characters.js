#!/usr/bin/node

const request = require('request');
const movieId = parseInt(process.argv[2], 10);

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, async (error, response, body) => {
	  if (error) return;
	  const movie = JSON.parse(body);

	  for (const character of movie.characters) {
		      const characterName = await new Promise((resolve, reject) => {
			            request.get(character, (error, response, body) => {
					            if (error) return;
					            const characterInfo = JSON.parse(body);
					            resolve(characterInfo.name);
					          });
			          });
		      console.log(characterName);
		    }
});

<<<<<<< HEAD
=======
  for (const character of movie.characters) {
    const characterName = await new Promise((resolve, reject) => {
      request.get(character, (error, response, body) => {
        if (error) return;
        const characterInfo = JSON.parse(body);
        resolve(characterInfo.name);
      });
    });
    console.log(characterName);
  }
});
>>>>>>> c6c8976977543e2bb8ea0c1ad08d56dd09a6bcd7
