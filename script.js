function processJSON(){

let input = document.getElementById("jsonInput").value

fetch("/process",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:input

})

.then(response => response.json())

.then(data => {

document.getElementById("result").innerText =
JSON.stringify(data,null,2)

})

}
