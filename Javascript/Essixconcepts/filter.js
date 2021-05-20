var arr=[101,202,330,40,51,45,67,88,98,68]
//arr.filter(num=>num%2==0).forEach(num=>console.log(num))
//arr.sort((no1,no2)=>no1-no2).forEach(num=>console.log(num))
arr.sort((no1,no2)=>no1>no2?1:-1).forEach(no=>console.log(no))