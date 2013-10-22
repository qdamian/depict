depict
======

[![Build Status](https://travis-ci.org/qdamian/depict.png?branch=master)](https://travis-ci.org/qdamian/depict)
[![Coverage Status](https://coveralls.io/repos/qdamian/depict/badge.png?branch=master)](https://coveralls.io/r/qdamian/depict?branch=master)

Status of the project
---------------------

Not yet useful in any way.

Description
-----------

> /dɪˈpɪkt/: to represent or show something in a picture or story

depict has two components:

* A python module to model the structure and behavior of a program based on the program's source code and data gathered during the program execution.

* An HTML application to display a graphical representation of that model.

See some [alternatives](https://github.com/qdamian/depict#alternatives) below.

Like disptrace, depict uses HTML5 as the prefered type of output format, and provides collapse/expand capabilities to choose which part of the repesentation is displayed.

Like pyreverse, depict allows to limit the scope of the representation to a part of the program, e.g. a group of classes.

Alternatives
------------

[pycallgraph][pycallgraph] is a module that creates call graph visualizations for Python applications. 

[pyreverse][pyreverse] is a Python Reverse engineering tool. It's able to generate UML like diagram from Python source code.

[disptrace][disptrace] is a great project that traces a program and creates an HTML5 document displaying called functions.

[andypatterns][andypatterns] is a reverse engineering tool for Python source code. Requires wxPython

[pytrace][pytrace] allows to record and view function calls, arguments and return values

[pycallgraph]: http://pycallgraph.slowchop.com/en/master/ "pycallgraph"
[pyreverse]: http://www.logilab.org/2560 "pyreverse"
[disptrace]: https://github.com/atsuoishimoto/disptrace "disptrace"
[andypatterns]: http://www.andypatterns.com/index.php/products/pynsource/ "andypatterns"
[pytrace]: https://github.com/alonho/pytrace "pytrace"

Contact
-------

Feel free to email me at qdamian@gmail.com

---

Copyright 2013, Damian Quiroga
