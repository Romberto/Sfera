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

    /* валидция поля ввода суммы на кастомномном жетоне */

    $('.js_custom_input').keyup(function(){
        var data = $(this).val()
        var excursion_id = $('#excursion_id').text()
        if($.isNumeric(data) && parseInt(data) >= 3000){
            $('.query__excursion_link span').css('height', '0px')
            $('.js_custom__price_link').attr('href', ''+excursion_id+'/'+data+'')
        }else{
            $('.query__excursion_link span').css('height', '50px')
        }
    })

    $('.js_button_plus').on('click', function(e){
        var number = parseInt($(this).next().text())
        if(number<9){
            $(this).next().text(number+1)
        }else{
            e.preventDefault()
        }


    });

    $('.js_button_minus').on('click', function(e){
        var number =parseInt($(this).prev().text())
        if(number>1){
            $(this).prev().text(number-1)
        }else{
            e.preventDefault()
        }
    });

    $('.js_excursion_link').on('click', function(e){
        var count_human = $(this).parent().find('.count_human_window').text()
        $(this).attr('href', function(){
           // e.preventDefault()
           // console.log(this.href)
            if(this.href.includes('/?count_human=')){
                var fields = this.href.split('?count_human=')
                return fields[0]+'?count_human='+count_human
            }else{
                return this.href+'?count_human='+count_human
            }
        })
    })

});