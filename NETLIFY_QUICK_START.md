# ⚡ Netlify Quick Start - 5 Minutes to Deploy

## 🎯 Fastest Way to Deploy

### Option 1: GitHub + Netlify UI (Easiest)

1. **Push to GitHub** (if not already done):
```bash
git add .
git commit -m "Ready for Netlify deployment"
git push origin main
```

2. **Go to Netlify**:
   - Visit https://app.netlify.com/
   - Click "Add new site" → "Import an existing project"
   - Connect your GitHub account
   - Select your JeduAI repository

3. **Configure Build**:
   - Build command: `flutter build web --release --web-renderer canvaskit`
   - Publish directory: `build/web`
   - Click "Deploy site"

4. **Done!** Your app will be live in 5-10 minutes at `your-app.netlify.app`

### Option 2: Drag & Drop (No Git Required)

1. **Build locally**:
```bash
flutter build web --release --web-renderer canvaskit
```

2. **Deploy**:
   - Go to https://app.netlify.com/drop
   - Drag the `build/web` folder
   - Done! Instant deployment

### Option 3: Netlify CLI (For Developers)

```bash
# Install CLI
npm install -g netlify-cli

# Login
netlify login

# Build
flutter build web --release

# Deploy
netlify deploy --prod
```

## 🔥 Post-Deployment Checklist

1. **Add Netlify domain to Firebase**:
   - Go to Firebase Console → Authentication → Settings
   - Add your Netlify URL to authorized domains

2. **Test your app**:
   - Visit your Netlify URL
   - Try logging in
   - Test all features

3. **Custom domain** (optional):
   - Netlify dashboard → Domain settings
   - Add your domain

## 🎉 That's It!

Your JeduAI app is now live on Netlify!

**Need detailed help?** See `NETLIFY_DEPLOYMENT_GUIDE.md`
