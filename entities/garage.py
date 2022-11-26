class Garage:
  renter_id = None

  def __init__(self, _id, locator_id, rent_price, address, size):
    self._id = _id
    self.locator_id = locator_id
    self.rent_price = rent_price
    self.address = address
    self.size = size

  def rent(self, renter_id):
    self.renter_id = renter_id

  def cancel_rent(self):
    self.renter_id = None