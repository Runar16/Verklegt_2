$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var zipVal = $('#zipSelect').val();
        let url_str = "";
        if(searchText !== ""){
            url_str += '?search_filter=' + searchText;
        }
        if(zipVal !== 'ZIP'){
            url_str += '?zip_filter=' + zipVal;
        }
        $.ajax({
            url: url_str,
            type: 'GET',
            success: function (resp) {
                display_searched(resp);
            },
            error: function (xhr, status, error) {
                // TODO show toastr
                console.error(error)
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
