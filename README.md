# Table of Contents


- [Table of Contents](#table-of-contents)
  - [Perfume Palace Store](#perfume-palace-store)
  - [User Stories](#user-stories)
    - [Site Users](#site-users)
    - [Site Admin](#site-admin)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Tools \& Technologies Used](#tools--technologies-used)
  - [Agile Development Process](#agile-development-process)
    - [GitHub Projects](#github-projects)
    - [GitHub Issues](#github-issues)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [Ecommerce Business Model](#ecommerce-business-model)
  - [Search Engine Optimization (SEO) \& Social Media Marketing](#search-engine-optimization-seo--social-media-marketing)
    - [Keywords](#keywords)
      - [Final AWS Setup](#final-aws-setup)
    - [Stripe API](#stripe-api)
    - [Gmail API](#gmail-api)
    - [Heroku Deployment](#heroku-deployment)
    - [Local VS Deployment](#local-vs-deployment)
  - [Credits](#credits)
    - [Content](#content)

## Perfume Palace Store

Perfume Palace Store, is an ecommerce site designed to provide perfumes of all kinds and brands, visitors of the site can find information about all types and kinds of perfumes, purchase them and get best deals of the most famous brands they want to. What makes Perfume Palace Store special is the fact that this store is providing the latest and the newest perfumes.

We give our users a place where they can look for perfumes and find information about them such as brand, description, ratings, and of course competitive price. Our user can create their own profiles and save their information securely in our database for future transactions or they can simply purchase their perfumes as guest users.

Store owners/admins can administer the site from the user interface, they have the option to add, edit and delete perfumes as well as have access to the recieved messages and their corresponding information in the contact us section.

![screenshot](documentation/am-i-responsive.png)


## User Stories

### Site Users

- As a Site User I would like to register for an account so that I can login and out with personal account and recover my password in case I forget it. 
- As a Site User I would like to view a list of perfumes so that I can select one or more to purchase. 
- As a Site User I would like to view an individual perfume so that I can identify its name, price, image, description, year, platform and rating. 
- As a Site User I would like to search for a specific perfume name so that I can easily find the perfume I want to purchase. 
- As a Site User I would like to sort perfume by price, description, name, and rating so that I can easily find the perfume according to my preferences. 
- As a Site User I would like to add, view, update and delete perfume in the shopping basket so that I can manage/review my shopping basket before proceeding to checkout. 
- As a Site User I would like to easily view the total amount of perfumes in my shopping basket so that I can know how many perfumes are there in my basket at all times. 
- As a Site User I would like to provide the necessary billing/delivery details so that I can purchase perfume and view an order confirmation after checkout to verify all the information from my purchase is accurate. 
- As a Site User I would like to receive an email confirmation after my purchase so that I can keep records of my transactions. 
- As a Site User I would like to create/manage my personal account profile so that I can view/update my profile, view my order history and save my payment information. 
- As a Site User I would like to contact the site administrator so that I can query/recommend the site admin on different topics. 
- As a Site User I would like to subscribe to a newsletter so that I can receive news, special offers and general information related to the store.
- As a Site User I would like to navigate to the site's about us, terms & conditions and privacy policy links so that I can inform myself in more depth about the site. 
- As a Site User I would like to receive an email every time a new perfume is added to the store so that I will be up to date with what perfumes are available. 
### Site Admin

- As a site administrator, I should be able to create/add, read, update and delete perfume so that I can manage the perfumes on the site, 
- As a site administrator, I should be able to add, update and delete  ratings so that I can assign ratings to perfumes, 
- As a site administrator, I should be able to add, update and delete platforms so that I can assign platforms to perfumes, 
- As a site administrator/site owner, I should be able to add/edit/delete perfumes from the website so that I can manage new perfumes, perfumes updates or perfumes that are no longer available, 



## Features

### Existing Features

- **Navagation Bar**

  - The navigation bar is located at the top of the screen and it's centered both vertically and horizontally. It has the site logo on the left side and the search bar in the center, below these two elements we find the navigation links for Home, About Us, all perfumes (dropdown menu), category(dropdown menu), special offers.
  - The navigation bar is fully responsive thanks to the use of Bootstrap, also the layout changes to expandable and fully vertical once small screens are used.
  - When small screens are used the search icon is clickable and once clicked on, it drops down a search bar.
    
    - The navigation menu is identical across all the pages on the site which provides quick navigation learning.

![NavBar](documentation/nav-bar.png)

- **Home/Index**

  - The home page welcomes the user (new or returning) to the site, it subtly and intuitively shows the user what the site is about  and what it offers, which is a site about perfume where users can easily find perfume for different brands, price, and categories, giving them as well a call to action button to start shopping. 

![Home](documentation/home.png)

- **Register**

  - The register page allows the user as its name indicates to register to the site. The user needs to supply a first name, last name, username, email and confirm email, password and confirm password, once the sign up button is clicked on, the user will be shown a message indicating a confirmation email has been sent to the email provided and that they need to confirm their email in order to complete the registration process.
  - The register page also provides a link for the user to go to the login page in case they're already registered as well as a back to login button.
    - This functionality is achieved thanks to the power of Django allauth.

![Register](documentation/register.png)

- **Register confirmation email**

  - Once the user is registered a confirmation email is sent to the email address provided, when the user clicks on the link provided in the confirmation email, the user is taken back to the site with a confirm email message, once the user clicks confirm, a success message is displayed and the user is taken to the login page.

![Register confirmation email](documentation/sign-up-email-confirmation.png)

- **Login**

  - The login page allows a registered user to login with their username and password.
  - The form contains a checkbox which is unchecked by default, this option will allow the user to remember their session or not.
    - Once logged in, the user can avail of the features that an authenticated user is allowed, such as create their own profile, view their order history and like perfumes.
    - Should the user not be registered yet, the option to do so is provided at the top of the form with a link.
  - At the the bottom of the form the user has 2 buttons, one to login and another to go home.
  - If the user forgot their password they have the option to reset it via a link provided at the end of the form.
    - As all the forms in the site, the login form was design to provide optimal UX.

![Login](documentation/login.png)

- **Logout**

  - The logout page allows a logged in user to logout.
  - A confirmation question will asked to the user before logging out.
  - There are two buttons at the bottom, one to confirm the logout action and one to cancel which will bring the user back home.

![Logout](documentation/logout.png)


![About-Us](documentation/about-us.png)

- **Product**

  - The product page is where the perfume of the store is selling are displayed, they're displayed in cards that contain the perfume image, name, price.
  - Thanks to bootstrap for large screens the cards are laid out in rows of four columns, for medium screens in rows of three columns and for small in rows of one column.
  - At the top of the screen a free delivery banner is shown to the user to let them know that delivery is free once they spend €30 or more.
  - After the free delivery offer banner, we find the heading and a series of badges indicating the available perfume groups by platform, should the user click on one of them, they will be brought to the perfume page filtered by the specific platform perfume group.
  - Next on the left side, there is a 'All product' link which will bring the user back to 'all perfume' meaning all perfume will be displayed without sorting or filtering. 
  - On the right side there is a 'Sort by' drop down menu that allows the user to sort the perfume  by price (low-high, high-low), name (low-high, high-low), rating (low-high, high-low), and category (A-Z, Z-A), thanks to a combination of python code in the view and Django template logic.


- **Perfume detail**

  - The perfume detail page shows the user all the perfume's attributes.
  - At the top of the screen the free delivery banner is displayed again the same as in the home page.
  - Next we find on the left of the screen the perfume's image and on the right side the name, price, quantity which can be adjusted by the user thanks to JS, a button to keep shopping which will bring the user back to 'all perfume' and a button to 'add to basket' which will indeed add the perfume to the basket.
  
  

- **Shooping basket**

  - The shopping basket page is where the user will put all the perfumes they want to purchase before proceeding with the checkout process.
  - Once a perfume is added to the basket the basket icon in the navbar will change in color, slightly in size and will show the amount of perfume in it at any given page the user decides to go.
  - In the basket page we see two headings, one to indicate it is the 'shopping basket' and the other one 'product info'.
  - The product info section is where all the info for the perfumes added to the basket will be, this section was built as a table for large and medium screens and with bootstrap rows and columns for small screens.
  - The product info section shows the perfume image, its name, price, quantity which can be adjusted by the user thanks to JS and the subtotal for that particular perfume (based on quantity).
  - Below the quantity amount there are two buttons one to update the quantity should the user decides to change it and one to remove the perfume altogether from the basket.
  - Next the user can see the 'basket total', the 'delivery' cost should there be any and the 'grand total' which is what the user will ultimately pay. Below the 'grand total' there will be a message for the user is the 'basket total' is below the free delivery threshold, this message will let the user know exactly how much more they will need to spend to avail of the free delivery offer.
  - Lastly there two buttons, one to 'keep shopping' which will bring the user back to 'all product' and one for 'secure checkout' which will take the user to the checkout page to start the checkout process.

![Shooping basket](documentation/shopping-basket.png)

- **Shooping basket empty**

  - Should the shopping basket be empty, a paragraph letting the user know will be displayed and there will be a button to 'keep shopping' which will take the user to 'all perfumes' page.

![Shooping basket empty](documentation/shopping-basket-empty.png)

- **Checkout**

  - The checkout page is where the user will input their delivery/payment details to complete the order.
  - Checkout is comprised by two sections, one is a form where the user will input their details such as full name, email address, phone number, street address, town, county, postal code, country, and card details, Should the user be registred and logged in, full name and email address will be prefilled and if they saved/updated their profile information the rest of the fields will also be prefilled (except for the card details). At the end of the form there will be two buttons and a message for the user. One button is to 'adjust basket' which brings the user back to the shopping basket and the other is to complete the order and the message is to indicate the user excatly how much their card will be charged.
  - The 'save info' checkbox in the form right after 'country' field, is for the user to save their info in their profile for future transactions and it is checked by default, in the case the user is annonymous then a message will show instead letting the user know that in order to save their info they need to register/login.
  - The second section will contain the order summary indicating the amount of perfume in the order, the perfume or perfumes name, platform, quantity and subtotal and lastly the 'order total', 'delivery' cost and 'grand total'.

![Checkout](documentation/checkout.png)

- **Loading spinner**

  - Once the user clicks on complete order, while the backend code and the stripe API do their job to process the payment, the user will see a friendly loading spinner indicating the payment is being processed.

![Loading spinner](documentation/loading-spinner.png)

- **Checkout success**

  - The checkout success page is where the user will be able to see the confirmation and summary of their just completed order.
  - In the checkout success page there is a heading thanking the user for their purchase, then a paragraph letting the user know that an order confirmation email will be sent to the email provided.
  - Below, the user can see a pseudo table with the 'order info' which contains 'order number' and 'order date', 'order details' containing perfume or perfume name, quantity and price, then all the delivery information and lastly the billing info containing 'order total', 'delivery' and 'grand total'.
  - At the bottom there is a button 'check out all our perfumes' which takes the user to the 'all perfume' page.

![Checkout success](documentation/checkout-success.png)

- **Oder confirmation email**

  - Once the order is successfully processed and completed a confirmation email will be sent to the user with the order details.

![Oder confirmation email](documentation/order-confirmation-email.png)

- **Profile**

  - The profile page shows the user their saved profile/delivery information and their order history.
  - At the top there is a heading indicating the user this is the 'my profile' page.
  - Below, the profile page is comprised of two sections, one with a form prefilled if the user decided to save their info in a previous purchase or if they updated their info in the profile page or empty otherwise, at the end of the form a button 'update information' which saves the information in the user profile.
  - The other section is the order history which is table containing the order or orders number, date, perfume or perfumes name and quantity and the order total.
  - The order number is hoverable (shows the complete order number) and clickable, it takes the user to the order history view for that particular order number.

![Profile](documentation/profile.png)

- **Order history**

  - The Order history page shows the user the information of a previous completed order.
  - Once the user clicks on the order number in their order history section in the profile page, the user is takes to the order history for that order.
  - The information shown in the order history is excatly to the information shown in the checkout success page given the same template is used, the difference thanks to some python code in the view and a little of Django template logic, is that for the order history, the user is shown an info message at the top indicating that 'This is a past confirmation for order number (order number). A confirmation email was sent on the order date.'
  - At the end of the page there is a button to go back to profile.

![Order history](documentation/order-history.png)

- **Add perfume**

  - The add perfume page allows authenticated users with superuser privileges to add a new perfume to the store.
  - There are two headings, one indicating you're in perfume management and a second one indicating that this is to add a perfume.
  - This page comprises a form with all the relevant fields to add a new perfume, such as name, price, description, rating, image (a button to open a directory to select the image from), available in other consoles and trailer.
  - At the end of the form there are to buttons, one to cancel the action which will bring the user to 'all product page' and another to add perfume.
  - Once the perfume is added the user will be taken to the perfume detail view for the newly added perfume with a success message at the top.

![Add perfume](documentation/add-perfume.png)

- **Edit perfume**

  - The edit perfume page allows authenticated users with superuser privileges to edit an existing perfume in the store.
  - There are two headings, one indicating you're in perfumes management and a second one indicating that this is to edit a perfume, also at the top of the page below the nav bar the user will see an info message indicating that they are editing the perfume.
  - This page comprises a form exactly the same as the add perfume form, the diference is that all the fields will be prefilled and the image (if any) will be shown as well as a checkbox to remove the image if the user chooses to.
  - At the end of the form there are to buttons, one to cancel the action which will bring the user to 'all perfumes page' and another to update perfume.
  - Once the perfume is updated the user will be taken to the perfume detail view for the newly updated perfume with a success message at the top.

![Edit perfume](documentation/edit-perfume.png)

- **Delete perfume**

  - The delete perfume page allows authenticated users with superuser privileges to delete an existing perfume in the store.
  - There are two headings, one indicating you're in perfumes management and a second one asking the user to confirm they are sure they want to delete the perfume.
  - There are to buttons at the bottom, one to cancel the action which will bring the user to 'all perfumes page' and another to delete perfume.
  - Once the perfume is deleted the user will be taken to the 'perfumes' page.

![Delete perfume](documentation/delete-perfume.png)

- **Forms errors**

  - As with every form across the entire site, should there be an error or missing information on a form, the user will be informed.

![Forms errors](documentation/forms-errors.png)

-
- 




- **Messages**

  - Every time the user completes an action whether it be register, login, logout, like a perfume, create a perfume, update a perfume, delete a perfume, add a perfume to the shopping basket and all the rest, a relevant message will be displayed at the top of the screen to inform the user about the action being completed successfully.
  - Also should the user perform an unauthorized action such as trying to force their way to a page that requires permission, a message will also show.

![Messages](documentation/messages.png)

- **404/500 Custom Pages**

  - The 404 and 500 custom error pages show said errors in a user friendly way.
  - The custom pages allow the user to avail of the navbar and footer present in all the other pages, making it easier for the user to go anywhere they want in the site after getting the error.

![404/500](documentation/404-500.png)

- **400/403 Custom Pages**

  - The 400 and 403 custom error pages show said errors in a user friendly way.
  - The custom pages allow the user to avail of the navbar and footer present in all the other pages, making it easier for the user to go anywhere they want in the site after getting the error.

![400/403](documentation/400-403.png)

- **Modals**

  - Privacy Policy and Terms & Conditions were included in modals.
  - A Bootstrap 4 scrolling long content modal was used for Terms & Conditions and Privacy Policy given the large content.
  - The [Privacy Policy Generator](https://www.termsfeed.com/privacy-policy-generator/) was used to created the privacy policy.

![Modals](documentation/modals.png)

- **Back to Top Button**

  - A back to top button was included across the site to improve UX. The user will be able to go back to the top of the page with the click of a button instead of manually doing so.
  - The back to top button will show up only when the user starts to scroll down, when the user is located at the very top of the page the button will not be visible.

![Back-To-Top](documentation/back-to-top.png)

- **Footer**

  - The footer the same as the navbar, is identical across the site.
  - The footer contains several links. Links to social media such as Facebook, Instagram, YouTube and Twitter which open in a different tab. It also contains links to Privacy Policy and Terms & Conditions, which are both modals. Also links to the about us and contact us pages.
  - At the end of the footer there is the name of the site and the programmer's credits.

![Footer](documentation/footer.png)

### Future Features

- Comment on perfumes
  - Offer the user the option to comment on perfumes.
- Edit/Update and delete own comments.
  - Offer the user the option to edit/update and delete their own comments.
- Create a blog app.
  - Create a blog app where the site's admin/owner can create content and the user can read on perfumes news, reviews, tips and more.
- Add webhooks to checkout process.
  - Implement the use of webhooks during the checkout process.
- Add view logic in add_perfume view to send emails to Newsletter subscribers every time a new perfume is added to the store.

  

 
## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.

- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) used to auto handle user authentication process.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Gunicorn](https://gunicorn.org/) used as a server provider for the site.
- [Psycopg2](https://pypi.org/project/psycopg2/) used as a postgres database adapter.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static and media file storage.


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/leonardo-simeone/perfumesground-store/projects?query=is%3Aclosed) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.


### GitHub Issues

[GitHub Issues](https://github.com/leonardo-simeone/perfumesground-store/issues?q=is%3Aissue+is%3Aclosed) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/leonardo-simeone/perfumesground-store/issues?q=is%3Aopen+is%3Aissue), There is only one open issue remaining (won't have) which will be addressed in a future iteration along with other issues to come for [Future Features](#future-features), [Link here](https://github.com/leonardo-simeone/perfumesground-store/issues/20).

![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/leonardo-simeone/perfumesground-store/issues?q=is%3Aissue+is%3Aclosed)

![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (_max 60% of stories_)
- **Should Have**: adds significant value, but not vital (_the rest ~20% of stories_)
- **Could Have**: has small impact if left out (_20% of stories_)


## Ecommerce Business Model

This site sells perfumes to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

![screenshot](documentation/keywords-selection.png)




#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
  - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
  - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- I understand that to achieve robust security and reliability in the checkout process, the use of webhooks is recommended, however due to a matter of time, I didn't implement webhooks for this project. It is though one of the future features I want to implement. The steps to implement them are as follow:
  - From your Stripe dashboard, click **Developers**, and select **Webhooks**.
  - From there, click **Add Endpoint**.
    - `https://perfumesground-store-6596e524f29e.herokuapp.com/checkout/wh/`
  - Click **receive all events**.
  - Click **Add Endpoint** to complete the process.
  - You'll have a new key here:
    - `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
  - Any custom name, such as "Django" or perfumesground-store
- You'll be provided with a 16-character password (API key).
  - Save this somewhere locally, as you cannot access this key again later!
  - `EMAIL_HOST_PASS` = user's 16-character API key
  - `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.


### Local VS Deployment

The only difference I found between local version and heroku deployment, was the verification emails. When Sign up or Order completed processes ocurred, the verification emails were not sent in the real world but to the developement terminal instead, whereas in the deployed version emails were sent to the actual emails provided by the user.

## Credits

### Content

| Source                                                                                                                                                                  | Location                             | Notes                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder)                                                                                                       | README and TESTING                   | Tool to help generate the Markdown files                                                                                                                     |
| [Fontawesome](https://fontawesome.com/search?o=r&m=free)                                                                                                                | Social Media Links & Across the Site | Icons                                                                                                                                                        |                     |
| [Mdbootstrap.com](https://mdbootstrap.com/snippets/standard/mdbootstrap/2964350#js-tab-view)                                                                            | entire site                          | Back to top button, used and adapted to my needs                                                                                                             |                                                                                                                              |                                                        |
| [Boutique Ado Code Institute Project](https://boutique-ado-leo.herokuapp.com/)                                                                                          | entire site                          | 'Code Institute walkthrough project to build a fully functional e-commerce site', used several parts of the walkthrough and adapted to my needs              |                                                                          |
