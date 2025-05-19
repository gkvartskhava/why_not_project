

const loginForm = document.getElementById("login-form");
const baseEndpoint = "http://localhost:8000/api";

if(loginForm){
    loginForm.addEventListener("submit",print)
}

function print(event){
    console.log("Hello World");
}

function handleLogin(event){
    event.preventDefault();
    console.log(event);
    
    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    console.log(loginObjectData)
    const options = {
        method: 'POST',
        headers : {
            'Content-Type': 'application/json',
        },
        body:''
    }
    fetch(loginEndpoint,options)

}

