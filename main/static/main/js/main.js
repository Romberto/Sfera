window.addEventListener('load', function(){

    $('.menu__mobile_burger').on('click', function(){
        $('.mobile__menu-nav').fadeIn(1000)
    })
    $('.mobile__menu_btn').on('click',function(e){
        e.preventDefault()
        $('.mobile__menu-nav').fadeOut()
    })

    	$(document).mouseup( function(e){ // событие клика по веб-документу
		var div = $( ".mobile__menu-nav" ); // тут указываем ID элемента
		if ( !div.is(e.target) // если клик был не по нашему блоку
		    && div.has(e.target).length === 0 ) { // и не по его дочерним элементам
			div.fadeOut(1000); // скрываем его

		}
	});
});