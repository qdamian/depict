import threading
from aa_mod import aa_func
from ba_mod import ba_func
from ab_mod import ab_func
from bb_mod import bb_func

for function in [aa_func, ba_func, ab_func, bb_func]:
    thread = threading.Thread(target=function)
    thread.start()
    thread.join()
