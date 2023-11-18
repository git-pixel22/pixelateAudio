// Get all elements with class "filter"
const filters = document.querySelectorAll('.filter');

// Loop through each filter element
filters.forEach(filter => {
    // Add click event listener to each filter
    filter.addEventListener('click', () => {
        // Toggle 'selected' class on click
        filter.classList.toggle('selected');
    });
});

 
 