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

define(['chai', 'chai-jquery', 'sinon', 'model/Module', 'DependencyGraph', 'ModuleDependencyGraph'],
    function(chai, chaiJquery, sinon, Module, DependencyGraph, ModuleDependencyGraph) {

    var should = chai.should();
    chai.use(chaiJquery);

    describe('ModuleDependencyGraph', function() {
        describe("constructor", function() {

            it('should represent each module as a node'), function() {
                dependencyGraphSpy = sinon.spy(DependencyGraph);
                module1 = new Module();
                module2 = new Module();
                moduleDepGraph = new ModuleDependencyGraph([module1, module2]);
                // dependencyGraphSpy.called.should.equal(true);
            };

            it('should represent each dependency as a link'), function() {
            };
        });
    });
}); 
