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
  Search = require 'scripts/src/control/Search'

  describe "Search", ->

    should = chai.should()

    beforeEach ->
      @html = $('html').clone(true, true)
      return undefined # jshint

    afterEach ->
      $('html').replaceWith(@html)

    describe "add", ->

      it "should create a new available option", ->
        # Given
        search = new Search()
        search.get("val1").text().should.equal ""

        # When
        search.add("val1")

        # Then
        search.get("val1").text().should.equal "val1"

      it "should preserve existing options", ->
        # Given
        search = new Search()
        search.add("val1")

        # When
        search.add("val2")

        # Then
        search.get("val1").text().should.equal "val1"
        search.get("val2").text().should.equal "val2"
