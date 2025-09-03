class Time():
    """
    Uma classe para representar um time de futebol e suas estatísticas.
    """
    def __init__(self, nome):
        """
        O construtor da classe.
        Inicializa o time com um nome e estatísticas zeradas.
        """
        self.nome = nome
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0

    def adicionar_vitoria(self):
        """
        Incrementa o número de vitórias do time.
        """
        self.vitorias += 1

    def adicionar_derrota(self):
        """
        Incrementa o número de derrotas do time.
        """
        self.derrotas += 1

    def adicionar_empate(self):
        """
        Incrementa o número de empates do time.
        """
        self.empates += 1

    def exibir_estatisticas(self):
        """
        Exibe as estatísticas completas do time.
        """
        print(f"\n--- Estatísticas do {self.nome} ---")
        print(f"Vitórias: {self.vitorias}")
        print(f"Empates: {self.empates}")
        print(f"Derrotas: {self.derrotas}")
        print("-" * 25)