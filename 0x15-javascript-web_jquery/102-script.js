$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.getJSON(url, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error: Could not retrieve translation.');
    });
  });
});
