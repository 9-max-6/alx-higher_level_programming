#!/usr/bin/node

const request = require('request');
let url;

try {
  const args = process.argv.slice(2);
  url = args[0];
} catch (e) {
  console.log(e);
}
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response && response.statusCode);
  }
});
