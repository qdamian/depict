/*
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
*/


(function() {
  define(function(require) {
    var Squire, chai, should, sinon;
    chai = require('chai');
    sinon = require('sinon');
    Squire = require('Squire');
    should = chai.should();
    return describe('data.source.File', function() {
      return describe('onMessage', function() {
        return it('should invoke the callback for entity', function(done) {
          var content, jquery_get, parser_stub, parser_stub_constructor;
          content = '{"name":"a"} --- {"name":"b"}';
          jquery_get = sinon.stub().callsArgWith(1, content);
          parser_stub = {
            parse: function(x) {
              return JSON.parse(x);
            }
          };
          parser_stub_constructor = Squire.Helpers.constructs(parser_stub);
          return new Squire().mock('jquery', {
            get: jquery_get
          }).mock('scripts/ModelJsonParser', parser_stub_constructor).require(['scripts/data/source/File'], function(File, mocks) {
            var callback;
            callback = sinon.spy();
            new File({
              on_msg: callback
            });
            callback.args[0][0].name.should.equal('a');
            callback.args[1][0].name.should.equal('b');
            return done();
          });
        });
      });
    });
  });

}).call(this);
