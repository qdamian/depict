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

window.define(['d3'], function(d3) {
    "use strict";

    var DependencyGraph = function(container, width, height) {
        this.svg = d3.select(container).append("svg")
                                       .attr("width", width)
                                       .attr("height", height);

        this.force = d3.layout.force();

        this.force
            .charge(-100)
            .linkDistance(300)
            .size([width, height]);
    };

    DependencyGraph.prototype.draw = function(nodesData, linksData) {
        this.force
            .nodes(nodesData)
            .links(linksData);

        var links = this._addLinks(linksData);
        var nodeGroups = this._addNodeGroups(nodesData);
        var circles = this._addNodes(nodeGroups);
        var texts = this._addTexts(nodeGroups);
        this._adjustPositionOnTick(circles, texts, links);

        this.force.start();
    }

    DependencyGraph.prototype._addNodeGroups = function(nodesData) {
        var nodes = this.svg.selectAll(".node").data(nodesData)
        var nodeGroups = nodes.enter()
                             .append("g");
        return nodeGroups;
    }

    DependencyGraph.prototype._addNodes = function(nodeGroups) {
        var circles = nodeGroups.append("circle")
                               .attr("class", "node")
                               .attr("r", function(d) {
            return 40;
        }).style("fill", "lightblue")
        return circles;
    }

    DependencyGraph.prototype._addTexts = function(nodeGroups) {
        var texts = nodeGroups.append("text")
                                   .text(function(d) {
                                        return d.name;
                                        })
                                   .attr("text-anchor", "middle");
        return texts;
    }

    DependencyGraph.prototype._addLinks = function(linksData) {
        var links = this.svg.selectAll(".link")
                            .data(linksData)
                            .enter()
                            .append("line")
                            .attr("class", "link")
                            .style("stroke-width",
                            function(d) {
                                return Math.sqrt(d.value);
                            });
        return links;
    }

    DependencyGraph.prototype._adjustPositionOnTick =
                              function(circles, texts, links) {
        this.force.on("tick", function() {
            circles.attr("cx", function(d) {
                return d.x;
            }).attr("cy", function(d) {
                return d.y;
            });

            texts.attr("x", function(d) {
                return d.x;
            }).attr("y", function(d) {
                return d.y;
            });

            links.attr("x1", function(d) {
                return d.source.x;
            }).attr("y1", function(d) {
                return d.source.y;
            }).attr("x2", function(d) {
                return d.target.x;
            }).attr("y2", function(d) {
                return d.target.y;
            });
        });
    }

    return DependencyGraph;
});