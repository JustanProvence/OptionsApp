import * as Google from 'expo-auth-session/providers/google';
import { useEffect, useState } from 'react';
import * as WebBrowser from 'expo-web-browser';

WebBrowser.maybeCompleteAuthSession();

type GoogleUser = {
  name: string;
  email: string;
  picture: string;
} | null;

export function useGoogleAuth() {
  const [user, setUser] = useState<GoogleUser>(null);

  const [request, response, promptAsync] = Google.useAuthRequest({
    clientId: '921792807633-1n8ma8hip9p0626b7bo53s0cgjhlbfrd.apps.googleusercontent.com',
    webClientId: '921792807633-1n8ma8hip9p0626b7bo53s0cgjhlbfrd.apps.googleusercontent.com',
    // Optionally add iosClientId, androidClientId if you want native support
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { authentication } = response;
      fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
        headers: { Authorization: `Bearer ${authentication?.accessToken}` },
      })
        .then(res => res.json())
        .then(data => {
          setUser({
            name: data.name,
            email: data.email,
            picture: data.picture,
          });
          console.log('Google user info:', data); // Log all user info
        }
        );
    }
  }, [response]);

  return { user, promptAsync, request };
}