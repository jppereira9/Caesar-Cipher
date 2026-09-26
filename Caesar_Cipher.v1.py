def criptografar(texto, chave):
    # Inicializa a string vazia que armazenará o resultado final
    resultado = ""
    
    # Itera sobre cada caractere da string de entrada
    for caractere in texto:
        # Verifica se o caractere é uma letra (ignora espaços, números e pontuações)
        if caractere.isalpha():
            # Define o valor base na tabela ASCII: 65 para 'A' (maiúsculas) e 97 para 'a' (minúsculas)
            ascii_base = ord('A') if caractere.isupper() else ord('a')
            
            # Cálculo do deslocamento:
            # 1. ord(caractere) - ascii_base: Converte a letra para um índice de 0 a 25.
            # 2. + chave: Aplica o deslocamento desejado.
            # 3. % 26: Aplica a operação de módulo para garantir a rotação do alfabeto (se passar de 'Z', volta para 'A').
            # 4. + ascii_base: Retorna o valor para a faixa correta da tabela ASCII.
            # 5. chr(...): Converte o código numérico final de volta para caractere.
            novo_caractere = chr((ord(caractere) - ascii_base + chave) % 26 + ascii_base)
            resultado += novo_caractere
        else:
            # Mantém o caractere original caso não seja uma letra do alfabeto
            resultado += caractere
            
    return resultado

def descriptografar(texto_cifrado, chave):
    # A descriptografia é exatamente o processo inverso, portanto, basta inverter o sinal da chave
    return criptografar(texto_cifrado, -chave)

def forca_bruta(texto_cifrado):
    print(f"\n--- Iniciando Ataque de Força Bruta ---")
    
    # O alfabeto possui 26 letras, logo, existem 25 chaves possíveis (1 a 25)
    for chave in range(1, 26):
        # Testa a descriptografia para a chave atual da iteração
        texto_decifrado = descriptografar(texto_cifrado, chave)
        
        # Exibe o resultado formatando o número da chave com dois dígitos (ex: 01, 02)
        print(f"[Chave {chave:02d}]: {texto_decifrado}")

def menu():
    # Loop infinito para manter a aplicação rodando até o usuário decidir sair
    while True:
        # Exibição da interface do menu
        print("\n" + "="*40)
        print("🛡️ CIFRA DE CÉSAR 🛡️")
        print("="*40)
        print("1. Criptografar mensagem")
        print("2. Descriptografar (com chave)")
        print("3. Descriptografar (Força Bruta)")
        print("4. Sair")
        print("="*40)
        
        # Coleta a opção escolhida pelo usuário
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == '1':
            texto = input("\nDigite a mensagem para criptografar:  ")
            # Bloco try-except para capturar erros caso o usuário digite texto em vez de número na chave
            try:
                chave = int(input("Digite a chave númerica de deslocamento: "))
                texto_cifrado = criptografar(texto, chave)
                print(f"\n🔒 Mensagem Criptografada: {texto_cifrado}")
            except ValueError:
                print("\n❌ Erro: A chave precisa ser um número inteiro.")
                
        elif opcao == '2':
            texto = input("\nDigite a mensagem criptografada: ")
            try:
                chave = int(input("Digite a chave utilizada na origem: "))
                texto_recuperado = descriptografar(texto, chave)
                print(f"\n🔓 Mensagem Descriptografada: {texto_recuperado}")
            except ValueError:
                print("\n❌ Erro: A chave precisa ser um número inteiro.")
                
        elif opcao == '3':
            texto = input("\nDigite a mensagem criptografada: ")
            # Executa a função que testará e imprimirá todas as 25 combinações
            forca_bruta(texto)
            print("\n✅ Busca finalizada. Procure a mensagem legível acima.")
            
        elif opcao == '4':
            # Interrompe o loop 'while' e finaliza a execução do programa
            print("\nEncerrando o programa. Até mais! 👋\n")
            break
            
        else:
            # Tratamento para opções inválidas (diferentes de 1, 2, 3 ou 4)
            print("\n⚠️ Opção inválida. Por favor, escolha um número de 1 a 4.")

# ==========================================
# Inicialização do Programa
# ==========================================
# Verifica se o script está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    menu()