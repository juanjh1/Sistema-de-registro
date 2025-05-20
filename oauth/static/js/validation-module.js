export class ValidateModule{

    constructor(){
        this.namesRegex = /^\s*[\s\p{L}]+$/u;
    }

    validateNames(string){
        if(!this.namesRegex.test(string.trim())){
            return false; 
        }
        return string.trim.replace(/\s+/g, " ");
    }



}