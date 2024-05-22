#!/usr/bin/node

const fs = require('fs');
const { exit } = require('process');

let filename;
let data;
try {
  const args = process.argv.slice(2);
  filename = args[0];
  data = args[1];
} catch (e) {
  exit(1);
}

fs.writeFile(filename, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
