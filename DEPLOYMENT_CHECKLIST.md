# ✅ Netlify Deployment Checklist

## Pre-Deployment

### 1. Code Preparation
- [ ] All changes committed to Git
- [ ] Code tested locally with `flutter run -d chrome`
- [ ] No console errors in browser
- [ ] All features working properly

### 2. Configuration Files
- [x] `netlify.toml` created (build settings & redirects)
- [x] `build.sh` created (build script)
- [x] `.nvmrc` created (Node.js version)
- [ ] `lib/firebase_options.dart` exists and configured
- [ ] API keys configured in `lib/config/` files

### 3. Firebase Setup
- [ ] Firebase project created
- [ ] Authentication enabled (Email/Password)
- [ ] Firestore database created
- [ ] Security rules configured
- [ ] Firebase config added to Flutter app

### 4. Build Test
```bash
# Test build locally
flutter build web --release --web-renderer canvaskit
```
- [ ] Build completes without errors
- [ ] Output in `build/web/` folder
- [ ] Test the build: `flutter run -d chrome --release`

## Deployment Steps

### Method 1: Netlify UI (Recommended)

#### Step 1: Push to Repository
```bash
git add .
git commit -m "Deploy to Netlify"
git push origin main
```
- [ ] Code pushed to GitHub/GitLab/Bitbucket

#### Step 2: Connect to Netlify
- [ ] Logged into https://app.netlify.com/
- [ ] Clicked "Add new site" → "Import an existing project"
- [ ] Connected Git provider
- [ ] Selected JeduAI repository

#### Step 3: Configure Build
- [ ] Build command: `flutter build web --release --web-renderer canvaskit`
- [ ] Publish directory: `build/web`
- [ ] Clicked "Deploy site"

#### Step 4: Wait for Build
- [ ] Build started (check build logs)
- [ ] Build completed successfully
- [ ] Site is live at Netlify URL

### Method 2: Netlify CLI

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
- [ ] CLI installed
- [ ] Logged in
- [ ] Deployed successfully

### Method 3: Drag & Drop

```bash
flutter build web --release
```
- [ ] Built locally
- [ ] Dragged `build/web` to https://app.netlify.com/drop
- [ ] Site deployed

## Post-Deployment

### 1. Firebase Configuration
- [ ] Opened Firebase Console
- [ ] Went to Authentication → Settings → Authorized domains
- [ ] Added Netlify domain (e.g., `your-app.netlify.app`)
- [ ] Saved changes

### 2. Testing
Visit your Netlify URL and test:

#### Authentication
- [ ] Login page loads
- [ ] Can create new account
- [ ] Can login with existing account
- [ ] Can logout
- [ ] Password reset works (if implemented)

#### Student Portal
- [ ] Dashboard loads
- [ ] Can view assessments
- [ ] AI Tutor works
- [ ] Translation features work
- [ ] Video player works
- [ ] Media translation works

#### Staff Portal
- [ ] Dashboard loads
- [ ] Can create assessments
- [ ] Can view students
- [ ] AI assessment generator works
- [ ] Analytics display correctly

#### Admin Portal
- [ ] Dashboard loads
- [ ] Can view all users
- [ ] Can manage staff
- [ ] Can manage students
- [ ] System monitor works

#### General Features
- [ ] Navigation works (all routes)
- [ ] Images load correctly
- [ ] Icons display properly
- [ ] Animations work smoothly
- [ ] No console errors
- [ ] Mobile responsive
- [ ] PWA installable

### 3. Performance Check
- [ ] Page load time < 3 seconds
- [ ] No layout shifts
- [ ] Smooth animations
- [ ] Fast navigation

### 4. SEO & Metadata
- [ ] Page title correct
- [ ] Meta description set
- [ ] Favicon displays
- [ ] Social media preview works

### 5. Custom Domain (Optional)
- [ ] Domain purchased
- [ ] Added to Netlify
- [ ] DNS configured
- [ ] HTTPS enabled
- [ ] Domain added to Firebase authorized domains

### 6. Monitoring Setup
- [ ] Build notifications enabled
- [ ] Error tracking configured (optional)
- [ ] Analytics added (optional)

## Troubleshooting

### Build Fails
- [ ] Check build logs in Netlify dashboard
- [ ] Verify Flutter version compatibility
- [ ] Check `build.sh` permissions
- [ ] Test build locally first

### Blank Page
- [ ] Check browser console for errors
- [ ] Verify Firebase configuration
- [ ] Check `base href` in `web/index.html`
- [ ] Ensure all assets included

### Authentication Issues
- [ ] Netlify domain added to Firebase
- [ ] Firebase API keys correct
- [ ] CORS configured properly

### Routing Issues
- [ ] `netlify.toml` in repository root
- [ ] Redirects configured correctly

## Optimization

### Performance
- [ ] Enable asset optimization in Netlify
- [ ] Compress images
- [ ] Tree-shake icons: `flutter build web --tree-shake-icons`
- [ ] Use canvaskit renderer for better performance

### Caching
- [ ] Headers configured in `netlify.toml`
- [ ] Static assets cached properly
- [ ] Service worker configured (optional)

### Security
- [ ] HTTPS enabled (automatic with Netlify)
- [ ] Security headers set
- [ ] Firebase security rules configured
- [ ] API keys secured

## Continuous Deployment

- [ ] Auto-deploy on push enabled
- [ ] Branch deploys configured (optional)
- [ ] Deploy previews enabled (optional)

## Documentation

- [ ] Deployment URL documented
- [ ] Admin credentials shared securely
- [ ] User guide updated
- [ ] API documentation updated

## Success Criteria

- [x] Site is live and accessible
- [ ] All features working
- [ ] No critical errors
- [ ] Performance acceptable
- [ ] Users can access the app
- [ ] Firebase integration working

## 🎉 Deployment Complete!

**Your JeduAI app is now live on Netlify!**

**Site URL**: _________________________

**Deployed on**: _________________________

**Deployed by**: _________________________

---

## Quick Commands

```bash
# Check site status
netlify status

# View logs
netlify logs

# Open site
netlify open:site

# Redeploy
netlify deploy --prod

# Check build
flutter build web --release
```

## Support Resources

- **Netlify Docs**: https://docs.netlify.com/
- **Flutter Web**: https://docs.flutter.dev/platform-integration/web
- **Firebase**: https://firebase.google.com/docs/web/setup
- **Project Docs**: See `NETLIFY_DEPLOYMENT_GUIDE.md`
