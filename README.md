![Logo](static/images/full-logo.png)

# The Veggie Patch

As my Milestone Project 3 for the Code Institute Full Stack Web Development course,
I have built an application where people are able to find and share vegetarian recipes with each other.

The application can be found at ....

## UX
The application is meant to be a platform for people who are interested in vegetarian cooking,
to get inspired and find and share recipes with each other.\
Data for the app is kept in a MongoDB document-based database with two collections.\
The app incorporates the four basic CRUD (create, read, update, delete) functions, and it was created using HTML, Flask, Jinja templating and CSS.

### User stories
1. as a user I want to be able to browse all recipes for inspiration
2. as a user looking for a specific type of recipe, I want to be able to filter on meal type
3. as a user looking to use up some ingredients, I want to be able to perform a search based on ingredients
3. as a user I want an easy overview of required ingredients
4. as a user I want to be able to print out a clean, well-structured copy of the recipe
5. as a user I want to be able to share recipes with other users
6. as a user who previously added a recipe, I want to be able to edit or delete it

### Wireframes
Wireframes for this project were created for [small screens](static/wireframes/small-screens.pdf)
and for [medium and up](static/wireframes/medium-large-screens.pdf). The decision to roll wireframes for medium and large screens into one
was taken when it quickly became clear that they would only have minor differences. Apart from the navigation bar being collapsed on medium-sized screens,
they are largely identical.

Differences between the wireframes and the actual layout are discussed in the [Features](#wireframe-differences) section below.

### Database
The data for this project is stored in a MongoDB database with two collections:\
**Categories collection**:
| Field Name  | Data Type |
| ------------|-----------|
| _id         | ObjectId  |
|category_name|String     |
|category_url |String     |

**Recipes collection**:
| Field Name   | Data Type |
|--------------|-----------|
|_id           |ObjectId   |
|name          |String     |
|category_name |String     |
|prep_time     |Integer    |
|cook_time     |Integer    |
|serves        |String     |
|ingredients   |Array      |
|image_url     |String     |
|instructions  |String     |
|id_key        |String     |
|total_time    |Integer    | 

The two collections have the category_name field in common.
This is so that it is possible to return recipes belonging to a specific category when that category is chosen in the category view.\
The ingredients are stored in an array in order to be able to display them on separate lines in an unordered list.\
total_time is the sum of prep_time and cook_time and it is not visible to the user, but is used for the filter function where users can
look up recipes based on how long it takes to make them.

## Features
### Design and layout
This is a multi-page app with a clean, user-friendly design. All pages make use of the same colour scheme and fonts and all have the same fixed-top navbar and footer.
Where the same elements are rendered on multiple pages at different times (for example cards showing an image and a name for a recipe),
the look is always identical to ensure smooth transitions and ecognisability.\
For the header, footer and borders a dark green (#026318) was used as green is associated with vegetables and this is a platform for sharing vegetarian recipes.\
Where text appears on a coloured background, the color is set to white to ensure it is easy to read.\
The logo was designed with [Canva](https://www.canva.com/) and consists of an image of tomatoes next to the name of the website in white on the green background.
A playful, relaxed font, Just Another Hand, was chosen to convey a sense of fun and informality. For all other text on the website, the font Cambay is used as it is a simple, sans-serif font which is easier on the eyes when reading on a screen.

#### Wireframe differences

- **Login/registration pages**: I initially planned on having login and registration pages, but during the first session with my mentor,
he pointed out that it was not a requirement for this project, and when I said I was concerned about letting everyone have access to editing
and deleting, he suggested the current setup with the secret key. The website does therefore not have login and registration pages as in the wireframes.
- **Recipe cards**: my wireframes for small screens show the recipe cards in rows with three in each row and for medium screens and up,
they are in rows of four. However, when I started building the site it was clear early on that the cards would be too small and too
compact-looking. I therefore decided to only have one card per row on small screens and three on medium-large.
- **Recipe view on small screens**: I changed the original layout from showing the picture next to the recipe info (prep time, servings etc)
to having the picture on top and the info underneath. As with the recipe cards, it just looked too compact and the picture was too narrow in the original design.

### Existing Features
The app incorporates the 4 CRUD functionalities:
- **CREATE**
  * Adding a recipe: the user has the option to add a recipe to the database by clicking on the "Add a Recipe" link in the navigation bar.
  Doing so will open a form that the user can fill out with recipe name, category, time it takes to prepare and cook, number of servings,
  ingredients, instructions and an image URL.\
  The user also has to provide a key that they need to remember in case they want to edit the recipe later.
- **READ**
  * Browsing: the landing-page displays all recipes in the database, and it is possible for users to scroll down and get inspired.
  * Filtering on Categories: by clicking on "Categories" in the navigation bar and then on a category card, it is possible for the user to only see the recipes belonging to that category (for example breakfast or desserts).
  * Searching: by clicking on "Search" in the navigation bar, the user is taken to a searchbox where they are able to search for recipes based on ingredients and names.
  This was set up by creating an index on the name and ingredients fields in the MongoDB database.\
  The user can also search for recipes based on a category and how much time they have.
  * Viewing a recipe: when a recipe card is clicked, the user is taken to the recipe view where they can see info, ingredients and instructions for that recipe.
- **UPDATE & DELETE**
  * Editing and deleting a recipe: the recipe view has an edit button the user can click if they wish to update or delete the recipe.
  In order to restrict access to these functions, the edit form will only open once the correct key has been entered (the key provided when the recipe was first added).
  This ensures that only the person who added the recipe is able to change or delete it.\
  The edit form autopopulates with the data from the MongoDB database and there is a checkbox that needs to be checked in order to delete the recipe completely.
  A checkbox is less likely to be clicked by accident than a button which is why this design was chosen.
- Feedback: Flash messages are displayed when a user has added, updated or deleted a recipe.

### Features Left to Implement
- **Register and Login functionality**: it would be useful to add the option for users to register on the website.
For now, the id_key serves to restrict who can edit and delete recipes which prevents others from randomly changing or deleting someone else's recipes,
but it is possible for anyone to add a recipe, and a registration/login option would allow for some more control in this area.\
It would also improve the user experience by giving them a profile overview where they would have quick access to all recipes added by themselves.
- **Advanced categories**: The current categorization of recipes is fairly basic and only covers one meal type per recipe.
Allowing multiple categories per recipe would make searching more efficient as some of them easily fit into more than one. It would then also be
possible to categorize by type of cusinine (Indian, Italian etc) and dietary needs (gluten-free, low calorie etc). 

## Technologies and Tools Used
- HTML, CSS, JavaScript and Python were used to build the webpage
- The [Flask framework](https://palletsprojects.com/p/flask/) and [Jinja template engine](https://palletsprojects.com/p/jinja/) were used to create and render dynamic HTML pages.
- The [Bootstrap](https://getbootstrap.com/) framework was used to set up a responsive layout
- [MongoDB Atlas](https://www.mongodb.com/) was used to store the data in a non-relational database
- [Gitpod](https://www.gitpod.io/) was used as the IDE for this Project
- [Git](https://git-scm.com/) and [GitHub](https://github.com/) were used for version control and repository hosting
- [Heroku](https://www.heroku.com/) was used as the platform for deployment of the website
- [Autoprefixer](https://autoprefixer.github.io/) was used to add vendor prefixes to CSS code
- [Google Fonts](https://fonts.google.com/) provided the fonts used throughout the website (Just Another Hand and Cambay)
- [Canva](https://www.canva.com/) was used to design the website logo and [Favicon.io](https://favicon.io/) to turn it into a favicon
- [Font Awesome](https://fontawesome.com/) provided all icons used throughout the website
- [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project


## Testing
JavaScript code was run through the [JSHint](https://jshint.com/) analysis tool to check for syntax errors.
In addition, CSS was checked in the [CSS Validator](https://jigsaw.w3.org/css-validator/) and HTML in the [HTML Validator](https://validator.w3.org/).

## Deployment
This project was developed in Gitpod and pushed regularly to the GitHub repository via git commands in the terminal.\
The website was deployed on Heroku via the following steps:
1. I created an app on Heroku and connected to it on Gitpod in the terminal
2. I set the necessary config vars in the Heroku Settings tab (secret key, MongoDB name, MongoDB URI, IP and PORT)
3. I regularly pushed code from Gitpod to Heroku via the command line (later I set up automatic deploys from the master branch
in the Heroku Deploy tab)
4. The app was then available on [https://the-veggie-patch.herokuapp.com/](https://the-veggie-patch.herokuapp.com/).

### Cloning and running the project locally
Follow these steps if you wish to run the project locally:
- go to the [repository page](https://github.com/Sarani1612/the-veggie-patch) on GitHub
- click the "clone or download" button on the right-hand side
- copy the URL that shows up
- in Terminal, change the current working directory to the location where you want the cloned directory to be made
- type 'git clone' and paste the URL from step 2
- press enter
- the local clone will be created

These instructions and more info can be found at [this GitHub Help Page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Issues
- **Updating a recipe**: I initially got a KeyError message when trying to update a recipe. It turned out that the following line was the issue:\
`if request.form['delete'] == 'checked':`\
Given that the 'delete' checkbox was not checked, trying to access the 'delete' key would of course return an error.
Solved by changing the code to `if request.form.get('delete') == 'checked':` as this does not throw an error when the key does not exist.
- **Filtering based on time**: I ran into an issue while setting up the filtering function. I wanted to be able to filter recipes according
to how much time they took to make (prep_time + cook_time). I was looking for a way to do something like
`results = mongo.db.recipes.find({'category_name': category, "prep_time"+"cook_time": {"$lte": 30}})`\
Obviously, it did not work with the plus symbol and I could not find another way to do it including with "$add" and "$sum".\
I solved it by batch updating all records in the database to include a new total_time key whose value was the sum of prep_time and cook_time.
I then added the same key-value pair to the insert_recipe and update_recipe functions so that all recipes now have the total_time field.\
The filter function now works with `results = mongo.db.recipes.find({'category_name': category, "total_time": {"$lte": 30}})`.
- **Flash messages not disappearing**: I have set a JavaScript setTimeout() function targeting elements with the ‘alert’ classname
to remove the flash messages after 5 seconds. A person who kindly tested my website said that the messages did not disappear,
while for me, there is only an issue with the flash message for successful deletion of a recipe.
I have not been able to find the cause yet and this bug has therefore been left unresolved for now.

## Credits
- [This article](https://pythonise.com/series/learning-flask/flask-message-flashing) by Julian Nash was used as a guide for flash messages

### Content and Media
- Landing page background photo is from [Pexels](https://www.pexels.com/)
- Recipes including photos are from the [BBC goodfood](https://www.bbcgoodfood.com/) website

### Acknowledgments

*This website is for educational purposes only. It was created as part of the Code Institute Full Stack Developer course.*
