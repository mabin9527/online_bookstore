let items=document.querySelectorAll('.editor-item');
let middle = document.querySelector('.middle');
let handler=document.querySelector('.handler');
let left_box=document.querySelector('.left-box');

function setActive(){
    items.forEach((item)=>{
        item.classList.remove('active');
    });
    this.classList.add('active');
    middle.classList.add('hidden');
}

items.forEach((item)=>{
    item.addEventListener('click',setActive);
});

handler.addEventListener('click',function(){
    if(!this.classList.contains('close')){
        left_box.style.width=0;
        this.classList.add('close');
    }else{
        left_box.style.width=250+'px';
        this.classList.remove('close');
    }
});