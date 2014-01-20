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
    var DefaultVisualiz, chai;
    chai = require('chai');
    DefaultVisualiz = require('scripts/visualiz/Default');
    return describe('visualiz.Default', function() {
      var should;
      should = chai.should();
      beforeEach(function() {
        this.html = $('html').clone(true, true);
        return void 0;
      });
      afterEach(function() {
        return $('html').replaceWith(this.html);
      });
      return describe('add', function() {
        it('should add an element to the canvas when an option is selected', function() {
          var visualiz;
          $('#canvas #entity_val1').length.should.equal(0);
          visualiz = new DefaultVisualiz();
          visualiz.on_search_option_chosen('val1');
          return $('#canvas #entity_val1').length.should.equal(1);
        });
        return it('should support slash characters in the entities ids', function() {
          var visualiz;
          visualiz = new DefaultVisualiz();
          visualiz.on_search_option_chosen('path/to/val1');
          return $('#canvas #entity_path_to_val1').length.should.equal(1);
        });
      });
    });
  });

}).call(this);
