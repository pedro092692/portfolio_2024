function bg(content){
    let overlay_div = content.nextElementSibling;
    overlay_div.classList.add('change-bg');
}

function end_bg(content){
    let overlay_div = content.nextElementSibling;
    overlay_div.classList.remove('change-bg');
}