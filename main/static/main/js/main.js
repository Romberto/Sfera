window.addEventListener('load', function(){

    $('.menu__mobile_burger').on('click', function(){
        $('.mobile__menu-nav').fadeIn(1000)
    })
    $('.mobile__menu_btn').on('click',function(e){
        console.log('ok')
        e.preventDefault()
        $('.mobile__menu-nav').fadeOut()
    })
});