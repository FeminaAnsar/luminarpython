var arr=[101,202,330,40,51,45,67,88,98,68]
let sum=arr.reduce((num1,num2)=>num1+num2)
console.log("sum "+sum);
let min=arr.reduce((num1,num2)=>num1<num2?num1:num2)
console.log("min "+min);