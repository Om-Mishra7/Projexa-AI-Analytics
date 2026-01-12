async function loadEvents() {
  const res = await fetch("/api/v1/events/recent");
  const events = await res.json();

  const root = document.getElementById("events");
  root.innerHTML = "";

  events.forEach((e) => {
    const div = document.createElement("div");
    div.className = "event";

    div.innerHTML = `
      <div class="type">${e.type}</div>
      <div class="meta">${new Date(e.timestamp).toISOString()}</div>
      <div class="data">${JSON.stringify(e.data, null, 2)}</div>
    `;

    root.appendChild(div);
  });
}

loadEvents();
setInterval(loadEvents, 5000);
