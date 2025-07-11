import React, { useState } from 'react';
import { View, Text, Button, Alert } from 'react-native';
import { GoogleSignin } from '@react-native-google-signin/google-signin';
import firebase from '../firebase';

const LoginScreen = () => {
  const [loading, setLoading] = useState(false);

  const signInWithGoogle = async () => {
    setLoading(true);
    try {
      await GoogleSignin.hasPlayServices();
      const userInfo = await GoogleSignin.signIn();
      const { idToken } = userInfo;

      // Create a Firebase credential with the Google ID token
      const credential = firebase.auth.GoogleAuthProvider.credential(idToken);
      
      // Sign in with credential from the Google user
      await firebase.auth().signInWithCredential(credential);
      Alert.alert('Login Successful', `Welcome ${userInfo.user.name}`);
    } catch (error) {
      console.error(error);
      Alert.alert('Login Failed', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View>
      <Text>Login Screen</Text>
      <Button
        title={loading ? 'Loading...' : 'Sign in with Google'}
        onPress={signInWithGoogle}
        disabled={loading}
      />
    </View>
  );
};

export default LoginScreen;