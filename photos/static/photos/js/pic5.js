
function getDescr(pic_id) {
    var html_descr = $.ajax
}


$(document).ready(function(){
    
    $('img').on('click', function(){
        var title = this.getAttribute('title');
        var thisid = this.id;
        var thislink = this.getAttribute("data-link");
        
        $('#modal-title').text(title);
        $('#photocontainer').html("<img class='modal-img' src="+thislink+">");
        $.get('/photos/descriptions/'+thisid, function(data){
            // console.log(data);
            $('#description').html(data)});
        $('#gallerymodal').modal('show');
        $("#add_description").on("click", function(){
            descriptionURL = '/photos/descriptions/'+thisid+'/new_comment/';
        $.get(descriptionURL, function(data){
            // console.log("jsondata", data);
            // addComments(data);
            $('#add_comment').html(data);
            $("#add_description").hide();

        })
        $('#gallerymodal').on('submit', function(){
            event.preventDefault();
            console.log("submit");
            var postURL = $('#new_description_form').attr("data-url");
            var sendData = $("#new_description_form").serialize();
            console.log("form", sendData);
            $.ajax({
                type: 'POST',
                url: postURL, 
                data: sendData, 
                dataType: 'json', 
                async: false,
                success: function(info)
                    {
                    console.log('ajaxdata', info);
                    $('#description').html(info);
                    $('#add_description').show();
                    }
                });
            
            
            
            })
        })
    })
});

// $('#gallerymodal').on('shown.bs.modal', function(){
//     $("#add_description").on("click", function(){
//         $.get('/photos/descriptions/new/', function(data){
//             $('#description').append(data);
//         })
        
//     })

