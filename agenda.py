from os import system as sistema
from funcoes_agenda import adicionar_contato, ver_contatos, contatos, limpar_terminal, editar_contato, favoritar_contato, desfavoritar_contato, deletar_contatos

while True:
  print("\nMinha Agenda de Contatos:\n")
  print("1. Adicionar")
  print("2. Ver minha lista")
  print("3. Editar")
  print("4. Marcar/Desmarcar favorito")
  print("5. Deletar")
  print("6. Sair")

  escolha = input("\nEscolha uma opção: ")

  match escolha:
    case "1":
      limpar_terminal(sistema)
      contato_nome = input("Digite o nome do contato que deseja adicionar: ")
      contato_telefone = input("Digite o telefone do seu contato: ")
      contato_email = input("Agora digite o email do contato: ")
      adicionar_contato(contato_nome, contato_telefone, contato_email)
    case "2":
      limpar_terminal(sistema)
      if len(contatos) >= 1:
        ver_contatos(contatos)
      else:
        print("\nNenhum contato foi adicionado!")
      
    case "3":
          while True:
            limpar_terminal(sistema)
            try:
              if len(contatos) == 0: 
                print("\nNenhum contato foi adicionado!")
                break 
              elif len(contatos) >= 1:
                ver_contatos(contatos)
                print("0. [ ] Voltar")
                entrada_contato = input("\nDigite o número do contato que deseja atualizar: ")
                if entrada_contato == "0":
                    limpar_terminal(sistema)
                    break
                if entrada_contato.isdigit():
                    indice_contato = int(entrada_contato)
                    if 1 <= indice_contato <= len(contatos):
                        print("\nContato selecionado:", contatos[indice_contato - 1]["contato"])
                        novo_nome_contato = input("\nDigite o novo nome do contato: ")
                        novo_telefone_contato = input("Digite o novo telefone do contato: ")
                        novo_email_contato = input("Agora digite o novo email do contato: ")
                        editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)
                        break
                    else:
                        print("\nNúmero da lista inexistente. Por favor digite um número entre 1 e", len(contatos))
                else:
                    print("\nEntrada inválida, por favor digite um número")
                    continue
            except ValueError:
                print("Opção inválida")

    case "4":
      while True:
        limpar_terminal(sistema)
        try:
          if len(contatos) == 0: 
            print("\nNenhum contato foi adicionado!")
            break 
          elif len(contatos) >= 1:
            ver_contatos(contatos)
            print("0. [ ] Voltar")
            entrada_contato = input("\nDigite o número do contato que deseja marcar/desmarcar: ")
          if entrada_contato == "0":
            limpar_terminal(sistema)
            break
          if entrada_contato.isdigit():
            indice_contato = int(entrada_contato)
            if contatos[indice_contato - 1]["favorito"] == "False":
              favoritar_contato(contatos, indice_contato)
            else:
              desfavoritar_contato(contatos, indice_contato)
          else:
            print("\nVocê não selecionou nenhum contato!")
        except ValueError:
         print("Opção inválida")      

    case "5":
      while True:
        limpar_terminal(sistema)
        if len(contatos) == 0: 
          print("\nNenhum contato foi adicionado!")
          break 
        elif len(contatos) >= 1:
          ver_contatos(contatos)
          print("0. [ ] Voltar")
          indice_contato = input("\nDigite o número do contato que deseja deletar: ")
          if indice_contato == "0":
            break
          elif indice_contato.isdigit():
            indice_contato = int(indice_contato)
            deletar_contatos(contatos, indice_contato)
            break
          else:
            print("\nEntrada inválida, por favor digite um número")

    case "6":
      break

    case __:
      limpar_terminal(sistema)
      print("\nOpção inválida")

print("\nPrograma finalizado")
