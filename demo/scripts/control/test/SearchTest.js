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
    var Search, chai;
    chai = require('chai');
    Search = require('scripts/control/Search');
    return describe('control.Search', function() {
      var should;
      should = chai.should();
      beforeEach(function() {
        this.html = $('html').clone(true, true);
        return void 0;
      });
      afterEach(function() {
        return $('html').replaceWith(this.html);
      });
      describe('add', function() {
        it('should create a new available option', function() {
          var search;
          search = new Search();
          search.get('val1').text().should.equal('');
          search.add('dummyGroup', 'val1');
          return search.get('val1').text().should.equal('val1');
        });
        it('should preserve existing options', function() {
          var search;
          search = new Search();
          search.add('dummyGroup', 'val1');
          search.add('dummyGroup', 'val2');
          search.get('val1').text().should.equal('val1');
          return search.get('val2').text().should.equal('val2');
        });
        return it('should raise an exception if no group is provided', function() {
          var aBadCall, search;
          search = new Search();
          aBadCall = function() {
            return search.add(void 0, 'val1');
          };
          return aBadCall.should["throw"](SyntaxError);
        });
      });
      return it('should notify the event when an option is chosen', function() {
        var callback, search;
        callback = sinon.spy();
        search = new Search({
          on_search_option_chosen: callback
        });
        search.onOptionSelected('val1');
        return callback.args[0][0].should.equal('val1');
      });
    });
  });

}).call(this);
