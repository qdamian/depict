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
from depict.modeling.function_call_collector import FunctionCallCollector
from depict.output.model_publisher import ModelPublisher
from depict.output.observable_model import ObservableModel

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
from depict.collection.dynamic.frame_digest import FrameDigest
from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.collection.static.source_code_parser import SourceCodeParser
from depict.model.entity.class_ import Class_
from depict.model.entity.function import Function
from depict.model.entity.function_call import FunctionCall
from depict.model.entity.method import Method
from depict.model.entity.module import Module
from depict.model.entity.thread import Thread
from depict.model.model import Model
from depict.model.util.entity_id_generator import EntityIdGenerator
from depict.model.util.entity_repo import EntityRepo
from depict.modeling.class_def_collector import ClassDefCollector
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.modeling.function_call_notifier import FunctionCallNotifier
from depict.modeling.function_def_collector import FunctionDefCollector
from depict.txt.trace.trace_repr import TraceRepr
from formic.formic import FileSet
from mock import create_autospec, MagicMock
import inspect
import uuid

__base_path = '.'
__SourceCodeParser = SourceCodeParser(__base_path)
__EntityIdGenerator = EntityIdGenerator(__base_path)
__Model = Model()
__Module = Module('module_id', 'module_name')
__NodeNG = NodeNG()
__DefCollectionOrchestrator = DefCollectionOrchestator(__base_path, __Model)
__Thread = Thread('thread_id')
__EntityRepo = EntityRepo()
__ThreadScopedTracer = ThreadScopedTracer(MagicMock())
__FrameDigest = FrameDigest(inspect.currentframe())
__Class_ = Class_('class_id', 'class_name', __Module)
__FileSet = FileSet(directory=__base_path, include='*.py')
__Function = Function('function_id', 'function_name', __Module)
__Method = Method('method_id', 'method_name', __Class_)
__ClassDefCollector = ClassDefCollector(__SourceCodeParser, __EntityIdGenerator, __Model)
__FunctionDefCollector = FunctionDefCollector(__SourceCodeParser, __EntityIdGenerator, __Model)
__TraceRepr = TraceRepr(__base_path)
__FunctionCallNotifier = FunctionCallNotifier(MagicMock(), __EntityIdGenerator, __DefCollectionOrchestrator)
__FunctionCall = FunctionCall('function_call_id', __Function, __Thread)
__FunctionCallCollector = FunctionCallCollector(__EntityIdGenerator, __Model)
__ModelPublisher = ModelPublisher()
__ObservableModel = ObservableModel(__ModelPublisher)

def fake(class_name, spec_set=True):
    return create_autospec(spec=globals()['__' + class_name], spec_set=spec_set)

def real(class_name):
    return deepcopy(globals()['__' + class_name])

def unique(entity):
    entity.id_ = str(uuid.uuid4())
    return entity
