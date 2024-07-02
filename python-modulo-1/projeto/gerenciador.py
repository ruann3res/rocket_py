def adicionar_tarefa(tarefas, nome_tarefa):
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarrefa {nome_tarefa} foi adicionada com sucesso!")
  return

def visualizar_tarefas(tarefas):
  print("\nLista de tarefas:")
  for index,tarefa in enumerate(tarefas, start=1):
    print(f"{index}. {tarefa['tarefa']} - {'completada' if tarefa['completada'] else 'pendente'}")
  return

def atualizar_tarefa(tarefas, indice_tarefa,novo_nome):
   tarefas
   
   return

tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Remover tarefa completada")
    print("6. Sair")
    
    escolha = input("Digite a sua escolha: ")

    match escolha:
        case "1":    
            nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
            adicionar_tarefa(tarefas, nome_tarefa)
        case "2":
            visualizar_tarefas(tarefas)
        case "3":
            visualizar_tarefas(tarefas)
            indice_tarefa = input("Digite o numero da tarefa: ")
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_tarefa(tarefas,indice_tarefa,novo_nome)
        case "6":
            break

   



print("Programa finalizado")