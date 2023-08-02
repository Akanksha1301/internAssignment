//cardCollection is the collection of all the cards, each card (I call it "parent") has two childs => [image, blank card behind image]

let cardCollection = document.getElementsByClassName('col');
const hoverFunc = (parent) => {
  
}
for(parent in cardCollection) {  
  let element1 = cardCollection[parent];
  let firstChild = element1.querySelector('.img-container');
  let secondChild = element1.querySelector('.team-details');
  let thirdchild =  secondChild.querySelector('span')

  element1.addEventListener("mouseover", (e) => {
    firstChild.classList.add("myHover-first");
    secondChild.classList.add("myHover");
    thirdchild.style.display='block';
  })
  element1.addEventListener("mouseout", (e) => {
    firstChild.classList.remove("myHover-first");
    secondChild.classList.remove("myHover");
    thirdchild.style.display='none';
  })
}
