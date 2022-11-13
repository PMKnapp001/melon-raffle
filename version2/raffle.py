"""Randomly pick customer and print customer info"""

from random import choice
import customers

def pick_winner(pool):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(pool)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    pool = customers.get_customers_from_file("customers.txt")
    pick_winner(pool)

print("V2")
run_raffle()