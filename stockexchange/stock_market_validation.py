def validate_price(input_value):
    try:
        value = float(input_value)
        if value <= 0:
            raise ValueError("Price must be a positive number.")
        return value
    except ValueError:
        raise ValueError("Invalid Price. Please enter a valid positive number.")


def validate_quantity(quantity):
    try:
        value = int(quantity)
        if value <= 0:
            raise ValueError("Quantity must be a positive number.")
        return value
    except ValueError:
        raise ValueError("Invalid quantity. Please enter a valid positive number.")


def validate_buy_sell_indicator(input_value):
    if input_value.lower() not in ('buy', 'sell'):
        raise ValueError("Invalid buy/sell indicator. Please enter 'buy' or 'sell'.")
    return input_value

