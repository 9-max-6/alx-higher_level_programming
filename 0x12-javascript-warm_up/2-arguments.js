#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
if (argv.length === 2) {
  console.log('No argument');
}
if (argv.length === 3) {
  console.log('Argument found');
}
if (argv.length > 3) {
  console.log('Arguments found');
}
