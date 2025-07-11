# Backend API Documentation

## Overview
This backend is built using FastAPI and serves as the backend for a React Native application that supports Google authentication. It communicates with Firebase services for user authentication and data storage.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd my-app/backend
   ```

2. **Install Poetry**
   If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. **Install Dependencies**
   Install the required Python packages listed in `pyproject.toml`:
   ```bash
   poetry install
   ```

4. **Set Up Firebase**
   - Create a Firebase project in the Firebase Console.
   - Obtain the service account key JSON file and place it in the `app` directory.
   - Set the environment variable for the Firebase credentials:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/serviceAccountKey.json"
     ```

5. **Run the FastAPI Application**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

## API Usage

### Authentication
- **Google Login**
  - Endpoint: `/auth/google`
  - Method: `POST`
  - Description: Handles Google login and returns user information and tokens.

### Firestore
- **Data Operations**
  - Functions for reading and writing data to Firestore are defined in `firestore.py`.

## Additional Notes
- Ensure that the Firebase project is configured to allow authentication via Google.
- Refer to the frontend documentation for details on how to integrate with this backend.