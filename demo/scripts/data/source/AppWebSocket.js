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
    var AppWebSocket, ModelJsonParser;
    ModelJsonParser = require('scripts/ModelJsonParser');
    return AppWebSocket = (function() {
      function AppWebSocket(callback) {
        var http_port, ws_port,
          _this = this;
        this.callback = callback;
        this.onMessage = function(msg) {
          var e, entity, modelJsonParser;
          modelJsonParser = new ModelJsonParser("id_");
          entity = modelJsonParser.parse(msg.data);
          try {
            return this.callback.on_msg(entity);
          } catch (_error) {
            e = _error;
            return console.log(e);
          }
        };
        http_port = +location.port || 80;
        ws_port = http_port + 1;
        this.socket = new WebSocket("ws://localhost:" + ws_port + "/");
        this.socket.onmessage = function(msg) {
          return _this.onMessage(msg);
        };
      }

      return AppWebSocket;

    })();
  });

}).call(this);
