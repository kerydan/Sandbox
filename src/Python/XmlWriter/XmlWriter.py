import io

def printwriterhello():
    print('Hello from printwriterhello !!')


class XmlWriter:
    tag = []        # analog of c++ vector
    indent = "    "
    def SetFile(self, f):
        self.file = f

    def Log2(self, text):
        print(text, end = "")
        self.file.write(text)


    def OpenElement(self, arg):
        self.tag.append(arg)
        s = self.indent + "<" + arg
        self.Log2(s)
        return self

    def CloseElement(self):
        s = " </" + self.tag.pop() + ">"
        self.Log2(s)
        return self

    def Attr(self, key, val):
        s = ' ' + key + '="' + val + '"'
        self.Log2(s)
        return self;
