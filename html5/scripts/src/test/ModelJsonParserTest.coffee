###
Copyright 2014, Damian Quiroga

This file is part of depict.

depict is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

depict is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with depict. If not, see <http://www.gnu.org/licenses/>.
###

define ["chai",
        "Squire",
        "model/Module"], (chai,
                          Squire,
                          Module) ->

  should = chai.should()

  describe "ModelJsonParser", ->
    describe "parse", ->
      it "should be able to create one object", ->
        new Squire().require ["ModelJsonParser"], (ModelJsonParser) ->
          # Arrange
          moduleJsonParser = new ModelJsonParser("id_")

          # Act
          obj = moduleJsonParser.parse("""
            {
                "id_":"../aa.py",
                "name":"aa",
                "parent":null,
                "dependencies":[],
                "branch_depth":0,
                "type":"Module",
                "children":[]
            }
          """)

          (obj instanceof Module).should.equal true
          obj.name.should.equal "aa"
