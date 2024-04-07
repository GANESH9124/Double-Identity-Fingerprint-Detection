document.addEventListener("DOMContentLoaded", function() {
    var statusMessage = document.getElementById("status-message");

    // Function to display the alert message
    function showAlterationMessage() {
        statusMessage.innerHTML = '<h3>Username Not Found</h3><p style= background-color: #f8d7da; color: #721c24; padding: 15px; text-size: 10px; border-radius: 5px;">The Username provided does not match any records in the database. Please ensure that the username is entered correctly.</p>';
    }

    // Start loading animation
    function showLoadingAnimation() {
        var loadingText = "Verifying fingerprint";
        var dots = "";
        var intervalId = setInterval(function() {
            if (dots.length < 3) {
                dots += ".";
            } else {
                dots = "";
            }
            statusMessage.textContent = loadingText + dots;
        }, 500);

        return intervalId;
    }

    // Start loading animation
    var intervalId = showLoadingAnimation();

    // Stop loading animation after 3 seconds and show alteration message
    setTimeout(function() {
        clearInterval(intervalId);
        showAlterationMessage();
    }, 3000); // Stop after 3 seconds
});
