        object.onload = function () {history_submit(user_id, property_id)};
        function history_submit(user_id, property_id) {
            document.getElementById("user_id").style.display = "none";
            document.getElementById("property_id").style.display = "none";
            console.log(user_id);
            console.log(property_id);
            $.ajax({
             url: '/update_history/',
             data: [{'user_id': user_id}, {'property_id': property_id}],
             type: 'POST'
           }).done(function(response){
             console.log(response);
           });
        }

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
        return `<div class="property">
                <a href="/property/${d.id}">
                    <div class="col-sm-6">
                        <div class="card" style="width: 18rem;">
                            <img class="card-img-top" src="${d.first_image}"/>
                            <h3 class="card-header d-flex" style="background: dodgerblue; text-align: center; color: white">${d.price}kr</h4>
                            <div class="card-body">
                                <h5 class="card-title">${d.street_name} ${d.street_number}</h5>
                            </div>
                        </div>
                    </div>
                </a>
            </div>`
    });
    $('.properties').html(newHtml.join(''));
}
