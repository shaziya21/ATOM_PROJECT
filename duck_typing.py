# dynamic typing : the type we can mention later.
class atom:

    def execute(self):
        print('compiling')
        print('running')

class myeditor:
    def execute(self):
        print('spell check')
        print('convention check')
        print('compiling')
        print('running')


class laptop:

    def code(self,ide):   #in dynamic typic we can replace this ide type
        ide.execute()


ide = atom()

lap1 = laptop()
lap1.code(ide)
