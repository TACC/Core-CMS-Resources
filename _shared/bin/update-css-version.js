#!/usr/bin/env node

/** Create CSS file to import that prints project version */

const fs = require('fs');

const root = __dirname;
const outFile = root + '/../static/css/src/_version.css';

const ver = process.env.npm_package_version;
const rev = getGitRev( getSubmodGitDir() ).substring(0, 7);

const output = `/*! @tacc/core-cms-resources#${rev} (≥ v${ver}) | MIT License | github.com/TACC/Core-CMS-Resources */`;

/**
 * Get the Git revision of the current working directory code
 * @param {string} [gitDir='.git'] - Path to Git directory
 * @return {string}
 * @see https://stackoverflow.com/a/34518749/11817077
 */
function getGitRev(gitDir='.git') {
  let rev = fs.readFileSync(gitDir + '/HEAD').toString().trim();
  const revFile = gitDir + '/' + rev.substring(5);

  if (rev.indexOf(':') !== -1) {
    console.log('Reading Git revision from: ' + revFile);
    rev = fs.readFileSync(revFile).toString().trim();
  }

  return rev;
}

/**
 * Get the Git directory of the current working directory submodule
 * @return {string} Path to the Git directory for the submodule
 */
function getSubmodGitDir() {
  const ref = fs.readFileSync('.git').toString().trim();

  return ref.substring(8);
}

console.log(`Updating CSS version to package version ${ver} and Git revision ${rev}[...]`);
fs.writeFileSync(outFile, output, 'utf8');
