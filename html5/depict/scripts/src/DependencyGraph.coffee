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

window.define ["d3"], (d3) ->
  "use strict"
  DependencyGraph = (container, width, height) ->
    @svg = d3.select(container).append("svg").attr("width", width).attr("height", height)
    @force = d3.layout.force()
    @force.charge(-100).linkDistance(300).size [width, height]
    return

  DependencyGraph::draw = (nodesData, linksData) ->
    @force.nodes(nodesData).links linksData
    links = @_addLinks(linksData)
    nodeGroups = @_addNodeGroups(nodesData)
    circles = @_addNodes(nodeGroups)
    texts = @_addTexts(nodeGroups)
    @_adjustPositionOnTick circles, texts, links
    @force.start()

  DependencyGraph::_addNodeGroups = (nodesData) ->
    nodes = @svg.selectAll(".node").data(nodesData)
    nodeGroups = nodes.enter().append("g")
    nodeGroups

  DependencyGraph::_addNodes = (nodeGroups) ->
    circles = nodeGroups.append("circle").attr("class", "node").attr("r", (d) ->
      40
    ).style("fill", "lightblue")
    circles

  DependencyGraph::_addTexts = (nodeGroups) ->
    texts = nodeGroups.append("text").text((d) ->
      d.name
    ).attr("text-anchor", "middle")
    texts

  DependencyGraph::_addLinks = (linksData) ->
    links = @svg.selectAll(".link").data(linksData).enter().append("line").attr("class", "link").style("stroke-width", (d) ->
      Math.sqrt d.value
    )
    links

  DependencyGraph::_adjustPositionOnTick = (circles, texts, links) ->
    @force.on "tick", ->
      circles.attr("cx", (d) ->
        d.x
      ).attr "cy", (d) ->
        d.y

      texts.attr("x", (d) ->
        d.x
      ).attr "y", (d) ->
        d.y

      links.attr("x1", (d) ->
        d.source.x
      ).attr("y1", (d) ->
        d.source.y
      ).attr("x2", (d) ->
        d.target.x
      ).attr "y2", (d) ->
        d.target.y

  DependencyGraph

