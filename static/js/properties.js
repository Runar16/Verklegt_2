$(document).ready(function (){
    $.ajax({
    type: 'GET',
    url: '?heh=',
    success: function(resp){
       var properties = resp
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
            success: function (resp) {
                display_searched(resp);
            },
            error: function (xhr, status, error) {
                $('.toast').toast('show');
                console.error(error);
            }

        })
    });
    $('#order-by-btn').on('click', function (e) {
        $.ajax({
            url: '',
            type: 'GET',
            success: function (resp) {
                display_order(resp)
            },
            error: function (xhr, status, error) {
                $('.toast').toast('show');
                console.error(error);
            }

        })
    });
});



function display_searched(resp) {
    console.log(resp.data);
    var newHtml = resp.data.map(d => {
        return `<div class="property" style="margin-right:1%">
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
