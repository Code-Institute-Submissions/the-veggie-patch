import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    '''
    Groups all recipes by category and renders them on the landing page view.
    '''
    recipes = mongo.db.recipes.find().sort('category_name', 1)
    return render_template('index.html',
                           recipes=recipes,
                           title='The Veggie Patch')


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    current_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html',
                           recipe=current_recipe,
                           title=current_recipe['name'])


@app.route('/categories')
def categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find(),
                           title='Browse Categories')


@app.route('/categories/<category_name>')
def view_category(category_name):
    recipes = mongo.db.recipes.find({"category_name": category_name}).sort('name', 1)
    return render_template('viewcategory.html',
                           recipes=recipes,
                           category_heading=category_name,
                           title=category_name)


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find(),
                           title='Add a Recipe')


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    '''
    Gets data from the form the user has filled out and inserts the recipe in the database.
    Returns a view of the new recipe.
    '''
    recipes = mongo.db.recipes
    new_recipe = {'name': request.form.get('recipe_name'),
                  'category_name': request.form.get('category_name'),
                  'prep_time': int(request.form.get('prep_time')),
                  'cook_time': int(request.form.get('cook_time')),
                  'serves': request.form.get('serves'),
                  'ingredients': request.form.get('ingredients').split(";"),
                  'image_url': request.form.get('image_url'),
                  'instructions': request.form.get('instructions'),
                  'id_key': request.form.get('id_key'),
                  'total_time': int(request.form.get('prep_time'))+int(request.form.get('cook_time'))}
    new_id = recipes.insert_one(new_recipe)
    flash('Your recipe has been added!', 'success')
    return redirect(url_for('view_recipe',
                            recipe_id=new_id.inserted_id))


@app.route('/edit_recipe/<recipe_id>', methods=["POST"])
def edit_recipe(recipe_id):
    '''
    Checks if the key supplied by the user matches the one in the database.
    If yes, the user is sent to a form where they can edit the recipe.
    If not, they are sent back to the recipe.
    '''
    this_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    if request.form['edit_key'] == this_recipe['id_key']:
        return render_template('editrecipe.html',
                               recipe=this_recipe,
                               categories=mongo.db.categories.find(),
                               title='Edit Recipe')
    flash('Wrong key entered. Please try again.', 'danger')
    return redirect(url_for('view_recipe',
                            recipe_id=this_recipe['_id']))


@app.route('/submit_edit/<recipe_id>', methods=["POST"])
def submit_edit(recipe_id):
    '''
    Checks if the 'delete' checkbox has been checked.
    If yes, the recipe is deleted entirely from the database.
    If not, the recipe is updated.
    '''
    recipes = mongo.db.recipes
    this_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    if request.form.get('delete') == 'checked':
        recipes.delete_one(this_recipe)
        flash('Your recipe has been deleted', 'success')
        return render_template('index.html',
                               recipes=mongo.db.recipes.find(),
                               title='The Veggie Patch')
    else:
        recipes.update_one({"_id": ObjectId(recipe_id)},
                           {"$set":
                           {
                               'name': request.form.get('recipe_name'),
                               'category_name': request.form.get('category_name'),
                               'prep_time': int(request.form.get('prep_time')),
                               'cook_time': int(request.form.get('cook_time')),
                               'serves': request.form.get('serves'),
                               'ingredients': request.form.get('ingredients').split(";"),
                               'image_url': request.form.get('image_url'),
                               'instructions': request.form.get('instructions'),
                               'total_time': int(request.form.get('prep_time'))+int(request.form.get('cook_time'))
                            }})
        flash('Your recipe has been updated', 'success')
        return redirect(url_for('view_recipe',
                                recipe_id=this_recipe['_id']))


@app.route('/search')
def search():
    return render_template('search.html',
                           categories=mongo.db.categories.find(),
                           title='Search Recipes')


@app.route('/searchresults', methods=['POST'])
def search_results():
    '''
    Allows the user to search for recipes using words from the ingredients and name fields.
    '''
    query = request.form['searchbox']
    results = mongo.db.recipes.find({"$text": {"$search": query}})
    return render_template('searchresults.html',
                           results=results,
                           heading=f'Results for "{query}"',
                           title=f'Results for "{query}"')


@app.route('/filterresults', methods=['POST'])
def filter_results():
    category = request.form['cat_filter']
    if request.form.get('time_filter') == 'half_hour':
        results = mongo.db.recipes.find({'category_name': category, "total_time": {"$lte": 30}})
        return render_template('searchresults.html',
                               results=results,
                               heading="Results",
                               title="Results")
    elif request.form['time_filter'] == 'up_to_hour':
        results = mongo.db.recipes.find({'category_name': category, "total_time": {"$lte": 60, "$gte": 31}})
        return render_template('searchresults.html',
                               results=results,
                               heading="Results",
                               title="Results")
    else:
        results = mongo.db.recipes.find({'category_name': category, "total_time": {"$gte": 61}})
        return render_template('searchresults.html',
                               results=results,
                               heading="Results",
                               title="Results")


@app.errorhandler(404)
def page_not_found(error):
    '''
    Displays custom 404 error page.
    '''
    return render_template('404.html', title="Page not found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    '''
    Displays custom internal server error page.
    '''
    return render_template('500.html', title="Something went wrong"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
