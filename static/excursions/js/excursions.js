window.addEventListener('load', function(){



    $('.block__btn').click(function(e){
        e.preventDefault()
        var name = $(this).attr('data-value') // название экскурсии
        $('.hidden').html('<input class="hidden__input" type="hidden" data-value="'+name+'">')
        $('.excursion__list, .excursion__title').fadeOut(500)
        $('.phone').fadeIn(900)
    });






    $('.limitInput').keyup(function(){
        var count = $(this).val().length
        console.log(count)
        if(count === 4){
            $(this).fadeOut()
            $.ajax({

            })
        }
    });



});