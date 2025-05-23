document.getElementById("analyze-btn").addEventListener("click", function () {
    let textInput = document.getElementById("text-input");
    let resultDiv = document.getElementById("result");
    let analyzeBtn = document.getElementById("analyze-btn");
    
    let text = textInput.value.trim();
    if (text === "") {
        alert("Please enter a sentence!");
        return;
    }

    // Show loading message and disable button
    resultDiv.innerHTML = "<h3>Analyzing...</h3>";
    analyzeBtn.disabled = true;

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `<h3>Sentiment: ${data.sentiment}</h3>`;
    })
    .catch(error => {
        resultDiv.innerHTML = `<h3 style="color: red;">Error analyzing sentiment.</h3>`;
        console.error("Error:", error);
    })
    .finally(() => {
        analyzeBtn.disabled = false; // Re-enable button after response
    });
});
