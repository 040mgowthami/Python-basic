class employee:
  def __init__(self,name,e_id,salary):
    self.name=name
    self.e_id=e_id
    self.salary=salary
  def display(self):
    print("name:",self.name)
    print("e_id:",self.e_id)
    print("salary:".self.salary)
e=employee("gowthu",101,75000)
e.display()
