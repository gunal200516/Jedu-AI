# 🌐 Netlify Deployment Files

This folder contains all the necessary files to deploy your JeduAI Flutter web app to Netlify.

## 📁 Files Overview

### Configuration Files

1. **`netlify.toml`**
   - Main Netlify configuration file
   - Defines build command and publish directory
   - Sets up redirects for Flutter routing
   - Configures security headers and caching

2. **`build.sh`**
   - Automated build script
   - Installs Flutter if needed
   - Runs the web build process
   - Handles all build steps

3. **`.nvmrc`**
   - Specifies Node.js version (18)
   - Ensures consistent build environment

### Documentation Files

1. **`NETLIFY_QUICK_START.md`**
   - ⚡ 5-minute deployment guide
   - Three deployment methods
   - Quick post-deployment steps

2. **`NETLIFY_DEPLOYMENT_GUIDE.md`**
   - 📚 Complete deployment documentation
   - Detailed step-by-step instructions
   - Troubleshooting guide
   - Configuration examples

3. **`DEPLOYMENT_CHECKLIST.md`**
   - ✅ Comprehensive checklist
   - Pre-deployment tasks
   - Deployment steps
   - Post-deployment testing
   - Optimization tips

## 🚀 Quick Start

### Fastest Deployment (3 Steps)

1. **Push to GitHub**:
```bash
git add .
git commit -m "Deploy to Netlify"
git push origin main
```

2. **Connect to Netlify**:
   - Go to https://app.netlify.com/
   - Click "Add new site" → "Import an existing project"
   - Select your repository

3. **Configure & Deploy**:
   - Build command: `flutter build web --release --web-renderer canvaskit`
   - Publish directory: `build/web`
   - Click "Deploy site"

**Done!** Your app will be live in 5-10 minutes.

## 📖 Which Guide to Use?

- **New to Netlify?** → Start with `NETLIFY_QUICK_START.md`
- **Want detailed instructions?** → Read `NETLIFY_DEPLOYMENT_GUIDE.md`
- **Need a checklist?** → Use `DEPLOYMENT_CHECKLIST.md`

## 🔧 Build Commands

### Local Build Test
```bash
flutter build web --release --web-renderer canvaskit
```

### Deploy with Netlify CLI
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod
```

### Manual Drag & Drop
```bash
flutter build web --release
# Then drag build/web to https://app.netlify.com/drop
```

## ⚙️ Configuration

### Build Settings in Netlify UI
- **Build command**: `flutter build web --release --web-renderer canvaskit`
- **Publish directory**: `build/web`
- **Base directory**: (leave empty)

### Environment Variables (Optional)
- `FLUTTER_VERSION`: `3.10.0`

## 🔥 Post-Deployment

### 1. Update Firebase
Add your Netlify domain to Firebase authorized domains:
- Firebase Console → Authentication → Settings → Authorized domains
- Add: `your-app.netlify.app`

### 2. Test Your App
- Visit your Netlify URL
- Test login/signup
- Verify all features work

### 3. Custom Domain (Optional)
- Netlify dashboard → Domain settings
- Add your custom domain
- Update DNS records

## 🐛 Common Issues

### Build Fails
- Check Flutter version compatibility
- Verify `build.sh` has execute permissions
- Review build logs in Netlify dashboard

### Blank Page
- Check browser console for errors
- Verify Firebase configuration
- Ensure all assets are included

### Authentication Not Working
- Add Netlify domain to Firebase authorized domains
- Check Firebase API keys
- Verify CORS settings

## 📊 Monitoring

### Check Build Status
```bash
netlify status
```

### View Logs
```bash
netlify logs
```

### Open Site
```bash
netlify open:site
```

## 🎯 Success Checklist

- [ ] Site is live at Netlify URL
- [ ] Login/authentication works
- [ ] All pages load correctly
- [ ] Firebase integration working
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Custom domain configured (optional)

## 📞 Support

- **Netlify Docs**: https://docs.netlify.com/
- **Flutter Web Docs**: https://docs.flutter.dev/platform-integration/web
- **Firebase Docs**: https://firebase.google.com/docs/web/setup

## 🎉 Ready to Deploy?

Choose your method:
1. **Easiest**: Netlify UI with GitHub
2. **Fastest**: Drag & Drop
3. **Most Control**: Netlify CLI

See `NETLIFY_QUICK_START.md` to get started!

---

**Made with ❤️ for JeduAI - Smart Learning Platform**
