DESIGN Documentation for Detox by Lawrence Zhang

Prerequisites:
Detox relies on several Python libraries to work, including tweepy (for Twitter), praw (for Reddit), and pytrends (for Google).
Note: these libraries are not installed by default on CS50 IDE. These
can be installed via the following comands: "pip install pytrends", "pip install praw", and "pip install tweepy".

Implementation and Design:
Detox is implemented as a web app with the Flask microframework, using the languages of Python, HTML, CSS, and JavaScript.
I selected Flask instead of just traditional HTML/CSS/JavaScript because I needed by website to be dynamically generated based on
the current day's trending internet posts/headlines. Python (and Flask's application.py) provided the perfect way for me to get data
using various APIs on sources across the internet, particularly with Python's immense number of useful libraries (like the ones mentioned above).
In addition, I used the CSS library Bulma as opposed to Bootstrap because I wanted to learn something new, as well as
because Bulma provided excellent, easy-to-use column sizing options compared to Bootstrap. Column sizes are everything in Detox, as all
social media content is displayed in tables, so this was critical in my project. Also, I liked Bulma's styling more and thought it would
bring a little freshness into the project as compared to continuing to use Boostrap. However, I had to create my own styles.css file that contains
some very short CSS to fix some of the odd styling issues I encountered with the form on Detox.

Most of the heavy-lifting occurs in application.py, where I first import the above-mentioned libraries as well as many more that are useful
in API requests, such as the library requests. Then, I proceed to use various API keys to query for data from those social media sites,
which I organize mostly into Python lists and dictionaries before passing those into Flask's render_template along with index.html, which is the only html
file apart from layout.html in my project. This is because Detox is as simple as it can be, with just one page on the site. Once passed into
index.html, I use Jinja in looping through the various elements in those Python lists/dictionaries, creating row-by-row the different
tables that belong to the different social media sites.

The only other complication is the form that accepts user input on Detox's home screen. This is implemented as a JavaScript script in layout.html. The
button labelled "Enter" has an onclick attribute set to the JavaScript script's function, setTime(), which uses the function setTimeout in order
to display a modal/pop-up over the screen after the user-inputted amount of time. I implemented this feature this way because it seemed to me
to be the simplest, most effective way to implement such a time-tracking feature.