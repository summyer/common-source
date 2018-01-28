class Query(object):

    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('begin')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('query info about %s ...' % self.name)

    
with Query('Bos') as q:
    q.query()


from contextlib import contextmanager
class Query2(object):


    def __init__(self,name):
        self.name = name

    def query(self):
        print('query2 info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')
with create_query('Ali') as a:
    q.query()


from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
