class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'

class ResponsiblePerson:
  def __init__(self, person):
    self.person = person


  @property
  def age(self):
      return self.person.age

  @age.setter
  def age(self, value):
      self.person.age = value

  def _is_too_young_to_drink(self):
        return self.age < 18

  def _is_too_young_to_drive(self):
        return self.age < 16

  def drink(self):
        if self._is_too_young_to_drink():
            return "Too young to drink"
        self.drunk = True
        return self.person.drink()
  

  def drive(self):
        if self._is_too_young_to_drive():
            return "Too young to drive"
        self.driving = True
        return self.person.drive()

  def drink_and_drive(self):
        if self._is_too_young_to_drink():
            return "Too young to drive drunk"
        return "Dead"
     
p = Person(10)
rp = ResponsiblePerson(p)
rp.age = 19

print(rp.drive())
print(rp.drink())
print(rp.drink_and_drive())
