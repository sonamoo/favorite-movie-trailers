import media
import fresh_tomatoes



pulp_finction = media.Movie("Pulp Fiction",
						"American neo-noir crime black comedy film written and directed by Quentin Tarantino",
						"https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover.jpg/220px-Pulp_Fiction_cover.jpg",  # NOQA
						"https://youtu.be/ewlwcEBTvcg",
						"Quentin Tarantino",
						"October 14, 1994",
						"John Travolta, Samuel L. Jackson, Uma Thurman")


avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
					 "https://youtu.be/EPTHpG7ovak",
					 "James Cameron",
					 "December 18, 2009",
					 "Sam Worthington, Zoe Saldana, Stephen Lang")



terminator2 = media.Movie("Terminator2",
						  "terminaotr2",
						  "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Terminator2poster.jpg/220px-Terminator2poster.jpg",  # NOQA
						  "https://youtu.be/lwSysg9o7wE",
						  "James Cameron",
						  "July 3, 1991",
						  "Arnold Schwarzeneger, Edward Furlong, Linda Hamilton")
						

the_matrix = media.Movie("The Matrix",
						 "the matrix",
						 "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",  # NOQA
						 "https://youtu.be/m8e-FF8MsqU",
						 "Lana Wachowski, Lilly Wachowski",
						 "March 31, 1999",
						 "Keanu Reeves, Carrie-Anne Moss, Laurence Fishburne")

the_loard_of_the_ring = media.Movie("The Loard of The Ring",
									"The Loard of The Ring",
									"http://vignette3.wikia.nocookie.net/lotr/images/7/74/LOTRFOTRmovie.jpg/revision/latest?cb=20150203040819",  # NOQA
									"https://youtu.be/r5X-hFf6Bwo",
									"Peter Jackson",
									"December 19, 2001",
									"Orlando Bloom, Elijah Wood, Ian McKellen")

the_true_man_show = media.Movie("The Trueman Show",
								"The Trueman Show",
								"http://www.film-studies.net/files/The_truman_show.jpg",
								"https://youtu.be/AiLB34EP_qE",
								"Peter Weir",
								"June 5, 1998",
								"Jim Carrey, Laura Linney, Ed Harris")


movies = [pulp_finction, avatar, terminator2, the_matrix, the_loard_of_the_ring,
		  the_true_man_show]

# Generate html page		  
fresh_tomatoes.open_movies_page(movies)

