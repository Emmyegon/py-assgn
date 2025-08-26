
def calculate_discount(price, discount_percent):
 
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
try:
    # Prompt user for original price
    original_price = float(input("Enter the original price of the item: $"))
    
    # Prompt user for discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display the results
    print("\n" + "="*40)
    if discount_percent >= 20:
        discount_amount = original_price - final_price
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Applied: {discount_percent}%")
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Final Price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied (discount was only {discount_percent}%)")
        print(f"Final Price: ${final_price:.2f}")
        
except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
    
    # # def calculate_discount(price, discount_percent):

# #     if discount_percent >= 20:
# #         discount_amount = price * (discount_percent / 100)
# #         final_price = price - discount_amount
# #         return final_price
# #     else:
# #         return price

# # # Get user input
# # try:
# #     original_price = float(input("Enter the original price of the item: $"))
# #     discount_percent = float(input("Enter the discount percentage: "))
    
# #     # Calculate final price
# #     final_price = calculate_discount(original_price, discount_percent)
    
# #     # Display results
# #     if discount_percent >= 20:
# #         print(f"\nOriginal Price: ${original_price:.2f}")
# #         print(f"Discount Applied: {discount_percent}%")
# #         print(f"Final Price after discount: ${final_price:.2f}")
# #     else:
# #         print(f"\nNo discount applied (discount was only {discount_percent}%)")
# #         print(f"Final Price: ${final_price:.2f}")
        
# # except ValueError:
# #     print("Error: Please enter valid numbers for price and discount percentage.")


# def calculate_discount(price, discount_percent):
  
#     if discount_percent >= 20:
#         # Calculate discount amount and subtract from original price
#         discount_amount = price * (discount_percent / 100)
#         final_price = price - discount_amount
#         return final_price
#     else:
#         # Return original price if discount is less than 20%
#         return price
    
    
# def main(price, discount_percent):
#     if discount_percent >= 20:
#         # Calculate discount amount and subtract from original price
#         discount_amount = price * (discount_percent / 100)
#         final_price = price - discount_amount
#         return final_price
#     else:
#         # Return original price if discount is less than 20%
#         return price