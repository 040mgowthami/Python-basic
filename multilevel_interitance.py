class A:
  def show(self):
    print("class A")

class B(A):
  pass
class c(B):
  pass
obj=c()
obj.show()

    
