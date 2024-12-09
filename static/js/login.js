const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const passwordInput = document.querySelector('input[name="password1"]');
const confirmPasswordInput = document.querySelector('input[name="password2"]');
const form = document.querySelector('form.sign-in-form'); // 确保选择的是注册表单

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

form.addEventListener("submit", function(event) {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;
    const initialErrorText = "Passwords do not match";

    if (password !== confirmPassword) {
        event.preventDefault();
        displayErrorInInput(confirmPasswordInput, initialErrorText);
    }
});

function displayErrorInInput(inputElement, errorText) {
    const errorSpan = document.createElement("span");
    errorSpan.textContent = errorText;
    errorSpan.style.color = "red";
    errorSpan.style.fontWeight = "bold";
    errorSpan.style.fontSize = "0.8em";
    errorSpan.style.position = "absolute";

    const inputParent = inputElement.parentNode;
    inputParent.style.position = "relative";
    inputParent.appendChild(errorSpan);

    setTimeout(() => {
        errorSpan.remove();
    }, 1000);
}