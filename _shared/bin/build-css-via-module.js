#!/usr/bin/env node

const coreStyles = require('core-styles');
const projectName = process.env.npm_config_project;

const ROOT = __dirname + '/../..';

build('core-cms');
if ( projectName && projectName !== 'core-cms') {
  build( projectName );
}

/**
 * Execute command to build CSS for given project (directory)
 * @param {string} projectName - The name of the project
 */
 function build( projectName ) {
  const path = projectName + '/static/' + projectName + '/css';

  coreStyles(
    `${ROOT}/${path}/src`,
    `${ROOT}/${path}/build`, {
      customConfigFiles: [
        `${ROOT}/_shared/.postcssrc.yml`,
        `${ROOT}/${path}/src/.postcssrc.yml`
      ],
      verbose: true,
    }
  );
}
