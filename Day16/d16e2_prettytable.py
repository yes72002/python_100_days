# import prettytable
from prettytable import PrettyTable

# create a PrettyTable object and save it to a veriable called table
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Suirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align) # 'c'
table.align = "l"
# table.align = "r"
 
print(table)
