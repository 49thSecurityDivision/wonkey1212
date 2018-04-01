import sys
from inspect import stack


if sys.version_info.major != 3:
    print("Psst. You are using Python %s" % (sys.version_info.major), file=sys.stderr)
    print("This course is intended to be ran with Python3!\n", file=sys.stderr)

if __name__ == "__main__":
    print("Hey! This is a library. Its not intended to run directly. Use 1212-part1.py instead!", file=sys.stderr)
    raise SystemExit

if 'idlelib.run' not in sys.modules:
    print("It doesn't look like you're using IDLE, I recommending switching to it for this \"course\", as it makes quite a few things easier to do for beginners")
    print("Open this file with IDLE, then press F5 to get started")
    print("(or you could use the 'python -i $filename' if you really want to)")



class sectionBase:
    def __init__(self, g):
        self._g = g
        buffer = set()
        self._cont = buffer.symmetric_difference
        self._done = self._doneFactory(buffer.add)
        
    @property
    def completed(self):
        output = [ str(x) for x in self._cont(set())]
        output.sort()
        print( ", ".join(output) )
                
    def _doneFactory(self, function):
        """
        This is a hack for sure, and not even a very good one.
        Helps stop people from adding challanges to the compeleted list.
        Obviously this is very easy to bypass.
        """
        def __done(value):
            tester = stack()[1]
            if hasattr(self, tester.function):
                if str(value) not in str(tester.function):
                    print("??")
                function(value)
                return tester
            else:
                print("hmmmmm something's not right here")
        return __done



class llist(list):
    pass


class section1(sectionBase):
    def __init__(self, g):
        super().__init__(g)


    def __repr__(self):
        return "<wonkey1212.section1>"
    
    def problem1(self):
        value = self._g.get('var1')
        if value != None:
            if value != 2:
                print("var1 equals '%s', set it to (integer) 2" % (value))
            else:
                self._done(1)
                print("Awesome!")
        else:
            print("var1 isn't set to anything, set it to (integer) 2")

    def problem2(self):
        value = self._g.get('var2')
        if isinstance(value, str):
            self._done(2)
            print("Awesome!")
        else:
            print("set var2 to a string")

    def problem4(self):
        value = self._g.get('var4')
        if isinstance(value, list):
            if value == [ x for x in range(0, 10000) ]:
                self._done(3)
                print("Awesome!")
            else:
                print("fix the for loop")
        else:
            print("set var4 to a list (array)")


    def problem3(self):
        value = self._g.get('var3')
        try:
            if value['hello'] == 'world':
                self._done(4)
                print("Awesome!")
            else:
                print("Doesn't equal hello world")
        except KeyError:
            print("Set key 'hello' to 'world'")
        except TypeError:
            print("Set var3 to a dictionary")


    def problem5(self):
        value = self._g.get('var5')

        try:
            if value() == "hello world":
                self._done(5)
                print("Awesome!")
            else:
                print("Thats a function, make it return \"hello world\"")
        except TypeError:
            print("Set var5 to a function that\n\t1) Takes no arguments\n\t2) returns \"hello world\"")

        
    def problem6(self):
        value = self._g.get('var6')

        try:
            if value() == "goodbye world":
                if value("wow") == "wow":
                    self._done(6)
                    print("Awesome!")
                else:
                    print("arguments don't seem to work")
            else:
                print("Wrong value returned when no arguments are supplied")
        except TypeError:
            print("Set var6 to a function with an optional argument")
            print("\t1) When no argument is supplied, return \"goodbye world\"")
            print("\t2) When an argument is supplied, return the argument")


    def problem7(self):
        vn = 'var7'
        value = self._g.get(vn)

        

        try:
            if list(map(value, [1,2,3,4,5,6,7,8,9])) == [1, 0, 1, 0, 1, 0, 1, 'eight!', 1, 0]:
                self._done(7)
                print("Awesome!")
            else:
                print("Doesn't seem to work right")
        except TypeError:
            print("Set %s to a function that accepts a single interger, and: " % (vn))
            print("\t1) returns 1 if the argument is odd")
            print("\t2) returns 0 if the argument is even")
            print("\t3) returns 'eight!' if the argument == 8")
                    

