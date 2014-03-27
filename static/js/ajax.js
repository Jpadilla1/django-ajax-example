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
            var html = "<li>" + data['first_name'] 
                    + " " + data['last_name'] + "</li>";
            $('#list').append(html);
        },
    });
};
