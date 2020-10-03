# Ghostpost -- back-end

This is the Django back-end to accompany the React front-end found here: https://github.com/pokeyjess/ghostpost-frontend

To run this program, have the front-end running on localhost: 3000, and the back-end on localhost: 8000.

Ghostpost allows users to post either boasts or roasts of just about anything. Other users can show their approval, or disapproval, of the posts.

This version of Ghostpost will allow you to see boasts and roasts, filtered by either the date they were posted, with the most recent first, or their ranking in terms of total up-votes. You can also see either boasts only, or roasts only. Plus, you can give individual boasts and roasts a thumb's up, or a thumb's down.

A way to create a new boast or roast from the browser is still in development. For now, posts can be created using the back-end API, or the admin panel.

## Requirements

python = "^3.8"

django = "^3.1.1"

djangorestframework = "^3.12.1"

django-cors-headers = "^3.5.0"

poetry >= "0.12"

