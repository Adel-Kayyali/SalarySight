// This function toggles dark mode by adding or removing a class
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    document.documentElement.classList.toggle('dark-mode');

    // Change the icon
    var icon = document.getElementById("dark-mode-toggle").querySelector('.fas');
    if (document.body.classList.contains('dark-mode')) {
        // Change to sun icon
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    } else {
        // Change to moon icon
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    }

    // Save the dark mode preference
    saveDarkModePreference();
}

// This function saves the dark mode preference in the browser's localStorage
function saveDarkModePreference() {
    if(document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
}

// Event listener for DOMContentLoaded to ensure the script runs after the document is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    // Attach the toggle function to the dark mode toggle button
    const toggleButton = document.getElementById('dark-mode-toggle');
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleDarkMode);
    }

    // Check for saved dark mode preference in localStorage and apply it
    if(localStorage.getItem('darkMode') === 'enabled') {
        toggleDarkMode();
    }
});
