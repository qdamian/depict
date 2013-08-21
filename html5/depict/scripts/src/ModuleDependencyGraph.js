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

window.define(['DependencyGraph', 'model/Module'],
        function(DependencyGraph, Module) {
    "use strict";

    var ModuleDependencyGraph = function(container, width, height) {
        this.dependencyGraph = new DependencyGraph(container, width, height);
    };

    ModuleDependencyGraph.prototype.draw = function(modules) {
        var links = this._findLinks(modules);
        this.dependencyGraph.draw(modules, links);
    }

    ModuleDependencyGraph.prototype._findLinks = function(modules) {
        var links = [];
        for (var mod_i=0; mod_i<modules.length; mod_i++) {
            var deps = modules[mod_i].dependencies;
            for (var dep_i=0; dep_i<deps.length; dep_i++) {
                links.push({ "source" : mod_i,
                             "target" : modules.indexOf(deps[dep_i]),
                             "value" : 1 });
            }
        }
        return links;
    }

    return ModuleDependencyGraph;
});