print("=" * 30)
print("App delivery")

pedido = float(input("Digite o valor do pedido (R$): "))
distancia = float(input("Digite a distância da entrega (km): "))
primeira_compra = input("É a primeira compra? (s/n): ")
cupom = input("Digite o cupom de desconto: ")

if pedido > 50:
    frete = 0.0
elif 20 <= pedido <= 50:
    frete = 5.99
else:
    frete = 9.99

desconto = 0

if primeira_compra == 's':
    desconto = 0.10  
elif cupom == "PROMO5": 
    desconto = 0.05

valor_desconto = pedido * desconto
total_final = pedido - desconto + frete    

if distancia < 2:
    tipo_entrega = "Expresso"
elif distancia < 6:
    tipoentrega = "Normal"
else:
    tipo_entrega = "Agendado"

print(f"Resumo do Pedido:")
print(f"Frete: R$ {frete:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_final:.2f}")
print(f"Tipo de entrega: {tipo_entrega}")
print("=" * 30)  