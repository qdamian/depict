class StaticDataCollector(object):
    def __init__(self):
        self.collectors = []
    
    def include(self, collector):
        self.collectors.append(collector)
    
    def process(self, file_name):
        for collector in self.collectors:
            with open(file_name, 'r') as input_file:
                instance = collector()
                instance.process(file_name, input_file)

# pylint: disable=C0103
GlobalStaticDataCollector = StaticDataCollector()
