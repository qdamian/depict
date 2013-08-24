/**
 * @licstart  The following is the entire license notice for the
 *  JavaScript code in this page.
 *
 * Copyright 2013 Damian Quiroga
 *
 * This file is part of Depict.
 *
 * Depict is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Depict is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Depict.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @licend  The above is the entire license notice
 * for the JavaScript code in this page.
 */

module.exports = function(grunt) {
  "use strict";

  grunt.loadNpmTasks('grunt-contrib-coffee');

  grunt.initConfig({
    shell: {
      'mocha-phantomjs': {
        command: 'mocha-phantomjs test/testRunner.html',
        options: {
          stdout: true,
          stderr: true,
          failOnError: true
        }
      }
    },
    watch: {
      jsFiles: {
        files: ['**/*.coffee', '**/*.js'],
        tasks: ['coffee', 'shell:mocha-phantomjs']
      }
    },
    coffee: {
      glob_to_multiple: {
        expand: true,
        flatten: true,
        cwd: 'scripts/src',
        src: ['*.coffee'],
        dest: 'scripts/src',
        ext: '.js'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', ['coffee', 'shell:mocha-phantomjs']);

};
