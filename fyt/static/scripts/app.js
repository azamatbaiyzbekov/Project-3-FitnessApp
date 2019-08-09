console.log('really really fyt')

$('.btn').on('click', function(event){
  event.preventDefault();
  const element = $(this);
  $.ajax({
    url: '/like_workout/',
    method: 'GET',
    data: {workout_id: element.attr('data-id')},
    success: function(response){
      element.html('<i class="far fa-heart"></i> ' + response);
    }
  })
})
