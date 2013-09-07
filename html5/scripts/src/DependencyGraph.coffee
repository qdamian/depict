###
Copyright 2013 Damian Quiroga

This file is part of Depict.

Depict is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Depict is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Depict. If not, see <http://www.gnu.org/licenses/>.
###

collide = (node) ->
    r = node.radius + 16
    nx1 = node.x - r
    nx2 = node.x + r
    ny1 = node.y - r
    ny2 = node.y + r
    (quad, x1, y1, x2, y2) ->
        if quad.point and (quad.point isnt node)
            x = node.x - quad.point.x
            y = node.y - quad.point.y
            l = Math.sqrt(x * x + y * y)
            r = node.radius + quad.point.radius
            if l < r
                l = (l - r) / l * .5
                node.x -= x *= l
                node.y -= y *= l
                quad.point.x += x
                quad.point.y += y
        x1 > nx2 or x2 < nx1 or y1 > ny2 or y2 < ny1

window.define ["d3"], (d3) ->
    "use strict"
    DependencyGraph = (container, width, height) ->
        @svg = d3.select(container)
                 .append("svg")
                 .attr("width", width)
                 .attr("height", height)

        @force = d3.layout.force()

        @force.gravity(0.05)
                    .charge(-200)
                    .linkDistance(60)
                    .size([width, height])
        return

    DependencyGraph::draw = (nodesData, linksData) ->
        for item in nodesData
          item.radius = 50

        @force.nodes(nodesData)
                    .links(linksData)

        links = @_addLinks(linksData)
        nodeGroups = @_addNodeGroups(nodesData)
        circles = @_addNodes(nodeGroups)
        texts = @_addTexts(nodeGroups)

        @_adjustPositionOnTick(nodesData, circles, texts, links)
        @force.start()

    DependencyGraph::_addNodeGroups = (nodesData) ->
        nodes = @svg.selectAll(".node").data(nodesData)
        nodes.enter()
             .append("g")
        root = nodesData[0]
        return nodes

    DependencyGraph::_addNodes = (nodeGroups) ->
        nodeGroups.append("circle")
                  .attr("class", "node")
                  .attr("r", (d) -> 40)
                  .style("fill", "lightblue")

    DependencyGraph::_addTexts = (nodeGroups) ->
        nodeGroups.append("text")
                  .text((d) -> d.name.replace /.*\..*\./, "")
                  .attr("text-anchor", "middle")

    DependencyGraph::_addLinks = (linksData) ->
        @svg.selectAll(".link")
            .data(linksData)
            .enter()
            .append("line")
            .attr("class", "link")
            .style("stroke-width", (d) -> Math.sqrt d.value)

    DependencyGraph::_adjustPositionOnTick = (nodes, circles, texts, links) ->
        @force.on "tick", ->
            q = d3.geom.quadtree(nodes)
            i = 0
            n = nodes.length
            q.visit collide(nodes[i])  while ++i < n
            
            circles.attr("cx", (d) -> d.x)
                   .attr("cy", (d) -> d.y)
          
            texts.attr("x", (d) -> d.x)
                 .attr("y", (d) -> d.y)

            links.attr("x1", (d) -> d.source.x)
                 .attr("y1", (d) -> d.source.y)
                 .attr("x2", (d) -> d.target.x)
                 .attr("y2", (d) -> d.target.y)

    DependencyGraph