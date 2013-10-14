# Copyright 2013 Damian Quiroga
#
# This file is part of Depict.
#
# Depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Depict.  If not, see <http://www.gnu.org/licenses/>.
from depict.core.consolidation.data_source import DataSource

from depict.core.model.entity.function_call import FunctionCall
from depict.core.collection.static.source_code_parser import SourceCodeParser
# from depict.core.consolidation.data_source import DataSource
from depict.core.consolidation.observable_model import ObservableModel

'''
This module creates instances of some classes (from depict and other libraries)
that serve as 'templates' to create other instance objects. These objects
created from the templates are meant to be used as sample data or mocks in unit
tests. They can be either real instances (deep copies of the template objects)
or mock objects (generated using Mock's autospeccing).

http://www.voidspace.org.uk/python/mock/helpers.html#autospeccing
'''

from astroid.bases import NodeNG
from copy import deepcopy
from depict.core.collection.dynamic.frame_digest import FrameDigest
from depict.core.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.core.model.entity.class_ import Class_
from depict.core.model.entity.function import Function
from depict.core.model.entity.method import Method
from depict.core.model.entity.module import Module
from depict.core.model.entity.thread import Thread
from depict.core.model.model import Model
from depict.core.model.util.entity_id_generator import EntityIdGenerator
from depict.core.model.util.entity_repo import EntityRepo
from depict.core.modeling.orchestrator import Orchestrator
from depict.core.modeling.static.driver import Driver as StaticModelingDriver
from depict.core.modeling.dynamic.driver import Driver as DynamicModelingDriver
from depict.core.modeling.static.class_ import Class_ as ClassModeler
from depict.core.modeling.static.function import Function as FunctionModeler
from depict.core.modeling.dynamic.function_call import FunctionCall as FunctionCallModeler
from depict.txt.trace.trace import Trace
from formic.formic import FileSet
from mock import create_autospec, MagicMock
import inspect
import uuid

def fake(class_name, spec_set=True):
    return create_autospec(spec=globals()['__' + class_name], spec_set=spec_set)

def real(class_name):
    return deepcopy(globals()['__' + class_name])

def unique(entity):
    entity.id_ = str(uuid.uuid4())
    return entity

__base_path = '.'
__SourceCodeParser = SourceCodeParser(__base_path)
__EntityIdGenerator = EntityIdGenerator(__base_path)
__Model = Model()
__Module = Module('module_id', 'module_name')
__NodeNG = NodeNG()
__Orchestrator = Orchestrator(__base_path, __Model)
__Thread = Thread('thread_id')
__EntityRepo = EntityRepo()
__ThreadScopedTracer = ThreadScopedTracer(MagicMock())
__FrameDigest = FrameDigest(inspect.currentframe())
__Class_ = Class_('class_id', 'class_name', __Module)
__FileSet = FileSet(directory=__base_path, include='*.py')
__Function = Function('function_id', 'function_name', __Module)
__Method = Method('method_id', 'method_name', __Class_)
__ClassModeler = ClassModeler(__SourceCodeParser, __EntityIdGenerator, __Model)
__FunctionModeler = FunctionModeler(__SourceCodeParser, __EntityIdGenerator, __Model)
__Trace = Trace(__base_path)
__StaticModelingDriver = StaticModelingDriver(__FileSet, __Model)
__DynamicModelingDriver = DynamicModelingDriver(MagicMock(), __EntityIdGenerator, __Orchestrator)
__FunctionCall = FunctionCall('function_call_id', __Function, __Thread)
__FunctionCallModeler = FunctionCallModeler(__EntityIdGenerator, __Model)
__DataSource = DataSource()
__ObservableModel = ObservableModel(__DataSource)
