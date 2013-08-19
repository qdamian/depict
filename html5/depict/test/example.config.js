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

require.config({
    baseUrl: "../scripts/src",
    paths: {
        'chai': '../../node_modules/chai/chai',
        'chai-jquery': '../../node_modules/chai-jquery/chai-jquery',
        'jquery': '../../node_modules/jquery-browser/lib/jquery',
        'sinon': '../../node_modules/sinon/pkg/sinon',
        'd3': '../../node_modules/d3/d3' 
    },
    shim: {
        sinon: {
            exports: 'sinon'
        },
        d3: {
            exports: 'd3'
        },
        'jquery': {
          exports: '$'
        },
        'chai-jquery': ['jquery', 'chai']
    }
});

require([
    '../../scripts/src/DependencyGraph',
], function(DependencyGraph) {
        var dependencyGraph = new DependencyGraph('body', 960, 500);
        graph = {"nodes": [ {"name":"Rio Tercero"},
                           {"name":"Cordoba"},
                           {"name":"San Salvador"},
                           {"name":"Buenos Aires"}],
                "links":[ {"source":1,"target":0,"value":1},
                          {"source":2,"target":0,"value":8},
                          {"source":3,"target":0,"value":10},
                          {"source":3,"target":2,"value":6}
                        ]
               }
        dependencyGraph.draw(graph.nodes, graph.links)
});
