window.onload = function() {

    $('select').material_select();
    $('.dropdown-trigger').dropdown();
    $('.modal').modal();

    $('#create_post_btn').click(function(){

        title = $('#title').val()
        content = $('#content').val()
        author = $('#author').val()
        
        $.ajax({
            url: "/publish_post/",
            type: "POST",
            data: {
                title: title,
                content: content,
                author: author
            },
            success: function(response) {
                console.log("Success!", response);
                Materialize.toast("Post published!");
            },
            error: function(xhr, textstatus, errorthrown) {
                console.log("Please report this error: "+errorthrown+xhr.status+xhr.responseText);
            }
        });
    });



    if(window.location.pathname.includes('/view_post/'))
    {
        post_pk = window.location.pathname.split("/")[2]

        $.ajax({
            url: "/get_post/",
            type: "POST",
            data: {
                post_pk: post_pk
            },
            success: function(response) {
                console.log("Success!", response);
                $('#title').html(response['title']);
                $('#content').html(response['content']);
                $('#author').html("Authored by "+response['author']);
            },
            error: function(xhr, textstatus, errorthrown) {
                console.log("Please report this error: "+errorthrown+xhr.status+xhr.responseText);
            }
        });
    }
}