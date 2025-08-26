# Membership check in dictionaries

inventory = {
  "gobblet": 25,
  "loaf of bread": 30,
  "quill": 30,
  "rose": 8,
  "mead": 0,
}

request_list = ["gobblet", "mead", "rose", "dagger"]

def inquire_availability(ware):
  if ware not in inventory:
    print(f"Sorry, we do not carry any {ware.capitalize()}.")

  elif inventory[ware] <= 0:
    print(f"My apologies, we are out of stock in {ware.capitalize()}.")

  else:
    print(f"{ware.capitalize()} available and we have {inventory[ware]} in stock.")


for ware in request_list:
  inquire_availability(ware)
