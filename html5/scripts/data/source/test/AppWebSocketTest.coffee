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
  sinon = require 'sinon'
  Squire = require 'Squire'

  should = chai.should()

  describe 'data.source.AppWebSocket', ->

    describe 'onMessage', ->

      it 'should invoke the callback passing the received entity', (done) ->

        parser_stub = {parse: -> 'fake_entity'}
        parser_stub_constructor = Squire.Helpers.constructs(parser_stub)

        new Squire()
          .mock('scripts/ModelJsonParser', parser_stub_constructor)
          .require ['scripts/data/source/AppWebSocket'], \
            (AppWebSocket, mocks) ->
              # Given
              callback = sinon.spy()
              appWebSocket = new AppWebSocket({on_msg: callback})

              # When
              appWebSocket.onMessage 'dummy_msg'

              # Then
              callback.args[0][0].should.equal 'fake_entity'
              done()
