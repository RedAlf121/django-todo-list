document.addEventListener("DOMContentLoaded", () => {
  const card = document.querySelector(".card");
  const showSignupLink = document.getElementById("show-signup");
  const showLoginLink = document.getElementById("show-login");
  const loginForm = document.getElementById("login-form");
  const signupForm = document.getElementById("signin-form");

  showSignupLink.addEventListener("click", (e) => {
    e.preventDefault();
    card.classList.add("flipped");
  });

  showLoginLink.addEventListener("click", (e) => {
    e.preventDefault();
    card.classList.remove("flipped");
  });

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    if (username === "" || password === "") {
      alert("Required fields");
      return;
    }
    url = e.target.dataset.url;
    data = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ username, password })
    });
    if (data.status === 200) {
      result=await data.json()
      console.log(result)
      console.log('autenticado') 
      window.location.href = result.redirect_url; // Redirect to the URL provided by the server
    } else {
      console.log(data.status);
      alert("Error al eliminar la tarea");
    }
  });

  signupForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("signin-username").value;
    const email = document.getElementById("signin-email").value;
    const password = document.getElementById("signin-password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
      alert("Passwords don't match!");
      return;
    }
    url = e.target.dataset.url;
    data = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ username, email, password })
      });
    if (data.status === 200) {
        result=await data.json()
        console.log(result)
        console.log('autenticado') 
        window.location.href = result.redirect_url; // Redirect to the URL provided by the server
    } else {
      console.log(data.status);
      alert("Error al eliminar la tarea");
    }
    // Here you would typically send the signup data to your server
  });
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
