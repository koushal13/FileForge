# 🚀 Quick Deploy Guide

## Deploy to Railway (Recommended - Easiest!)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/koushal13/FileForge)

1. Click the "Deploy on Railway" button above
2. Sign in with GitHub
3. Click "Deploy Now"
4. Wait 2-3 minutes for deployment
5. Your app will be live at `https://your-app.railway.app`

**Cost:** $5 free credits/month (enough for personal use)

---

## Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click "Deploy to Render" button
2. Connect your GitHub account
3. Select this repository
4. Click "Create Web Service"
5. Wait for build to complete

**Cost:** Free tier available (auto-sleeps after inactivity)

---

## Deploy to Fly.io (100% Free Tier)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch app (from project directory)
fly launch

# Deploy
fly deploy
```

**Cost:** Free tier includes 3 shared-cpu VMs

---

## Deploy with Docker

```bash
# Build the image
docker build -t fileforge .

# Run locally
docker run -p 5000:5000 fileforge

# Or use Docker Compose
docker-compose up
```

---

## Self-Host on Your Server

```bash
# Clone repository
git clone https://github.com/koushal13/FileForge.git
cd FileForge

# Install dependencies
pip install -r requirements-prod.txt

# Set environment variables
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
export PORT=5000
export FLASK_ENV=production

# Run with Gunicorn
gunicorn --bind 0.0.0.0:$PORT --workers 4 web_app:app
```

---

## Environment Variables

All platforms support these optional environment variables:

- `SECRET_KEY` - Flask secret key (auto-generated if not set)
- `PORT` - Server port (defaults to 5000)
- `FLASK_ENV` - Set to `production` for production mode

---

## Next Steps After Deployment

1. ✅ Test your deployment by uploading a file
2. 🔒 Set up a custom domain (optional)
3. 📊 Monitor your app's health
4. ⭐ Star the repo and share with friends!

Need help? [Open an issue](https://github.com/koushal13/FileForge/issues)
