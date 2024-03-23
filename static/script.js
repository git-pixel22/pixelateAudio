document.getElementById('file-upload').addEventListener('change', function(e) {
    var fileName = e.target.files[0].name;
    document.getElementById('file-name').textContent = fileName ? fileName : "No file chosen";
});
