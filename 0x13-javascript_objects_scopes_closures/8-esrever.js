#!/usr/bin/node

exports.esrever = function (list, searchElement) {
  const myArray = new Array(list.length).fill(0);
  let j = 0;
  for (let i = list.length; i > 0; i--, j++) {
    myArray[j] = list[i - 1];
  }
  return myArray;
};
