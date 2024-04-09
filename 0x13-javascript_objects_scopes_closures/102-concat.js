#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

const concatenatedContent = content1 + content2;

fs.writeFileSync(destination, concatenatedContent);
