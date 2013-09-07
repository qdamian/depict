[![Build Status](https://travis-ci.org/qdamian/depict.png?branch=master)](https://travis-ci.org/qdamian/depict)

Depict
======

Status of the project
---------------------

Not yet useful in any way.

Description
-----------

> /dɪˈpɪkt/: to represent or show something in a picture or story

Depict has two components:

* A python module to model the structure and behavior of a program based on the program's source code and data gathered during the program execution.

* An HTML application to display a graphical representation of that model.

See some [alternatives](https://github.com/qdamian/depict#alternatives) below.

Like disptrace, Depict uses HTML5 as the prefered type of output format, and provides collapse/expand capabilities to choose which part of the repesentation is displayed.

Like pyreverse, Depict allows to limit the scope of the representation to a part of the program, e.g. a group of classes.

Alternatives
------------

[pyreverse][pyreverse] is a Python Reverse engineering tool. It's able to generate UML like diagram from Python source code.

[disptrace][disptrace] is a great project that traces a program and creates an HTML5 document displaying called functions.

[andypatterns][andypatterns] A reverse engineering tool for Python source code. Requires wxPython

For JS, [violin] looks interesting.

[pyreverse]: http://www.logilab.org/2560 "pyreverse"
[disptrace]: https://github.com/atsuoishimoto/disptrace "disptrace"
[andypatterns]: http://www.andypatterns.com/index.php/products/pynsource/ "andypatterns"
[violin]: http://latentflip.com/hacks/violin/ "violin"

Contact
-------

Feel free to email me at qdamian@gmail.com

---

Copyright 2013 Damian Quiroga

This file is part of Depict.

Depict is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Depict is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Depict.  If not, see <http://www.gnu.org/licenses/>.
