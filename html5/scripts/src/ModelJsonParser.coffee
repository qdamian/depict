###
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
###

window.define ["d3"], (d3) ->
  "use strict"

  ModelJsonParser = (jsonFile, id, callback) ->
    @id = id
    @_createObjectsFromJsonFile(jsonFile, id, callback)
    return

  _indexObjects = (id, objects) ->
    index = {}
    for obj in objects
      index[obj[id]] = obj
    return index

  _reviveReferences = (id, index, object) ->
    for own key, value of object
      if value instanceof Array or value instanceof Object
        object[key] = _reviveReferences(id, index, object[key])
      if index[value]
        if not (object == index[value])
          object = index[value]
    return object

  ModelJsonParser::_createObjectsFromJsonFile = (jsonFile, id, callback) ->
    _processData = (error, data) ->
      objects = []
      if data then for item in data
        typeModule = require("model/#{item.type}")
        objects.push(new typeModule(item))
      index = _indexObjects(id, objects)
      objects = _reviveReferences(id, index, objects)
      callback(objects)
    d3.json(jsonFile, _processData)

  ModelJsonParser
