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

  $ = require 'jquery'

  class File

    constructor: (@callback) ->
      modelJsonParser = new ModelJsonParser "id_"
      $.get "data.txt", (content) =>
        for msg in content.split '---'
          try
            entity = modelJsonParser.parse msg
            @callback.on_msg entity
          catch e
            console.log e
