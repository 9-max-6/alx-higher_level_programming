#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const convertedNumber = Number(argv[2]);

if (Number.isNaN(convertedNumber)) {
  console.log('Missing size');
} else {
  for (let i = 1; i < convertedNumber; i++) {
    for (let i = 1; i < convertedNumber; i++) {
      process.stdout.write('X');
    }
    console.log('X');
  }
}
