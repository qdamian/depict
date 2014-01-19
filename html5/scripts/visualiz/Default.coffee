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

  $ = require 'jquery'

  do style_entities = ->
    $('<link>',
      rel: 'stylesheet'
      href: 'css/main.css'
    ).prependTo 'head:first-child'

  class Default

    constructor: () ->

    on_search_option_chosen: (value) ->
      $('<div>',
        class: 'entity'
        id: 'entity_' + value.replace /\//g, "_"
      ).appendTo '#canvas'
