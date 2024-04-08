#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const a = Number(argv[2]);
const myFunc = function factorial (a) {
  if (Number.isNaN(a)) {
    return (1);
  }
  if (a === 1) {
    return (1);
  }
  return (a * myFunc(--a));
};
console.log(`${myFunc(a)}`);
