def printwriterhello():
    print('Hello from printwriterhello !!')


class XmlWriter:
    tag = []
    def print(self):
        print("It goes from XmlWriter !!!!22!!")
    def Indent(self):
        print("   ", end = "")

    def OpenElement(self, arg):
            self.tag.append(arg)
            self.Indent()
            print("<", end = "")
            print(arg, end = "")
            return self

    def CloseElement(self):
        self.Indent()
        print("</", end = "")
        print(self.tag.pop(), end = "")
        print(">", end = "")
        return self

