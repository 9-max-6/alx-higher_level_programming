#!/usr/bin/node

const { argv } = require('node:process');

let biggestArgument = 0;
let secondBiggestArg = 0;

if (argv.length > 2) {
  argv.slice(2).forEach(element => {
    const num = Number(element);
    if (num > biggestArgument) {
      secondBiggestArg = biggestArgument;
      biggestArgument = num;
    } else if (num > secondBiggestArg && num < biggestArgument) {
      secondBiggestArg = num;
    }
  });
}

console.log(`${secondBiggestArg}`);
