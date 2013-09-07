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

define(['chai', 'chai-jquery', 'sinon', 'd3', 'DependencyGraph'],
    function(chai, chaiJquery, sinon, d3, DependencyGraph) {

    var should = chai.should();
    chai.use(chaiJquery);

    TEST_NODES = [{
        "name" : "Node1"
    }, {
        "name" : "Node2"
    }]

    TEST_LINKS = [{
        "source" : 0,
        "target" : 1,
        "value" : 1
    }, {
        "source" : 1,
        "target" : 0,
        "value" : 1
    }]

    describe('DependencyGraph', function() {
        beforeEach(function() {
            var chargeStub = sinon.stub();
            var linkDistanceStub = sinon.stub();
            nodesStub = sinon.stub();
            linksStub = sinon.stub();
            startSpy = sinon.stub();
            onStub = sinon.stub();
            gravityStub = sinon.stub();

            d3Methods = {
                charge : chargeStub,
                linkDistance : linkDistanceStub,
                size : sinon.stub(),
                nodes : nodesStub,
                links : linksStub,
                on : onStub,
                start : startSpy,
                gravity: gravityStub
            }

            chargeStub.returns(d3Methods);
            linkDistanceStub.returns(d3Methods);
            nodesStub.returns(d3Methods);
            linksStub.returns(d3Methods);
            onStub.returns(d3Methods);
            gravityStub.returns(d3Methods);
        });

        afterEach(function() {
        });

        describe("constructor", function() {

            it('should create an SVG canvas filling its container', function() {
                $("<div id=test-canvas/>").appendTo("body");

                dependencyGraph = new DependencyGraph('#test-canvas', 10, 20);

                $('#test-canvas svg').should.exist;
                $('#test-canvas svg').should.have.css('width', '10px');
                $('#test-canvas svg').should.have.css('height', '20px');

                $('#test-canvas').remove();
            });

            it('should initialize a D3 force layout', function() {
                forceStub = sinon.stub(d3.layout, "force").returns(d3Methods);

                dependencyGraph = new DependencyGraph('body', 10, 20);

                forceStub.called.should.equal(true)

                d3.layout.force.restore();
            });
        });

        describe("draw", function() {

            it('should start the force layout', function() {
                forceStub = sinon.stub(d3.layout, "force").returns(d3Methods);
                sinon.mock(d3.layout)
                dependencyGraph = new DependencyGraph('body', 10, 20);

                dependencyGraph.draw(TEST_NODES, TEST_LINKS);

                startSpy.called.should.equal(true);

                d3.layout.force.restore();
            });

            it('should add a circle for each node', function() {
                $("<div id=test-circles/>").appendTo("body");

                dependencyGraph = new DependencyGraph('#test-circles', 10, 20);

                dependencyGraph.draw(TEST_NODES, TEST_LINKS);

                $('#test-circles circle').length.should.equal(2);
                $('#test-circles').remove()
            })

            it('should add a text for each node', function() {
               $("<div id=test-texts/>").appendTo("body");
               
               dependencyGraph = new DependencyGraph('#test-texts', 10, 20);
               
               dependencyGraph.draw(TEST_NODES, TEST_LINKS);
               
                $('#test-texts text').length.should.equal(2);
                $('#test-texts').remove()
            });

            it('should add a line for each link', function() {
                $("<div id=test-lines/>").appendTo("body");

                $('line').remove()
                dependencyGraph = new DependencyGraph('#test-lines', 10, 20);
                dependencyGraph.draw(TEST_NODES, TEST_LINKS);

                $('#test-lines line').length.should.equal(2);
                $('#test-lines').remove()
            });
        });
    });
}); 
