#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(`${argv[2]}`);
}
