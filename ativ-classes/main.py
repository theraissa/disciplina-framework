from team import Time

def main():
    """
    Função principal para demonstrar a classe Time.
    """
    inter = Time("Internacional")
    gremio = Time("Grêmio")

    print("Simulação de um Grenal!")
    
    gols_inter = int(input(f"Gols do {inter.nome}: "))
    gols_gremio = int(input(f"Gols do {gremio.nome}: "))

    if gols_inter > gols_gremio:
        print(f"\n{inter.nome} venceu o Grenal!")
        inter.adicionar_vitoria()
        gremio.adicionar_derrota()
    elif gols_gremio > gols_inter:
        print(f"\n{gremio.nome} venceu o Grenal!")
        gremio.adicionar_vitoria()
        inter.adicionar_derrota()
    else:
        print("\nO Grenal terminou em empate!")
        inter.adicionar_empate()
        gremio.adicionar_empate()
    
    inter.exibir_estatisticas()
    gremio.exibir_estatisticas()

if __name__ == "__main__":
    main()