$(function() {
    $('#btnGetInfo').click(function() {
        $.ajax({
            url: '/getInfo',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
				$("textarea#result").val(response);
				//alert(response);
            },
            error: function(error) {
                console.log(error);
				$("textarea#result").val(error);
            }
        });
    });
});
