#!/usr/bin/node

const fs = require('fs');
const { exit } = require('process');

let filename;
try {
  const args = process.argv.slice(2);
  filename = args[0];
} catch (e) {
  exit(1);
}

fs.readFile(filename, 'utf-8', (err, fd) => {
  if (err) {
    console.log(err);
  }
  console.log(fd);
});
