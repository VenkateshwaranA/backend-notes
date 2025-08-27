# Notes App Backend

This is a Python-based Notes application backend built with **FastAPI**.  
It allows users to **create, view, edit, and delete notes** with proper authentication and optimized performance.

---

## Features

1. **CRUD Operations for Notes**
   - Create, Read, Update, Delete notes
   - Each note has `note_title`, `note_content`, `user_id`, `created_on`, and `last_update`

2. **Authentication**
   - JWT-based authentication system
   - Secure password hashing

3. **Optional Features**
   - Rich Text Editor support for notes (Extra Points)
   - SEO metadata: title, description, OG, keywords
   - Optimized code: reusable components, code splitting, render optimization

---

## Backend Requirements

- **Framework**: Python FastAPI / Django / Flask
- **Database**: MySQL (SQL) or MongoDB (NoSQL)
- **Authentication**: JWT or session-based
- **Folder Structure**: Properly organized for maintainability and scalability
- **Performance**: Optimized endpoints and code (performance testing reports included)

---

## Database Models

### User
| Field        | Type     | Description                  |
|--------------|---------|------------------------------|
| user_id      | UUID     | Unique identifier for user   |
| user_name    | varchar  | Name of the user             |
| user_email   | varchar  | User's email address         |
| password     | varchar  | Hashed password              |
| last_update  | date     | Last updated timestamp       |
| created_on   | date     | Account creation timestamp   |

### Notes
| Field        | Type     | Description                  |
|--------------|---------|------------------------------|
| note_id      | UUID     | Unique identifier for note   |
| note_title   | varchar  | Title of the note            |
| note_content | text     | Content of the note          |
| user_id      | UUID     | Reference to the user        |
| created_on   | date     | Note creation timestamp      |
| last_update  | date     | Last updated timestamp       |

---

## API Endpoints

| Endpoint                   | Method | Description                    |
|-----------------------------|--------|--------------------------------|
| `/auth/signup`             | POST   | Create a new user              |
| `/auth/login`              | POST   | User login (returns JWT)       |
| `/notes/`                  | GET    | Get all notes for authenticated user |
| `/notes/`                  | POST   | Create a new note              |
| `/notes/{note_id}`         | GET    | Get a specific note            |
| `/notes/{note_id}`         | PUT    | Update a note                  |
| `/notes/{note_id}`         | DELETE | Delete a note                  |

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/notes-app.git
cd notes-app


python -m venv venv
source venv\Scripts\activate      

pip install -r requirements.txt


start your application : uvicorn main:app --reload

