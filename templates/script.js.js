// Handle Login
function loginUser(event) {
  event.preventDefault(); // prevent form from reloading page

  let name = document.getElementById("username").value;
  let phone = document.getElementById("phone").value;

  if (name.trim() === "" || phone.trim() === "") 
    {
    alert("Please enter all details!");
    return;
  }
  

  // Store user in localStorage
  localStorage.setItem("agriUser", JSON.stringify({ name, phone }));

  alert("Login Successful ✅");
  window.location.href = "profile.html"; // redirect to profile page
}

// Load Profile Data
function loadProfile() {
  let user = JSON.parse(localStorage.getItem("agriUser"));

  if (user) {
    document.getElementById("profileName").innerText = user.name;
    document.getElementById("profilePhone").innerText = user.phone;
  } else {
    document.getElementById("profileName").innerText = "Guest";
    document.getElementById("profilePhone").innerText = "Not Logged In";
  }
}

// Logout Function
function logoutUser() {
  localStorage.removeItem("agriUser");
  alert("Logged out successfully 🚪");
  window.location.href = "login.html";
}
// Preview uploaded image
function previewImage(event) {
  let preview = document.getElementById("preview");
  let file = event.target.files[0];

  if (file) {
    preview.src = URL.createObjectURL(file); // Show chosen image
    preview.style.display = "block";
  }
}
// Preview uploaded image
function previewImage(event) {
  let preview = document.getElementById("preview");
  let file = event.target.files[0];

  if (file) {
    preview.src = URL.createObjectURL(file); // show chosen image
    preview.style.display = "block";
  }
}
// Set profile picture from uploaded file
function setProfileImage(event) {
  let file = event.target.files[0];
  let profileImg = document.getElementById("profileImage");

  if (file) {
    profileImg.src = URL.createObjectURL(file);

    // Save to localStorage so it stays after refresh
    localStorage.setItem("profilePic", profileImg.src);
  }
}

// Load saved profile picture on page load
window.onload = function () {
  let savedPic = localStorage.getItem("profilePic");
  if (savedPic) {
    document.getElementById("profileImage").src = savedPic;
  }
};
// Set profile picture from uploaded file
function setProfileImage(event) {
  let file = event.target.files[0];
  let profileImg = document.getElementById("profileImage");

  if (file) {
    profileImg.src = URL.createObjectURL(file);

    // Save to localStorage so it stays after refresh
    localStorage.setItem("profilePic", profileImg.src);
  }
}

// Load saved profile picture on page load
window.onload = function () {
  let savedPic = localStorage.getItem("profilePic");
  if (savedPic) {
    document.getElementById("profileImage").src = savedPic;
  }
  
};

