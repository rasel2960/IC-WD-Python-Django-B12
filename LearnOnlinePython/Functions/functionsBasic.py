def calculate_order_summary(items, tax_rate=0.15, discount=0):
    """Calculate comprehensive order information"""
    # Calculate subtotal
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    print(f"Subtotal: {subtotal}")
    # for item in items:
    #     print(item)
    #     print(f"{item['price']}: {item['quantity']}")


    # Apply discount
    discount_amount = subtotal * discount
    print(f"Discount: {discount_amount}")
    subtotal_after_discount = subtotal - discount_amount
    print(f"Subtotal after discount: {subtotal_after_discount}")

    # Calculate tax and total
    tax_amount = subtotal_after_discount * tax_rate
    print(f"Tax: {tax_amount}")
    total = subtotal_after_discount + tax_amount
    print(f"Total: {total}")

    # Return comprehensive summary
    return {
        'subtotal': subtotal,
        'discount': discount_amount,
        'tax': tax_amount,
        'total': total,
        'item_count': len(items)
    }

# Example order
order_items = [
    {'name': 'Laptop', 'price': 100, 'quantity': 2},
    {'name': 'Mouse', 'price': 200, 'quantity': 4}
]

summary = calculate_order_summary(tax_rate=0.15, discount=0.1, items=order_items)
print(f"Order total: ${summary['total']:.2f}")
print(f"You saved: ${summary['discount']:.2f}")




def calculate_price(item: str, price: float, quantity: int =1):
    """Calculate the total price for an item"""
    total_price = price * quantity
    return total_price

calculated_price = calculate_price(item='Laptop', price=float(input("Enter the price of the item: ")), quantity=int(input("Enter the quantity: ")))
print(f"Calculated price: ${calculated_price:.2f}")