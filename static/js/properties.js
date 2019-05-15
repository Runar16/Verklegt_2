$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var zipVal = $('#zipSelect').val();
        var typeVal = $('#typeSelect').val();
        let url_str = "";
        url_str += '?search_filter=' + searchText;
        if(zipVal !== 'ZIP'){
            if(url_str === "") {
                url_str += '?zip_filter=' + zipVal;
            }
            else{
                url_str += '&zip_filter=' + zipVal;
            }
        }
        if(typeVal !== 'Type'){
            if(url_str === "") {
                url_str += '?type_filter=' + typeVal;
            }
            else{
                url_str += '&type_filter=' + typeVal;
            }
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
});

function display_searched(resp) {
     var newHtml = resp.data.map(d => {
        return `<div class="property" style="margin-right:1%">
                    <a href="/property/${ d.id }">
                            <div class="card" style="width:20rem;">
                                <img src="${ d.first_image }" class="card-img-top" alt="${ d.image_tag }">
                                <div class="card-header" id="property-card-header"><h4 style="color:white; opacity: 1;">${ d.price }kr.</h4>
                                </div>
                                    <div class="card-body" style="padding: 0">
                                        <div class="left-block-container">
                                            <span style="display:block; font-weight:bold">${ d.street_name } ${ d.street_number }</span>
                                            <span style="display:block; padding-top:10px">${ d.city }, ${ d.zip }</span>
                                        </div>
                                        <div class="right-block-container">
                                            <span style="display:block;">${ d.size }m&sup2;</span>
                                            <span style="display:block; padding-top:10px; font-weight:lighter">${ d.type}</span>
                                        </div>
                                </div>
                            </div>
                    </a>
                </div>`
    });
    $('.properties').html(newHtml.join(''));
}
