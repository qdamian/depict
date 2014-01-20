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
    var Function, ModelJsonParser, Module, Thread;
    Module = require('scripts/model/Module');
    Function = require('scripts/model/Function');
    Thread = require('scripts/model/Thread');
    return ModelJsonParser = (function() {
      function ModelJsonParser(id) {
        this.id = id;
      }

      ModelJsonParser.prototype.parse = function(json) {
        var data, typeModule;
        data = JSON.parse(json);
        if (data) {
          typeModule = require("scripts/model/" + data.type);
          return new typeModule(data);
        }
      };

      return ModelJsonParser;

    })();
  });

}).call(this);
