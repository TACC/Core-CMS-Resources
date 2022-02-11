#!/usr/bin/env node

const cmd = require('node-cmd');

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

  cmd.runSync(`
    core-styles\
    --input-dir "${ROOT}/${corePath}/src"\
    --output-dir "${ROOT}/${corePath}/build"\
    --custom-config-files\
      "${ROOT}/${corePath}/.postcssrc.yml"\
    --verbose\
  `);

  if (corePath !== projectPath) {
    cmd.runSync(`
      core-styles\
      --input-dir "${ROOT}/${projectPath}/src"\
      --output-dir "${ROOT}/${projectPath}/build"\
      --custom-config-files\
        "${ROOT}/${corePath}/.postcssrc.yml"\
        "${ROOT}/${projectPath}/.postcssrc.yml"\
      --verbose\
    `);
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
