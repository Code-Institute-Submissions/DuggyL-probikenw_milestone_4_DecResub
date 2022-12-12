# Probike North Wales - Milestone Project 4

View live project here. [view](https://probike-nw.herokuapp.com/)

## Demonstration Accounts

To enable you to test the website functionality, a number of demo accounts, products, and, transactions have been created. 

| Email | Password | Desription |
| ----- | -------- | ---------- |
| admin | mile5tone4 | Admin account with create and update permissions to all custom models. |
| customer | mile5tone4 | Customer account for testing. |

# Design Brief
This is a Full Stack Frameworks (Django) project for Code Institute to demonstrate what I have learned throughout the course so far. I chose to develop an ecommerce shopping website for the local Motorcycle Training School base in North Wales (Deeside). 

The idea of the project is that Probike rents equipment to students during training and consistently asks by students what equipment they should buy for riding. After seeing an influx of new riders around the country especially in North Wales, the owner of Probike saw an opportunity to branch out from motorcycling training and offer to sell motorcycle apparel directly to students or anyone looking to buy motorcycling gears.

An online ecommerce (B2C) business specialising in motorcycling gears including helmets, clothes and maybe more in the future. Upon entering the website, from browsing products to checkout, the owner wants a website to offer a smooth and easy online shopping experience. The website also handled customer payment, which dealt with sensitive customer information which required an approach with a security conscious perspective.

There are a number of features due to time constraints that were not possible to implement at this point in time. But I believe I produced an ecommerce application that has met Probike owner requirements with more room to expand in the future. 

## As a shopper
- As a shopper, I can view a list of products.
- As a shopper, I can view individual product details.
- As a shopper, I can identify the product's name, descriptions, ratings, images, prices and available sizes. So I can make informed decisions before purchasing.
- As a shopper, I can select products to purchase.
- As a shopper, I can easily view the total of my purchases at any time. 
- As a shopper, I can easily register for an account, allowing myself to access my account containing personal details and order history and save my payment information.

## As a shopper, sorting and searching
- As a shopper, I can sort the list of available products.
- As a shopper, I can sort a specific category of products. I can find the best-priced or best-rated products in specific categories or sort the products in that category by name.
- As a shopper, I can search for a product by name or description.
- As a shopper, I can easily see the products I’ve searched for and the number of results.

## As a shopper, purchasing and checking out
- As a shopper, I can easily select the size and quantity of a product when purchasing it. Ensure I don’t accidentally select the wrong product, quantity or size.
- As a shopper, I can view items in my bag to be purchased.
- As a shopper, I can adjust the number of individual items in my bag, allowing me to make changes to my purchase before checkout.
- As a shopper, I can effortlessly enter my payment information. Checkout is quick and with no hassles.
- As a shopper, I can feel confident my personal and payment information is safe and secure. 
- As a shopper, I can view an order confirmation after checkout.
- As a shopper, I can see order history after checkout and confirmation of what I’ve purchased on my purchase history. 

## As store owner, admin and store management
- As a store owner, I can add, delete, and edit products on my store. I can change product names, descriptions, images, prices and other product criteria.

## Design
Using Code Institute Boutuqe Ado project as baseline, I opted for a simple design, where the products themselves are the focus. And there aren't too many graphics cluttering and detract visitors. 

## Colour Scheme
The two main primary colours used are blue & white.
The colours scheme of this project is according to Probike corporate identity guidelines. Any combinations of colours I used throughout the project is to emphasise colour contrast and prioritise readability.

## Typography
I used sans-serif Google Fonts “Montserrat” throughout the webpage to maintain cohesion across the project. Using different font weights (from Thin to Black) to convey emphasis and importance on some of the content. It has high readability and ease of scaling make Montserrat a suitable typeface for web pages. 

## Database model and wireframe
- Database diagram [view](https://probike-nw.herokuapp.com/)
- Homepage wireframe [view](https://probike-nw.herokuapp.com/)
- Mobile wireframe [view](https://probike-nw.herokuapp.com/)
- Tablet wireframe [view](https://probike-nw.herokuapp.com/)

# Features

## Homepage
- The homepage greets visitors with a big hero image of a motorcycle racer, an idea to draw attention as soon as they open the site. The homepage is deliberately kept simple and communicates with visitors directly using a single image letting visitors know what this website is about. A big button to invite shoppers and see what the store has to offer.

## Product / Product Details Page
- The categories of products are bold and obvious, for the shopper ease of navigation to browse products of their choice. In order to make the products take centre stage, I chose to display the product as big as possible on all screen sizes. The name of the products are big and easy to read, right below the name, all the information the shoppers need at first glance. By clicking on the products images, will lead to the product details page for more information about products.
- The options to select size and quantity will not appear if selected product run out of stock. The product page details page will inform the shopper of how many the store currently have in stock, if the stock is 0 it will say  “out of stock”. The ‘add to cart’ button will place the selected item into the shopping cart. 

## Navigation Bar
- The Navigation bar at the top of all pages maintains a consistent look across the website. It contains links to homepage, login, profile, search bar, and shopping basket if the shoppers are already logged in. 

## Login Page
- Only available when the user is not logged in. The login link in the navbar will direct the user to the login page where they can login or register a new account.

## Profile Page
- User profile can be clicked from the navbar. This will only be available to visitors who are logged in. The profile page contained visitors' information and ordered history. 
- Only available to logged in users. Clicking on the username will present the user with two options; Profile and Logout. Profile will direct the user to the user's profile area and Logout will log the user out and direct them to a logout page notifying the user they have been logged out and offer an option to sign in again.
- Shoppers can view their order history in the Orders History section, and update their personal information.

## Shopping Cart
- Only available to logged in users. Clicking the cart will direct the shoppers to the cart page providing there are items in the users cart, otherwise they will receive an alert. The number of items within the user's cart is visible next to the cart icon.
- Users can view their shopping cart which will list all items they have ‘Added to cart’, including quantity and a total price for all items. User can adjust the quanity of items in their cart or remove completely.

## Checkout
- In the checkout section, users will fill in their delivery details further checkout sections to be included. A list of items to be purchased is also found beside form as well as an order total. The users inout their address, the address will be saved for future use. User cannot proceed to the payment section until all field of delivery address have been complete.

## User notification
- Users will receive alerts throughout this site for various actions, including adding items to cart, removing items from cart, updating profile page, saving address, password change etc.

## Payment
- User can purchase their items using the Stripe payment platform.

## Payment Success
- User will be directed to the 'order success' page when they purchase an item.

## Features to add
- Create a star rating system for each product.
- Shoppers can review the product in details and post it on the website. (Required moderation team to monitor what been post.)
- Create a wishlist for customers to add their favourite products. (Maybe email shoppers if their favourited products currently in discount.

## Testing
The JSHint Lighthouse, W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no errors in the project.

- Found 9 functions with same 2 warnings regarding browser extension. link
- HTML Validator found 1 error from Materialize jQuery preset. link
- CSS Validator found 1 error from Materialize css preset. link
- Python PEP8 online found 2 error regarding expected lines

### Manual Testing

| # | Test | Test Criteria | Result |
|---|------|--------|------|
| 1 | Click logo in Navbar | Take user to homepage | YES |
| 2 | Click ‘Login’ (when not logged in) in Navbar | Take user to login section | YES |
| 3 | Click ‘Account’ (when logged in) in Navbar | Dropdown showing profile, logout options and product management (supersuer) | YES |
| 4 | Click ‘Product Management’ in Navbar (superuser) | User taken to product mManagement page | YES |
| 5 | Click ‘My Profile’ (when logged in) in Navbar | User taken to profile page | YES |
| 6 | Click ‘Logout’ (when logged in) in Navbar | User logged out | YES |
| 7 | Click ‘All Products’ in Navbar (normal user) | Dropdown showing categories of products | YES
| 8 | Click shopping bag icon in Navbar (when logged in and no items have been added to bag) | Users receive alert ‘No items in your bag’ | YES |
| 9 | Click shopping bag icon in Navbar (when logged in and there is items added to bag) | Users are directed to bag page where they can view their order | YES | 
| 10 | Click inside search bar in Navbar | Allows user to type and search | YES |
| 11 | Click ‘Motocyle Clothing’ category link on homepage | Dropdown showing motocyle clothing sub-categories | YES |
| 12 | Click ‘Motocyle Helmets’ category link on homepage | Dropdown showing motocyle helmets sub-categories | YES |
| 13 | Click on any sub-category link on homepage | Directs user to selected sub-categories page | YES |
| 14 | Clicking on any product | Directs user to correct product information page | YES |
| 15 | Clicking ‘Add to bag’ button | Adds 1 relevant item to the users bag | YES 
| 16 | Clicking ‘Add to bag’ button | Users receives alert ‘Item added to bag | YES |
| 17 | Clicking ‘Add to bag’ button when item is already in bag | Users receives alert ‘The number of items have been updated’ | YES
| 18 | Clicking ‘Save changes’ button in profile page | Saves any updates to profile page | YES |
| 19 | Clicking 'Save changes' button in profile page | Users receive alert ‘Your profile has been updated successfully!’ | YES |
| 20 | Clicking ‘+’ button in bag page on selected product | Item within bag is increased by 1 | YES |
| 21 | Clicking ‘-’ button in bag page on selected product | Item within bag is decreased by 1 | YES |
| 22 | Clicking ‘Update’ below quantity number field in bag page | Users receive alert confirmation ‘{item.name} quantity updated’ | YES | 
| 23 | Clicking ‘Remove’ below quantity number field in bag page | Users receive alert ‘{item.name} removed’ | YES |
| 24 | Clicking ‘Remove from bag’ button in bag page | The selected item is removed from the user bag | YES |
| 25 | Clicking ‘Remove from bag’ button in bag page | Users receive alert ‘Item removed from bag’ | YES |
| 26 | Clicking ‘Continue Shopping’ button in bag page | Users directed to homepage | YES | 
| 27 | Clicking ‘Checkout’ button in bag page | Users directed to checkout page | YES |
| 28 | Clicking ‘Update Information’ button in checkout page | ‘Proceed to Checkout’ button becomes available to press | YES |
| 29 | Clicking ‘Update Information’ button in ‘Profile’ page | Users receive alert ‘Success! Your profile updated successfully’ | YES | 
| 30 | Clicking ‘Complete Order’ button in checkout page(when not complete) | Users receive alert ‘Please fill in this field’ | YES |
| 31 | Clicking ‘Complete Order’ button in checkout page | Only works if address fields have been completed | YES |
| 32 | Clicking ‘Secured Checkout’ button in checkout page | Directs user to payment page | YES | 
| 33 | Entering stripe test card payment details with valid email address and click on ‘Complete Order’ button | Order processes successfully and user directed user order confirmation page | YES | 

## Mobile / Tablet Devices:
The website was tested for responsiveness using Google/Firefox Chrome Developer Tools.
- Galaxy S10
- Galaxy S20
- Galaxy Note
- iPhone X Pro/Max
- iPhone 11 Pro/Max
- iPhone 12 Mini/Pro/Max
- iPhone 13 Mini/Pro/Max
- iPad
- iPad Pro

## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- Frameworks
- Bootstrap
- JQuery
- Font Awesome
- Django
- Django-allauth
- Django-crispy-forms
- Third-party services
- Stripe
    - This is used to securely process customer payment details. No payment data is handled or stored by the application, it is all handled by Stripe. This makes for easy and secure integration and verification of payments.

## GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
2. At the top of the Repository locate the "Settings".
3. Click on "Pages" will open "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. At the top near github header to locate the now published site [link](https://duggyl.github.io/chef-dicson-milestone-project-1/).

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository.
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository.
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied.

## Credits
### Code
- This project is heavily based on Code Institute Boutique Ado tutorials.
- Other tutorials I used to help me completed the project:
    - Udemy Course: Django with React | An Ecommerce Website by Dennis Ivy & Brad Traversy.
    - Udemy Course: Build Ecommerce Website to Master Django and Python by The Zero2Launch Team.

### Media
- All images provided by Probike NW
- Main image and testimonial banner were found on istockphoto.com
- Montserrat fonts provided by Google Fonts
- Logo icons by Fontawesome
- Images used in readme were screenshot from W3 Validators and Am I Responsive

### Acknowledgements
- Stack Overflow developers on the questions forum who provided helpful tips and solutions.