#!/usr/bin/node
const fs = require('fs');
// Checks if the file path is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

// Gets the file path from the command line arguments
const filePath = process.argv[2];

// Reads the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File content:', data);
});
