#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const a = argv[2];
const b = argv[3];
const myAddition = function add (a, b) {
  const convertedNumberOne = Number(a);
  const convertedNumberTwo = Number(b);
  console.log(`${convertedNumberOne + convertedNumberTwo}`);
};
myAddition(a, b);
