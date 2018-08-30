document.addEventListener('DOMContentLoaded',getRatings)

function getRatings(){
const starsTotal = 5

for(i=0;i<commentRating.length;i++){
    commentRating[i]=commentRating[i].toString();
    commentRatingPk[i]=commentRatingPk[i].toString();
    console.log(commentRating[i]+' '+commentRatingPk[i]);

    // let userRating = document.getElementById("userCommentRatingValue").value;
    // let userRatingPK = document.getElementById("userCommentRatingPK").value;
    let userRatingPercentage =  `${Math.round(((commentRating[i]/starsTotal)*100)/10)*10}%`;
    console.log(userRatingPercentage);
    document.querySelector(`.${commentRatingPk[i]} .stars-inner`).style.width = userRatingPercentage;
}


let avgRating = document.getElementById("myVar").value;

let commentsObject = document.getElementById("commentsCount").value;
for (i = 0; i < commentsObject; i++) { 
    console.log(i);
    let userRating = document.getElementById("userCommentRatingValue").value;
let userRatingPK = document.getElementById("userCommentRatingPK").value;
let userRatingPercentage =  `${Math.round(((userRating/starsTotal)*100)/10)*10}%`;
console.log(userRatingPercentage);
document.querySelector(`.${userRatingPK} .stars-inner`).style.width = userRatingPercentage;
}
// console.log(commentsObject)


const starPercentage = (avgRating/starsTotal)*100;
const starPercentageRounded = `${Math.round(starPercentage/10)*10}%`;
document.querySelector(`.stars-inner`).style.width = starPercentageRounded;
console.log(starPercentageRounded);

// let userRating = document.getElementById("userCommentRatingValue").value;
// let userRatingPK = document.getElementById("userCommentRatingPK").value;
// let userRatingPercentage =  `${Math.round(((userRating/starsTotal)*100)/10)*10}%`;
// console.log(userRatingPercentage);
// document.querySelector(`.${userRatingPK} .stars-inner`).style.width = userRatingPercentage;


}