# [Cart] Price calculation in the cart.

## The test verifies whether the price in the cart is recalculated after increasing the number of pieces of the product.

https://skleptest.pl

## Preconditions:

* Skleptest.pl website is open.
* At least one product added to the cart.

# Steps

|   | Action                                                 | Input | Expected Result                                          |
|---|--------------------------------------------------------|-------|----------------------------------------------------------|
| 1 | Click `My Cart` button.                                |       | The user is redirected to cart view.                     |
|   |                                                        |       | Url change: https://skleptest.pl/cart/                   | 
| 2 | Click the `+` button three times in `Quantity` column. |       | The number of products in the quantity column increases. |
| 3 | Click `UPDATE CART` button.                            |       | The price in the cart changes (increases).               |
| 4 | Click `-` button three times in `Quantity` column.     |       | The number of products in the quantity column decreases. |
