$('#contact-form').submit(function() {
    
    var c_email = $('#c_email').val();
    var c_name = $('#c_name').val();
    var c_type = $('#c_type').val();
    var c_comments = $('#c_comments').val();
    
    $.ajax({
      type: "POST",
      url: "https://mandrillapp.com/api/1.0/messages/send.json",
      data: {
        'key': 'pKV8ERvPpB0ryiTw0YseVw',
        'message': {
          'from_email': 'no-reply@gong.io',
          'to': [
              {
                'email': c_email,
                'type': 'to'
              }
          ],
          "headers": {
                "Reply-To": c_email
          },
          'autotext': 'true',
          'subject': '[Gongio] New query',
          'html': c_name + '<br>' + c_type + '<br><br>' + c_comments
        }
      }
     }).done(function(response) {
        $('#contact-form').html('<h3 style="color:green">Awesome! We will get back to you soon :)</h3');
     });
    
    return false;  
    
});