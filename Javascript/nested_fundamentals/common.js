var arr1=[10,20,30,40]
var arr2=[21,22,30,31,40]
for(let i of arr1){
    for(let j of arr2){
        if(i==j){
            console.log(i);
        }
    }
}