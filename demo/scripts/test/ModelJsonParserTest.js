/*
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
*/


(function() {
  define(function(require) {
    var Function, ModelJsonParser, Module, Squire, assert, chai;
    chai = require('chai');
    Squire = require('Squire');
    Module = require('scripts/model/Module');
    Function = require('scripts/model/Function');
    ModelJsonParser = require('scripts/ModelJsonParser');
    assert = chai.assert;
    return describe('ModelJsonParser', function() {
      return describe('parse', function() {
        it('should create a Module object if type is Module', function() {
          var moduleJsonParser, obj;
          moduleJsonParser = new ModelJsonParser('id_');
          obj = moduleJsonParser.parse('{\n  "id_":"../aa.py",\n  "name":"aa",\n  "parent":null,\n  "dependencies":[],\n  "branch_depth":0,\n  "type":"Module",\n  "children":[]\n}');
          assert.instanceOf(obj, Module);
          return assert.equal(obj.name, 'aa');
        });
        return it('should create a Function object if type is Function', function() {
          var moduleJsonParser, obj;
          moduleJsonParser = new ModelJsonParser('id_');
          obj = moduleJsonParser.parse('{\n  "id_": "aa.py:1",\n  "name": "fake_function_name",\n  "type": "Function"\n}');
          assert.instanceOf(obj, Function);
          return assert.equal(obj.name, 'fake_function_name');
        });
      });
    });
  });

}).call(this);
