import requests
import json





def add_review(product_name, rating, review_text):
    review = {
        "product_name": product_name,
        "rating": rating,
        "review_text": review_text
    }

    result = requests.post(
        'http://127.0.0.1:5000/addreview',
        headers={'content-type': 'application/json'},
        data=json.dumps(review)
    )

    return result.json()






# Ask user if they want to add a review
#If no then user can continue shopping
#if yes then user can write a review
def ask_for_review():
    while True:
        choice = input("Do you want to add a review? (yes/no): ").lower().capitalize()
        if choice == 'Yes':
            product_name = input("Enter the product name: ").capitalize()
            rating = int(input("Enter the rating (1-5): "))
            review_text = input("Enter your review: ")
            add_review(product_name, rating, review_text)
            break
        elif choice == 'No':
            print("No review added.")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")








ask_for_review()