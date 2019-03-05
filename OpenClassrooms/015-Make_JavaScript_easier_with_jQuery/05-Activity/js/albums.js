$.getJSON('./albums.json')
  .done(function(response){
    var albumList = '<ul class="albums">';
    $.each(response, function(index, album) {
      albumList += '<li>';

      albumList += '<i>' + album.name + '</i>, ';
      albumList += album.author + ', ';
      albumList += album.year + ', ';
      albumList += album.nbtracks + ' tracks';

      albumList += '</li>';
    });
    albumList += '</ul>';

    $('#albums-json-content').html(albumList);
})
