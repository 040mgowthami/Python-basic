class parent:
  def display(self):
    print("parent class")
class child(parent):
  def display(self):
    print("child class")
c=child()
c.display()
