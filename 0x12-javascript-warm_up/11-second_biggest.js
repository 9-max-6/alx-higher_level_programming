#!/usr/bin/node

const { argv } = require('node:process');
let biggestArgument = 0;
if (argv.length > 2) {
  argv.forEach((element, index) => {
    if (index !== 1 || index !== 2) {
      if (element > biggestArgument) {
        biggestArgument = element;
      }
    }
  });
}
console.log(`${biggestArgument}`);
