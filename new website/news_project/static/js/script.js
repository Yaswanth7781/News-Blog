// This file can be used for future client-side interactivity.
// For now, the site is mostly server-rendered by Django.

document.addEventListener('DOMContentLoaded', function() {
    console.log("PYR News website loaded.");

    // Simple animation for article cards on load
    const cards = document.querySelectorAll('.article-card');
    cards.forEach((card, index) => {
        card.style.animation = `fadeInUp 0.5s ease-out ${index * 0.1}s forwards`;
        card.style.opacity = 0;
    });
});

// Add a keyframe animation rule to the stylesheet
const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = `
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
`;
document.head.appendChild(styleSheet);