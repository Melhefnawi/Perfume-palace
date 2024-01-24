# Testing

Return back to the [README.md](README.md) file.

## Code Validation

In this section I ran validation for all the code I produced in the project. I found bugs in the code and fixed them, in order for it to work optimally and pass the tests.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
![screenshot](media/base-html-test.JPG)

only one error appears as it shown in the above image, tried to fix it but couldn't find the location of the error in the code. moved all the charset in the meta at the top of the base template but still having the error. 
### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

![screenshot](media/base-css-test.JPG)

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.


![screenshot](media/base-js-test.jpg) 

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Checkout view.py

![screenshot](media/base-py-test.JPG)

#### product view.py

![screenshot](media/base-py-test-product.JPG)

#### profile view.py

![screenshot](media/base-py-test-profile.JPG)

#### bag view.py

![screenshot](media/base-py-test-bag.JPG)



## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.


 #### Mobile (DevTools)  
 
 Works as expected
 
 ![screenshot](media/mobile-view-01.JPG)  
 
 #### Tablet (DevTools) 

 Works as expected
 
 ![screenshot](media/lpad-view-01.JPG)
 
 
  
 
#### Desktop (DevTools) 

![screenshot](media/Deck-top-view-01.JPG)  



## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

#### Desktop view

Works as expected

 ![screenshot](media/lighthouse-desktop-view.JPG)

#### Mobile view

 Works as expected
 
 ![screenshot](media/lighthouse-mobile-view.JPG)

 
## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on Home link in Sign in page | Redirection to Home page | Pass | |
| | Click on Cancel link in Logout page | Redirection to Home page | Pass | |
| | Search bar display in every page and functionality | Search bar is displayed in every page as expected and functionality works as expected | Pass | When the search bar is clicked on but no characters (no query) is input in it and enter is pressed or the magnifying glass icon is clicked or tapped on, an error message will be generated, indicating the user to do so in order to search |
| About Us Page | | | | |
| | Click on About Us link in footer | Redirection to About Us page | Pass | |
| | Click on the Cancel link in the Newsletter page | Redirection to All perfumes page showing all perfumes for all Brands | Pass | |
| | Click on the Cancel link in the Add perfume (perfume management) page | Redirection to All perfumes page showing all perfumes for all Brands | Pass | |
| | Click on the Cancel link in the Edit perfume (perfume management) page | Redirection to All perfumes page showing all perfumes for all Brands | Pass | |
| | Click on the Keep shopping link in the perfume detail page | Redirection to All perfumes page showing all perfumes for all Brands | Pass | |
| | Click on the Keep shopping link in the Basket page | Redirection to All perfumes page showing all perfumes for all Brands | Pass | |
| | Click on a specific perfume card in the perfumes page | Redirection to the corresponding specific perfume detail page | Pass | |
| | Load images, names, prices, and rating for perfumes | All info is loaded as expected | Pass | |
| | Free delivery offer banner display | Free delivery offer banner is displayed as expected | Pass | |
| | Sort by bar display and functionality | Sort by bar is displayed as expected and functionality works as expected | Pass | |
| | Logged in as Superuser | Edit and Delete buttons will show | Pass | |
| perfume Detail Page | | | | |
| | Load image, name, price, quantity, platform, rating, available in other Brands, description and trailer for perfume | All info is loaded as expected | Pass | |
| | Click on the custom quantity buttons or the built in ones in the form, will adjust the perfume quantity that will be added to the basket | All quantity buttons work as expected | Pass | |
| | Click on Add to basket button | Effectively adds the perfume(quantity) to the shopping basket | Pass | A message will show at the top of the page to indicate the user they've added the perfume to the basket successfully |
| | Logged in as Superuser | Edit and Delete buttons will show | Pass | |
| Contact Us Page | | | | |
| | Click on Contact Us link in footer | Redirection to Contact Us page | Pass | |
| | Click on any of the Contact Us links in privacy policy modal | Redirection to Contact Us page | Pass | |

| Register | | | | |
| | Click on Register link in navbar, | Redirection to Register page | Pass | |
| | Enter valid first name | Field will accept free text format | Pass | |
| | Enter valid last name | Field will accept free text format | Pass | |
| | Enter valid username | Field will accept free text format | Pass | |
| | Enter valid email address (twice) | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on the Register button without requiered form values | An error will show on the form to indicate the user what's missing | Pass | |
| | Click on Register button | User is sent a confirmation email where they need to click on the link provided to confirm email | Pass | Information text will show on screen indicating the user they need to confirm their email address to complete the registration process |
| | Click on Confirm email link provided in confirmation email | User is redirected to the store page containing an information text indicating to click on the Confirm button to complete the process | Pass | |
| | Click on Confirm button | User is redirected to the login page | Pass | A message will show at the top of the page to inform the user they have confirmed the email address |
| | Click on Register button without requiered values | An error will show on the form to indicate the user what's missing | Pass | |
| Log In | | | | |
| | Click on the Login link in navbar | Redirection to Login page | Pass | |
| | Enter valid username | Field will accept free text format | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | A message will show at the top of the page to indicate the user they've logged in successfully |
| | Click Login button with wrong data | An error will show on the form to indicate the user what's wrong | Pass | |
| | Click on the Forgot password link | Takes user to the Password reset page to enter their email address and receive an email with a password reset link | Pass | |
| Log Out | | | | |
| | Click on the Logout link in navbar | Redirection to Logout page | Pass | A confirmation text will be displayed on screen asking the user if they're sure they want to log out |
| | Click Sign out button | Logs out user and redirects user to home page | Pass | A message will show at the top of the page to indicate the user they've logged out successfully |
| Add perfume Page | | | | |
| | Click on perfumes Management link in navbar | Redirection to Add perfume page | Pass | |
| | Add perfume form load | Loads a form with all the corresponding fields to add a new perfume | Pass | |
| | Click on Add perfume button | New perfume will be created and user redirected to the newly created perfume detail page | Pass | A message will show at the top of the page to indicate the user they've added the perfume successfully |
| | Click on Add perfume button without requiered values for perfume | An error will show on the form to indicate the user what's missing | Pass | |
| | Brute forcing the URL to get to Add perfume page without logging in first | User will be redirected to Login page | Pass | |
| | Brute forcing the URL to get to Add perfume page logged in not as a Superuser | User will be redirected to Home page and an error will show at the top of the page to indicate the user that only store owners can do that | Pass | |
| Edit perfume Page | | | | |
| | Click on Edit button for a perfume in perfumes page | Redirection to Edit perfume page | Pass | |
| | Click on Edit button for a perfume in perfume detail page | Redirection to Edit perfume page | Pass | |
| | Edit perfume form load | Loads a form with all the corresponding fields(prefilled with the existing data) for the perfume | Pass | |
| | Click on Update perfume button | perfume will be updated and user redirected to the newly updated perfume detail page | Pass | A message will show at the top of the page to indicate the user they've updated the perfume successfully |
| | Click on Update perfume button without requiered values for perfume | An error will show on the form to indicate the user what's missing | Pass | |
| | Brute forcing the URL to get to Edit perfume page without logging in first | User will be redirected to Login page | Pass | |
| | Brute forcing the URL to get to Edit perfume page logged in not as a Superuser | User will be redirected to Home page and an error will show at the top of the page to indicate the user that only store owners can do that | Pass | |
| Delete perfume Page | | | | |
| | Click on Delete button for a perfume in perfumes page |  Delete perfume  | Pass | A confirmation text will be displayed on screen confirm the delete of the perfume |
| | Click on Delete perfume button | Existing perfume will be deleted and user redirected to perfumes page | Pass | A message will show at the top of the page to indicate the user they've deleted the perfume successfully |
| | Brute forcing the URL to get to Delete perfume page without logging in first | User will be redirected to Login page | Pass | |
| | Brute forcing the URL to get to Delete perfume page logged in not as a Superuser | User will be redirected to Home page and an error will show at the top of the page to indicate the user that only store owners can do that | Pass | |
| Basket Page | | | | |
| | Click on basket link in navbar | Redirection to Basket page | Pass | |
| | Basket link in navbar | Basket link in navbar changes color, slightly increases size and shows amount if perfumes in it when perfumes are added to it | Pass | |
| | Basket page loads data | Basket page loads perfumes information, subtotal, delivery cost and grand total | Pass | |
| | Click on the custom quantity buttons or the built in ones  | Click on the custom quantity buttons or the built in ones in the form, will adjust the perfume quantity that will be updated in the basket, all quantity buttons work as expected | Pass | |
| | Click on the Remove button | Click on the Remove button will remove the perfume(all its quantity) from the basket | Pass | |
| | Free delivery information text | Free delivery information text will display should the user not reach the free delivery threshold | Pass | The information text will indicate the user exactly how much more they need to spend to avail of free delivery |
| | Click on the Secure checkout button | Click on the Secure checkout button will redirect the user to the checkout page | Pass | |
| | Empty basket | Click on basket link in navbar when the basket is empty, user will be redirected to Basket page and an information text will display on screen to indicate the user that they have no perfumes in their basket | Pass | |
| Checkout Page | | | | |
| | Checkout page loads data | Checkout page loads a form for the user to fill out to complete the order and a summary (total quantity) of the perfumes (images, quantity, name, platform, subtotal) in the order and the order total, delivery cost and grand total | Pass | Should the user be logged in, the fields in the form will be prefilled with the user's information stored in the user and user profile objects |
| | Save information checkbox | When a logged in user checks the save info box, their information will be stored in user profile for future transactions | Pass | Should the user not be logged in, an information text with calls to action links to Create an account (register) or login to save this information, will be displayed on screen instead |
| | Click on the adjust basket button | Redirection to basket page | Pass | |
| | Click on the Complete order button without requiered form values | An error will show on the form to indicate the user what's missing | Pass | |
| | Click on the Complete order button | Processes the payment and redirection to checkout success view | Pass | |
| | Card charges text | Information text will be displayed at the end of the form, indicating exactly how much the user's card will be charged | Pass | |
| | Brute forcing the URL to get to Checkout page with an empty basket | User will be redirected to perfumes page | Pass | An error will show at the top of the page to indicate the user that there's nothing in their basket at the moment |
| Checkout Success Page | | | | |
| | Checkout success page loads data | Checkout success page loads the completed order information to indicate the user that the order is confirmed, it contains the order number and date, the details of the perfumes in the order, delivery information and billing information | Pass | A message will show at the top of the page to indicate the user the order successfully processed, showing the order number and indicating that a confirmation email will be sent to the email provided during checkout |
| | Thank you text | Information text will be displayed at the top of the order information summary, thanking the user for their purchase | Pass | |
| | Click on the Check out all our perfumes button | Takes the user to All perfumes page | Pass | |
| | Brute forcing the URL to get to Checkout success page of their own or a different user's order | User will be redirected to Basket page | Pass | An error will show at the top of the page indicating the user that they can only access this page after completing a purchase |
| Profile Page | | | | |
| | Profile page loads data | Profile page loads a form with the user profile fields for the user to fill out and a table with the user's order history (none if no transactions have been completed) | Pass | Should the user have completed previous transactions and saved their information during the process then these fields will be prefilled because the information will be attached to their user profile |
| | Click on Update information button | Existing user profile will be updated | Pass | A message will show at the top of the page to indicate the user the profile updated successfully, no field in this form is required hence the user can update/delete information in their profile at will |
| | Order history table | If the user has completed previous transactions, information pertaining to those transactions will be displayed on the order history table, showing order number(cropped), order date, perfumes purchased and order total | Pass | The order number is hoverable (shows user full order number) and clickable, allowing the user to go to that order history on click |
| | Brute forcing the URL to get to Profile page as a logged out user | User is redirected to login page | Pass | |
| Order History Page | | | | |
| | Click on order number on order history table in profile page | Redirection to Order history page | Pass | |
| | Order history page loads data | Order history page loads the same data as in Checkout success page given that the same template is used | Pass | The difference in this page is that a message will show at the top of the page to indicate the user that this is a past confirmation for the order number and that a confirmation email was sent on the order date, also a Back to profile button will show instead of a Check out all our perfumes button |
| | Click on Back to profile button | Redirection to Profile page | Pass | |
| | Brute forcing the URL to get to Order history Page without logging in first or when logged in, to get to Order history Page of a different user | User will be redirected to Home page and an error will show at the top of the page to indicate the user that they do not have permission to view this order history | Pass | |
| Footer | | | | |
| | Click on footer links | All footer links work correctly | Pass | External links in footer open in new page |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a site user, I would like to register for an account, so that I can  login and out with personal account and recover my password in case I forget it. | Done |
| As a site user, I would like to view a list of perfumes, so that I can select one or more to purchase. | Done |
| As a site user, I would like to view an individual perfume, so that I can identify its name, price, image, genre, description, year, platform, pegi rating, trailer video and likes count. | Done |
| As a site user, I would like to search for a specific perfume name or genre, so that I can easily find the perfume I want to purchase. | Done |
| As a site user, I would like to sort perfumes by price, genre, name, pegi rating and popularity, so that I can easily find the perfumes according to my preferences. | Done |
| As a site user, I would like to add, view, update and delete perfumes in the shopping basket, so that I can manage/review my shopping basket before proceeding to checkout. | Done |
| As a site user, I would like to provide the necessary billing/delivery details, so that I can purchase perfumes and view an order confirmation after checkout to verify all the information from my purchase is accurate. | Done |
| As a site user, I would like to receive an email confirmation after my purchase, so that I can keep records of my transactions. | Done |
| As a site user, I would like to create/manage my personal account profile, so that I can view/update my profile, view my order history and save my payment information. | Done |
| As a site user, I would like to contact the site administrator, so that I can query/recommend the site admin on different topics. | Done |
| As a site user, I would like to subscribe to a newsletter, so that I can receive news, special offers and general information related to the store. | Done |
| As a site user, I would like to navigate to the site's about us, terms & conditions and privacy policy links, so that I can inform myself in more depth about the site. | Done |
| As a site administrator, I should be able to create/add, read, update and delete perfumes, so that I can manage the perfumes on the site. | Done |
| As a site administrator, I should be able to add, update and delete Brands, so that I can assign Brands to perfumes. | Done |
| As a store owner, I should be able to add/edit/delete perfumes from the website, so that I can manage new perfumes, perfumes updates or perfumes that are no longer available. | Done |


## Bugs

| Language/Bug | To fix bug | Before Screenshot | After Screenshot |
| --- | --- | --- | --- |
| Python - Failed to sort by brand name. | had to update the view in the product app to seach by the brand and during these steps, another bug appears that i had to split the get method, to be able to sort with the brand name.  | Fixed |
| Django - giving 500 error while deploying in Heroku. | I had to update the settings with the correct variables to initiate the gmail and the stripe, and avoid the 500 error | Done |
| Django - undeployed migrations. | after importing the country field to the model, there was a migrations problem that cease the whole migration process, after contacting the tutor support, i had to delete all the migrations and rebuild the checkout model and deploy my migration once again. | Fixed |

| Python - `E501 line too long` (90 > 79 characters). | This error replicated along all my python files. To fix it, I followed my mentor's suggestion which was to press enter right after the first bracket so I didn't have to 'guess' where the proper indentantion was. | Fixed |

## Unfixed Bugs

-  `Email confirmation` 

  - Attempted fix: I tried to register from heroku and the project but wasn't able to get a confirmation email. I had to confirm the email by copying the confirmation link and paste it in the url, to be directed to the confirm email page and confirm email. 
