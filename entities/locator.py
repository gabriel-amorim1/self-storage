from entities.person import Person

class Locator(Person):
  def __init__(self, name, document, phone):
    super().__init__(name, document, phone)