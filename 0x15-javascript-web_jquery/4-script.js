const handleClick = function () {
  $('header').toggleClass('green red');
};
$('DIV#toggle_header').on('click', handleClick);
