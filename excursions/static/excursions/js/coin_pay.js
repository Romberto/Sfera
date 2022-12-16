window.addEventListener('load', function(){

    $('.coin__pay_btn').on('click', function(e){
        var name = $(this).attr('data-value') // название экскурсии
        $('.hidden').html('<input class="hidden__input" type="hidden" data-value="'+name+'">')
        $('.phone').css('visibility', 'visible')
        $(this).hide()

    });

    $('.phone_btn').on('click',function(e){
    e.preventDefault()
    var id = $('.coin__pay_btn').attr('data-value') // название экскурсии
    var phone = $('#phone').val()
    $('.hidden').html('<input class="hidden__input" type="hidden" data-value="'+phone+'">')
    let regex = /^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/;
    // дальше идет проверка на соответствие выражению
    if(!regex.test(phone)){
    alert('Не корректный номер телефона');
    }else{

        $.ajax({
            url: '/excursions/check_phone/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {id: id, phone: phone},            /* Параметры передаваемые в запросе. */
            success: function(response){
                $('.phone').css('visibility', 'hidden')
                $('.code').css('visibility', 'visible')
                console.log(response['code'])

            },
            error:function (error){
                console.log(error)
            }

            });
        }
    });
// подтверждение телефона проверка кода подтверждения
// ajax запрос
    $('.limitInput').keyup(function(){
        var count = $(this).val().length
        if(count === 4){
            var phone = $('.hidden__input').attr('data-value')
            var code = $(this).val()
            var price = $('#cod_price').val()
            $.ajax({
                url: '/excursions/check_code/',            /* Куда пойдет запрос */
                method: 'get',                  /* Метод передачи (post или get) */
                dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
                data: {phone: phone, code: code, price:price},            /* Параметры передаваемые в запросе. */
                success: function(response){
                    if(response['status']){
                        $('.code').hide(1000)
                        $('.success__phone').css('visibility', 'visible')
                        $('#popup__phone b').text(phone)
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
//перейти к оплате
// заполняем форму
    $('.js_pay_btn').on('click', function(e){
        $('.popup__inner').hide()
        $('.pay__widget').css('visibility', 'visible')
        var phone = $('.hidden__input').attr('data-value')
            $.ajax({
                url: '/excursions/widget/',            /* Куда пойдет запрос */
                method: 'get',                  /* Метод передачи (post или get) */
                dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
                data: {phone: phone},            /* Параметры передаваемые в запросе. */
                success: function(response){
                    console.log(response)
                    $('.pay__widget form #form_phone').attr('value', response['phone'])
                   // $('.pay__widget form #order').attr('value', response['order'])


                },
                error:function (error){
                    console.log(error)
                }

            })




    });

    $('.js_no_pay_btn').on('click', function(){
        $('.success__phone').hide()
        $('.coin__pay_btn').show()
    });

    $('.js_success_pay').on('click', function(e){
        var phone = $('.hidden__input').attr('data-value')
        // забрать сумму оплаты из системы оплаты для идентификации экскурсии
        // пока будем брать заголовок страницы
        var excursion_name = $('#excursion_title').text()
                    $.ajax({
                url: '/excursions/excursion_code/',            /* Куда пойдет запрос */
                method: 'get',                  /* Метод передачи (post или get) */
                dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
                data: {phone: phone, exc: excursion_name},            /* Параметры передаваемые в запросе. */
                success: function(response){
                    console.log(response)
                }
                })
    })



});