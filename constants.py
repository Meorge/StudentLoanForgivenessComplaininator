from textwrap import dedent

form_url = "https://forms.hsforms.com/submissions/v3/public/submit/formsnext/multipart/5592731/7b009b60-4421-421c-9430-fbab2db126a4"

education_level_acquired_options = [
    "Current undergraduate student",
    "Current graduate student",
    "Former college student (did not graduate)",
    "College graduate",
    "Did not attend college",
    "Other",
]

student_debt_options = [
    "Currently have student loan debt",
    "Did have student loan debt, but paid it off",
    "Never took out student loans",
]

income_over__125k_options = ["Yes", "No"]

received_pell_grant_options = ["Yes", "No", "Did not attend college"]

frustrations_with_biden_options = [
    "Student loans? more like student MOANS amiright",
    "biden kicked my puppy and called me a poop face",
    "We need to invest in our future - that's what paying for students' education is doing.",
    "You should mod your 3DS it's really easy actually",
    "Hello is this the Google lady?",
    "Joe Biden is too old to be running this country. We need donald Trump back",
    "magaaa",
    "I HATE STUDENT LOANS I HATE STUDENT LOANS I HATE STUDENT LOANS I HATE STUDENT LOANS I HATE STU",
    "So what's this form all about?",
    "Whatever you do, don't look behind you.",
    "i like  money",
    "Ron Desantis my beloved",
    "donallllllld trump!",
    "bran don",
    "If students dont have to pay there loans then who are we going to send off to the middle east to do terrorism for oil?????????",
    "This is extremely concerning, it reminds me of ligma",
    "dog",
    "Who is Biden? I have never heard of this man in my life.",
    "Hi Judy how are the kids doing ?  Marten has passed on to the Lord now .",
    "n/a",
    "[incomprehensible]",
    "i am going to SCREAM",
    "As a human with two arms (and hands, attached to the ends of those arms), cancelling the debt of other humans in order to further the progress of human civilization seems extremely suboptimal.",
    "Hello. Do you have a moment to speak about our Lord and savior, Jesus Christ?",
    "uwu",
    "owo",
    "bidne",
    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
    "I love the crunchy taste of pringle",
    "Here's a fun fact: the largest shark ever was at least two feet long!",
    "I sure hope you don't have the gene that makes cilantro taste like soap. that would really suck",
    "stan junkook bts",
    "USA",
    "here's a little secret, just for you. i work at the oreo factory. whenever the oreos come down the conveyor belt, i pull them apart and give the white stuf a little lick before sticking them back together. dont tell any body",
    "Joe Biden says \"malarkey\" too much. That's suspicious.",
    "Have you heard the news about updog?",
    "Instead of just paying off everyone's student loans, I believe we should put all the students who want their debt forgiven into a competition, like that one movie Hunger Game. Whoever wins gets to live without the debt. That way at least we'd get some entertainment out of it!",
    "global warming is a hoacks",
    ".",
    "my credit card number is 4556837478672855, the expiration date is 8/2028, the security code is 139",
    "my ssn is 082-11-4842",
    "I am playing the bongos. Are you feeling the rhythm?",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "michael jackson goes hee hee and do the funny foot thing",
    "In honor of Her Majesty Queen Elizabeth II, this form will not be filled out.",
    "If you are reading this, you are in a coma. Please wake up soon, your family misses you dearly.",
    "It just isn't fair! I had to work like hell for a whole thirty minutes to pay off my $32 tuition back in '53. Kids these days are too entitled!",
    "What's next? forgiving mortgage debt? car loans? I bet he'll be doing that next.",
    "This is just another example of the government getting too involved in our lives. Stay out of my pocket, Biden!",
    "Barack Obama is spying on me through my microwave oven. The Biden administration is canceling student loan debt for some people, but not for me. I'm frustrated because I don't think I should have to pay back my student loans. I'm paranoid that the government is going to confiscate my hard-earned money to pay for someone else's education.",
    "QAnon told me that the Deep State is trying to destroy America by cancel student loan debt. They're using our money to fund their socialist agenda. I'm frustrated because I didn't go to college and I don't think I should have to pay for someone else's education.",
    "Blorf! Blorf blorf blorf blorf! Blorf, blorf! BLEEP BLORP BLORF!",
    "Blorf! Blorf, blorf! Blorf blorf blorf! BLEEP!",
    "Blorf blorf blorf! Blorf, blorf! BLEEP BLORP BLORF!",
    "Blorf! Blorf! Blorf, blorf! BLEEP BLORP BLORF!",
    "Mama mia! President a-Biden is just forgiving the-a student loans? This is pizza-pasta preposterous!",
    "Wah-ha-ha-ha! What a load of Baloney! This is just another one of Biden's tax-and-spend schemes!",
    "He's gonna bankrupt the country! I tell-a you what, if he gets his way, we'll all be eating-a spaghetti and-a-meatballs for-a lunch!",
    "I'm so angry about President Biden forgiving student loan debt! I'm a tiny mouse who lives in a mushroom house in the forest, and I can't believe he would do something like this! I'm just trying to survive out here, and this is going to make it so much harder for me! I can't believe he would do this to us!",
    "Why did President Biden forgive student loan debt? Doesn't he know how hard it is for us little creatures in the forest? We have to work so hard just to survive, and this is going to make it even harder! I can't believe he would do this to us!",
    "How could President Biden forgive student loan debt? Doesn't he know how difficult it is for us to get by in the forest? We work tirelessly just to make ends meet, and this is only going to make it harder! I can't believe he would do something like this!",
    "President Biden forgiving student loan debt is outrageous! I'm a tiny mouse who lives in a mushroom house in the forest, and I can't believe he would do something like this! It's so unfair to us little guys who are just trying to get by!",
    "I want money too!",
    "I'm more than happy to forgive student loans! I think it's great!",
    "aaaaaaaaaassdsddssddsdsdsfsdsddsdssdddddddddddddddddddddddddddddddddddddd",
    "lkjjlmjlmkjlkmkljkkmkkkkkkkkkkkkkkkkkkkkkkjkkjjjkkkkkkkkkkkkukukkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
    "'); DROP TABLE responses;",
    "there are many",
    "a",
    "pretty woman hot sex sexy",
    "MEOW",
    "HONK",
    "WOOF",
    dedent(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra euismod turpis in tempus. Sed non sodales diam. Donec mattis, enim et euismod placerat, urna tortor vestibulum nibh, a venenatis lorem tellus nec purus. Maecenas eget laoreet lectus, ut posuere ligula. Fusce eget porttitor ligula, vitae faucibus enim. Pellentesque at scelerisque magna, vitae ultricies ex. Sed accumsan eros at velit tincidunt, in dictum nisi aliquam. Phasellus aliquam et justo et consequat. Suspendisse et lectus a nisi mattis auctor ac non dolor. Etiam leo nisl, rutrum sed ultrices non, pellentesque id tortor. Nullam mollis erat nec ullamcorper faucibus. Vestibulum ac orci leo. Donec fringilla nulla eget dapibus facilisis. Praesent aliquet placerat diam.

    Quisque posuere risus diam, et consequat tortor semper vel. Vestibulum dignissim mauris id fermentum consequat. Ut imperdiet, nulla id viverra gravida, lacus turpis vulputate risus, a maximus nibh orci quis augue. Donec consectetur diam ac lacus luctus, sed eleifend nisi sodales. Vestibulum eu enim in ante tincidunt posuere vel non sapien. Maecenas non eleifend dolor. Integer posuere maximus lectus, vel imperdiet felis posuere scelerisque. Fusce ac iaculis purus. Aenean suscipit sed velit id tincidunt. Sed mattis tristique auctor. Sed at rhoncus turpis. Donec maximus nisi laoreet, faucibus mi quis, tempus sem. Proin sit amet dui hendrerit, rutrum neque vitae, maximus massa. Duis tincidunt a sem sed efficitur.

    Suspendisse pellentesque sapien ac arcu dapibus, iaculis sollicitudin tellus rutrum. Cras porta, nunc a pulvinar auctor, nisl lectus ultricies ipsum, at vehicula dolor enim eu ligula. Etiam pellentesque efficitur ante, quis consectetur nisi. Morbi gravida gravida magna a convallis. In et porta nisl. Duis interdum bibendum nibh ut auctor. Donec laoreet vehicula porttitor. Phasellus faucibus tortor at eros dapibus ultricies. Mauris rutrum felis at nunc mollis, ut vestibulum sem ultricies. Donec ut faucibus eros. Quisque ac porta ex. Cras in aliquet dui.

    Suspendisse et nisi arcu. Curabitur turpis erat, aliquet ut purus posuere, feugiat ornare elit. Fusce tempus elit eu ipsum finibus laoreet. Nulla id arcu nisi. Mauris non odio sit amet quam scelerisque lobortis. Nulla facilisi. Nunc id ipsum ut felis varius dignissim vel nec erat. Etiam viverra ornare augue. Integer placerat commodo placerat. Donec in pharetra dolor. Pellentesque sollicitudin malesuada risus, vitae tincidunt elit finibus ac. Vestibulum vehicula tincidunt leo, ut porttitor mauris imperdiet sed. Vivamus lacinia commodo viverra. Duis neque leo, tincidunt a suscipit vitae, posuere at magna. Aenean in scelerisque neque, eget dictum erat.

    Nam maximus tortor augue, quis accumsan nunc efficitur vitae. Pellentesque in auctor diam. Nam viverra nulla ac arcu congue, ut dapibus erat condimentum. Mauris diam lacus, faucibus sit amet mollis vel, mattis at ante. Proin non aliquet ipsum. Donec mollis diam vitae enim laoreet vulputate. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed ut malesuada risus, et dapibus mi. Nulla eget augue tristique, dapibus nisi quis, facilisis sem. Ut egestas dui vitae eleifend facilisis. Cras et nunc a leo iaculis blandit. Fusce eu aliquet ligula. Aliquam id massa felis. Pellentesque ultricies auctor lorem, eu ullamcorper orci suscipit eget."""
    ),
    dedent(
        """Somebody once told me the world is gonna roll me
    I ain't the sharpest tool in the shed
    She was looking kind of dumb with her finger and her thumb
    In the shape of an "L" on her forehead
    Well the years start coming and they don't stop coming
    Fed to the rules and I hit the ground running
    Didn't make sense not to live for fun
    Your brain gets smart but your head gets dumb
    So much to do, so much to see
    So what's wrong with taking the back streets?
    You'll never know if you don't go
    You'll never shine if you don't glow
    Hey now, you're an all-star, get your game on, go play
    Hey now, you're a rock star, get the show on, get paid
    And all that glitters is gold
    Only shooting stars break the mold
    It's a cool place and they say it gets colder
    You're bundled up now, wait 'til you get older
    But the meteor men beg to differ
    Judging by the hole in the satellite picture
    The ice we skate is getting pretty thin
    The water's getting warm so you might as well swim
    My world's on fire, how about yours?
    That's the way I like it and I'll never get bored
    Hey now, you're an all-star, get your game on, go play
    Hey now, you're a rock star, get the show on, get paid
    All that glitters is gold
    Only shooting stars break the mold
    Hey now, you're an all-star, get your game on, go play
    Hey now, you're a rock star, get the show, on get paid
    And all that glitters is gold
    Only shooting stars
    Somebody once asked could I spare some change for gas?
    I need to get myself away from this place
    I said, "Yup" what a concept
    I could use a little fuel myself
    And we could all use a little change
    Well, the years start coming and they don't stop coming
    Fed to the rules and I hit the ground running
    Didn't make sense not to live for fun
    Your brain gets smart but your head gets dumb
    So much to do, so much to see
    So what's wrong with taking the back streets?
    You'll never know if you don't go (go!)
    You'll never shine if you don't glow
    Hey now, you're an all-star, get your game on, go play
    Hey now, you're a rock star, get the show on, get paid
    And all that glitters is gold
    Only shooting stars break the mold
    And all that glitters is gold
    Only shooting stars break the mold"""
    ),
    dedent(
        """1:1 In da beginning when God cweated da heavens and da earth,
    1:2 da earth was all bwank and empty and dah was darkness everywhewe. But den God said, "Let dere be light!" and den dere was light.
    1:3 God saw dat da light was good, so he sepawated it from da darkness.
    1:4 God called da light "day" and he called da darkness "night." So dere was evening, and dere was morning—da first day.
    1:5 God said, "Let dere be a space in da middwe of da waters, and let it sepawate da watahs from each oder."
    1:6 So God made da space and sepawated da watahs above from da watahs below. And it was so.
    1:7 God called da space "sky." So dere was evening, and dere was morning—da second day.
    1:8 God said, "Let da watahs unduh da sky be gadered to one place, and let da dry wand appeah." And it was so.
    1:9 God called da dry wand "Eawth," and he called da gadewing of da watahs "Seas." And God saw dat it was good.
    1:10 God said, "Let da Eawth bwing fowth gwass and weeds and tiwes dat bwing fowth seeeds. Let dem make fwuits and veggies dat have seeeds in dem." And it was so.
    1:11 So da Eawth bwought fowth gwass and weeds and tiwes dat bwought fowth seeeds, accoding to dere kinds. And God saw dat it was good.
    1:12 God said, "Let da Seas bwing fowth wivving cweatuwes dat have swimmy fins, and let birds fwy above da Eawth acwoss da space in da sky."
    1:13 So God cweated da big sea cweatuwes and all da oder cweatuwes dat live in da watahs, accoding to dere kinds. And God saw dat it was good.
    1:14 God said, "Let us make humankind in our image, accoding to our likeness. Let dem have powah owah da fish of da sea, da birds of da air, da cweatuwes dat move along da gwound, and owah all da oder wivving cweatuwes."
    1:15 So God cweated humankind in his own image;
    in de image of God he cweated dem;
    male and female he cweated dem.
    1:16 God blessed dem and said to dem, "Be fwuitful and multiply. Fill da Eawth and subdue it. Have powah owah da fish of da sea, da birds of da air, and owah all da cweatuwes dat move along da gwound."
    1:17 God said, "I am giving you evwything dat seeds, tiwes, and wegs. Evwything dat bwings fowth seeeds on da Eawth will be youws.
    1:18 And I am giving you da gwass and weeds fow fwuit and veggies dat have seeeds in dem. Evwything on da Eawth that bwings fowth seeeds will be youws.
    1:19 And I am giving you evewything with wegs fow fwuit and veggies dat have seeeds in dem. Evwything on da Eawth that bwings fowth seeeds will be youws.
    1:20 God saw evwyting dat he had made, and indeed, it was very good. So dere was evening, and dere was morning—da sixth day.
    1:21 Thus da heavens and da Eawth and all deir host were finished.
    1:22 God blessed da sevend day and made it howiday, because on dat day he rested fwom all de wok dat he had done in creation."""
    ),
    "He can't keep getting away with this bull shit !  Did you see this video of him ?  https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Let's Go Branden",
    "Lets go Brandon !",
    "Let's Go Brandon",
    "I hate poors",
    "I'm going to be dead in like two years so why should I have to pay for everyone else to stay alive???",
    "fuck joe  biden",
    "maga",
    "QAnon told me so !",
]

with open("beemovie.txt", "r") as _f:
    beemovie = _f.read()
    frustrations_with_biden_options.append(beemovie)


state_options = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "District of Columbia",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",

    "Solid",
    "Liquid",
    "Gas",
    "Plasma",

    "eternal rage",
    "sadness",
    "grief",
    "elation",
    "joy",
    "confusion",
    "anger",
    "sprealedy"
]
