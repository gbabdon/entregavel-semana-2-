senha_correta = "1234"

tentativas = 0

acesso_liberado = False

while tentativas < 3:
    senha = input("Digite a senha: ")

    tentativas += 1

    if senha == senha_correta:
        acesso_liberado = True
        break
    else:
        print(f"Senha incorreta. Tentativa {tentativas} de 3.")

if acesso_liberado:
    print(f"Acesso liberado após {tentativas} tentativa(s).")
else:
    print(f"Acesso bloqueado após {tentativas} tentativa(s).")
