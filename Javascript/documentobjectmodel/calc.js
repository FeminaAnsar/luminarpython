function disBox(num){
    var res=document.querySelector(".control")
    res.value+=num
}

function equals(){
    var res=document.querySelector(".control").value
    var out=eval(res)
    document.querySelector(".control").value=out

}

function del(){
    var res=document.querySelector(".control").value 
    var data=res.slice(0,-1)
    document.querySelector(".control").value=data
}