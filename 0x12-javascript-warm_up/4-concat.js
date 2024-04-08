#!/usr/bin/node

const process = require('node:process');
const argv = process.argv;
const format = ' is ';
const completedstring = argv[2] + format + argv[3];
console.log(completedstring);
