/*
Copyright 2013, Damian Quiroga

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
  define(["chai", "Squire", "model/Module"], function(chai, Squire, Module) {
    var should;
    should = chai.should();
    return describe("ModelJsonParser", function() {
      return describe("parse", function() {
        return it("should be able to create one object", function() {
          return new Squire().require(["ModelJsonParser"], function(ModelJsonParser) {
            var moduleJsonParser, obj;
            moduleJsonParser = new ModelJsonParser("id_");
            obj = moduleJsonParser.parse("{\n    \"id_\":\"../aa.py\",\n    \"name\":\"aa\",\n    \"parent\":null,\n    \"dependencies\":[],\n    \"branch_depth\":0,\n    \"type\":\"Module\",\n    \"children\":[]\n}");
            (obj instanceof Module).should.equal(true);
            return obj.name.should.equal("aa");
          });
        });
      });
    });
  });

}).call(this);
