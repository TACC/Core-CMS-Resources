#!/usr/bin/env node

const fs = require('fs');

const root = __dirname;
const inFile = root + '/update-version.css';
const outFile = root + '/../static/css/src/_version.css';

const input = fs.readFileSync(inFile, 'utf8');
const output = input.replace(/{{ver}}/g, process.env.npm_package_version);

fs.writeFileSync(outFile, output, 'utf8');
