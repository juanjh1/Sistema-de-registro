import {ValidateModule} from "./validation-module.js"

const nameInput = document.getElementById("name")
const nameLabel = document.querySelector(`label[for="${nameInput.id}"]`);
const lastNameInput = document.getElementById("lastName")
const lastNameLabel = document.querySelector(`label[for="${lastNameInput.id}"]`);
const emailInput = document.getElementById("email")
const emailLabel = document.querySelector(`label[for="${emailInput.id}"]`);
const userInuput = document.getElementById("userName")
const userLabel = document.querySelector(`label[for="${userInuput.id}"]`);
const passwordInput = document.getElementById("password")
const passwordLabel = document.querySelector(`label[for="${passwordInput.id}"]`);
const submitBtn = document.getElementById("submitBtn")
const registerForm = document.getElementById("registerForm")
const validatorInstance = new ValidateModule()

let validationDict = {
    name: {
        input: nameInput,
        label: nameLabel,
        validator: validatorInstance.validateNames.bind(validatorInstance),
        errorMessage: "Tu nombre solo deberia contener letras"
    },
    lastName: {
        input: lastNameInput,
        label: lastNameLabel,
        validator: validatorInstance.validateNames.bind(validatorInstance),
        errorMessage: "Tu apellido solo deberia contener letras"
    },
    email: {
        input: emailInput,
        label: emailLabel,
        validator: validatorInstance.validateEmail.bind(validatorInstance),
        errorMessage: "Email invalido"
    },
      userName: {
        input: userInuput,
        label: userLabel,
        validator: validatorInstance.validateUsername.bind(validatorInstance),
        errorMessage: "Username invalido"
    },
     password: {
        input: passwordInput,
        label: passwordLabel,
        validator: validatorInstance.validatePassword.bind(validatorInstance),
        errorMessage: "Password invalido"
    }

}

submitBtn.addEventListener("click",
    (e) => {
        
        e.preventDefault()
        let isValid = ValidateModule.validateInputs(validationDict)
        
        if(isValid){
            registerForm.submit()
        }



    }
)


passwordInput.addEventListener("input", 
    ()=>{

    }
)