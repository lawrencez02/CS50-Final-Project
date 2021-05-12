README Documentation for Detox by Lawrence Zhang

YouTube video link: https://youtu.be/5n_QnqeYxNI

Prerequisites:
Detox relies on several Python libraries to work, including tweepy (for Twitter), praw (for Reddit), and pytrends (for Google).
Note: these libraries are not installed by default on CS50 IDE. These
can be installed via the following comands: "pip install pytrends", "pip install praw", and "pip install tweepy".

Quickstart:
Simply cd into the project folder and enter "flask run" and click on the generated link. This will take you to Detox.

Introduction:
Detox is a website that calls various social media sites' APIs and gathers the trendiest information on those sites into one place.
It then displays all of that information in one place, on on page, in a distraction-free, simple, clean manner. Detox aims to be
a website that you can spend a few minutes on, get up to speed on the latest in the world and the internet, and then get back to your day,
avoiding the addictive, endless scrolling of the Instagrams or Twitters of the world.

Features:
Upon visiting Detox, you will see Detox's title and logo, as well as a form in the lower-left part of the page, that invites you to
enter in a numerical input that is the number of minutes you want to spend on Detox. You can choose to either fill out this form if you want
to keep yourself accountable or not fill out the form, if you aren't as pressed for time. If you fill it out, after you press Enter,
a timer will invisibly start in the background, and you're off to read the content on Detox!

To the right of the form, you'll see several buttons labeled with different social media/internet sites. If you want to, you can click on
a button, which will take you to the appropriate section on Detox' page. Or, you can simply just scroll down from the initial Detox screen
and begin reading the internet content.

This internet content from various sources is displayed in the most distraction-free, addictive-free way possible: simple tables, with
no images or links. This is intended, so that you spend the least amount of time possible on the site, so you can get back to your real life
as quickly as possible. If you entered an amount of time in the initial form, once that amount of time has passed, a modal/pop-up will display on the screen,
alerting you that your time is up. There is no way to close the modal, intentionally.

And you're done! Enjoy.
