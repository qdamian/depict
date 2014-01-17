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

  Module = require 'scripts/src/model/Module'
  Function = require 'scripts/src/model/Function'
  Thread = require 'scripts/src/model/Thread'

  class ModelJsonParser

    constructor: (@id) ->

    parse: (json) ->
      data = JSON.parse(json)
      if data
        typeModule = require("scripts/src/model/#{data.type}")
        return new typeModule(data)
