$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('volunteer_me/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
});