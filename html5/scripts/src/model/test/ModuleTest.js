/**
 * @licstart  The following is the entire license notice for the
 *  JavaScript code in this page.
 *
 * Copyright 2013, Damian Quiroga
 *
 * This file is part of depict.
 *
 * depict is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * depict is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with depict.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @licend  The above is the entire license notice
 * for the JavaScript code in this page.
 */

define(['chai', 'chai-jquery', 'sinon', 'model/Module'],
                function(chai, chaiJquery, sinon, Module) {

    var should = chai.should();
    chai.use(chaiJquery);

    describe('Module', function() {
        describe("constructor", function() {

            it('should provide sensible default values', function() {
                module = new Module();

                module.name.should.equal('');
                module.dependencies.should.have.members([]);
            });

            it('should allow construction from a JSON object', function() {
                data = {
                    "name" : "fakeModule",
                    "dependencies" : ["fakeDependency1", "fakeDependency2"]
                };

                module = new Module(data);

                module.name.should.equal("fakeModule");
                module.dependencies.should.have.members(["fakeDependency1",
                                                         "fakeDependency2"]);
            });
        });
    });
});
