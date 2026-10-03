# Vercel Deployment Guide for CodesbyFebin Portfolio

## Quick Setup (5 minutes)

### 1. Connect Repository to Vercel

1. Go to https://vercel.com/new
2. Click **"Import Project"**
3. Paste repository URL: `https://github.com/CodesbyFebin/CodesbyFebin`
4. Vercel will auto-detect the project

### 2. Configure Deployment

**Project Settings:**
- **Framework Preset:** Other (Static Site)
- **Root Directory:** `.` (current directory)
- **Build Command:** Leave empty
- **Output Directory:** Leave empty
- **Install Command:** Leave empty

**Environment Variables:** (Optional)
- None required for static portfolio

### 3. Deploy

Click **Deploy** — Vercel will:
- Deploy immediately (no build step needed)
- Provide live URL: `https://codesbyfebin.vercel.app`
- Set up automatic SSL/TLS
- Configure global CDN

---

## Update GitHub Pages DNS (Optional)

If you want to keep using `codesbyfebin.github.io` domain, configure Vercel with custom domain:

### In Vercel Dashboard:
1. Go to Project Settings → Domains
2. Click **Add Custom Domain**
3. Enter: `codesbyfebin.github.io`
4. Add DNS records as instructed by Vercel

**OR** Update GitHub Pages source:
- Go to GitHub Repo → Settings → Pages
- Set Source to: None (if using Vercel only)

---

## Live Status

### URLs After Deployment:

- **Portfolio URL:** `https://codesbyfebin.vercel.app`
- **GitHub Pages (legacy):** `https://codesbyfebin.github.io` (still works via GitHub Pages)
- **RSS Feed:** Available at both URLs: `/feed.xml`

### Automatic Deployments

Once connected, Vercel will:
- Auto-deploy on every git push to `main` branch
- Invalidate cache instantly
- Show deployment status on GitHub PRs
- Provide preview deployments for branches

---

## Verification After Deployment

### 1. Test Live Site
```bash
curl https://codesbyfebin.vercel.app | grep "og:title"
```

### 2. Verify OG Tags
- Twitter: https://cards-dev.twitter.com/validator?url=https://codesbyfebin.vercel.app
- LinkedIn: Paste URL in post composer
- Facebook: https://developers.facebook.com/tools/debug/?url=https://codesbyfebin.vercel.app

### 3. Check RSS Feed
```bash
curl https://codesbyfebin.vercel.app/feed.xml | head -20
```

### 4. Verify Assets
- Banner: `https://codesbyfebin.vercel.app/assets/profile-header.svg`
- Pages: `https://codesbyfebin.vercel.app/portfolio.html`

---

## Performance Advantages Over GitHub Pages

| Feature | GitHub Pages | Vercel |
|---------|-------------|--------|
| Cache Invalidation | 5-15 minutes | Instant |
| Global CDN | Limited | ✓ 280+ edge locations |
| HTTPS/SSL | ✓ | ✓ (auto) |
| Caching Control | Limited | ✓ Full control via vercel.json |
| Build Speed | N/A | Instant (no build) |
| Deployments | Via branches | Automatic on push |
| Preview URLs | No | ✓ Yes, per branch |
| Status Badge | No | ✓ Yes, embeddable |

---

## Troubleshooting

### Issue: RSS feed returns 404
**Fix:** Vercel might need cache refresh
```bash
# Trigger redeploy
git commit --allow-empty -m "Trigger Vercel redeploy"
git push origin main
```

### Issue: Old content still showing
**Fix:** Clear browser cache or use incognito mode
```bash
# Or use curl without cache
curl -H "Cache-Control: no-cache" https://codesbyfebin.vercel.app
```

### Issue: Images not loading
**Fix:** Check that `assets/` directory exists
```bash
ls -la assets/
```

---

## Rollback (if needed)

If deployment goes wrong:
1. Go to Vercel Dashboard → Deployments
2. Click previous working deployment
3. Click "Promote to Production"

---

## Files Required for Deployment

```
codesbyfebin-portfolio/
├── index.html              ✓ Main landing page
├── portfolio.html          ✓ Projects showcase  
├── feed.xml               ✓ RSS feed
├── assets/
│   └── profile-header.svg ✓ Banner image
├── vercel.json            ✓ Deployment config
└── .vercelignore          ✓ Build exclusions
```

All files are present and ready for deployment.

---

## Next Steps

1. **Go to Vercel:** https://vercel.com/new
2. **Import this repository**
3. **Configure as per "Configure Deployment" section above**
4. **Click Deploy**
5. **Test live URL**
6. **Update social media profiles with Vercel URL**

---

## Support

- **Vercel Docs:** https://vercel.com/docs
- **GitHub Issue:** Create issue in this repository
- **Twitter:** @codesbyfebin

---

**Deployment Date:** 2026-10-03  
**Status:** Ready for Vercel deployment
