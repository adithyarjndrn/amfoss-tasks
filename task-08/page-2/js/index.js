function addtolocalstorage(){
    var add=prompt("Type something to add to local storage");
    localStorage.setItem("something",add);
}

function currenttime(){
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    alert(time);
}

var i=0;
function changebackground(){
    colors=["green","black","white","yellow","grey","blue"]
    var c=colors[i];
    document.getElementById("screen").style.background = c; 
    i+=1;
    if (i==5){
        i=0;
    }
}