count_orders = int(input())
total_price = 0.0

while count_orders > 0:
    price, days, capsules = float(input()), int(input()), int(input())
    price_coffe = 0

    if not any(
            [
                not (0.01 <= price <= 100),
                not (0 < days < 32),
                not (0 < capsules < 2001)
            ]
    ):
        price_coffe = price * days * capsules
        print(f"The price for the coffee is: ${price_coffe:.2f}")
    #     count_orders -= 1
    #     continue
    #
    # price_coffe = price * days * capsules
    # print(f"The price for the coffee is: ${price_coffe:.2f}")

    total_price += price_coffe

    count_orders -= 1

print(f"Total: ${total_price:.2f}")