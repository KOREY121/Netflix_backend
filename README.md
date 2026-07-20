# StreamVault

A Netflix-clone backend built with Django REST Framework and PostgreSQL, paired with a multi-file frontend using a sapphire and black color palette.

## Features

- **Users & Auth** — registration, JWT login/logout, profile CRUD, maturity levels
- **Profiles** — multi-profile support per account
- **Subscriptions** — plans and billing history
- **Content** — movies, series, genres, and seasons
- **Streaming** — watch history, sessions, downloads, device tracking, search history
- **Payments** — payment history endpoint
- **Reviews** — ratings, reviews, "My List" toggle, recommendations

## Tech Stack

- **Backend:** Django REST Framework + PostgreSQL
- **API Docs:** drf-spectacular (OpenAPI/Swagger schema)
- **Filtering:** django-filter

## Project Structure

Apps live at the project root (`users/`, `profiles/`, `subscriptions/`, `content/`, `streaming/`, `payments/`, `reviews/`) — **not** nested under an `apps/` package. URL includes reference them directly, e.g. `include('users.urls')`, not `include('apps.users.urls')`.

## Setup

\`\`\`bash
# clone the repo
git clone https://github.com/KOREY121/Netflix_backend.git
cd Netflix_backend

# create and activate a virtual environment
python -m venv env
env\Scripts\activate   # Windows

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# run the dev server
python manage.py runserver
\`\`\`

## Notes

- `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` is set in `core/settings.py` to avoid primary key warnings.
- `__pycache__/` is gitignored — if you see tracked `.pyc` files after pulling, run:
  \`\`\`bash
  git rm -r --cached **/__pycache__
  \`\`\`

## Branching Strategy

This project follows a stacked Gitflow workflow — feature branches are created from the previous feature branch, and all PRs target `develop`.