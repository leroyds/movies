document.addEventListener('DOMContentLoaded',getRatings)

function getRatings(){
const starsTotal = 5
let avgRating = document.getElementById("myVar").value;

const starPercentage = (avgRating/starsTotal)*100;
const starPercentageRounded = `${Math.round(starPercentage/10)*10}%`;
document.querySelector(`.stars-inner`).style.width = starPercentageRounded;
console.log(starPercentageRounded);

let userRating = document.getElementById("userCommentRatingValue").value;
let userRatingPK = document.getElementById("userCommentRatingPK").value;
let userRatingPercentage =  `${Math.round(((userRating/starsTotal)*100)/10)*10}%`;
console.log(userRatingPercentage);
document.querySelector(`.${userRatingPK} .stars-inner`).style.width = userRatingPercentage;

let commentsObject = document.getElementById("commentsObject").value;
console.log(commentsObject);
}