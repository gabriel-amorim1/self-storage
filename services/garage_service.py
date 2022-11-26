from entities.garage import Garage

class GarageService:
  garages = []

  def __init__(self, locator_service, renter_service, system_balance_service):
    self.renter_service = renter_service 
    self.system_balance_service = system_balance_service
    self.locator_service = locator_service


  def register_garage(self, locator_document, rent_price, address, size):
    locator = self.locator_service.get_locator_by_document(locator_document)
    if (locator == None):
      print('Locador não encontrado')
      return

    garage_id = str(len(self.garages) + 1)
    garage = Garage(garage_id, locator._id, rent_price, address, size)
    self.garages.append(garage)
    return garage


  def find_garage_by_id(self, garage_id):
    for garage in self.garages:
      if (garage._id == garage_id):
        return garage


  def rent_garage(self, garage_id, renter_document):
    garage_found = self.find_garage_by_id(garage_id)

    if (garage_found == None):
      print('Garagem não encontrada')
      return

    renter = self.renter_service.get_renter_by_document(renter_document)
    if (renter == None):
      print('Locatário não encontrado')
      return

    garage_found.rent(renter._id)
    self.system_balance_service.charge_system_tax()
    print('Garagem locada com sucesso')
    return garage_found


  def cancel_rent(self, garage_id):
    garage_found = self.find_garage_by_id(garage_id)

    if (garage_found == None):
      print('Garagem não encontrada')
      return

    garage_found.cancel_rent()

    print('Locação cancelada com sucesso')
    return garage_found


  def search_garages_by_size(self, garage_size):
    garages_found = []

    for garage in self.garages:
      if (garage.size >= garage_size):
        garages_found.append(garage)

    if (len(garages_found) == 0):
      print('Não encontramos nenhuma garagem com o tamanho igual ou maior ao especificado')
      return

    print('Id\t Tamanho \t Preço \t\t Endereço')
    for garage in garages_found:
      print(garage._id, "\t", garage.size, "\t\t R$ ", garage.rent_price, "\t\t", garage.address)

    return garages_found

  def search_garages_by_renter(self, renter_document):
    renter = self.renter_service.get_renter_by_document(renter_document)
    if (renter == None):
      print('Locatário não encontrado')
      return

    garages_found = []
    for garage in self.garages:
      if (garage.renter_id == renter._id):
        garages_found.append(garage)

    if (len(garages_found) == 0):
      print('O locatário não tem garagens locadas no momento')
      return

    print('Id\t Tamanho \t Preço \t\t Endereço')
    for garage in garages_found:
      print(garage._id, "\t", garage.size, "\t\t R$ ", garage.rent_price, "\t\t", garage.address)
