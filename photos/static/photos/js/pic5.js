
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
            console.log(data);
            $('#description').html(data)});
        $('#gallerymodal').modal('show');
    })
});

$('#gallerymodal').on('shown.bs.modal', function(){
    $("#add_description").on("click", function(){
        $.get('/photos/descriptions/new/', function(data){
            $('#description').append(data);
        })
        
    })
})
