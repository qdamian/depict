/**
 * @licstart  The following is the entire license notice for the
 *  JavaScript code in this page.
 *
 * Copyright 2014, Damian Quiroga
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
    baseUrl: ".",
    paths: {
        'd3': '3rdparty/d3/d3',
        'jquery': '3rdparty/jquery/jquery',
        'selectize': '3rdparty/selectize/selectize',
    },
    shim: {
        'd3': {
            exports: 'd3'
        },
        'jquery' : {
            exports: '$'
        },
        "selectize" : {
            deps: ['jquery'],
        }
    }
});

require([
    'scripts/src/control/Search',
    'scripts/src/data/Receiver',
], function(SearchControl, DataReceiver) {
        var searchControl = new SearchControl();
        var dataReceiver = new DataReceiver(searchControl);
});
