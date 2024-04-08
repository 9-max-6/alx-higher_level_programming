#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const convertedNumber = Number(argv[2]);

if (Number.isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedNumber}`);
}
