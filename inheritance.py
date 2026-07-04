class animal:
  def __init__(self):
    print("animal makes sound")

class dog(animal):
  def __init__(self):
    print("dog barks")
d=dog()
d.sound()
d.bark()
