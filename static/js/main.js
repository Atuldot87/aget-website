// Mobile menu toggle
document.getElementById('menuBtn')?.addEventListener('click', () => {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('hidden');
});

// Active nav link highlight
const path = window.location.pathname;
document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === path) link.classList.add('active');
});

// Navbar scroll shadow
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (nav) {
        nav.classList.toggle('shadow-lg', window.scrollY > 10);
    }
});

// Scroll reveal for sections
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('section').forEach(el => observer.observe(el));
