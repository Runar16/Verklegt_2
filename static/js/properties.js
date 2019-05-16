$(document).ready(function (){
    $.ajax({
    type: 'GET',
    url: '?order=',
    success: function(resp){
       window.properties = resp
    }});
    $('#search-btn').on('click', function (e) {

        e.preventDefault();
        var searchText = $('#search-box').val();
        var zipVal = $('#zipSelect').val();
        var typeVal = $('#typeSelect').val();
        var priceFromVal = $('#price-from-box').val();
        var priceToVal = $('#price-to-box').val();
        var sizeFromVal = $('#size-from-box').val();
        var sizeToVal = $('#size-to-box').val();
        var RoomsVal = $('#rooms-box').val();
        let url_str = "";
        url_str += '?search_filter=' + searchText;
        if(zipVal !== 'ZIP'){
            url_str += '&zip_filter=' + zipVal;
        }
        if(typeVal !== 'Type'){
            url_str += '&type_filter=' + typeVal;
        }
        if(priceFromVal !== ''){
            url_str += '&priceFrom_filter=' + priceFromVal;
        }
        if(priceToVal !== ''){
            url_str += '&priceTo_filter=' + priceToVal;
        }
        if(sizeFromVal !== ''){
            url_str += '&sizeFrom_filter=' + sizeFromVal;
        }
        if(sizeToVal !== ''){
            url_str += '&sizeTo_filter=' + sizeToVal;
        }
        if(RoomsVal !== ''){
            url_str += '&rooms_filter=' + RoomsVal;
        }
        $.ajax({
            url: url_str,
            type: 'GET',
            beforeSend: function(){
                $("#search-loader").show();
                },
            success: function (resp) {
                display_searched(resp);
            },
            complete:function(){
                $("#search-loader").hide();
            },
            error: function (xhr, status, error) {
                $('.toast').toast('show');
                console.error(error);
            }

        })
    });
    $('#order-a-z-btn').on('click', function () {
        $("#order-by-loader").show();
        window.properties.data.sort(sort_by('street_name', order, function(a){return a.toUpperCase()}));
        setTimeout(function() {
            display_searched(window.properties);
            if (order === true) {
                $("#order-a-z-btn").html("Order By A-Z&uarr;");
            } else {
                $("#order-a-z-btn").html("Order By A-Z&darr;");
            }
            $("#order-by-loader").hide();
            order = !order;
        }, 500)
    });

      $('#order-by-price-btn').on('click', function () {
          $("#order-by-loader").show();
          window.properties.data.sort(sort_by('price', price_order, parseInt));
          setTimeout(function(){
              display_searched(window.properties);
              if(price_order === true) {
                  $("#order-by-price-btn").html("Order By Price&darr;");
              }
              else{
                  $("#order-by-price-btn").html("Order By Price&uarr;");
              }
              $("#order-by-loader").hide();
              price_order = !price_order;
          }, 500);
        })
});



function display_searched(resp) {
    var newHtml = resp.data.map(d => {
        d.price = d.price.toLocaleString();
        return `
<div class="property" style="margin-right:1%">
                    <a href="/property/${d.id}">
                            <div class="card" style="width:20rem;">
                                <img src="${d.first_image}" class="card-img-top" alt="${d.image_tag}">
                                <div class="card-header" id="property-card-header"><h4 style="color:white; opacity: 1;">${d.price}kr.</h4>
                                </div>
                                    <div class="card-body" style="padding: 0">
                                        <div class="left-block-container">
                                            <span style="display:block; font-weight:bold">${d.street_name} ${d.street_number}</span>
                                            <span style="display:block; padding-top:10px">${d.city}, ${d.zip}</span>
                                        </div>
                                        <div class="right-block-container">
                                            <span style="display:block;">${d.size}m&sup2;</span>
                                            <span style="display:block; padding-top:10px; font-weight:lighter">${d.type}</span>
                                        </div>
                                </div>
                            </div>
                    </a>
                </div>`
    });
    $('.properties').html(newHtml.join(''));
}


//https://stackoverflow.com/a/979325

var sort_by = function(field, reverse, primer){
   var key = primer ?
       function(x) {return primer(x[field])} :
       function(x) {return x[field]};

   reverse = !reverse ? 1 : -1;

   return function (a, b) {
       return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
     }
};

var order = true;
var price_order = true;
