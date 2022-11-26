class SystemBalanceService():
  def __init__(self):
    self.balance = 0

  def get_system_balance(self):
    print("Saldo do sistema: R$ %.2f" % self.balance)
    return self.balance

  def charge_system_tax(self):
    self.balance = self.balance + 5