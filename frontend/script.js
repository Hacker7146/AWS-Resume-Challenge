const apiUrl = window.VISITOR_COUNTER_API_URL || "";

async function updateVisitorCount() {
  const counterElement = document.getElementById("visitor-count");

  if (!apiUrl) {
    counterElement.textContent = "API not configured";
    return;
  }

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    const payload = await response.json();
    counterElement.textContent = payload.count;
  } catch (error) {
    console.error("Unable to update visitor count", error);
    counterElement.textContent = "unavailable";
  }
}

updateVisitorCount();
