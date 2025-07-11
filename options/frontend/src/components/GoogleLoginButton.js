import React from 'react';
import { Button } from 'react-native';
import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
import firebase from '../firebase';

const GoogleLoginButton = () => {
    const auth = getAuth(firebase);
    const provider = new GoogleAuthProvider();

    const handleLogin = async () => {
        try {
            await signInWithPopup(auth, provider);
            // Handle successful login (e.g., navigate to another screen)
        } catch (error) {
            console.error("Error during Google login:", error);
            // Handle login error (e.g., show an alert)
        }
    };

    return (
        <Button title="Login with Google" onPress={handleLogin} />
    );
};

export default GoogleLoginButton;