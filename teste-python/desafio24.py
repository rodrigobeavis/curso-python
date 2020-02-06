nomeCidade = (input('Digite o nome de uma cidade: \n')).strip()


check = (nomeCidade.upper().find("SANTO", 0, 5) == 0) and "Sim" or "Não";

print(" O nome da cidade começa com a palavra Santo {}? \n".format(check))