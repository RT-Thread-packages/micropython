# import os
class HelloRtt:

    def __repr__(self):
        self.__call__()
        return ""
    
    def __call__(self):
        print("hello world!!")
        print("hello RTT")

hello = HelloRtt()
