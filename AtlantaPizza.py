count_pizza = int(input('Сколько пицц вы желаете заказать: '))
price_pizza = int(input('Сколько стоит пицца:'))
all_price_pizza = count_pizza * price_pizza
tax_pizza = all_price_pizza * 8 / 100
end_price = all_price_pizza + tax_pizza
print(f'Вы должны заплатить: ${end_price}, в том числе ${all_price_pizza} за пиццу и ${tax_pizza} налог с продаж')