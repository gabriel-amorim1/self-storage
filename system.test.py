import unittest

from services.garage_service import GarageService
from services.locator_service import LocatorService
from services.renter_service import RenterService
from services.system_balance_service import SystemBalanceService

class SystemServiceTest(unittest.TestCase):
  locator_service = LocatorService()
  renter_service = RenterService()
  system_balance_service = SystemBalanceService()
  garage_service = GarageService(locator_service, renter_service, system_balance_service)
  
  locator = locator_service.register_locator("Locator", "1234567890", "988887777")
  renter = renter_service.register_renter("Renter", "0123456789", "998887775")
  garage = garage_service.register_garage(locator.document, 200, "Rua bla bla bla 123", 100)

  def test_rent_garage(self):
    garage_rented = self.garage_service.rent_garage(self.garage._id, self.renter.document)
    self.assertEqual(garage_rented.renter_id, self.renter._id)


  def test_cancel_rent(self):
    garage_rented = self.garage_service.cancel_rent(self.garage._id)
    self.assertEqual(garage_rented.renter_id, None)


  def test_get_system_balance(self):
    self.garage_service.rent_garage(self.garage._id, self.renter.document)
    balance = self.system_balance_service.get_system_balance()
    self.assertEqual(balance, 5)


if __name__ == '__main__':
    unittest.main()