$(document).ready(function(){
  $(window).scroll(function(){
    if($(this).scrollTop()){
        $("nav").css({
            "position":"fixed",
            "right" : 0,
            "left":0,
            "top" :0,
            "z-index" :999,
        })
    }
    else{
        $("nav").css({
            "position":"relative",

        })
    }
  })
})


