from entities.renter import Renter

class RenterService:
  renters = []

  def register_renter(self,name, document, phone):
    renter = Renter(name, document, phone)
    self.renters.append(renter)
    return renter


  def get_renter_by_document(self, document):
    for renter in self.renters:
        if (renter.document == document):
            return renter