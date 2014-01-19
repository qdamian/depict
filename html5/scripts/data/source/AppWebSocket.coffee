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

  ModelJsonParser = require 'scripts/ModelJsonParser'

  class AppWebSocket

    constructor: (@callback) ->

      @onMessage= (msg) ->
        modelJsonParser = new ModelJsonParser "id_"
        entity = modelJsonParser.parse msg.data
        try
          @callback.on_msg entity
        catch e
          console.log e

      http_port = +location.port or 80
      ws_port = http_port + 1
      @socket = new WebSocket "ws://localhost:#{ws_port}/"
      @socket.onmessage = (msg) =>
        @onMessage msg
