/*
Copyright 2013 Damian Quiroga

This file is part of Depict.

Depict is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Depict is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Depict.  If not, see <http://www.gnu.org/licenses/>.
*/


(function() {
  window.define(["DependencyGraph", "model/Module"], function(DependencyGraph, Module) {
    "use strict";
    var ModuleDependencyGraph;
    ModuleDependencyGraph = function(container, width, height) {
      this.dependencyGraph = new DependencyGraph(container, width, height);
    };
    ModuleDependencyGraph.prototype.draw = function(modules) {
      var links;
      links = this._findLinks(modules);
      this.dependencyGraph.draw(modules, links);
    };
    ModuleDependencyGraph.prototype._findLinks = function(modules) {
      var dep, links, mod, _i, _j, _len, _len1, _ref;
      links = [];
      for (_i = 0, _len = modules.length; _i < _len; _i++) {
        mod = modules[_i];
        _ref = mod.dependencies;
        for (_j = 0, _len1 = _ref.length; _j < _len1; _j++) {
          dep = _ref[_j];
          links.push({
            source: modules.indexOf(mod),
            target: modules.indexOf(dep),
            value: 1
          });
        }
      }
      return links;
    };
    return ModuleDependencyGraph;
  });

}).call(this);
