var firststep = document.getElementById("consaltation-choise");
var diabetes = document.querySelector(".diabetes");
var heart = document.getElementById("heart");
var consaltation = document.getElementById("consaltation");
var closeForm = document.querySelector(".close");
var backMain = document.getElementById("back");
var popup = document.getElementById("popup");

// hide forms
heart.style.display = "none";
document.querySelector(".diabetes").style.display = "none";
firststep.style.display = "none";
closeForm.style.display= "none";
backMain.style.display= "none";
popup.style.display="none";

// show next step
consaltation.onclick = function(){
    firststep.style.display = "block";
    closeForm.style.display= "block";
   
}

// show daibetes form 
function diabetesForm(){
    heart.style.display = "none";
    firststep.style.display = "none";
    diabetes.style.display = "block";
    backMain.style.display= "block";
}

// show heart form
function heartForm(){
    diabetes.style.display = "none";
    firststep.style.display = "none";
    heart.style.display = "block";
    backMain.style.display= "block";
}

// closs popup form 
  function close() {
    heart.style.display = "none";
    diabetes.style.display = "none";
    firststep.style.display = "none";
    closeForm.style.display= "none";
    backMain.style.display = "none";
    popup.style.display= "none";
}

// to back to main 
backMain.onclick = function(){
    heart.style.display = "none";
    diabetes.style.display = "none";
    firststep.style.display = "block";
    backMain.style.display = "none";
    
}