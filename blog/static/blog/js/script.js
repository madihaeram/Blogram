// script.js

// Example JavaScript code to add interactivity

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and DOM is ready.');
    
    // Example: Add a click event to all buttons with the class 'btn'
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    });
});
