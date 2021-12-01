const Chance = require('chance')
var chance1 = new Chance();

// These yield the same values, in sequence
console.log(chance1.integer({ min: 1, max: 100 }));