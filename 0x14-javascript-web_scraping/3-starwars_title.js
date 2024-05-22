#!/usr/bin/node

const { exit } = require('process');
const request = require('request');
let movieId;
const url = 'https://swapi-api.alx-tools.com/api/films/';
try {
  const args = process.argv.slice(2);
  movieId = args[0];
} catch (e) {
  exit(1);
}
const fullUrl = url + movieId;

request(fullUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
