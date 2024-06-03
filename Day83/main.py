from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy import desc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE TABLE
class Project(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    day: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
    video_url: Mapped[str] = mapped_column(String(500), nullable=True)
    code_url: Mapped[str] = mapped_column(String(500), nullable=True)
    terminal: Mapped[bool] = mapped_column(Boolean, nullable=False)
    object: Mapped[bool] = mapped_column(Boolean, nullable=False)
    turtle_screen: Mapped[bool] = mapped_column(Boolean, nullable=False)
    file_handling: Mapped[bool] = mapped_column(Boolean, nullable=False)
    gui_tkinter: Mapped[bool] = mapped_column(Boolean, nullable=False)
    web_scraping: Mapped[bool] = mapped_column(Boolean, nullable=False)
    website_route: Mapped[bool] = mapped_column(Boolean, nullable=False)
    automation: Mapped[bool] = mapped_column(Boolean, nullable=False)
    database: Mapped[bool] = mapped_column(Boolean, nullable=False)
    python: Mapped[bool] = mapped_column(Boolean, nullable=False)
    html: Mapped[bool] = mapped_column(Boolean, nullable=False)
    css: Mapped[bool] = mapped_column(Boolean, nullable=False)
    sqlite: Mapped[bool] = mapped_column(Boolean, nullable=False)
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class ProjectForm(FlaskForm):
    day = StringField('Day', validators=[DataRequired()])
    name = StringField('Project Name', validators=[DataRequired()])
    description = StringField('Project description', validators=[DataRequired()])
    # img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    img_url = StringField('Project Image URL', validators=[DataRequired()])
    video_url = StringField('Project Video URL', validators=[DataRequired()])
    code_url = StringField('Project Code URL', validators=[DataRequired()])
    terminal = StringField('Project Ter', validators=[DataRequired()])
    object = StringField('Project Object', validators=[DataRequired()])
    turtle_screen = StringField('Project Turtle_screen', validators=[DataRequired()])
    file_handling = StringField('Project File Handling', validators=[DataRequired()])
    gui_tkinter = StringField('Project GUI Tkinter', validators=[DataRequired()])
    web_scraping = StringField('Project Web-Scraping', validators=[DataRequired()])
    website_route = StringField('Project Website Route', validators=[DataRequired()])
    automation = StringField('Project Automation', validators=[DataRequired()])
    database = StringField('Project Database', validators=[DataRequired()])
    python = StringField('Project Python', validators=[DataRequired()])
    html = StringField('Project Html', validators=[DataRequired()])
    css = StringField('Project Css', validators=[DataRequired()])
    sqlite = StringField('Project Sqlite', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    # result = db.session.execute(db.select(Project))
    result = db.session.execute(db.select(Project).order_by(desc(Project.id)))
    all_posts = result.scalars().all()
    # print(all_posts)
    posts = all_posts
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    print(f"post_id = {post_id}")
    requested_post = db.session.execute(db.select(Project).where(Project.id == post_id)).scalar()
    # requested_post = "Grab the post from your database"
    if   post_id == 1: return render_template("pj1_guess_the_number.html", post=requested_post)
    elif post_id == 2: return render_template("pj2_higher_lower_game.html", post=requested_post)
    elif post_id == 3: return render_template("pj3_coffee_machine.html", post=requested_post)
    elif post_id == 4: return render_template("pj4_quiz_game.html", post=requested_post)
    elif post_id == 5: return render_template("pj5_random_walk.html", post=requested_post)
    elif post_id == 6: return render_template("pj6_hirst_panting.html", post=requested_post)
    elif post_id == 7: return render_template("pj7_turtle_race.html", post=requested_post)
    elif post_id == 8: return render_template("pj8_snake_game.html", post=requested_post)
    elif post_id == 9: return render_template("pj9_pong_game.html", post=requested_post)
    elif post_id == 10: return render_template("pj10_turtle_crossing_game.html", post=requested_post)
    elif post_id == 11: return render_template("pj11_snake_game_with_hightest_score.html", post=requested_post)
    elif post_id == 12: return render_template("pj12_us_states_game.html", post=requested_post)
    elif post_id == 13: return render_template("pj13_miles_to_km_converter.html", post=requested_post)
    elif post_id == 14: return render_template("pj14_pomodoro_timer.html", post=requested_post)
    elif post_id == 15: return render_template("pj15_password_manager.html", post=requested_post)
    elif post_id == 16: return render_template("pj16_flash_card_app.html", post=requested_post)
    elif post_id == 17: return render_template("pj17_kanye_quotes.html", post=requested_post)
    elif post_id == 18: return render_template("pj18_quizzler.html", post=requested_post)
    elif post_id == 19: return render_template("pj19_movie_website_scraping.html", post=requested_post)
    elif post_id == 20: return render_template("pj20_send_gamil.html", post=requested_post)
    elif post_id == 21: return render_template("pj21_cookie_clicker.html", post=requested_post)
    elif post_id == 22: return render_template("pj22_fill_google_sheet.html", post=requested_post)
    elif post_id == 23: return render_template("pj23_guess_the_number_website.html", post=requested_post)
    elif post_id == 24: return render_template("pj24_jims_blog.html", post=requested_post)
    elif post_id == 25: return render_template("pj25_coffee_wifi_project.html", post=requested_post)
    elif post_id == 26: return render_template("pj26_movie_card.html", post=requested_post)
    elif post_id == 27: return render_template("pj27_jims_project.html", post=requested_post)
    elif post_id == 28: return render_template("pj28_tic_tac_toe.html", post=requested_post)
    elif post_id == 29: return render_template("pj29_typing_speed_test.html", post=requested_post)
    elif post_id == 30: return render_template("pj30_breakout_game.html", post=requested_post)
    elif post_id == 31: return render_template("pj31_cafe_and_wifi_website.html", post=requested_post)
    elif post_id == 32: return render_template("pj32_todo_list.html", post=requested_post)
    elif post_id == 33: return render_template("pj33_disapearing_text.html", post=requested_post)
    elif post_id == 34: return render_template("pj34_audio_book_scraping", post=requested_post)
    elif post_id == 35: return render_template("pj35_dinosaur.html", post=requested_post)
    elif post_id == 36: return render_template("pj36_space_invader.html", post=requested_post)
    elif post_id == 37: return render_template("pj37_coffee_online_shop.html", post=requested_post)
    else:               return render_template("post.html", post=requested_post)

# add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    add_form = ProjectForm()
    if request.method == 'POST':
        new_day =  add_form.day.data
        new_name =  add_form.name.data
        new_description =  add_form.description.data
        new_img_url =  add_form.img_url.data
        new_video_url =  add_form.video_url.data
        new_code_url =  add_form.code_url.data
        new_terminal =  add_form.terminal.data
        new_object =  add_form.object.data
        new_turtle_screen =  add_form.turtle_screen.data
        new_file_handling =  add_form.file_handling.data
        new_gui_tkinter =  add_form.gui_tkinter.data
        new_web_scraping =  add_form.web_scraping.data
        new_website_route =  add_form.website_route.data
        new_automation =  add_form.automation.data
        new_database =  add_form.database.data
        new_python =  add_form.python.data
        new_html =  add_form.html.data
        new_css =  add_form.css.data
        new_sqlite =  add_form.sqlite.data
        new_post = Project(
            day            = new_day,
            name           = new_name,
            description    = new_description,
            img_url        = new_img_url,
            video_url      = new_video_url,
            code_url       = new_code_url,
            terminal       = new_terminal,
            object         = new_object,
            turtle_screen  = new_turtle_screen,
            file_handling  = new_file_handling,
            gui_tkinter    = new_gui_tkinter,
            web_scraping   = new_web_scraping,
            website_route  = new_website_route,
            automation     = new_automation,
            database       = new_database,
            python         = new_python,
            html           = new_html,
            css            = new_css,
            sqlite         = new_sqlite,
        )

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=add_form, post_h1="New Project")

# edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_update = db.get_or_404(Project, post_id)
    edit_form = ProjectForm(
        name=post_to_update.name,
        map_url=post_to_update.map_url,
        img_url=post_to_update.img_url,
        location=post_to_update.location,
        seats=post_to_update.seats,
        has_toilet=post_to_update.has_toilet,
        has_wifi=post_to_update.has_wifi,
        has_sockets=post_to_update.has_sockets,
        can_take_calls=post_to_update.can_take_calls,
        coffee_price=post_to_update.coffee_price,
    )
    if request.method == 'POST':
        new_name           = edit_form.name.data
        new_map_url        = edit_form.map_url.data
        new_img_url        = edit_form.img_url.data
        new_location       = edit_form.location.data
        new_seats          = edit_form.seats.data
        new_has_toilet     = edit_form.has_toilet.data
        new_has_wifi       = edit_form.has_wifi.data
        new_has_sockets    = edit_form.has_sockets.data
        new_can_take_calls = edit_form.can_take_calls.data
        new_coffee_price   = edit_form.coffee_price.data
        post_to_update.name           = new_name
        post_to_update.map_url        = new_map_url
        post_to_update.img_url        = new_img_url
        post_to_update.location       = new_location
        post_to_update.seats          = new_seats
        post_to_update.has_toilet     = new_has_toilet
        post_to_update.has_wifi       = new_has_wifi
        post_to_update.has_sockets    = new_has_sockets
        post_to_update.can_take_calls = new_can_take_calls
        post_to_update.coffee_price   = new_coffee_price
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=edit_form, post_h1="Edit Project")

# delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>', methods=["GET", "POST"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(Project, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
