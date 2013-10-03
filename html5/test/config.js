/**
 * @licstart  The following is the entire license notice for the 
 *  JavaScript code in this page.
 *
 * Copyright 2013, Damian Quiroga
 *
 * This file is part of depict.
 *
 * depict is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * depict is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with depict.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @licend  The above is the entire license notice
 * for the JavaScript code in this page.
 */

require.config({
    baseUrl: '../scripts/src',
    paths: {
        'chai': '../../../node_modules/chai/chai',
        'chai-jquery': '../../../node_modules/chai-jquery/chai-jquery',
        'd3': '../../../node_modules/d3/d3',
        'jquery': '../../../node_modules/jquery-browser/lib/jquery',
        'sinon': '../../../node_modules/sinon/pkg/sinon',
        'Squire': '../../../node_modules/squirejs/src/Squire'
    },
    shim: {
        'd3': {
            exports: 'd3'
        },
        'jquery': {
          exports: '$'
        },
        'chai-jquery': ['jquery', 'chai'],
        'sinon': {
            exports: 'sinon'
        }
    }
});

require([
    'test/DependencyGraphTest',
    'test/ModuleDependencyGraphTest',
    'test/ModelJsonParserTest',
    'model/test/ModuleTest',
], function() {
    if (typeof mochaPhantomJS !== "undefined") { mochaPhantomJS.run(); }
    else { mocha.run(); }
});
