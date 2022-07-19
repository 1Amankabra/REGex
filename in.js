document.getElementsByClassName("type").innerHTML="hii everyone";

function greet(){
    let total_class_in_html = document.getElementsByClassName("type").length;
    console.log(total_class_in_html);
    for(let i=0;i<total_class_in_html;i++){
        document.getElementsByClassName("type")[i].innerHTML="Every one fine...."
    }
}

greet();

function show_alert(){
    alert("Hello! How are you?");
}