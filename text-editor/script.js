// Function to execute commands like bold, italic, underline
function execCommand(command) {
    document.execCommand(command, false, null);
}

// Optional: Add an event listener to show the current style of selected text
document.getElementById('editor').addEventListener('mouseup', function() {
    const selection = window.getSelection();
    console.log(`Selected text: ${selection.toString()}`);
});
