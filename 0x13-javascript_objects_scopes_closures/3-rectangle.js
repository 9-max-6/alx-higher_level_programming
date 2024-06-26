#!/usr/bin/node
const process = require('node:process');
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
}
module.exports = Rectangle;
