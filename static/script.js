document.querySelector('form').addEventListener('submit', function(event) {
    const minRating = parseFloat(document.getElementById('min_rating').value);
    const maxRating = parseFloat(document.getElementById('max_rating').value);

    // Check if ratings are within the valid range (1-10) and if minRating is less than maxRating
    if (minRating < 1 || minRating > 10 || maxRating < 1 || maxRating > 10 || minRating > maxRating) {
        alert("Please enter a valid rating range (1 to 10) and ensure the min rating is less than the max rating.");
        event.preventDefault(); 
    }
});
