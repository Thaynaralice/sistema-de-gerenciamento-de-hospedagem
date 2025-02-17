import datetime

valor_diaria = 0.0
total_quartos = 0

lista_checkin = []  # Lista de hóspedes hospedados no momento
lista_agendamentos = []  # Lista de agendamentos
historico_hospedes = []  # Lista de hóspedes que já fizeram check-out

def popular_listas(total_quartos: int, lista: list):
    for i in range(total_quartos):
        lista.append(None)

def criar_novo_hospede(nome: str, numero_quarto: int, data_entrada: datetime.datetime, data_saida: datetime.datetime, status_hospedagem: bool) -> dict:
    return {
        "nome": nome,
        "numero_quarto": numero_quarto,
        "data_entrada": data_entrada,
        "data_saida": data_saida,
        "status_hospedagem": status_hospedagem
    }

def verificar_agendamento_na_data(numero_quarto: int, data_desejada: datetime.datetime) -> bool:
    for agendamento in lista_agendamentos:
        if agendamento["numero_quarto"] == numero_quarto and agendamento["data_entrada"] <= data_desejada < agendamento["data_saida"]:
            return True  
    return False  

def fazer_checkin():
    nome = input("Nome do hóspede: ")
    numero_quarto = int(input("Número do quarto: "))
    data_entrada = input("Data de check-in (dd-mm-aaaa): ")
    data_saida = input("Data de check-out (dd-mm-aaaa): ")
    
    data_entrada = datetime.datetime.strptime(data_entrada, "%d-%m-%Y")
    data_saida = datetime.datetime.strptime(data_saida, "%d-%m-%Y")
    
    novo_hospede = criar_novo_hospede(nome, numero_quarto, data_entrada, data_saida, True)
    lista_checkin.append(novo_hospede)
    print(f"Check-in realizado para {nome} no quarto {numero_quarto}.")

def fazer_checkout():
    nome = input("Nome do hóspede que está fazendo check-out: ")
    for hospede in lista_checkin:
        if hospede["nome"] == nome:
            hospede["status_hospedagem"] = False
            historico_hospedes.append(hospede)
            lista_checkin.remove(hospede)
            print(f"Check-out realizado para {nome}.")
            return
    print("Hóspede não encontrado.")

def exibir_dashboard_historico():
    if not historico_hospedes:
        print("Nenhum hóspede realizou check-out ainda.")
        return
    print("=== Histórico de Hóspedes que Fizeram Check-Out ===")
    for hospede in historico_hospedes:
        print(f"Nome: {hospede['nome']}, Quarto: {hospede['numero_quarto']}, Check-in: {hospede['data_entrada'].strftime('%d-%m-%Y')}, Check-out: {hospede['data_saida'].strftime('%d-%m-%Y')}")

def menu():
    while True:
        print("\n1. Fazer Check-in")
        print("2. Fazer Check-out")
        print("3. Exibir Dashboard de Histórico")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            fazer_checkin()
        elif opcao == "2":
            fazer_checkout()
        elif opcao == "3":
            exibir_dashboard_historico()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()