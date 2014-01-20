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
    var $, Search, init_selectize_js;
    $ = require('jquery');
    require('selectize');
    (init_selectize_js = function() {
      return $('<link>', {
        rel: 'stylesheet',
        href: '3rdparty/selectize/selectize.css'
      }).prependTo('head:first-child');
    })();
    return Search = (function() {
      function Search(controller) {
        var search,
          _this = this;
        this.controller = controller;
        search = $('<select>', {
          id: 'search'
        }).prependTo('body');
        search.selectize({
          create: false,
          onItemAdd: function(value) {
            return _this.onOptionSelected(value);
          }
        });
        this.control = $('#search')[0].selectize;
      }

      Search.prototype.add = function(group, name) {
        if (!group || !name) {
          throw SyntaxError("Missing values");
        }
        this.control.addOptionGroup(group, {
          label: group
        });
        this.control.addOption({
          text: name,
          value: name,
          optgroup: group
        });
        return this.control.refreshOptions();
      };

      Search.prototype.get = function(name) {
        return this.control.getOption(name);
      };

      Search.prototype.onOptionSelected = function(value) {
        return this.controller.on_search_option_chosen(value);
      };

      return Search;

    })();
  });

}).call(this);
