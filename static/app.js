const toast = document.getElementById("toast");
function showToast(message) { toast.textContent = message; toast.classList.add("visible"); window.setTimeout(() => toast.classList.remove("visible"), 2800); }
document.getElementById("deployButton").addEventListener("click", () => showToast("Deployment draft created. Connect your CI provider to continue."));
document.getElementById("runbookButton").addEventListener("click", () => showToast("Opening the incident response runbook..."));