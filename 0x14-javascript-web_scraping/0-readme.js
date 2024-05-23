#!/usr/bin/node
const fs = require('fs');
// Reads the content of the file
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
