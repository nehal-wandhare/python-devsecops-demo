async function checkHealth() {

    const result = document.getElementById("health-result");

    try {

        const response = await fetch("/health");

        const data = await response.json();

        result.style.display = "block";

        result.innerHTML =
            "✓ Application is healthy | " +
            "Status: " + data.status +
            " | Time: " + data.timestamp;

    } catch (error) {

        result.style.display = "block";

        result.style.background = "#fef2f2";
        result.style.color = "#b91c1c";

        result.innerHTML =
            "✕ Application health check failed";

    }
}