print("Olá, tudo bem? ")
dicionario = []
while True:
    existe = 0
    teste = 0
    termo_encontrado = 0
    try:
        teste = len(dicionario)
        alternativa_user = input("Deseja pôr um termo novo ou saber um termo('Pôr' - Para pôr novo termo / 'Termo' - para ver termo / 'Sair' - para encerrar)? ").upper()
        if alternativa_user == "SAIR":
            break
        elif alternativa_user != "SAIR":
            if alternativa_user == "PÔR" or alternativa_user == "POR":
                termo_dentro_do_dicionario = input("Qual termo deseja pôr no dicionário? ").upper()
                significado_desejado = input("Qual siginificado do termo? ")
                for itens in dicionario:
                    if termo_dentro_do_dicionario == itens["TERMO"]:
                        existe = 1
                        print("Termo já existente.")
                        break
                if existe == 0:
                    print(f"Como o vocabulário não consta no dicionário, será adicionado.\nO termo adicionado foi {termo_dentro_do_dicionario.capitalize()}")
                    item_atual = {
                        "TERMO": termo_dentro_do_dicionario, 
                        "SIGNIFICADO": significado_desejado
                    }
                    dicionario.append(item_atual)
            elif alternativa_user == "TERMO":
                if teste != 0:
                    desejo_usuario = input("Qual termo gostaria de descobrir o significado? ").upper()
                    for elementos in dicionario:
                        if elementos["TERMO"] == desejo_usuario:
                            print(f"O significado de {desejo_usuario.capitalize()} é: {elementos['SIGNIFICADO'].capitalize()}")
                            termo_encontrado = 1  # Sinaliza que achou
                            break  # Para o loop imediatamente, não precisa continuar procurando      
                        # 2. Só verificamos se NÃO encontrou DEPOIS que o loop acabou
                    if termo_encontrado == 0:
                        print("Termo não existente, tente novamente")    
                elif teste == 0:
                    print(f"Dicionário vazio, adicione o primeiro termo")
    except ValueError:
        print("Valor inválido, tente novamente.")