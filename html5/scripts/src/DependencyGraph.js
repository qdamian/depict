/*
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
*/


(function() {
  var collide;

  collide = function(node) {
    var nx1, nx2, ny1, ny2, r;
    r = node.radius + 16;
    nx1 = node.x - r;
    nx2 = node.x + r;
    ny1 = node.y - r;
    ny2 = node.y + r;
    return function(quad, x1, y1, x2, y2) {
      var l, x, y;
      if (quad.point && (quad.point !== node)) {
        x = node.x - quad.point.x;
        y = node.y - quad.point.y;
        l = Math.sqrt(x * x + y * y);
        r = node.radius + quad.point.radius;
        if (l < r) {
          l = (l - r) / l * .5;
          node.x -= x *= l;
          node.y -= y *= l;
          quad.point.x += x;
          quad.point.y += y;
        }
      }
      return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
    };
  };

  window.define(["d3"], function(d3) {
    "use strict";
    var DependencyGraph;
    DependencyGraph = function(container, width, height) {
      this.svg = d3.select(container).append("svg").attr("width", width).attr("height", height);
      this.force = d3.layout.force();
      this.force.gravity(0.05).charge(-200).linkDistance(60).size([width, height]);
    };
    DependencyGraph.prototype.draw = function(nodesData, linksData) {
      var circles, item, links, nodeGroups, texts, _i, _len;
      for (_i = 0, _len = nodesData.length; _i < _len; _i++) {
        item = nodesData[_i];
        item.radius = 50;
      }
      this.force.nodes(nodesData).links(linksData);
      links = this._addLinks(linksData);
      nodeGroups = this._addNodeGroups(nodesData);
      circles = this._addNodes(nodeGroups);
      texts = this._addTexts(nodeGroups);
      this._adjustPositionOnTick(nodesData, circles, texts, links);
      return this.force.start();
    };
    DependencyGraph.prototype._addNodeGroups = function(nodesData) {
      var nodes, root;
      nodes = this.svg.selectAll(".node").data(nodesData);
      nodes.enter().append("g");
      root = nodesData[0];
      return nodes;
    };
    DependencyGraph.prototype._addNodes = function(nodeGroups) {
      return nodeGroups.append("circle").attr("class", "node").attr("r", function(d) {
        return 40;
      }).style("fill", "lightblue");
    };
    DependencyGraph.prototype._addTexts = function(nodeGroups) {
      return nodeGroups.append("text").text(function(d) {
        return d.name.replace(/.*\..*\./, "");
      }).attr("text-anchor", "middle");
    };
    DependencyGraph.prototype._addLinks = function(linksData) {
      return this.svg.selectAll(".link").data(linksData).enter().append("line").attr("class", "link").style("stroke-width", function(d) {
        return Math.sqrt(d.value);
      });
    };
    DependencyGraph.prototype._adjustPositionOnTick = function(nodes, circles, texts, links) {
      return this.force.on("tick", function() {
        var i, n, q;
        q = d3.geom.quadtree(nodes);
        i = 0;
        n = nodes.length;
        while (++i < n) {
          q.visit(collide(nodes[i]));
        }
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
        return links.attr("x1", function(d) {
          return d.source.x;
        }).attr("y1", function(d) {
          return d.source.y;
        }).attr("x2", function(d) {
          return d.target.x;
        }).attr("y2", function(d) {
          return d.target.y;
        });
      });
    };
    return DependencyGraph;
  });

}).call(this);
