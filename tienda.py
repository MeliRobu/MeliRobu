# Level 1 : Basic sale - English
# Level 2 : adding taxes / VAT (value added tax), it is a mistatake , the descount goes before VAT calcule
# Level 3: costumer type
# Level 4: smarts validations 
# Level 5: purchase clasifiying 

print("\nWelcome: Please choose your costumer type")
# ct = costumer type
ct= int(input("1. Regular \n2. VIP \nChoose 1 or 2: "))

""" 
Definir función, en la cual hay condiciones , si se cumple la condicion o condiciones , no sales de la función 
Una vz sale de la función condiconal, sigue ejecutandose el código en el "return" del Else , se guarda la variable name 
"""

def c_name():
    
    name_c = input("\nPlease type your name: ")
    if name_c == "" or name_c == " ":
        print("\nThe name is mandatory, it cannot be empthy,please try again ")
        return c_name()
    else:
        return name_c 
client_name = c_name()

def p_name():
    
    name_p = input("\nType the product name: ")
    if name_p == "" or name_p == " ":
        print("\nThe name is mandatory, it cannot be empthy,please try again")
        return p_name()
    else: 
        return name_p
    
product_name = p_name()

def p_price():
    
    price_p = float(input("\nType the product price: "))
    if price_p== 0 :
        print("\nInvalid price, please try again ")
        return p_price()
    else: 
        return price_p
product_price = p_price()

def p_amount():
    
    amount_p = float(input("\nType the exact product amount: "))
    if amount_p == 0 :
        print("\nInvalid amount, please try again ")
        return p_amount()
    else: 
        return amount_p
    
product_amount = p_amount()

subtotal = product_price*product_amount

 
if ct==1:
    product_dcto5=(subtotal*5)/100
    vat_dcto5= (product_dcto5*19)/100
    final_price_dcto5= (subtotal-product_dcto5)+ vat_dcto5

    print(f"\nCostumer type: Regular \nClient: {client_name} \nProduct: {product_name} \nSubtotal: {subtotal} \nDescount of 5%: {product_dcto5} \nVAT 19%: {vat_dcto5} \nTotal price: {final_price_dcto5} ") 

    if final_price_dcto5 <50000:
        print("\nPurchase clasification or type : small purchase")
        print(f"Thanks {client_name} for your purchase, you are a regular costumer. Have a nice day!")
    elif 50000<= final_price_dcto5 <150000:
        print("P\nurchase clasification or type : medium purchase")
        print(f"Thanks {client_name} for your purchase, you are a regular costumer. Have a nice day!")
    elif final_price_dcto5 >=150000:
        print("\nPurchase clasification or type : big purchase")
        print(f"Thanks {client_name} for your purchase, you are a regular costumer. Have a nice day!")

elif ct==2 :
    if subtotal > 200000:
        product_dcto15=(subtotal*15)/100
        vat_dcto15= (product_dcto15*19)/100
        final_price_dcto15= (subtotal-product_dcto15)+ vat_dcto15 
        print(f"\nCostumer type: VIP \nClient: {client_name} \nProduct: {product_name} \nSubtotal: {subtotal} \nDescount of 15%: {product_dcto15} \nVAT 19%: {vat_dcto15} \nTotal price: {final_price_dcto15} ") 

        if final_price_dcto15  <50000:
            print("\nPurchase clasification or type : small purchase")
            print(f"Thanks {client_name} for your purchase, you are a VIP costumer. Have a nice day!")
        elif 50000<= final_price_dcto15 <150000:
            print("\nPurchase clasification or type : medium purchase")
            print(f"Thanks {client_name} for your purchase, you are a VIP costumer. Have a nice day!")
        elif final_price_dcto15 >=150000:
            print("\nPurchase clasification or type : big purchase")
            print(f"Thanks {client_name} for your purchase, you are a VIP costumer. Have a nice day!")

    else: 
        product_dcto10=(subtotal*10)/100
        vat_dcto10= (product_dcto10*19)/100
        final_price_dcto10= (subtotal-product_dcto10)+ vat_dcto10 

        print(f"\nCostumer type: VIP \nClient: {client_name} \nProduct: {product_name} \nSubtotal: {subtotal} \nDescount of 10%: {product_dcto10} \nVAT 19%: {vat_dcto10} \nTotal price: {final_price_dcto10} ") 
    
        if final_price_dcto10  <50000:
            print("\nPurchase clasification or type : small purchase")
            print(f"Thanks {client_name} for your purchase, you are a VIP costumer. Have a nice day!")
        elif 50000<= final_price_dcto10 <150000:
            print("\nPurchase clasification or type : medium purchase")
            print(f"Thanks {client_name} for your purchase, you are a VIP costumer. Have a nice day!")
        elif final_price_dcto10 >=150000:
            print("\nPurchase clasification or type : big purchase")
            print(f"Thanks {client_name} for your purchase,you are a VIP costumer. Have a nice day!")

else:
    print("\nThis option is not available, this costumer type is not valid")
    print("\nThanks. Have a nice day!")










