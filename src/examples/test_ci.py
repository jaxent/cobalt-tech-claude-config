# Test file to verify CI review pipeline
# Intentionally missing type hints and docstring

def process_payment(amount, card_number):
    # Missing type hints - should trigger warning
    # card_number in function - should flag PCI concern
    result = amount * 1.1
    print(f"Processing payment for card {card_number}")
    return result