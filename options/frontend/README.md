# Frontend React Native Application

This is the frontend part of the application built using React Native. It is designed to authenticate users using Google login through Firebase Authentication and manage data with Cloud Firestore.

## Getting Started

### Prerequisites

- Node.js (version 14 or later)
- npm (Node Package Manager)
- React Native CLI
- Firebase account

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-app/frontend
   ```

2. Install the dependencies:
   ```
   npm install
   ```

3. Set up Firebase:
   - Create a Firebase project in the Firebase Console.
   - Enable Google Authentication in the Authentication section.
   - Add your app to the Firebase project and obtain the configuration details.

4. Configure Firebase:
   - Update the `firebase.js` file with your Firebase configuration.

### Running the Application

To run the application on Android or iOS, use the following commands:

- For Android:
  ```
  npx react-native run-android
  ```

- For iOS:
  ```
  npx react-native run-ios
  ```

To run the application on the web, use:
```
npm start
```

### Usage

- The main entry point of the application is `App.js`.
- The login functionality is handled in the `LoginScreen.js` component.
- The `GoogleLoginButton.js` component triggers the Google login process.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.