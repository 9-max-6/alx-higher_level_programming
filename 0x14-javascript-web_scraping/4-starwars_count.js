#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

const apiURL = argv[2];

request(apiURL, function (err, response, body) {
  if (err) {
    console.error('Error making the request:', err);
    return;
  }

  if (response && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    const dataCount = results.reduce(function (count, result) {
      const endsWithCount = result.characters.reduce((acc, characterUrl) => {
        return acc + (characterUrl.endsWith('/18/') ? 1 : 0);
      }, 0);
      return count + endsWithCount;
    }, 0);

    console.log(dataCount);
  } else {
    console.error('Received a non-200 response status:', response.statusCode);
  }
});
