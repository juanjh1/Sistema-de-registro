import {ValidateModule} from "./validation-module.js"

let nameInput = document.getElementById("name")
let lastNameInput = document.getElementById("lastName")
let emailInput = document.getElementById("email")
let userInuput = document.getElementById("userName")
let passwordInput = document.getElementById("password")
let submitBtn = document.getElementById("submitBtn")



submitBtn.addEventListener("click",
    (e) => {
        
        e.preventDefault()
        let validatorInstance = new ValidateModule()
        if(validatorInstance.validateNames(nameInput.value)){

        }
    }
)