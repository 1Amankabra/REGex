const links = document.querySelectorAll(".link");
const sections = document.querySelectorAll("section");

console.log(links);
console.log(sections);

let activelink = 0;

links.forEach((link,i) => {
    link.addEvntListener("click", () => {
        if(activelink !=i){
            links[activelink].classList.remove("active");
            links[i].classList.add("active");
            sections[activelink].classList.remove("active");
            sections[i].classList.add("active");
            activelink =i;
        }
    });
});