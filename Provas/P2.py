class Question:
    # Construtor da classe Question. Define como uma questão é criada.
    def __init__(self, code, statement, options, correct_answer_key, justification, question_type="Objetiva"):
        self.code = code  # Código único da questão.
        self.statement = statement  # Enunciado da questão.
        self.options = options  # Opções de múltipla escolha (se for objetiva). É um dicionário.
        self.correct_answer_key = correct_answer_key  # Chave da resposta correta (ex: 'a', ou a resposta completa para discursivas).
        self.justification = justification  # Justificativa da resposta.
        self.question_type = question_type  # Tipo da questão (Objetiva ou Discursiva).
        self.viewed = False  # Indica se a questão já foi visualizada pelo usuário. Inicia como False.

    # Método para exibir a questão e interagir com o usuário.
    def display(self):
        self.viewed = True  # Marca a questão como visualizada ao ser exibida.
        print(f"\n--- Questão {self.code} ({self.question_type}) ---")
        print("Enunciado:")
        print(self.statement)

        # Se a questão for de múltipla escolha (Objetiva).
        if self.question_type == "Objetiva":
            print("\nOpções:")
            # Exibe cada opção disponível para o usuário, iterando sobre o dicionário de opções.
            for key, value in self.options.items():
                print(f"{key}) {value}")

            # Loop para garantir que o usuário digite uma opção válida.
            while True:
                user_answer = input("Sua resposta (digite a letra da opção): ").strip().lower()
                if user_answer in self.options: # Verifica se a opção digitada existe nas opções da questão.
                    break
                else:
                    print("Opção inválida. Por favor, digite uma das letras das opções disponíveis (ex: 'a', 'b', etc.).")

            # Compara a resposta do usuário com a resposta correta.
            if user_answer == self.correct_answer_key.lower():
                print("Correto!")
            else:
                print(f"Errado. A resposta correta era: {self.correct_answer_key}) {self.options[self.correct_answer_key]}")
            print("\n--- Justificativa ---")
            print(self.justification)
        # Se a questão for discursiva.
        elif self.question_type == "Discursiva":
            print("\n--- Resposta Esperada ---")
            # Para discursivas, a 'correct_answer_key' contém a resposta completa.
            print(self.correct_answer_key)
            print("\n--- Justificativa ---")
            print(self.justification)

        print("-" * 50) # Linha separadora para melhor visualização entre questões.

def main():
    questions = []  # Lista para armazenar todos os objetos de questão.

    # --- Definição das Questões ---

    # Questão 1 (Objetiva)
    q1_statement = """O gás metano (CH4) é um hidrocarboneto simples, altamente inflamável e que apresenta pouca solubilidade na água, sendo um dos principais compostos que potencializa o efeito estufa no mundo.
Considerando a estrutura da molécula de CH4 é incorreto afirmar que:"""
    q1_options = {
        'a': 'A molécula é apolar.',
        'b': 'As ligações C-H são polares.',
        'c': 'O carbono realiza ligações simples.',
        'd': 'Possui geometria do tipo piramidal.',
        'e': 'A hibridização do carbono é sp3.'
    }
    q1_correct_answer_key = 'd'
    q1_justification = """A geometria da molécula CH4 é tetraédrica. O gás metano é um composto formado por 5 átomos e o carbono, que é o átomo central, contém 4 ligantes."""
    questions.append(Question("45205", q1_statement, q1_options, q1_correct_answer_key, q1_justification, question_type="Objetiva"))

    # Questão 2 (Discursiva)
    q2_statement = """Os compostos SO3, PCI5 são exemplos distintos que ilustram a diversidade das geometrias moleculares e suas implicações nas propriedades químicas. A geometria do trióxido de enxofre (SO3) influencia sua reatividade como um agente oxidante forte e sua utilidade na indústria química. A geometria molecular do pentacloreto de fósforo (PCI5) afeta suas propriedades como um sólido cristalino e sua reatividade como um reagente químico.
Identifique corretamente a geometria das seguintes moléculas e justifique: SO3, PCI5, H2O"""
    q2_options = {} # Discursiva, sem opções
    q2_correct_answer_key = """SO3 = trigonal plana
PCl5 = trigonal bipiramidal
H2O = angular"""
    q2_justification = """SO3 - apresenta geometria trigonal plana, pois o átomo central de enxofre (S) contém 3 ligantes. PCl5 - apresenta geometria bipiramidal trigonal, pois o átomo central de fósforo(P) contém 5 ligantes. H2O - apresenta geometria angular, pois o átomo central de oxigênio (O) contém 2 ligantes e pares de elétrons emparelhados disponíveis."""
    questions.append(Question("45208", q2_statement, q2_options, q2_correct_answer_key, q2_justification, question_type="Discursiva"))

    # Questão 3 (Objetiva)
    q3_statement = """Alotropia é a propriedade pela qual um mesmo elemento químico pode formar duas ou mais substâncias simples diferentes, denominadas variedades alotrópicas do elemento.
São elementos que apresentam formas alotrópicas:"""
    q3_options = {
        'a': 'fósforo e enxofre',
        'b': 'sódio e cloro',
        'c': 'hidrogênio e hélio',
        'd': 'nitrogênio e oxigênio',
        'e': 'carbono e flúor'
    }
    q3_correct_answer_key = 'a'
    q3_justification = """Alótropos do fósforo: fósforo vermelho e fósforo branco. Alótropos do enxofre: enxofre rômbico e enxofre monoclínico."""
    questions.append(Question("45209", q3_statement, q3_options, q3_correct_answer_key, q3_justification, question_type="Objetiva"))

    # Questão 4 (Discursiva)
    q4_statement = """A polaridade das ligações químicas é determinada pela diferença de eletronegatividade entre os átomos ligados, afetando a distribuição de carga ao longo da ligação e, consequentemente, a natureza polar ou não polar da molécula resultante.
Determine se as ligações a seguir são polares ou apolares e especifique também se são iônicas ou covalentes: HCl, Cl2, CO2"""
    q4_options = {} # Discursiva, sem opções
    q4_correct_answer_key = """HCl = Covalente polar
Cl2 = Covalente apolar
CO2 = covalente apolar"""
    q4_justification = """HCl - Ligação covalente polar. Cl2 - Ligação covalente apolar. CO2 - Ligações covalentes polares (mas a molécula é apolar devido à sua geometria linear e vetores dipolo se cancelarem). Nota: A justificativa original da prova para CO2 estava ligeiramente ambígua, mas a resposta final da polaridade da molécula de CO2 como apolar está correta. Mantenho a justifcativa original para fins de fidelidade à prova."""
    questions.append(Question("45220", q4_statement, q4_options, q4_correct_answer_key, q4_justification, question_type="Discursiva"))

    # Questão 5 (Objetiva)
    q5_statement = """A sacarose, conhecida comumente como açúcar, é um sólido cristalino à temperatura ambiente, que se dissolve em água e possui sabor doce.
A massa molecular do composto C12H22O11 é igual a: Dados: H=1; O=16; C=12."""
    q5_options = {
        'a': '180 u',
        'b': '342 u',
        'c': '242 u',
        'd': '400 u',
        'e': '360 u'
    }
    q5_correct_answer_key = 'b'
    q5_justification = """Para saber a resposta, devemos multiplicar a quantidade de cada elemento por sua massa atômica e, em seguida, somar os resultados: M = (12 * 12) + (22 * 1) + (11 * 16) = 144 + 22 + 176 = 342 u."""
    questions.append(Question("45230", q5_statement, q5_options, q5_correct_answer_key, q5_justification, question_type="Objetiva"))

    # Questão 6 (Objetiva)
    q6_statement = """O ácido acetilsalicílico, também conhecido como ASA, é um composto químico cuja fórmula molecular é C9H8O4. Este composto é amplamente conhecido por suas propriedades analgésicas, antipiréticas (reduz a febre) e anti-inflamatórias. É o princípio ativo da aspirina, um medicamento comum utilizado para tratar dor e inflamação.
Submetida a um tratamento médico, uma pessoa ingeriu um comprimido contendo 45 mg de ácido acetilsalicílico (C9H8O4). Considerando a massa molar de C9H8O4 180g/mol e o número de Avogadro 6,0.10^23, qual o número de moléculas da substância ingerida?"""
    q6_options = {
        'a': '6,0 . 10^20 moléculas',
        'b': '1,5 . 10^20 moléculas',
        'c': '3,0 . 10^22 moléculas',
        'd': '4,5 . 10^19 moléculas',
        'e': '9,0 . 10^21 moléculas'
    }
    q6_correct_answer_key = 'b'
    q6_justification = """A massa molar do C9H8O4 é 180g/mol e 1 mol tem 6,0 . 10^23 moléculas. Primeiro, converta 45 mg para gramas: 45 mg = 0,045 g.
Agora, faça uma regra de três:
180 g de C9H8O4 ------ 6,0 . 10^23 moléculas
0,045 g de C9H8O4 ----- x moléculas
x = (0,045 * 6,0 . 10^23) / 180
x = (270 * 10^-3 * 10^23) / 180
x = (270 * 10^20) / 180
x = 1,5 . 10^20 moléculas"""
    questions.append(Question("45233", q6_statement, q6_options, q6_correct_answer_key, q6_justification, question_type="Objetiva"))

    # Questão 7 (Objetiva)
    q7_statement = """A glicose (C?H??O?) desempenha um papel fundamental como fonte de energia para os organismos vivos através da respiração celular. É encontrada em muitos alimentos e é transportada no sangue para fornecer energia às células do corpo humano e de outros seres vivos.
Determine a fórmula percentual da glicose, sendo que na decomposição de 1,8 g foram produzidas: 0,72 g de carbono, 0,12 g de hidrogênio e 0,96 g de oxigênio."""
    q7_options = {
        'a': 'C40% H6,67% O53,33%',
        'b': 'C30% H10% O60%',
        'c': 'C50% H5% O45%',
        'd': 'C45% H7,5% O47,5%',
        'e': 'C35% H8% O57%'
    }
    q7_correct_answer_key = 'a'
    q7_justification = """Para determinar as porcentagens de cada composto na amostra é possível seguir dois caminhos diferentes. No primeiro, usa-se a seguinte fórmula: Porcentagem de massa do elemento = (massa do elemento na amostra / massa total da amostra) * 100%.
Assim, usa-se essa fórmula para cada elemento:
Porcentagem de massa do carbono = (0,72 g / 1,8 g) * 100% = 40%
Porcentagem de massa do hidrogênio = (0,12 g / 1,8 g) * 100% = 6,67%
Porcentagem de massa do oxigênio = (0,96 g / 1,8 g) * 100% = 53,33%
Assim, a fórmula centesimal pode ser expressa por: C40%H6,67%O53,33%."""
    questions.append(Question("45237", q7_statement, q7_options, q7_correct_answer_key, q7_justification, question_type="Objetiva"))

    # Questão 8 (Objetiva)
    q8_statement = """A cada 10 m de profundidade a pressão sobre um mergulhador aumenta 1 atm com relação à pressão atmosférica. Sabendo-se disso, qual seria o volume de 1 L de ar (comportando-se como um gás ideal) inspirado pelo mergulhador ao nível do mar, quando ele estivesse a 30 m de profundidade?"""
    q8_options = {
        'a': '250 mL',
        'b': '500 mL',
        'c': '750 mL',
        'd': '1000 mL',
        'e': '1250 mL'
    }
    q8_correct_answer_key = 'a'
    q8_justification = """Ao nível do mar (0m), a pressão é de 1 atm. A cada 10m de profundidade, a pressão aumenta 1 atm.
A 30m de profundidade, o aumento é de 3 atm (30m / 10m por atm = 3 atm).
A pressão total a 30m de profundidade será 1 atm (atmosférica) + 3 atm (aumento) = 4 atm.
Usando a Lei de Boyle (P1 * V1 = P2 * V2), onde a temperatura é constante:
P1 = 1 atm (nível do mar)
V1 = 1 L (volume inicial)
P2 = 4 atm (a 30m de profundidade)
V2 = ?
1 atm * 1 L = 4 atm * V2
V2 = 1 / 4 L
V2 = 0.25 L = 250 mL"""
    questions.append(Question("45238", q8_statement, q8_options, q8_correct_answer_key, q8_justification, question_type="Objetiva"))

    # Questão 9 (Objetiva)
    q9_statement = """Um gás ideal está confinado em um recipiente cúbico de aresta igual a 0,5 m. A pressão exercida sobre as paredes do recipiente corresponde a 59760 Pa. Sabendo que a temperatura do gás é de 300 K, determine o número de moléculas contidas no recipiente. Dado: Considere R=8,3(J/mol.K)"""
    q9_options = {
        'a': '1 mol',
        'b': '3 mol',
        'c': '5 mol',
        'd': '0,5 mol',
        'e': '2 mol'
    }
    q9_correct_answer_key = 'b'
    q9_justification = """Primeiro, calcule o volume do recipiente: V = aresta^3 = (0,5 m)^3 = 0,125 m³.
Aplicando a equação de Clapeyron (Lei dos Gases Ideais), PV = nRT:
P = 59760 Pa
V = 0,125 m³
n = número de mols (o que queremos encontrar)
R = 8,3 J/(mol.K)
T = 300 K
Reorganizando para encontrar n: n = (P * V) / (R * T)
n = (59760 Pa * 0,125 m³) / (8,3 J/(mol.K) * 300 K)
n = 7470 / 2490
n = 3 mol"""
    questions.append(Question("45240", q9_statement, q9_options, q9_correct_answer_key, q9_justification, question_type="Objetiva"))

    # Questão 10 (Objetiva)
    q10_statement = """Uma solução foi preparada dissolvendo-se 4,0 g de cloreto de sódio (NaCl) em 2,0 litros de água. Considerando que o volume da solução permaneceu 2,0 L, qual é a concentração da solução final?"""
    q10_options = {
        'a': '0,5 g/L',
        'b': '1,0 g/L',
        'c': '2,0 g/L',
        'd': '4,0 g/L',
        'e': '8,0 g/L'
    }
    q10_correct_answer_key = 'c'
    q10_justification = """A concentração comum (C) é calculada pela massa do soluto (m1) dividida pelo volume da solução (V):
C = m1 / V
C = 4,0 g / 2,0 L
C = 2,0 g/L"""
    questions.append(Question("45242", q10_statement, q10_options, q10_correct_answer_key, q10_justification, question_type="Objetiva"))

    # Cria um dicionário para acessar as questões pelo código de forma eficiente.
    question_map = {q.code: q for q in questions}

    # Loop principal que mantém o menu do programa em execução.
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ver todas as questões")
        print("2. Ver uma questão específica por código")
        print("3. Ver questões já visualizadas")
        print("4. Ver questões não visualizadas")
        print("5. Sair")

        # Solicita a escolha do usuário. O .strip() remove espaços extras e .lower() converte para minúsculas.
        choice = input("Escolha uma opção: ").strip()

        # Estrutura condicional para lidar com as diferentes escolhas do usuário.
        if choice == '1':
            # Se a escolha for '1', exibe todas as questões.
            for q in questions:
                q.display()
        elif choice == '2':
            # Se a escolha for '2', pede o código da questão ao usuário.
            code = input("Digite o código da questão que deseja ver (ex: 45205): ").strip()
            # Verifica se o código digitado existe no nosso mapa de questões.
            if code in question_map:
                question_map[code].display() # Exibe a questão correspondente.
            else:
                print("Código de questão inválido. Tente novamente.") # Mensagem de erro se o código não for encontrado.
        elif choice == '3':
            # Se a escolha for '3', filtra e exibe as questões que já foram visualizadas.
            viewed_questions = [q for q in questions if q.viewed]
            if viewed_questions:
                print("\n--- Questões Visualizadas ---")
                for q in viewed_questions:
                    print(f" - Código: {q.code}, Tipo: {q.question_type}")
            else:
                print("Nenhuma questão foi visualizada ainda.") # Mensagem se nenhuma questão foi visualizada.
        elif choice == '4':
            # Se a escolha for '4', filtra e exibe as questões que ainda não foram visualizadas.
            unviewed_questions = [q for q in questions if not q.viewed]
            if unviewed_questions:
                print("\n--- Questões Não Visualizadas ---")
                for q in unviewed_questions:
                    print(f" - Código: {q.code}, Tipo: {q.question_type}")
            else:
                print("Todas as questões foram visualizadas.") # Mensagem se todas as questões foram visualizadas.
        elif choice == '5':
            # Se a escolha for '5', encerra o loop e o programa.
            print("Saindo do programa. Até mais!")
            break
        else:
            # Para qualquer outra entrada inválida.
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

# Chama a função principal para iniciar a execução do programa.
main()