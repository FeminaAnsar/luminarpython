var clk = document.querySelector("#clk")

clk.addEventListener("click", () => {
    clk.textContent = "clicked once";
    clk.style.color = "red";
})
var dbl=document.querySelector("#dbl")
dbl.addEventListener("dblclick",()=>{
    dbl.textContent="Double clicked";
    dbl.style.color="green";
})
var ove=document.querySelector("#ove")
ove.addEventListener("mouseover",()=>{
    ove.textContent="Mouse over me";
    ove.style.color="blue";
})
ove.addEventListener("mouseout",()=>{
    ove.textContent="Mouse not over me";
    ove.style.color="cyan";
})
