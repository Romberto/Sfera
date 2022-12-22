window.addEventListener('load', function(){

    $('.js_cart_delete').on('click', function(e){
        id_item_product = $(this).attr('data-value')
        $(this).parent().css('display', 'none')
        $.ajax({
            url: '/cart/delete_product/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {id_item_product:id_item_product},            /* Параметры передаваемые в запросе. */
            success: function(response){
                $('.cart_total_sum').html(response['summ'])
            },
            error:function (error){
                console.log(error)
            }
        })
    })




    $('.js_cart_minus').on('click', function(e){
        id_item_product = $(this).attr('data-value')
        count = $(this).prev().text()
        if(parseInt(count) == 1){
            $(this).parent().parent().css('display', 'none')
        }
        $.ajax({
            url: '/cart/cart_minus/',       /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {id_item_product:id_item_product},            /* Параметры передаваемые в запросе. */
            success: function(response){
                $(".js_count_human_"+id_item_product).load(location.href + " .js_count_human_"+id_item_product);
                $('.cart_total_sum').html(response['summ'])
            },
            error:function (error){
                console.log(error)
            }
        })
    })


    $('.js_cart_plus').on('click', function(e){
        id_item_product = $(this).attr('data-value')
        count = $(this).next().text()
        if(parseInt(count) >= 9){
            e.preventDefault()
        }else{
        $.ajax({
            url: '/cart/cart_plus/',            /* Куда пойдет запрос */
            method: 'get',                  /* Метод передачи (post или get) */
            dataType: 'json',               /* Тип данных в ответе (xml, json, script, html). */
            data: {id_item_product:id_item_product},            /* Параметры передаваемые в запросе. */
            success: function(response){
                $(".js_count_human_"+id_item_product).load(location.href + " .js_count_human_"+id_item_product);
                $('.cart_total_sum').html(response['summ'])
            },
            error:function (error){
                console.log(error)
                }
            })
        }
    })





});



