export class ValidateModule {

    constructor() {
        this.namesRegex = /^\s*[\s\p{L}]+$/u;
        this.emailRegex = /^(?!.*\.\.)(?!\.)[-\p{L}_+%.0-9*'*\/=]+(?<!\.)@(?!-)[\p{L}-]{1,63}(?<!-)(?:\.(?!-)[\p{L}-]{1,63}(?<!-)){0,2}(\.[\p{L}]{2,}){0,2}$/u;
        this.userNameVlidator = /^(?!_)(?!-)(?!.*__)(?!.*--)[-\p{L}_0-9]{3,20}(?<!-)(?<!_)/u;
        this.passwordValidator = /^(?=.*\p{Ll})(?=.*\d)(?=.*\p{Lu})(?=.*[!@#$%.^&*])[\p{L}\d!@#$.%^&*]{8,16}$/u

        this.passwordValidations = {
            
        }
    }

    validateNames(string) {
        if (!this.namesRegex.test(string.trim())) {
            return false;
        }
        return string.trim().replace(/\s+/g, " ");
    }

    validateEmail(string) {
        if (!this.emailRegex.test(string)) {
            return false;
        }
        return string;
    }

    validateUsername(string) {
        string = string.trim()
        if(! this.userNameVlidator.test(string)){
            return false;
        }
        return string;
    }

    
    validatePassword(string) {
        if(! this.passwordValidator.test(string)){
            return false;
        }
        return string;
    }


    static showError(input, label, message = "") {
        input.style.borderColor = "red";
        input.style.backgroundColor = "#f4bebe"
        label.textContent = message;
        label.style.color = "red";
        label.style.fontSize = "12px";
    }

    static clear(input, label) {

    }

    static validateInputs(dict) {
        let status = true
        for (const key in dict) {
            const { input, label, validator, errorMessage } = dict[key];
            const result = validator(input.value)

            if (!result) {
                status = false;
                ValidateModule.showError(input, label, errorMessage)
            } else {
                input.value = result;
            }
        }
        return status;
    }

    //needs implement
    passwordValidatorHot(string){
        for (const key in this.passwordValidations) {
            console.log()
        }
        

    }


}