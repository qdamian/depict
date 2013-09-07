/*
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
*/


(function() {
  var __hasProp = {}.hasOwnProperty;

  window.define(["d3"], function(d3) {
    "use strict";
    var ModelJsonParser, _indexObjects, _reviveReferences;
    ModelJsonParser = function(jsonFile, id, callback) {
      this.id = id;
      this._createObjectsFromJsonFile(jsonFile, id, callback);
    };
    _indexObjects = function(id, objects) {
      var index, obj, _i, _len;
      index = {};
      for (_i = 0, _len = objects.length; _i < _len; _i++) {
        obj = objects[_i];
        index[obj[id]] = obj;
      }
      return index;
    };
    _reviveReferences = function(id, index, object) {
      var key, value;
      for (key in object) {
        if (!__hasProp.call(object, key)) continue;
        value = object[key];
        if (value instanceof Array || value instanceof Object) {
          object[key] = _reviveReferences(id, index, object[key]);
        }
        if (index[value]) {
          if (!(object === index[value])) {
            object = index[value];
          }
        }
      }
      return object;
    };
    ModelJsonParser.prototype._createObjectsFromJsonFile = function(jsonFile, id, callback) {
      var _processData;
      _processData = function(error, data) {
        var index, item, objects, typeModule, _i, _len;
        objects = [];
        if (data) {
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            item = data[_i];
            typeModule = require("model/" + item.type);
            objects.push(new typeModule(item));
          }
        }
        index = _indexObjects(id, objects);
        objects = _reviveReferences(id, index, objects);
        return callback(objects);
      };
      return d3.json(jsonFile, _processData);
    };
    return ModelJsonParser;
  });

}).call(this);
