#!/usr/bin/env node

/** Build CSS using the Core-Styles module */

const coreStyles = require('core-styles');

const ROOT = __dirname + '/../..';
const CORE_NAME = 'core-cms';
const PROJECT_NAME = process.env.npm_config_project || CORE_NAME;

build(PROJECT_NAME);

/**
 * Execute command to build CSS for given project (directory)
 * @param {string} projectName - The name of the project
 */
function build( projectName ) {
  const corePath = getPath(CORE_NAME);
  const projectPath = getPath(projectName);

  // To illustrate Project is built on top of Core:
  // // build Core first  coreStyles(
  coreStyles(
    `${ROOT}/${corePath}/src`,
    `${ROOT}/${corePath}/build`, {
      customConfigFiles: [
        `${ROOT}/${corePath}/.postcssrc.yml`
      ],
      verbose: true,
    }
  );
  // // build Project next (if not Core)
  if (corePath !== projectPath) {
    coreStyles(
      `${ROOT}/${projectPath}/src`,
      `${ROOT}/${projectPath}/build`, {
        customConfigFiles: [
          `${ROOT}/${corePath}/.postcssrc.yml`,
          `${ROOT}/${projectPath}/.postcssrc.yml`
        ],
        verbose: true,
      }
    );
  }
}

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @return {string} - The path
 */
function getPath( dirName ) {
  return dirName + '/static/' + dirName + '/css';
}
