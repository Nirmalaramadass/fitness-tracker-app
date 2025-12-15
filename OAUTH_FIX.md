# OAuth Configuration Fix - Setup Instructions

## Problem
The app was showing "Error 400: redirect_uri_mismatch" because the redirect URI wasn't properly configured for different environments (local vs production).

## Solution Implemented

### 1. Environment Variables Setup
- Created `.env` file for local development credentials
- Created `.env.example` as a template
- Updated `app.py` to read redirect URI from environment variables

### 2. Steps to Fix the OAuth Error

#### For Local Development:

1. **Update your `.env` file**:
   - Open `.env` file
   - Replace `YOUR_CLIENT_SECRET_HERE` with your actual client secret from the Google Cloud Console
   - Keep `REDIRECT_URI=http://localhost:5000/callback` for local testing

2. **Add localhost redirect URI to Google Cloud Console**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Navigate to: APIs & Services → Credentials
   - Click on your OAuth 2.0 Client ID (the one starting with 620527182020...)
   - Under "Authorized redirect URIs", add: `http://localhost:5000/callback`
   - Click "Save"

#### For Production (Render.com):

1. **Set Environment Variables in Render**:
   - Go to your Render dashboard
   - Select your web service
   - Go to "Environment" tab
   - Add these environment variables:
     ```
     GOOGLE_CLIENT_ID=620527182020-m20qmmc2b7mohm12redh7egdn5bb5pq5.apps.googleusercontent.com
     GOOGLE_CLIENT_SECRET=your_actual_client_secret
     FLASK_SECRET_KEY=generate_a_random_secret_key
     REDIRECT_URI=https://fitness-tracker-app-j9hm.onrender.com/callback
     FLASK_ENV=production
     ```

2. **Verify Production Redirect URI in Google Cloud Console**:
   - Ensure `https://fitness-tracker-app-j9hm.onrender.com/callback` is in the authorized redirect URIs list
   - It should already be there based on your client_secret JSON file

### 3. Getting Your Client Secret

Your client secret is in the `client_secret_*.json` file. Copy it from there and paste it into:
- `.env` file (for local development)
- Render environment variables (for production)

### 4. Testing

**Local Testing**:
```bash
python app.py
```
Then visit `http://localhost:5000` and try logging in.

**Production Testing**:
After deploying to Render with the environment variables set, visit your production URL and try logging in.

## Important Security Notes

1. ✅ `.env` is already in `.gitignore` - don't commit it to Git
2. ✅ Use `.env.example` as a template for other developers
3. ✅ Never commit the `client_secret_*.json` file to a public repository
4. ✅ Use strong, random secret keys for production

## Common Issues

### Issue: Still getting redirect_uri_mismatch
**Solution**: Double-check that:
- The redirect URI in `.env` matches exactly what's in Google Cloud Console
- There are no extra spaces or trailing slashes
- You've saved changes in Google Cloud Console and waited a few minutes

### Issue: Environment variables not loading
**Solution**: 
- Ensure `python-dotenv` is installed: `pip install python-dotenv`
- Verify `.env` file is in the same directory as `app.py`
- Restart your Flask application after changing `.env`

### Issue: Different redirect URI for local vs production
**Solution**: 
- Use `.env` for local development with `http://localhost:5000/callback`
- Use Render environment variables for production with `https://...onrender.com/callback`
- Both URIs must be registered in Google Cloud Console
