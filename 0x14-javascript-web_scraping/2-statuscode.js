#!/usr/bin/node

const { exit } = require('process');
const request = require('request');
let url;

try {
  const args = process.argv.slice(2);
  url = args[0];
} catch (e) {
  exit(1);
}
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
