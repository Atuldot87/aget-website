# Asharfi Global Educational Trust — AGET Website

## 🗂️ Project Structure

```
aget/
├── app.py                  # Flask backend
├── requirements.txt
├── templates/
│   ├── base.html           # Shared layout (nav + footer)
│   ├── index.html          # Homepage
│   ├── about.html          # About Us page
│   ├── programs.html       # Programs page
│   ├── donate.html         # Donation + Receipt page
│   └── contact.html        # Contact page
└── static/
    ├── css/style.css       # Custom styles
    ├── js/main.js          # JS interactions
    └── images/
        └── logo.png        # AGET logo
```

## 🚀 Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser at
http://localhost:5000
```

## 📝 Customization Checklist

1. **Chairman Photo** — Replace the placeholder in `index.html` (Leadership section) with an `<img>` tag pointing to the chairman's actual photo.
2. **Trustee Photos** — Similarly update the two trustee placeholders.
3. **Bank Details** — In `donate.html`, replace `[Your Account Number]`, `[IFSC Code]`, `[Bank Name]`, and `[upi@bank]` with real bank info.
4. **Trust Names** — Add actual trustee names in `index.html` Leadership section.
5. **Domain** — Update canonical URLs in `base.html` to your actual domain.
6. **Email** — Replace `info@aget.org.in` with actual email addresses.
7. **80G Certificate No.** — Add once received from Income Tax Department.
8. **Payment Gateway** — For actual online payments, integrate Razorpay/PayU/CCAvenue by adding their SDK to `donate.html`.

## 🔐 Production Deployment

- Set `SECRET_KEY` to a secure random string in `app.py`
- Use gunicorn: `gunicorn -w 4 app:app`
- Add Nginx as reverse proxy
- Enable HTTPS via Let's Encrypt

## ✅ SEO Features Built-in

- Meta title, description, keywords on every page
- Open Graph + Twitter Card tags
- Schema.org structured data (EducationalOrganization)
- Canonical URLs
- Semantic HTML5 (`<section>`, `<article>`, `<nav>`, `<address>`, `<h1>-<h6>`)
- `aria-label` attributes for accessibility

## 🎨 Design

- Colors: Navy Blue (#1a3a6e) + Gold (#d4a017) on White
- Fonts: Playfair Display (serif, headings) + Nunito Sans (body)
- Fully responsive (mobile-first Tailwind CSS)
- Print-friendly donation receipt
