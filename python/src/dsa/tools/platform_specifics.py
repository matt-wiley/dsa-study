import platform
import json


class PythonDetails:

    def __init__(self):
        # self.machine = platform.machine()
        self.implementation = platform.python_implementation()
        # self.processor = platform.processor()
        self.uname = platform.uname()

    def __repr__(self):
        self_dict = {}
        for k in self.__dict__.keys():
            if not k.startswith("_"):
                self_dict[k] = self.__dict__.get(k)
        return f"{json.dumps(self_dict, indent=2)}"


if __name__ == '__main__':
    print(PythonDetails())