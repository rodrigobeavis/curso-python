nome = (input('Digite o nome: \n')).strip()


check = (nome.upper().find("SILVA") >= 0) and "Sim" or "Não";

print(" O nome possuí  'silva' ?  \n {}".format(check))