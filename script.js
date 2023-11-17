document.querySelectorAll('.filter').forEach(filter => {
    filter.addEventListener('click', () => {
        filter.style.backgroundColor = 'lightblue';
    });
 });
 
 document.querySelector('#audio-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const audioFile = document.querySelector('#audio-file').files[0];
    const selectedFilters = Array.from(document.querySelectorAll('.filter')).filter(filter => filter.style.backgroundColor === 'lightblue').map(filter => filter.id);
    // Send audioFile and selectedFilters to the backend server for processing
 });
 