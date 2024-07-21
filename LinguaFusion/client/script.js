const inputForm = document.getElementById('input-form');
const inputText = document.getElementById('input-text');
const submitBtn = document.getElementById('submit-btn');
const outputContainer = document.getElementById('output-container');

submitBtn.addEventListener('click', async (e) => {
  e.preventDefault();
  const text = inputText.value.trim();
  if (text) {
    try {
      const response = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const result = await response.json();
      outputContainer.innerHTML = `
        <h2 class="output-header">Analysis Result</h2>
        <p class="output-text">Sentiment: ${result.sentiment}</p>
        <p class="output-text">Entities: ${result.entities.join(', ')}</p>
      `;
    } catch (error) {
      console.error(error);
      outputContainer.innerHTML = `<p class="output-text">Error: ${error.message}</p>`;
    }
  }
});