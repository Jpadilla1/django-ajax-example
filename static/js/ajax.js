function sendInfo() {
    $.ajax({
        type: "POST",
        url: "/",
        data: {
            'first_name': $('#id_first_name').val(),
            'last_name': $('#id_last_name').val(),
        },
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {
            var html = "";
            $.each(data, function(idx, obj) {
              html += "<li>" + obj['fields']['first_name'] 
                    + " " + obj['fields']['last_name'] + "</li>";
            });
            $('#list').html(html);
        },
    });
};
