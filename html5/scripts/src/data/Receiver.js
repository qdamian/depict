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
  window.define(["scripts/src/ModelJsonParser"], function(ModelJsonParser) {
    "use strict";
    var Receiver;
    Receiver = function() {
      this.socket = new WebSocket("ws://localhost:9876/");
      this.socket.onopen = function() {
        return console.log("websocket opened");
      };
      this.socket.onmessage = function(msg) {
        var e, entity, moduleJsonParser, name, selectize_tags;
        console.log("msg received" + msg.data);
        moduleJsonParser = new ModelJsonParser("id_");
        entity = moduleJsonParser.parse(msg.data);
        try {
          name = entity.name;
          console.log("name is " + name);
          selectize_tags = $("#search")[0].selectize;
          selectize_tags.addOption({
            text: name,
            value: name
          });
          return selectize_tags.refreshItems();
        } catch (_error) {
          e = _error;
          return console.log(e);
        }
      };
    };
    return Receiver;
  });

}).call(this);
