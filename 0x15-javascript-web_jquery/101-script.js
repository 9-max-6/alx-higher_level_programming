$(() => {
	const myList = $("UL.my_list");

	const handleClick = function () {
		if (this.id === "add_item") {
			const newElement = "<li>Item</li>";
			myList.append(newElement);
		} else if (this.id == "remove_item") {
			myList.children().last().remove();
		} else if (this.id == "clear_list") {
			myList.empty();
		}
	};
	$("DIV#add_item").click(handleClick);
	$("DIV#remove_item").click(handleClick);
	$("DIV#clear_list").click(handleClick);
});
