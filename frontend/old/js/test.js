const testBtn = document.getElementsByClassName('test');
const hoverOnImg = document.getElementsByClassName('test2');
testBtn[0].addEventListener('click', function(){
    console.log("clicked");
    alert("clicked test")
})

hoverOnImg[0].addEventListener('mouseover', function(){
    confirm("Hovered over the search");
})


// function hooping(){
//     confirm("hooping high")
// }