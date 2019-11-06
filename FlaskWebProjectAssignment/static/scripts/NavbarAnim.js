// When the user scrolls down 200px from the top of the document, resize the header's font size
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        document.getElementById("header").style.fontSize = "10px";
        document.getElementById("header").style.background = "rgba(184, 131, 222,0.4)"
        document.getElementById("header").style.paddingTop = "5px"
        document.getElementById("header").style.paddingBottom = "5px"
       
    } else {
        document.getElementById("header").style.fontSize = "20px";
        document.getElementById("header").style.background = "rgba(131, 4, 138,0.9)"
        document.getElementById("header").style.paddingTop = "10px"
        document.getElementById("header").style.paddingBottom = "10px"
       
        
    }
}