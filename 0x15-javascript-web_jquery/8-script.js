const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, textStatus) {
	if (data && data.results) {
		const listItems = data.results.map((film) => `<li>${film.title}</li>`).join('');
		$('UL#list_movies').html(listItems);
	}
});
