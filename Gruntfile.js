/**
 * @licstart  The following is the entire license notice for the
 *  JavaScript code in this page.
 *
 * Copyright 2014 Damian Quiroga
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

  grunt.initConfig({
    shell: {
      'mocha-phantomjs': {
        command: 'mocha-phantomjs depict/html5/test/runner.html',
        options: {
          stdout: true,
          stderr: true,
          failOnError: true
        }
      }
    },
    jshint: {
      options: {
        curly: true,
        eqeqeq: true,
        eqnull: true,
        browser: true,
        globals: {
          jQuery: true
        },
      },
      files: {
        src: ['depict/html5/**/test/*.js']
      },
    },
    coffeelint: {
      app: ['depict/html5/**/*.coffee'],
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
        cwd: '.',
        src: ['depict/html5/scripts/**/*.coffee', 'depict/html5/test/**/*.coffee'],
        dest: '.',
        ext: '.js'
      }
    },
    sass: {
      compile: {
        files: {
            'depict/html5/css/main.css': 'depict/html5/css/main.scss'
        }
      }
    }
  });

  require('load-grunt-tasks')(grunt);

  grunt.registerTask('compile', ['coffee',
                                 'sass']);

  grunt.registerTask('lint', ['compile',
                              'coffeelint',
                              'jshint']);

  grunt.registerTask('test', ['coffee',
                              'shell:mocha-phantomjs']);

  grunt.registerTask('default', ['lint',
                                 'test'])
};
