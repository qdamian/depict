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

define (require) ->

  chai = require 'chai'
  Squire = require 'Squire'
  Module = require 'scripts/model/Module'
  Function = require 'scripts/model/Function'
  ModelJsonParser = require 'scripts/ModelJsonParser'

  assert = chai.assert

  describe 'ModelJsonParser', ->
    describe 'parse', ->
      it 'should create a Module object if type is Module', ->
        # Arrange
        moduleJsonParser = new ModelJsonParser 'id_'

        # Act
        obj = moduleJsonParser.parse('''
          {
            "id_":"../aa.py",
            "name":"aa",
            "parent":null,
            "dependencies":[],
            "branch_depth":0,
            "type":"Module",
            "children":[]
          }
        ''')

        # Assert
        assert.instanceOf obj, Module
        assert.equal obj.name, 'aa'

      it 'should create a Function object if type is Function', ->
        # Arrange
        moduleJsonParser = new ModelJsonParser('id_')

        # Act
        obj = moduleJsonParser.parse('''
          {
            "id_": "aa.py:1",
            "name": "fake_function_name",
            "type": "Function"
          }
        ''')

        # Assert
        assert.instanceOf obj, Function
        assert.equal obj.name, 'fake_function_name'
