from stock.models import Stock

def add_to_stock(transaction):
    stock_instance = Stock.objects.get(product=transaction.product)
    stock_instance.quantity += transaction.quantity
    stock_instance.save()

def remove_stock(transaction):
    stock_instance = Stock.objects.get(product=transaction.product)
    stock_instance.quantity -= transaction.quantity
    stock_instance.save()

def mirrow_modifications_purchase(new_purchase, old_purchase_product, old_purchase_quantity):
    old_stock = Stock.objects.get(product=old_purchase_product)

    if new_purchase.product == old_purchase_product:
        print("Is the same stock instance")
        old_stock.quantity -= old_purchase_quantity
        old_stock.quantity += new_purchase.quantity

    else:
        new_stock = Stock.objects.get(product=new_purchase.product)
        print("Stock instance was changed")
        old_stock.quantity -= old_purchase_quantity
        new_stock.quantity += new_purchase.quantity
        new_stock.save()
    old_stock.save()

def mirrow_modifications_sale(new_sale, old_sale_product, old_sale_quantity):
    old_stock = Stock.objects.get(product=old_sale_product)

    if new_sale.product == old_sale_product:
        print("Is the same stock instance")
        old_stock.quantity += old_sale_quantity
        old_stock.quantity -= new_sale.quantity

    else:
        new_stock = Stock.objects.get(product=new_sale.product)
        print("Stock instance was changed")
        old_stock.quantity += old_sale_quantity
        new_stock.quantity -= new_sale.quantity
        new_stock.save()
    old_stock.save()

def calc_profit_on_sale(purchase):
    purchase_price = purchase.final_price
    sale_price = purchase.product.final_price * purchase.quantity
    return round(float(sale_price) - float(purchase_price), 2)
     