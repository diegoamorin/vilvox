$(".owl-nome").owlCarousel({
	loop: true,
	margin: 10,
	nav: true,
	dots: true,
	navText: [
		"<i class='fa fa-angle-left'></i>",
		"<i class='fa fa-angle-right'></i>"
	],
	responsive: {
		0: {
			items: 1
		},
		400: {
			items: 2
		},
		600: {
			items: 3
		},
		1000: {
			items: 5
		}
	}
});
