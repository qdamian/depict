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

  chai = require 'chai'
  DefaultVisualiz = require 'scripts/src/visualiz/Default'

  describe 'visualiz.Default', ->

    should = chai.should()

    beforeEach ->
      @html = $('html').clone(true, true)
      return undefined # jshint

    afterEach ->
      $('html').replaceWith(@html)

    describe 'add', ->

      it 'should add an element to the canvas when an option is selected', ->
        $('#canvas #entity_val1').length.should.equal 0
        # Given
        visualiz = new DefaultVisualiz()

        # When
        visualiz.on_search_option_chosen 'val1'

        # Then
        $('#canvas #entity_val1').length.should.equal 1

      it 'should support slash characters in the entities ids', ->
        # Given
        visualiz = new DefaultVisualiz()

        # When
        visualiz.on_search_option_chosen 'path/to/val1'

        # Then
        $('#canvas #entity_path_to_val1').length.should.equal 1
