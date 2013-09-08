###
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
###

window.define ["DependencyGraph", "model/Module"], (DependencyGraph, Module) ->
  "use strict"
  ModuleDependencyGraph = (container, width, height) ->
    @dependencyGraph = new DependencyGraph(container, width, height)
    return

  ModuleDependencyGraph::draw = (modules) ->
    links = @_findLinks(modules)
    @dependencyGraph.draw(modules, links)
    return

  ModuleDependencyGraph::_findLinks = (modules) ->
    links = []

    for mod in modules
      for dep in mod.dependencies
        links.push
          source: modules.indexOf mod
          target: modules.indexOf dep
          value: 1
    links
 
  ModuleDependencyGraph
