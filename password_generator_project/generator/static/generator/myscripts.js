
function copytext() {
    let password = document.getElementById("password");
    var temp = document.createElement("textarea");
    document.body.appendChild(temp);
    temp.value= password.innerText
    temp.select();
    document.execCommand("copy");
    document.body.removeChild(temp);
    alert("Password copied to clipboard: " + password.textContent);
}