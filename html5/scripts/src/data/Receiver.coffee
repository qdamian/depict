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

window.define ["scripts/src/ModelJsonParser", \
               "scripts/src/control/Search"], \
                (ModelJsonParser, \
                 Search) ->
  Receiver = () ->
    @socket = new WebSocket "ws://localhost:9876/"

    @socket.onopen = () ->
      console.log "websocket opened"

    @socket.onmessage = (msg) ->
      moduleJsonParser = new ModelJsonParser("id_")
      entity = moduleJsonParser.parse(msg.data)
      try
        Search.add(entity.name)
      catch e
        console.log e

    # @socket.onclose = (e) ->
    #      console.log "websocket closed"

    # @socket.onerror = (e) ->
    #   console.log "websocket onerror"
    #  console.log e

    return

  Receiver
