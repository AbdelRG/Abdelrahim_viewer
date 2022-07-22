


document.querySelectorAll(".img").forEach(item=>
 {item.addEventListener('click', event=>{
 var img2 = document.getElementById("img2");
 var imgTitle = document.getElementById("staticBackdropLabel");
 img2.src = item.src;
 path = item.src;
 imgTitle.innerHTML = item.alt;


 })});


