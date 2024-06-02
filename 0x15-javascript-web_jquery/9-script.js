$(() => {
	const onSuccess = function (response) {
		$("DIV#hello").text(response.hello);
	};
	const onError = function (jqxHR) {
		console.error("'jqXHR", jqxHR);
	};
	$.ajax({
		method: "GET",
		url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
		success: onSuccess,
		error: onError,
	});
});
