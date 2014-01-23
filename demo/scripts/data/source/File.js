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
    var $, File, ModelJsonParser;
    ModelJsonParser = require('scripts/ModelJsonParser');
    $ = require('jquery');
    return File = (function() {
      function File(callback) {
        var modelJsonParser,
          _this = this;
        this.callback = callback;
        modelJsonParser = new ModelJsonParser("id_");
        $.get("data.txt", function(content) {
          var e, entity, msg, _i, _len, _ref, _results;
          _ref = content.split('---');
          _results = [];
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            msg = _ref[_i];
            try {
              entity = modelJsonParser.parse(msg);
              _results.push(_this.callback.on_msg(entity));
            } catch (_error) {
              e = _error;
              _results.push(console.log(e));
            }
          }
          return _results;
        });
      }

      return File;

    })();
  });

}).call(this);
