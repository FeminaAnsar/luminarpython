var number=50;
var flag=0;
for(let i=2;i<16;i++){
    if(number%i==0){
        flag=flag+1;
        break
    }
    else{
        flag=0;
    }
}
if(flag==0){
    console.log("Prime");
}
else{
    console.log("Not Prime");
}