# Possibility to change the number of products in the cart.

## The test checks whether it is possible to change the quantity of each product on the shopping cart screen. 

https://skleptest.pl 

# Preconditions:
* The website skleptest.pl is open
* At least one product has been added to the cart.

## Steps

|| Action | Input | Expected Result |
|----|--------|-------|-----------------|
|1|Click `My Cart` button.|| |The user is redirected to cart view.
|||| |Url change: https://skleptest.pl/cart/| 
|2|Click `+` button.|| |The quantity of the product in the cart will increase.|