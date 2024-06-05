def limpar_terminal(sistema): # Função para limpar o terminal
  if sistema == 'nt':
    return sistema('cls')  # Se sistema for Windows
  else:
    return sistema('clear')  # Se sistema for Linux/Unix

def adicionar_contato(contato_nome, contato_telefone, contato_email):
  contato = {"contato": contato_nome, "telefone": contato_telefone, "email": contato_email, "favorito": "False"}
  contatos.append(contato)
  print(f"\nContato '{contato_nome}' foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nMeus Contatos:\n")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "✓" if contato["favorito"] == "True" else " "
    contato_nome = contato["contato"]
    contato_telefone = contato["telefone"]
    contato_email = contato["email"]
    print(f"{indice}. [{favorito}] Nome: {contato_nome} Tel: {contato_telefone} Email: {contato_email}")
  return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    velho_nome_contato = contatos[indice_contato_ajustado]["contato"]
    contatos[indice_contato_ajustado]["contato"] = novo_nome_contato if novo_nome_contato != "" else contatos[indice_contato_ajustado]["contato"]
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato if novo_telefone_contato != "" else contatos[indice_contato_ajustado]["telefone"]
    contatos[indice_contato_ajustado]["email"] = novo_email_contato if novo_email_contato != "" else contatos[indice_contato_ajustado]["email"]
    print(f"\nO seu contato '{velho_nome_contato}' foi atualizado")
  else:
    print("Indice do contato inexistente")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = "True"
  nome_contato = contatos[indice_contato_ajustado]["contato"]
  print(f"\nContato '{nome_contato}' foi marcado como favorito!")
  return

def desfavoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = "False"
  nome_contato = contatos[indice_contato_ajustado]["contato"]
  print(f"\nContato '{nome_contato}' foi desmarcado como favorito!")
  return
def deletar_contatos(contatos, indice_contato):
  if 0 < indice_contato <= len(contatos):
    nome_contato = contatos[indice_contato - 1]["contato"]
    del contatos[indice_contato - 1]
    print(f"\nContato '{nome_contato}' foi apagado com sucesso!")
  else:
    print("Índice de contato inválido.")
  return

contatos = []