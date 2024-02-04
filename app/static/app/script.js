
document.addEventListener("DOMContentLoaded", function() {
  var editButton = document.getElementById("edit-button");
  var editProfileForm = document.getElementById("edit-profile-form");

  editButton.addEventListener("click", function() {
    if (editProfileForm.style.display === "none") {
      editProfileForm.style.display = "block";
    } else {
      editProfileForm.style.display = "none";
      
      editProfileForm.reset();
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("resumeForm");

  form.addEventListener("submit", function (event) {
      let valid = true;

      const errorElements = document.querySelectorAll(".error");
      errorElements.forEach((error) => (error.textContent = ""));

      const name = form.name.value;
      if (name.trim() === "") {
          valid = false;
          document.getElementById("nameError").textContent = "Name is required.";
      }

      const email = form.email.value;
      if (email.trim() === "") {
          valid = false;
          document.getElementById("emailError").textContent = "Email is required.";
      }

      const phone = form.phone.value;
      if (phone.trim() === "") {
          valid = false;
          document.getElementById("phoneError").textContent = "Phone Number is required.";
      }

      const about = form.about.value;
      if (about.trim() === "") {
          valid = false;
          document.getElementById("aboutError").textContent = "About is required.";
      }

      const skills = form.skills.value;
      if (skills.trim() === "") {
          valid = false;
          document.getElementById("skillsError").textContent = "Skills are required.";
      }

      const degree = form.degree.value;
      if (degree.trim() === "") {
          valid = false;
          document.getElementById("degreeError").textContent = "Degree is required.";
      }

      const university = form.university.value;
      if (university.trim() === "") {
          valid = false;
          document.getElementById("universityError").textContent = "University is required.";
      }

      const experience = form.experience.value;
      if (experience.trim() === "") {
          valid = false;
          document.getElementById("experienceError").textContent = "Experience is required.";
      }

      if (!valid) {
          event.preventDefault();
      }
  });
});
