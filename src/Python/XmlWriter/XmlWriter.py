def printwriterhello():
    print('Hello from printwriterhello !!')


class XmlWriter:
    tag = []        # analog of c++ vector

    def Indent(self):
        print("   ", end = "")

    def OpenElement(self, arg):
            self.tag.append(arg)
            self.Indent()
            print("<", end = "")
            print(arg, end = "")
            return self

    def CloseElement(self):
        print(" </", end = "")
        print(self.tag.pop(), end = "")
        print(">", end = "")
        return self

    def Attr(this, key, val):
        print( " " + key + '="' + val + '"', end = "")
        return this;
