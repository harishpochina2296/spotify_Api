A simple backend project built using Django and Django REST Framework (DRF) that allows users to manage tracks and playlists, with authentication using JWT.
User Authentication (JWT)
Create, Read, Update, Delete (CRUD) for Tracks
Create, Read, Update, Delete (CRUD) for Playlists
Add/Remove tracks from playlists
User-specific playlists
Optimized queries using select_related
 
Tech Stack
Python
Django
Django REST Framework
SQLite (default DB)
JWT Authentication (SimpleJWT)

Setup Instructions
git clone "My Project Github path"
cd sptify_Api

Create virtual environment
python -m venv spotify_env 
venv\Scripts\.\activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makemigrations 
python manage.py migrate

Run server
python manage.py runserver


Authentication
This project uses JWT Authentication.

Get Token
POST /api/token/
Use Token

Add this header in Postman:

Authorization: Bearer <your_access_token>


API Endpoints
Tracks
GET /api/tracks/
POST /api/tracks/
PUT /api/tracks/<id>/
PATCH /api/tracks/<id>/
DELETE /api/tracks/<id>/

Playlists
GET /api/playlists/
POST /api/playlists/
PUT /api/playlists/<id>/
PATCH /api/playlists/<id>/
DELETE /api/playlists/<id>/

Notes
Always use trailing slash / in endpoints
JWT token is required for protected routes


