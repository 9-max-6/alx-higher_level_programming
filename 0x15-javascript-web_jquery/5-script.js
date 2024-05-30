const handleClick = function () {
  $('UL.my_list').html(function (index, existingHTML) {
    return existingHTML + '<li>Item</li>';
  });
};
$('DIV#add_item').on('click', handleClick);
