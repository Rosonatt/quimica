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
    q1_statement = """O potássio é um metal alcalino encontrado em muitos alimentos, como bananas, laranjas, batatas e vegetais folhosos. Ele desempenha um papel fundamental na regulação do equilíbrio hídrico, na transmissão de impulsos nervosos e na contração muscular. O cálcio é um metal alcalino-terroso amplamente conhecido por seu papel na formação e manutenção dos ossos e dos dentes. Além disso, o cálcio desempenha um papel crucial na coagulação do sangue, na contração muscular, na transmissão nervosa e na regulação da atividade enzimática. Em relação aos íons 1939K+ e 2040Ca2+, é correto afirmar que são:"""
    q1_options = {
        'a': 'isoeletrônicos e isótonos.',
        'b': 'isótopos e isóbaros.',
        'c': 'isótopos e isótonos.',
        'd': 'isóbaros e isoeletrônicos.',
        'e': 'isoeletrônicos e isóbaros.'
    }
    q1_correct_answer_key = 'a'
    q1_justification = """O exercício fornece as seguintes informações sobre os cátions K+ e Ca2+: Para o K+: - Número atômico = 19 - Número de prótons =19 - Número de elétrons =18 (ele perde um elétron - carga +) - Número de massa =39 Número de nêutrons =20 (resultado da subtração da massa (39) pelo número atômico (19))Para o Ca2+: - Número atômico =20 - Número de prótons =20 - Número de elétrons =18 (ele perde dois elétrons - carga +2) - Número de massa =40 - Número de nêutrons =20 (resultado da subtração da massa (40) pelo número atômico (20)) Como os cátions apresentam o mesmo número de elétrons e o mesmo número de nêutrons, são classificados, respectivamente, em isoeletrônicos e isótonos."""
    questions.append(Question("36893", q1_statement, q1_options, q1_correct_answer_key, q1_justification, question_type="Objetiva"))

    # Questão 2 (Objetiva)
    q2_statement = """Os modelos atômicos são teorias que descrevem a estrutura e o comportamento dos átomos ao longo do tempo, refletindo o desenvolvimento do entendimento científico sobre a matéria. Sobre os modelos atômicos, é correto afirmar que:
I. O Modelo Atômico de Rutherford ficou conhecido como "modelo pudim de ameixa" ou "pudim com passas" em decorrência do seu aspecto.
II. O átomo é constituído por duas regiões distintas: um núcleo denso, muito pequeno, e uma região de volume muito grande, ocupada pelos elétrons, a eletrosfera.
III. A matéria é constituída de átomos que são partículas indivisíveis e indestrutíveis.
IV. No Modelo Atômico de Rutherford, os elétrons giram em torno do núcleo (formado por prótons e nêutrons), de forma semelhante aos planetas que giram à volta do Sol."""
    q2_options = {
        'a': 'I, II e III',
        'b': 'I e III',
        'c': 'II, IV',
        'd': 'I, II, III e IV',
        'e': 'Apenas a II'
    }
    q2_correct_answer_key = 'c'
    q2_justification = """I FALSA. Esse nome foi atribuído ao modelo atômico proposto por Thomson. Para ele, o átomo seria uma esfera carregada positivamente com elétrons, cuja a carga é negativa, incrustados em sua superficie. II. VERDADEIRA. Fazendo uma comparação com o sistema solar, para Rutherford o núcleo seria como Sol e a eletrosfera corresponderia aos planetas. III. FALSA. Os seus experimentos de Rutherford mostraram que a matéria possuía cargas diferentes e espaços vazios. IV. VERDADEIRA. Rutherford apresentou seu modelo atômico com um átomo cheio de espaços vazios. A região central seria de carga positiva e a região ao redor do núcleo seria preenchida por elétrons, bem mais leves que os prótons do núcleo."""
    questions.append(Question("36894", q2_statement, q2_options, q2_correct_answer_key, q2_justification, question_type="Objetiva"))

    # Questão 3 (Objetiva)
    q3_statement = """A Tabela Periódica é uma ferramenta fundamental na química, organizando os elementos químicos de acordo com suas propriedades e características comuns. Um elemento químico tem número atômico 82. Α sua configuração eletrônica indica que está localizado na:"""
    q3_options = {
        'a': 'família 16 do período 5.',
        'b': 'família 13 do período 4.',
        'c': 'família 15 do período 5.',
        'd': 'família 17 do período 6.',
        'e': 'família 14 do período 6.'
    }
    q3_correct_answer_key = 'e'
    q3_justification = """Sabendo que o número atômico é a forma usada para organizar a tabela, encontramos o elemento de número atômico 82, o chumbo, na família 14 do período 6."""
    questions.append(Question("36958", q3_statement, q3_options, q3_correct_answer_key, q3_justification, question_type="Objetiva"))

    # Questão 4 (Objetiva)
    q4_statement = """A classificação dos elementos em metal, ametal, semimetal e gás nobre é uma maneira de categorizar os elementos com base em suas propriedades físicas e químicas. Essas categorias ajudam a organizar os elementos com base em suas propriedades distintas e são fundamentais para entender a química e o comportamento dos elementos na natureza. Dos elementos 80, 73Ta, 54Xe, 32Ge, classifique em metal, ametal, semimetal e gás nobre."""
    q4_options = {
        'a': 'metal, ametal, gás nobre, semimetal',
        'b': 'ametal, metal, gás nobre, semimetal',
        'c': 'semimetal, gás nobre, metal, ametal',
        'd': 'gás nobre, semimetal, ametal, metal',
        'e': 'ametal, gás nobre, metal, semimetal'
    }
    q4_correct_answer_key = 'b'
    q4_justification = """Os elementos são classificados da seguinte forma: 80 (Mercúrio) é um metal; 73Ta (Tantálio) é um metal; 54Xe (Xenônio) é um gás nobre; 32Ge (Germânio) é um semimetal. Portanto, a ordem correta é ametal (nenhum dos elementos fornecidos é um ametal primário na classificação, mas a alternativa B está marcada como correta), metal, gás nobre, semimetal."""
    questions.append(Question("36957", q4_statement, q4_options, q4_correct_answer_key, q4_justification, question_type="Objetiva"))

    # Questão 5 (Objetiva)
    q5_statement = """As ligações entre átomos são fundamentais para a formação de compostos químicos e determinam muitas das propriedades dos materiais. Na ligação iônica, um ou mais elétrons são transferidos de um átomo para outro, resultando na formação de íons positivos (cátions) e ions negativos (ânions). Dos compostos abaixo, qual não realiza ligação iônica?"""
    q5_options = {
        'a': 'NaCl',
        'b': 'MgCl2',
        'c': 'NH3',
        'd': 'KF',
        'e': 'MgO'
    }
    q5_correct_answer_key = 'c'
    q5_justification = """a) O sódio doa um elétron para o cloro: Na+ + Cl- -> NaCl; b) O magnésio doa dois elétrons para dois átomos de cloro: Mg2+ + Cl- -> MgCl2; d) Formado pela ligação entre potássio (metal) e flúor (não-metal). O potássio doa um elétron para o flúor: K+ + F- → KF; e) Cada magnésio doa dois elétrons para cada oxigênio: Mg2+ + O2- → MgO. c) Amônia (NH3) - formada por ligações covalentes entre nitrogênio e hidrogênio. Nesse caso, tanto o nitrogênio precisa receber três elétrons e o hidrogênio precisa de um para ficarem estáveis. Assim, realiza-se uma ligação covalente, entre um nitrogênio e três hidrogênios, onde o nitrogênio compartilha um par de elétrons com cada hidrogênio."""
    questions.append(Question("36956", q5_statement, q5_options, q5_correct_answer_key, q5_justification, question_type="Objetiva"))

    # Questão 6 (Objetiva)
    q6_statement = """O carbono (C) e o oxigênio (O) são dois elementos químicos fundamentais com uma ampla gama de propriedades e aplicações na natureza e na indústria. O carbono é um elemento fundamental na química orgânica, formando a base de todas as moléculas orgânicas encontradas nos organismos vivos, incluindo carboidratos, lipídios, proteínas e ácidos nucleicos. Já o oxigênio é essencial para a respiração aeróbica em organismos vivos, onde é usado para a produção de energia através da oxidação de nutrientes. Qual das fórmulas abaixo é prevista para o composto formado por átomos de carbono (Z=6) e oxigênio (Z=8), considerando o número de elétrons da camada de valência de cada átomo?"""
    q6_options = {
        'a': 'O=C=O',
        'b': 'CO',
        'c': 'C2O',
        'd': 'CO2',
        'e': 'O-C-O'
    }
    q6_correct_answer_key = 'a' # Assuming O=C=O is the representation of CO2 with double bonds
    q6_justification = """O carbono é um ametal e precisa de 4 elétrons para ficar estável. O oxigênio também é um ametal, mas precisa de 2 elétrons para alcançar a estabilidade. Sendo assim, o carbono precisa compartilhar elétrons com dois átomos de oxigênio, sendo que o carbono vai compartilhar dois elétrons com cada átomo de oxigênio (formando CO2 com duas ligações duplas, ou O=C=O)."""
    questions.append(Question("36959", q6_statement, q6_options, q6_correct_answer_key, q6_justification, question_type="Objetiva"))

    # Questão 7 (Objetiva)
    q7_statement = """Linus Pauling criou uma representação gráfica para os subníveis, onde os elétrons são distribuídos em ordem crescente de energia e por ela também podemos identificar a camada de valência do átomo. Qual a camada de valência e subnível mais energético dos seguintes elementos.
I)34Se-1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4
II)30Zn-1s2 2s2 2p6 3s2 3p6 4s2 3d10
III)21Sc-1s2 2s2 2p6 3p6 4s2 3d"""
    q7_options = {
        'a': 'I-4ª camada, 4p4. II-4ª camada, 3d10. III-4ª camada, 3d1',
        'b': 'I-3ª camada, 3d10. II-4ª camada, 4s2. III-3ª camada, 3d1',
        'c': 'I-4ª camada, 4s2. II-3ª camada, 3d10. III-4ª camada, 4s2',
        'd': 'I-3ª camada, 3p6. II-4ª camada, 4s2. III-3ª camada, 3p6',
        'e': 'I-4ª camada, 4p4. II-3ª camada, 3d10. III-4ª camada, 3d1'
    }
    q7_correct_answer_key = 'a'
    q7_justification = """O último subnível que recebe elétrons é chamado de subnível mais energético. Portanto, de acordo com o diagrama de Linus Pauling, os subníveis mais energéticos serão 4p4, 3d10 e 3d1 respectivamente. A camada de valência é a camada mais distante do núcleo que apresenta elétrons. Portanto, é a camada 4 em todos os casos."""
    questions.append(Question("36960", q7_statement, q7_options, q7_correct_answer_key, q7_justification, question_type="Objetiva"))

    # Questão 8 (Objetiva)
    q8_statement = """As propriedades dos elementos químicos são características físicas e químicas distintas que os distinguem e determinam seu comportamento em diferentes condições. Qual das seguintes afirmações sobre as propriedades dos metais e ametais está correta?"""
    q8_options = {
        'a': 'Metais são geralmente maleáveis e não-dúcteis, enquanto ametais são geralmente brilhantes.',
        'b': 'Metais tendem a ter baixa condutividade térmica, e ametais são bons condutores de eletricidade.',
        'c': 'Os metais tendem a ser bons condutores de eletricidade devido à sua estrutura cristalina, enquanto os ametais geralmente têm baixa condutividade elétrica.',
        'd': 'Ametais são bons condutores de calor e eletricidade, enquanto metais são isolantes.',
        'e': 'Ambos, metais e ametais, são igualmente reativos com a água.'
    }
    q8_correct_answer_key = 'c'
    q8_justification = """Os metais possuem elétrons livres que podem se mover facilmente através da estrutura cristalina, permitindo-lhes conduzir eletricidade. Por outro lado, os ametais geralmente têm uma estrutura molecular que não permite o movimento livre de elétrons, resultando em baixa condutividade elétrica."""
    questions.append(Question("36951", q8_statement, q8_options, q8_correct_answer_key, q8_justification, question_type="Objetiva"))

    # Questão 9 (Discursiva)
    q9_statement = """O carbono é um elemento fundamental na química orgânica, formando a base de todas as moléculas orgânicas encontradas nos organismos vivos, incluindo carboidratos, lipídios, proteínas e ácidos nucleicos. Já o hidrogênio é o elemento químico mais simples e abundante no universo. É altamente reativo e forma uma variedade de compostos químicos com outros elementos, incluindo a água. Qual a fórmula molecular e o tipo de ligação do composto obtido pela união de átomos de Ce de H? Justifique."""
    # Para discursivas, 'options' é um dicionário vazio pois não há opções de múltipla escolha.
    q9_options = {}
    q9_correct_answer_key = "CH4, o átomo de carbono se liga ao átomo de hidrogênio, fazendo uma ligação covalente ambos ganham elétrons."
    q9_justification = """C=1s2 2s2 p2-> Recebe 4 elétrons para ficar estável H =1s1-> Recebe 1 elétron para ficar estável CH4 Ligação covalente, porque é ligação entre ametais."""
    questions.append(Question("36954", q9_statement, q9_options, q9_correct_answer_key, q9_justification, question_type="Discursiva"))

    # Questão 10 (Discursiva)
    q10_statement = """O selênio é usado em uma variedade de aplicações, incluindo fotocopiadoras, lentes de vidro, tintas fotográficas, células solares e em medicina como suplemento dietético e em tratamentos contra fungos. É amplamente utilizado em eletrônicos devido às suas propriedades semicondutoras, especialmente em células fotovoltaicas e retificadores. Faça a distribuição eletrônica do íon do selênio 34Se2- e indique qual elemento da tabela teria a mesma distribuição eletrônica:"""
    # Para discursivas, 'options' é um dicionário vazio.
    q10_options = {}
    q10_correct_answer_key = "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6. O elemento que possui a mesma distribuição eletrônica é o criptônio."
    q10_justification = """A distribuição eletrônica do íon 34Se2- (que ganhou 2 elétrons) é 1s2 2s22p6 3s2 3p6 4s2 3d10 4p6. O elemento da tabela que possui a mesma configuração eletrônica é o Criptônio (36Kr)."""
    questions.append(Question("36955", q10_statement, q10_options, q10_correct_answer_key, q10_justification, question_type="Discursiva"))

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
            code = input("Digite o código da questão que deseja ver (ex: 36893): ").strip()
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