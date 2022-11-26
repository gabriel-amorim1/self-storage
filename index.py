from services.garage_service import GarageService
from services.locator_service import LocatorService
from services.renter_service import RenterService
from services.system_balance_service import SystemBalanceService

class Main:
  def __init__(self):
    self.locator_service = LocatorService()
    self.renter_service = RenterService()
    self.system_balance_service = SystemBalanceService()
    self.garage_service = GarageService(self.locator_service, self.renter_service, self.system_balance_service)


  def register_locator(self):
    name = input('Digite o nome do locador: ')
    document = input('Digite o número do documento do locador: ')
    phone = input('Digite o telefone do locador: ')

    self.locator_service.register_locator(name, document, phone)


  def register_renter(self):
    name = input('Digite o nome do locatário: ')
    document = input('Digite o número do documento do locatário: ')
    phone = input('Digite o telefone do locatário: ')

    self.renter_service.register_renter(name, document, phone)


  def register_garage(self):
    locator_document = input('Digite o documento do locador: ')
    rent_price = input('Digite o valor do aluguel: ')
    address = input('Digite o endereço: ')
    size = input('Digite o tamanho da garagem em metros quadrados: ')

    self.garage_service.register_garage(locator_document, rent_price, address, size)


  def rent_garage(self):
    garage_id = input('Digite o id da garagem: ')
    renter_document = input('Digite o documento do locatário: ')

    self.garage_service.rent_garage(garage_id, renter_document)


  def cancel_rent(self):
    garage_id = input('Digite o id da garagem: ')

    self.garage_service.cancel_rent(garage_id)


  def search_garages_by_size(self):
    garage_size = input('Digite o tamanho da garagem desejada: ')

    self.garage_service.search_garages_by_size(garage_size)


  def search_garages_by_renter(self):
    renter_document = input('Digite o documento do locatário: ')

    self.garage_service.search_garages_by_renter(renter_document)


  def get_system_balance(self):
    self.system_balance_service.get_system_balance()


  def menu(self):
    menuChoice = 0

    while(menuChoice != "9"):
      print("Selecione uma das opções abaixo:")
      print("1- Cadastrar Locador.")
      print("2- Cadastrar Locatário.")
      print("3- Cadastrar Garagem.")
      print("4- Alugar Garagem.")
      print("5- Desalugar Garagem.")
      print("6- Buscar Garagens por tamanho.")
      print("7- Buscar Garagens por locatário.")
      print("8- Consultar orçamento do sistema.")
      print("9- Sair.")
      menuChoice = input()

      if (menuChoice == "9"):
        return

      actionChoices = {
          "1": self.register_locator,
          "2": self.register_renter,
          "3": self.register_garage,
          "4": self.rent_garage,
          "5": self.cancel_rent,
          "6": self.search_garages_by_size,
          "7": self.search_garages_by_renter,
          "8": self.get_system_balance
      }

      actionChoices[menuChoice]()
    

Main().menu()