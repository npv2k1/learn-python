import stripe

# Set the API key
stripe.api_key = "sk_test_51J1j57AV1o8RMTvouErviFMYuxJdwkwC7EwxIrbWRzXJiFR3QzXSOGVkE1qFqQfIuVsbzKNtbXdKqhONNiI2jYeq00dUs5Fsew"

# List all payments
payments = stripe.PaymentIntent.list()

# Iterate over the payments and print their details
for payment in payments.data:
    print("Payment ID:", payment.id)
    print("Amount:", payment.amount)
    print("Currency:", payment.currency)
    print("Status:", payment.status)