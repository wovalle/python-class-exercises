list = ["Massih", "Es", "Un", "Forzador."]

string = " ".join(list)
print("Lista Original:", list)
print("Joined:", string)
print("Capitalized:", string)

splitted = string.split()
print("Splitted:", splitted)

# new_string="1,2,3,45"
# print("New Str Splitted:", new_string.split(',', 2))

string_rep = string.replace("Massih", "Numero 2")
print("Replaced:", string_rep.replace('Un', 'Medio').replace(' ', '_', 2))
