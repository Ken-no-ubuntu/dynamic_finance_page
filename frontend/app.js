const API_URL = "http://localhost:8080";

const list = document.getElementById("transactions");
const form = document.getElementById("transaction-form");

async function loadTransactions() {
  const res = await fetch(`${API_URL}/transactions`);
  const data = await res.json();

  list.innerHTML = "";
  data.forEach(tx => {
    const li = document.createElement("li");
    li.textContent = `${tx.description}: $${tx.amount}`;
    list.appendChild(li);
  });
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const amount = parseFloat(document.getElementById("amount").value);
  const description = document.getElementById("description").value;

  await fetch(`${API_URL}/transactions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, description })
  });

  form.reset();
  loadTransactions();
});

loadTransactions();
