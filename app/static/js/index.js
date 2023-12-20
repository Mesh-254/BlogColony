// Function to truncate paragraphs with class 'card-text'
function truncateParagraph() {
    // Get all elements with class 'card-text'
    let content = document.getElementsByClassName('card-text');

    // Maximum number of words
    const maxWords = 30;

    // Loop through each element
    for (let i = 0; i < content.length; i++) {
        // Get the text content of the current element
        let text = content[i].textContent;

        // Split the paragraph into an array of words
        let words = text.split(" ");

        // Truncate the first 'maxWords' words and join them back into a string
        let truncatedText = words.slice(0, maxWords).join(" ");

        // Display the truncated text in the current element
        content[i].textContent = truncatedText;
    }
}

// Run the truncateParagraph function when the window has loaded
window.onload = function() {
    truncateParagraph();
};
