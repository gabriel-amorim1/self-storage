import uuid

class Person:
  def __init__(self, name, document, phone):
    self._id = uuid.uuid4()
    self.name = name
    self.document = document
    self.phone = phone

