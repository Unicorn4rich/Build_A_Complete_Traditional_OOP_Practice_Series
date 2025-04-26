# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.


class Bank:
  bank_name = "Habib Bank Limited"

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name
    print("Chaging the name: ", cls.bank_name)


bankoo1 = Bank()
bankoo2 = Bank()

bankoo2.change_bank_name("Meezab Bank") # Chaging the name:  Meezab Bank

print(bankoo1.bank_name) # Meezab Bank
print(bankoo2.bank_name) # Meezab Bank