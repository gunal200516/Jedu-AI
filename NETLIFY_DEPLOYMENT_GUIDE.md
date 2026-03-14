# 🚀 Netlify Deployment Guide for JeduAI

This guide will help you deploy your Flutter web app to Netlify.

## 📋 Prerequisites

- A Netlify account (free tier works fine)
- Your project pushed to GitHub/GitLab/Bitbucket
- Firebase configuration completed (for authentication)

## 🎯 Deployment Methods

### Method 1: Deploy via Netlify UI (Recommended for Beginners)

#### Step 1: Prepare Your Repository
1. Make sure all changes are committed:
```bash
git add .
git commit -m "Prepare for Netlify deployment"
git push origin main
```

#### Step 2: Connect to Netlify
1. Go to [Netlify](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose your Git provider (GitHub/GitLab/Bitbucket)
4. Authorize Netlify to access your repositories
5. Select your **JeduAI** repository

#### Step 3: Configure Build Settings
In the Netlify build settings, enter:

- **Base directory**: Leave empty (or enter `.`)
- **Build command**: `chmod +x build.sh && ./build.sh`
- **Publish directory**: `build/web`

#### Step 4: Environment Variables (Optional)
If you need to set environment variables:
1. Click **"Show advanced"**
2. Add any required environment variables
3. For example:
   - `FLUTTER_VERSION`: `3.10.0`

#### Step 5: Deploy
1. Click **"Deploy site"**
2. Wait for the build to complete (5-10 minutes for first build)
3. Your site will be live at a random Netlify URL like `random-name-123.netlify.app`

#### Step 6: Custom Domain (Optional)
1. Go to **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Follow the instructions to configure your domain

### Method 2: Deploy via Netlify CLI

#### Step 1: Install Netlify CLI
```bash
npm install -g netlify-cli
```

#### Step 2: Login to Netlify
```bash
netlify login
```

#### Step 3: Build Your Flutter App
```bash
flutter build web --release --web-renderer canvaskit
```

#### Step 4: Deploy
```bash
# Deploy to a draft URL
netlify deploy

# When ready, deploy to production
netlify deploy --prod
```

Follow the prompts:
- **Publish directory**: `build/web`

### Method 3: Manual Drag & Drop

#### Step 1: Build Locally
```bash
flutter build web --release --web-renderer canvaskit
```

#### Step 2: Deploy
1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag and drop the `build/web` folder
3. Your site will be deployed instantly!

## ⚙️ Configuration Files

The following files have been created for you:

### `netlify.toml`
- Configures build settings
- Sets up redirects for Flutter routing
- Adds security headers
- Optimizes caching

### `build.sh`
- Installs Flutter if needed
- Builds the web app
- Handles all build steps automatically

### `.nvmrc`
- Specifies Node.js version for Netlify

## 🔧 Important Configuration

### Firebase Configuration
Make sure your Firebase configuration is properly set up:

1. Check `lib/firebase_options.dart` exists
2. Verify Firebase is initialized in `lib/main.dart`
3. Update Firestore security rules to allow web domain

### Web Renderer
The build uses `canvaskit` renderer for better performance. If you prefer HTML renderer:
```bash
flutter build web --release --web-renderer html
```

## 🌐 Post-Deployment Steps

### 1. Update Firebase Authorized Domains
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to **Authentication** → **Settings** → **Authorized domains**
4. Add your Netlify domain (e.g., `your-app.netlify.app`)

### 2. Test Your Deployment
Visit your Netlify URL and test:
- ✅ Login/Signup functionality
- ✅ Navigation between pages
- ✅ AI features (Gemini API)
- ✅ Video translation
- ✅ All user roles (Student, Staff, Admin)

### 3. Configure Custom Domain (Optional)
1. In Netlify dashboard, go to **Domain settings**
2. Add your custom domain
3. Update DNS records as instructed
4. Enable HTTPS (automatic with Netlify)

## 🐛 Troubleshooting

### Build Fails
**Issue**: Flutter not found or build errors

**Solution**:
1. Check `build.sh` has execute permissions
2. Verify Flutter version compatibility
3. Check build logs in Netlify dashboard

### Blank Page After Deployment
**Issue**: App loads but shows blank page

**Solution**:
1. Check browser console for errors
2. Verify `base href` in `web/index.html`
3. Check Firebase configuration
4. Ensure all assets are included in build

### Firebase Authentication Not Working
**Issue**: Can't login on deployed site

**Solution**:
1. Add Netlify domain to Firebase authorized domains
2. Check Firebase API keys are correct
3. Verify CORS settings

### Routing Issues
**Issue**: Direct URLs don't work (404 errors)

**Solution**:
- The `netlify.toml` file handles this with redirects
- Make sure the file is in your repository root

## 📊 Build Optimization

### Reduce Build Size
```bash
flutter build web --release --web-renderer canvaskit --tree-shake-icons
```

### Enable Compression
Netlify automatically compresses files, but you can verify in:
- **Site settings** → **Build & deploy** → **Post processing**
- Enable **Asset optimization**

## 🔄 Continuous Deployment

Netlify automatically rebuilds when you push to your repository:

1. Make changes to your code
2. Commit and push:
```bash
git add .
git commit -m "Update feature"
git push origin main
```
3. Netlify automatically detects the push and rebuilds
4. Your site updates in 5-10 minutes

## 📈 Monitoring

### Build Status
- Check build logs in Netlify dashboard
- Set up build notifications via email/Slack

### Analytics
- Enable Netlify Analytics (paid feature)
- Or integrate Google Analytics in your Flutter app

## 🎉 Success Checklist

- [ ] Repository connected to Netlify
- [ ] Build completes successfully
- [ ] Site is accessible via Netlify URL
- [ ] Firebase authentication works
- [ ] All features functional
- [ ] Custom domain configured (optional)
- [ ] HTTPS enabled
- [ ] Firebase authorized domains updated

## 🆘 Need Help?

- **Netlify Docs**: https://docs.netlify.com/
- **Flutter Web Docs**: https://docs.flutter.dev/platform-integration/web
- **Firebase Docs**: https://firebase.google.com/docs/web/setup

## 📝 Quick Commands Reference

```bash
# Build locally
flutter build web --release

# Deploy with Netlify CLI
netlify deploy --prod

# Check build status
netlify status

# View site logs
netlify logs

# Open site in browser
netlify open:site
```

---

**🎓 Your JeduAI app is now live on Netlify!**

Share your deployment URL with users and enjoy your Flutter web app in production! 🚀
