# apresentação do calculo do imc - indice de massa corporal

# Baixo peso muito grave = abaixo de 16 kg/m².
# Baixo peso grave = entre 16 e 16,99 kg/m².
# Baixo peso = entre 17 e 18,49 kg/m².
# Peso normal = entre 18,50 e 24,99 kg/m².
# Sobrepeso = entre 25 e 29,99 kg/m².
# Obesidade grau I = entre 30 e 34,99 kg/m².
# Obesidade grau II = entre 35 e 39,99 kg/m².
# Obesidade grau III (obesidade mórbida) = maior que 40 kg/m².

print("Vamos calcular o seu IMC - índice de massa corporal :D")
altura = float(input("Escreva sua altura utilizando ponto, exemplo 1.78: "))
print("Obrigado, agora o seu peso em kg!")
peso = float(input("Escreva aqui seu peso: "))
imc =  peso / (altura**2)
if imc < 16:
    print("Seu IMC calculado é...")
    print(imc)
    print("Você está a baixo do peso, muito grave!")
else:
    if imc == 16.00 or imc <= 16.99:
        print("Seu IMC calculado é...")
        print(imc)
        print("Você está  a baixo peso, grave!")
    else:
        if imc == 17 or imc <= 18.49:
            print("Seu IMC calculado é...")
            print(imc)
            print("Você está a baixo do peso!")
        else:
            if imc == 18.50 or imc <= 24.99:
                print("Seu IMC calculado é...")
                print(imc)
                print("Você tem o peso normal!")
            else:
                if imc == 25.00 or imc <= 29.99:
                    print("Seu IMC calculado é...")
                    print(imc)
                    print("Você está sobrepeso!")
                else:
                    if imc == 30.00 or imc <= 34.99:
                        print("Seu IMC calculado é...")
                        print(imc)
                        print("Cuidado, obesidade de grau 1 !")
                    else:
                        if imc == 35.00 or imc <= 39.99:
                            print("Seu IMC calculado é...")
                            print(imc)
                            print("Extremo, obesidade de grau 2 !")
                        else:
                            if imc == 40.00 or 41.00 <= imc:
                                print("Seu IMC calculado é...")
                                print(imc)
                                print("DANGER, obesidade grau 3 ! MUITO CUIDADO!")
