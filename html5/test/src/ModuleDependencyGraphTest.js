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

define(['Squire', 'chai', 'sinon', 'model/Module'],
    function(Squire, chai, sinon, Module) {

    var should = chai.should();

    describe('ModuleDependencyGraph', function() {
        describe("constructor", function() {
            it('should create a dependency graph', function() {
                var depGraphMock = sinon.mock();
                var injector = new Squire();
                injector
                    .mock('DependencyGraph', Squire.Helpers.returns(depGraphMock))
                    .require(['ModuleDependencyGraph', 'mocks'], function(ModuleDependencyGraph, mocks) {
                        var moduleDepGraph = new ModuleDependencyGraph("#test1", 20, 30);
                        depGraphMock.calledWith("#test1", 20, 30).should.equal(true);
                    });
            });

            it('should represent each module as a node', function() {
                var drawMock = sinon.mock();
                var injector = new Squire();
                injector
                    .mock('DependencyGraph', Squire.Helpers.constructs({draw: drawMock}))
                    .require(['ModuleDependencyGraph', 'mocks'], function(ModuleDependencyGraph, mocks) {
                    var module1 = new Module({"name":"John"});
                    var module2 = new Module();
                    var moduleDepGraph = new ModuleDependencyGraph();
                    moduleDepGraph.draw([module1, module2]);
                    drawMock.calledWith([module1, module2]).should.equal(true);
                  });
            });

            it('should represent each dependency as a link', function() {
                var drawMock = sinon.mock();
                var injector = new Squire();
                injector
                    .mock('DependencyGraph', Squire.Helpers.constructs({draw: drawMock}))
                    .require(['ModuleDependencyGraph', 'mocks'], function(ModuleDependencyGraph, mocks) {
                    var module1 = new Module({"name": "module1"})
                    var module2 = new Module({"name": "module2"})
                    var module3 = new Module({"name": "module3"})
                    module1.dependencies = [module3];
                    module2.dependencies = [module1];
                    var moduleDepGraph = new ModuleDependencyGraph();
                    moduleDepGraph.draw([module1, module2, module3]);
                    var expected_links = [{
                            "source" : 0,
                            "target" : 2,
                            "value" : 1
                        }, {
                            "source" : 1,
                            "target" : 0,
                            "value" : 1
                        }]
                    drawMock.calledWith([module1, module2, module3], expected_links).should.equal(true);
                });
            });
        });
    });
}); 
