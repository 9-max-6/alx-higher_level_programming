#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const convertedNumber = Number(argv[2]);
const myText = 'C is fun';

if (Number.isNaN(convertedNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedNumber; i++) {
    console.log(myText);
  }
}
