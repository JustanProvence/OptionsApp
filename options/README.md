# My App

This project is a full-stack application that utilizes React Native for the frontend and FastAPI for the backend. It implements Google authentication using Firebase Authentication, and stores user data in Cloud Firestore. The application is designed to run on Android, iOS, and the web.

## Project Structure

```
my-app
├── backend
│   ├── app
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   ├── auth.py          # Authentication logic for Google login
│   │   └── firestore.py      # Firestore database interactions
│   ├── requirements.txt      # Python dependencies for the backend
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── App.js                # Main entry point for the React Native application
│   ├── package.json          # Configuration file for npm
│   ├── firebase.js           # Firebase services initialization
│   ├── src
│   │   ├── screens
│   │   │   └── LoginScreen.js # Component for user login
│   │   └── components
│   │       └── GoogleLoginButton.js # Button for Google login
│   └── README.md             # Documentation for the frontend
└── README.md                 # Overview of the entire project
```

## Getting Started

### Prerequisites

- Node.js and npm installed for the frontend
- Python 3.7+ and pip installed for the backend
- Firebase project set up with Authentication and Firestore enabled

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Configure Firebase in `firebase.js` with your project's credentials.

4. Run the React Native application:
   ```
   npm start
   ```

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Usage

- Access the frontend application through your mobile device or web browser.
- Use the Google login button to authenticate users.
- The backend will handle authentication and data storage in Firestore.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.