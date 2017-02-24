import media
import fresh_tomatoes

# Creating movie objects
the_matrix = media.Movie("The Matrix",
             "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",  # NOQA
             "The Matrix is a 1999 science fiction film written"
             " and directed by The Wachowskis, starring Keanu "
             "Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo "
             "Weaving, and Joe Pantoliano. It depicts a dystopian "
             "future in which reality as perceived by most humans "
             "is actually a simulated reality called 'the Matrix',"
             " created by sentient machines to subdue the human "
             "population, while their bodies' heat and electrical "
             "activity are used as an energy source.",
             "https://youtu.be/m8e-FF8MsqU")

lucia = media.Movie("Lucia",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Lucia_kannada_film_poster1.jpg/220px-Lucia_kannada_film_poster1.jpg",  # NOQA
                  "Lucia is an Indian Kannada romantic psychological "
                  "thriller film.The film's plot is about Nikki, an "
                  "usher in theatre who suffers from insomnia but after "
                  "consuming a special pill, he gets entangled in a "
                  "different kind of dream. Lucia was the first Kannada film"
                  " to be crowdfunded by the people which created a trend.",
                  "https://youtu.be/pgIL2H-OdcA")

rangitaranga = media.Movie("RangiTaranga",
               "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/2015_Kannada_film_Rangitaranga_poster.jpg/220px-2015_Kannada_film_Rangitaranga_poster.jpg",  # NOQA
               "RangiTaranga (English: Colourful Wave) is a 2015 "
               "Indian Kannada language mystery thriller film "
               "written and directed by Anup Bhandari in his debut."
               "RangiTaranga is set in Kamarottu, a fictional "
               "village in the Tulunadu region of dakshina kannada"
               " district Karnataka, as Indu's (Radhika Chetan) "
               "ancestral village. She and her husband Gautam "
               "(Nirup Bhandari), decide to perform a ritual to "
               "ward off evil spirits. The story follows Gautam "
               "uncovering a mysterious trail of crime on finding "
               "his wife missing and the final discovery of"
               " the criminal.",
               "https://youtu.be/inBBiSDnEy4")

nowYouSeeMe = media.Movie("Now You See Me",
              "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Now_You_See_Me_Poster.jpg/220px-Now_You_See_Me_Poster.jpg",  # NOQA
              "Now You See Me is a 2013 American heist thriller "
              "film directed by Louis Leterrier and written by "
              "Ed Solomon, Boaz Yakin and Edward Ricourt.Four "
              "stage magicians are each given a tarot card that "
              "lead them to the same empty New York City "
              "apartment, where they find information from an "
              "unknown benefactor.",
              "https://youtu.be/KzJNYYkkhzc")

kirikParty = media.Movie("Kirik Party",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Kirik_Part_Poster.jpg/220px-Kirik_Part_Poster.jpg",  # NOQA
                         "Kirik Party is the story of a gang of mischievous "
                         "students, led by the protagonist Karna, who have "
                         "just joined an engineering college. They belong "
                         "to different streams of engineering but develop a "
                         "bond while staying together in the hostel. The "
                         "treatment is stylish with light humour throughout "
                         "while exploring the college life of these "
                         "youngsters. Karna, the protagonist from a small "
                         "town has joined this engineering college and he "
                         "gangs up with his hostel mates Loki, Alexander, "
                         "Manja and others to fuel a lot of mischief in the "
                         "college. During the first year he befriends Saanvi "
                         "a Final year student and certain incidents impact "
                         "Karna's life making him question his very "
                         "basic thought process.",
                         "https://youtu.be/IfvnbER_6sQ")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "Inception is a 2010 science fiction heist thriller "
                        "film written, co-produced, and directed by "
                        "Christopher Nolan, and co-produced by Emma Thomas. "
                        "The film stars Leonardo DiCaprio as a professional "
                        "thief who steals information by infiltrating the "
                        "subconscious, and is offered a chance to have his "
                        "criminal history erased as payment for a seemingly "
                        "impossible task: 'inception', the implantation of "
                        "another person's idea into a target's subconscious.",
                        "https://youtu.be/66TuSJo4dZM")


# Creating a list of movie objects to pass to open_movies_page method
movies = [the_matrix, lucia, rangitaranga, nowYouSeeMe, kirikParty, inception]
# Calling the open_movies_page take the list of movies and open a browser.
fresh_tomatoes.open_movies_page(movies)
