from entities.locator import Locator

class LocatorService:
  locators = []

  def register_locator(self, name, document, phone):
    locator = Locator(name, document, phone)
    self.locators.append(locator)
    return locator
    

  def get_locator_by_document(self, document):
    for locator in self.locators:
      if (locator.document == document):
          return locator