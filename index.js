// index.js (or main.js, or any name you prefer)

// This script assumes your Python files (word_counter.py, etc.) are in the same directory as index.html and index.js
// If they are in a different location, adjust the paths accordingly.

document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        const preElement = card.querySelector('pre');
        const projectName = card.querySelector('h2').textContent.split('. ')[1]; // Extract project name

        // Construct the filename based on the project name (lowercase, replace spaces with underscores)
        const filename = projectName.toLowerCase().replace(/ /g, '_') + '.py';

        // Fetch the Python code (adjust path if needed)
        fetch(filename)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`File ${filename} not found`);
                }
                return response.text();
            })
            .then(code => {
                preElement.textContent = code; // Display the code in the <pre> element
            })
            .catch(error => {
                preElement.textContent = `Error loading ${filename}: ${error.message}`;
                preElement.style.color = 'red'; // Style the error message
                console.error(error);
            });
    });
});