window.addEventListener('load', function(){

    $('.block__btn').click(function(e){
        e.preventDefault()
        var name = $(this).attr('data-value') // название экскурсии
        $('.hidden').html('<input class="hidden__input" type="hidden" data-value="'+name+'">')
        $('.excursion__list, .excursion__title').fadeOut(500)
        $('.phone').fadeIn(900)
    });


    /* валидция поля ввода суммы на кастомномном жетоне */

    $('.js_custom_input').keyup(function(){
        var data = $(this).val()
        var excursion_id = $('#excursion_id').text()
        if($.isNumeric(data) && parseInt(data)){
            $(this).parent().next().fadeIn()
        }else{
            $(this).parent().next().fadeOut()
        }
    })

    $('.js_button_plus').on('click', function(e){
        var number = parseInt($(this).next().text())

        if(number<9){
            $(this).next().text(number+1)
            $(this).parent().parent().find('.js_btn_add_to_cart').fadeIn()
            $(this).parent().parent().find('.query__excursion_text').css('visibility', 'hidden')
        }else{
            e.preventDefault()
        }
    });

    $('.js_button_minus').on('click', function(e){
        var number =parseInt($(this).prev().text())
        if(number>=1){
            $(this).prev().text(number-1)
            if(number-1 == 0){
                $(this).parent().parent().find('.js_btn_add_to_cart').fadeOut()
                $(this).parent().parent().find('.query__excursion_text').css('visibility', 'visible')
            }
        }
        else{
            e.preventDefault()
        }
    });

//    $('.js_excursion_link').on('click', function(e){
//        var count_human = $(this).parent().find('.count_human_window').text()
//        $(this).attr('href', function(){
//            if(this.href.includes('/?count_human=')){
//                var fields = this.href.split('?count_human=')
//                return fields[0]+'?count_human='+count_human
//            }else{
//                return this.href+'?count_human='+count_human
//            }
//        })
//    })

    // вызывает виджет регистрации телефона при нажатие на кнопку корзина, елси номер не зарегистрирован
    $('.js_cart_check_phone').on('click', function(e){
        e.preventDefault()
        $('.phone').css('visibility','visible')
        $('.mobile__menu-nav').css('display', 'none')
        $('html, body').animate({
            scrollTop: $("#scroll_phone").offset().top
        }, 1000);
    })

    $('.phone_btn').on('click',function(e){
    e.preventDefault()
    var phone = $('#phone').val()
    let regex = /^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/;
    // дальше идет проверка на соответствие выражению
    if(!regex.test(phone)){
    alert('Не корректный номер телефона');
    }else{

        $.ajax({
            url: '/excursions/check_phone/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {phone: phone},            /* Параметры передаваемые в запросе. */
            success: function(response){
                var phone = response['phone']
                $('.phone__form').css('visibility', 'hidden')
                $('.code').css('visibility', 'visible')
                $('#user_phone').val(phone)
                console.log(response['code'])
            },
            error:function (error){
                console.log(error)
            }

            });
        }
    });

    $('.limitInput').keyup(function(){
    var count = $(this).val().length
    if(count === 4){
        var phone = $('#user_phone').val()
        var code = $(this).val()
        $.ajax({
            url: '/excursions/check_code/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {phone: phone, code: code},            /* Параметры передаваемые в запросе. */
            success: function(response){
                if(response['status']){
                    location.reload();
                }else{
                    $('.text__error').text('не верный код')

                }
            },
            error:function (error){
                console.log(error)
            }
        })
        }
        });

    $('.js_btn_add_to_cart').on('click',function(e){
        var count = $(this).parent().find('.js_count_human').text() // количество жетонов
        var custom_price = 0
        if(!count){
            count = '1';
            custom_price = $(this).parent().find('.js_custom_input').val()
        }

        var id_exc = $(this).attr('data-value')                        // id жетона
        var btn = $(this)
        $(this).parent().find('.js_custom_input').val("0")
        $.ajax({
            url: '/excursions/add_to_cart/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {id_exc: id_exc, count: count, custom_price:custom_price},            /* Параметры передаваемые в запросе. */
            success: function(response){
                if(response['success']){
                    btn.fadeOut()
                    btn.prev().css('visibility', 'visible')
                    btn.parent().find('.js_count_human').text(0)
                }
            },
            error:function (error){
                console.log(error)
            }
        })
    })






});