#!/usr/bin/node
exports.callMeMoby = function call (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
