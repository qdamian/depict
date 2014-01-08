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

define ['chai', 'sinon', 'Squire'], (chai, sinon, Squire) ->

  should = chai.should()

  describe 'Receiver', ->

    describe 'onMessage', ->

      it 'should invoke the callback', ->

        parser_stub = {parse: -> {name: 'fake_name'}}
        parser_stub_constructor = Squire.Helpers.constructs(parser_stub)

        new Squire()
          .mock('scripts/src/ModelJsonParser', parser_stub_constructor)
          .require ['scripts/src/data/Receiver', 'mocks'], (Receiver, mocks) ->

            # Given
            callback = sinon.spy()
            receiver = new Receiver({on_msg: callback})

            # When
            receiver.onMessage 'dummy_msg'

            # Then
            callback.args[0][0].should.equal 'fake_name'

