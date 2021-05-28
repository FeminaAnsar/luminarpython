
class Bank {
    static accountDetails() {
        let userData = {
            1000: { accno: 1000, password: "user1", balance: 5000 },
            1001: { accno: 1001, password: "user2", balance: 5035 },
            1002: { accno: 1002, password: "user3", balance: 10000 },
            1003: { accno: 1003, password: "user4", balance: 2000 },
            1004: { accno: 1004, password: "user5", balance: 9000 }
        }
        return userData
    }
    static authenticate(acno, password) {
        var dataset = Bank.accountDetails()
        if (acno in dataset) {
            if (password == dataset[acno]["password"]) {
                //successful authentication
                return 1
            }
            else {
                //invalid password
                return 0
            }

        }
        else {
            //invalid accno
            return -1
        }
    }
    static setStorage(acntno,pswd){
       let obj={
           actno:acntno,
           pswd:pswd
       }
       localStorage.setItem("data",JSON.stringify(obj))
    }
    static login() {
        var accno = document.querySelector("#acno").value
        var password = document.querySelector("#pwd").value
        let user = Bank.authenticate(accno, password) //0,1,-1
        if (user == 0) {
            alert("Invalid Password")
        }
        else if (user == 1) {
            alert("Success")
            Bank.setStorage(accno,password)
            window.location.href = "home.html"
        }
        else if (user == -1) {
            alert("Invalid Account Number")
        }
    }
    static withdrawal() {
        let detail = Bank.accountDetails()
        var accno = document.querySelector("#acno").value
        var password = document.querySelector("#pwd").value
        let amount = document.querySelector("#amount").value
        let user = Bank.authenticate(accno, password)
        if (user == 0) {
            alert("Incorrect password")
        }
        else if (user == 1) {
            if (amount > detail[accno]["balance"]) {
                alert("Insufficient balance. Current balance is Rs " + detail[accno]["balance"])
            }
            else {
                let bal = detail[accno]["balance"] - amount
                alert(" Rs " + amount + " successfully debited and current balance is Rs " + bal)
            }
        }
        else if (user == -1) {
            alert("Invalid Account Number")
        }

    }

    static deposit() {

        let detail = Bank.accountDetails()
        var accno = document.querySelector("#acno").value
        var password = document.querySelector("#pwd").value
        let amount = document.querySelector("#amount").value
        let user = Bank.authenticate(accno, password)
        if (user == 0) {
            alert("Invalid password")
        }
        else if (user == 1) {
            let bal=detail[accno]["balance"]+amount
            
            alert("Rs "+amount+" deposited")
        }
        else if (user == -1) {
            alert("Invalid Account number")
        }
    }
}