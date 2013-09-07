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

define ["chai", "sinon", "Squire", "model/Module"], (chai, sinon, Squire, Module) ->

    should = chai.should()

    fakeJsonData = [{id_: "fake_id1", type: "Module"},
                    {id_: "fake_id2", type: "Module",
                    dep: [{id_: "fake_id1", type: "Module"}]}]

    describe "ModelJsonParser", ->
        describe "constructor", ->
            it "should create objects based on their type", ->
                # Arrange
                jsonStub = sinon.stub().callsArgWith(1, undefined, fakeJsonData)
                callbackSpy = sinon.stub()
                new Squire().mock("d3", Squire.Helpers.returns(json: jsonStub))
                                   .require ["ModelJsonParser", "mocks"],
                                   (ModelJsonParser, mocks) ->
                                       
                    # Act
                    moduleJsonParser = new ModelJsonParser("fake_file.json", "id_", callbackSpy)

                    # Assert
                    obj = callbackSpy.args[0][0]
                    (obj[0] instanceof Module).should.equal true
                    obj[0].id_.should.equal "fake_id1"
                    (obj[1] instanceof Module).should.equal true
                    obj[1].id_.should.equal "fake_id2"

            it "should revive references", ->
                # Arrange
                jsonStub = sinon.stub().callsArgWith(1, undefined, fakeJsonData)
                callbackSpy = sinon.stub()
                new Squire().mock("d3", Squire.Helpers.returns(json: jsonStub))
                                   .require ["ModelJsonParser", "mocks"],
                                   (ModelJsonParser, mocks) ->

                    # Act
                    moduleJsonParser = new ModelJsonParser("fake_file.json", "id_", callbackSpy)

                    # Assert
                    obj = callbackSpy.args[0][0]
                    obj[1].dep[0].should.equal obj[0]
                    (obj[1].dep[0] instanceof Module).should.equal true
