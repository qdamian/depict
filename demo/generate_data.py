import dissect
from dissect.consolidation.util.entity_to_json import EntityToJson

def handle(entity):
    print('%s\n\n---\n\n' % EntityToJson().convert(entity, 'id_'))

dissect.run('./test/system/data/one/main.py', handle)
