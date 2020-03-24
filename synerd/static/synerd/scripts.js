var slideIndex = 1;
var tabIndex = 1;
//showSlides(slideIndex);
//showTabs(tabIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function currentTab(n) {
    showTabs(tabIndex = n);
}

function showTabs(n) {
    var i;
    var tabs = document.getElementsByClassName("myTabs");
    var btns = document.getElementsByClassName("tab");
    if (n > tabs.length) {tabIndex = 1}
    if (n < 1) {tabIndex = tabs.length}
    for (i = 0; i < tabs.length; i++) {
        tabs[i].style.display= "none";
    }
    for (i = 0; i < btns.length; i++) {
        btns[i].className = btns[i].className.replace(" active", "");
        btns[i].style.color = "white";
    }
    tabs[tabIndex-1].style.display = "block";
    btns[tabIndex-1].className += " active";
    btns[tabIndex-1].style.color = "black";
}

function search() {
    var text = document.getElementById("searchbox");
    if (text && text.value) {
        alert("Search text validated");
    }
    else {
        alert("Please enter a search term!");
    }
}