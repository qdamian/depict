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
        'd3': '../d3' 
    },
    shim: {
        d3: {
            exports: 'd3'
        }
    }
});

require([
    '../../scripts/src/ModuleDependencyGraph',
    '../../scripts/src/model/Module',
], function(ModuleDependencyGraph, Module) {
        var rioTercero = new Module();
        var cordoba = new Module({"name": "Cordoba"});
        rioTercero.name = "Rio Tercero"
        rioTercero.dependencies = [cordoba]

        var sanSalvador = new Module({"name" : "San Salvador",
                                       "dependencies" : [rioTercero, cordoba]});
        var buenosAires = new Module({"name": "Buenos Aires"});
        buenosAires.dependencies = [sanSalvador];

        var moduleDepGraph = new ModuleDependencyGraph("body", 960, 500);
        moduleDepGraph.draw([rioTercero, cordoba, sanSalvador, buenosAires]);
});
