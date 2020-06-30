# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Keikumusume", color="#1adf0a")
define w = Character("Dr. Watson", color="#993333")
define r = Character("Riu", color="#b82d60")
define c = Character("Ichihime", color="#fc1b1b")
define n = Character("Nadeshiko", color="#11dae3")
define h = Character("Hana", color="#db0640")
define b = Character("Kaavi", color="#0b5ec2")
define i = Character("Kana", color="#ff33d4")
define u = Character("???", color="#fbfbfb")
define j = Character("Joseph", color="#fbfbfb")


label start:
    python:
        _preferences.set_volume('music', 0.5)
        renpy.restart_interaction()
    scene bg dining
    "Mahjong Soul Shrine. Dining room"
    play music "audio/itsumonofuukei.mp3"
    show jojo
    j "Nghhh... another cat hair in my soup."
    hide jojo
    show cat
    c "Wasn't me nyaa..."
    j "(Another day spent investigating these weirdos.)"
    j "(I'm so close to discovering which one of these floozies are cheating though. I already have half the evidence I need.)"
    j "(Just a few more days and I can go back to Mahjong Crimes Headquarters.)"
    hide cat
    show nade
    n "Yoohoo! Joseph! After breakfast why don't you show me a special mahjong lesson in my room?"
    j "Do I need to call the sexual harrassment hotline?"
    n "Ahahaha, you're so funny Joseph!"
    j "(My only sexual attraction is to justice.)"
    hide nade
    show kaavi
    b "Everyone, I have news! Big news!"
    b "I have foreseen it, tonight someone in this shrine will die! Someone in this shrine will definitely die!"
    j "This is stupid. You can't even predict the tiles I'm waiting on, let alone someones death. Take your fortune telling to the carnies."
    j "(Ow! did she just throw a tarot card at me?)"
    j "(There's no way anyone will die here. I just gotta sit through a few more days, just a few more days...)"
    scene bg winning with fade
    centered "{size=+10}>The Winning Team presents...{/size}"
    centered "{size=+10}A >The Winning Team Production...{/size}"
    "The proliferation of nuclear weapons between nations has accelerated. Humanity stands divided."
    "Tensions are bubbling over international disputes, and yet the outbreak of any armed conflict would result in mutual destruction for all parties involved."
    "As such, international conflicts are now settled by games of mahjong. In Tokyo, everyone is ranked according to their ability."
    "The bottom ranked players live in poverty, gambling over scraps in the bronze slums. The best of the best live in luxury in the mahjong shrine. They are worshipped by the public like celebrities."
    "WIth this amount of status attached to mahjong ability, players inevitably turned to cheating and other mahjong related crimes. In response to this, Japan formed its own Mahjong Crimes Division."
    "The MCD employs the best of the best detectives to track down mahjong criminals and send them to the shadow realm. This is the story of one such fledgling detective... "


label bedroom:
    scene bg bedroom with fade
    "Keikumusume's bedroom"
    play sound "audio/aba.mp3"
    "*ababababa* *ababababa*"

    k "uwaaaaaaaaah... what an annoying phone. I just want to sleep..."
    play sound "audio/aba.mp3"
    "*ababababa* *ababababa*"

    show hat
    k "(Alright, alright already. Geez, who could be texting me on a sunday morning like this... oh it's from uncle Watson!)"

    w "My dearest niece Keikumusume...."
    w "I need your assistance with a daunting task."

    k "(Hm? A task? But.... uncle Watson works for the MCD, and he's apparently pretty high up there too.) "
    k "(I don't even know anything about mahjong, and while I love detective stories, I definitely don't know anything about crimes. I don't know what I could possibly help him with.)"

    w "Please come to the mahjong shrine at 9am. I've let the guards know to let you in. It's urgent."

    k "(EEEEEE? The mahjong shrine? But that's where all the top players from Japan live! What could he possibly need me there for?)"

    k "(Aaaaaaa, I really was looking forward to a day of reading, and there's so much I need to do for the literature club... but I guess if he says he really needs me there, then he really needs me.)"

    k "(Hmph, this better be important!)"
    hide hat
label temple_start:
    scene bg temple with fade
    "Mahjong Soul Shrine"

    show hat
    k "(Wow this shrine sure is big. I'd better text uncle to let him know I'm here.)"

    k "(Gee, it's a shame writing doesn't pay like mahjong does. Aaaa, I wanna live in a place as nice as this. Oh, they even have their own maid!)"
    hide hat
    show riu
    r "Excuse me, but who are you and why have you come to the shrine?"

    k "Oh, um, well my uncle told me to come here. He said that he needed me to do something important..."

    r "What? Your uncle? Who is he?"
    k "Uncle Watson. He works with the MCD. He sent me a text telling me to come here straight away."
    r "Wait, that can't possibly be right. You can't possibly be the detective he mentioned. You look as if you're still in highschool."
    k "Eh? Detective? Me? EEEEEEH?!?!"
    play sound "audio/aba.mp3"
    "*ababababa* *ababababa*"

    k "(Oh, another text from Uncle Watson.)"
    hide riu
    w "Thank you so much for coming. Kids these days are so lazy, I wasn't actually sure if you'd come or not. Anyway, I need you to do some detective work for me."
    w "Ordinarily I'd do it myself, but I've got some more important matters to attend to. I know that you like detective novels a lot, so I'm sure you'll do just fine."
    w "Riu will fill you in on the details. I've known her for years, so you can definitely trust her. Don't even bother suspecting her."
    w  "I'll send you another text later so keep a close eye on your phone."
    w "Bye, and have fun."
    play music "audio/fishy.opus"

    k "Well Riu... I guess I really am the detective."
    show riu
    r "Honestly, what is that man thinking. Well, get to work."
    k "Y-yes of course! Where's the scene of this crime? Give me the details."
    r "Well, we think it happened last night. We found this body in the-"
    k "A body?! You mean my first case is a murder?!"
    r "Please do not interrupt me. But, yes we discovered the body this morning. His name was Joseph. He was an awfully talented player for a simple detective, so Joseph was chosen to go undercover as a spy to investigate cheating."
    r "The MCD suspected someone in the shrine was cheating during their internally ranked games, and sent him in to investigate."
    k "Wait, how do you know this? You're just the shrine's maid, right?"
    r "How rude. I am not just a simple maid. I'm the shrine's caretaker."
    r "It's actually a very important position you know. I'm basically in charge around here... even if I am technically a maid."
    r "The MCD has absolute trust in me, so I was made well aware of Joseph's position here. Now that he's passed away, everyone else has been made aware too."
    r "Anyway, come inside and I'll show you the crime scene."
    hide riu
    scene bg murder with fade
    "Mahjong Soul Shrine. Murder scene"
    show hat
    k "(I followed Riu through the hallway of the shrine to a room with a metal door on the front of it. She opened it and a terrible scene lay inside. At the far end of the room lay a dead man.)"
    k "(He was surrounded by bloodstains. His body looked cold and limp. There was a big red splotch around the mans shirt where his heart was. Beside him lay a katana with a little bit of blood on it.)"
    k "(In front of the metal door was another katana, with a blade coated in blood. There was a big rip on the wallpaper on one of the rooms walls. There was a book case that had fallen over, with books scattered around underneath.)"
    k "(There's also a broken grandfather clock, with glass scattered about underneath it. It looked like a scene where a truly terrible struggle had taken place.)"
    hide hat
    k "This... this is just horrible... it's too horrible!"
    show riu
    r " I agree. This mess is terrible."
    r "The books are all going to need to be reorganised, I'm going to have to sweep up that glass from the grandfather clock, the wallpaper needs to be done up again, and don't even get me started on how much disinfectant I'm going to need."
    r "Please solve this soon so that I can get to work."
    k "Ah, right, sure. Of course."
    hide riu
    k "(I went inside and investigated the room a little closer. I noticed that the grand father clock had stopped with its hands pointing at 1:15. There was a messy hole in the base of the clock.)"
    k "(The glass that would normally be on the face of the clock was scattered around the floor beneath it.)"
    k "(I then had a look at the two katanas lying down on the floor. Ones blade was half covered in blood, while the other ones blade just had a little bit of blood on it.)"
    k "(They both looked worn out, with chips and cracks on the edges of each blade. They were both surprisingly light.)"
    k "(Both of them had a very distinctive looking handle, shaped like a golden dragon.)"
    k "Riu, do you know where these swords might have come from?"
    show riu
    r "Ah, those tacky things. They belonged to a past resident of the shrine. He said they were ornamental swords, intended for decorative purposes."
    r "I don't think they were really meant to be used as weapons. Just look at how tacky that handle looks"
    k "You're right. Looking at them closely, they actually seem like they were made kinda cheaply."
    k "Oh Riu, did a doctor ever look at the body?"
    r "Correct. A very quick autopsy was performed. The victim died from a single stab wound to the heart. Unfortunately the exact time of death couldn't be determined."
    k "I see, thanks."
    hide riu
    k "(The last thing I noticed in the room was the hair. All of the hair everywhere. Strands of it sattered around the room.)"
    k "(Once I entered the room, it was very easy to notice. It was like a cat had come in and shed its hair everywhere.)"
    k "Riu, you don't happen to have a cat in this shrine do you?"
    show riu
    r "Well, I wouldn't say that we do. "
    r "But I also definitely wouldn't say that we don't."
    k " ...huh? Is this like one of those schroda-whatcha-ma-call-it cats where it simultaneously exists and doesn't exist?"
    r "You'll find out later when I introduce you to our suspects."
    k "Right, I guess I should investigate a little more first. I'd like to see the victims room."
    hide riu
label temple_jojo:
    scene bg jojo with fade
    "Joseph's room"
    k "(As we walked down the hallway to Joseph's room, I noticed there was even more bits of hair in the hallway.)"
    k "(Joseph's room looks orderly and well organised, like what you'd expect of a detective. Aside from all the cigarette butts of course.)"
    show hat
    k "Oh this is interesting, there's a piece of paper left lying on the floor in front of his door. It says:"
    u "I challenge you to a duel. You must accept, for I have something that I'm sure is extremely important to you. Meet me in the study room at 1am. "
    u "We'll be able to clash with no interruptions. You do know how to get in there after it's locked, right? If you can't figure that out, then you're not the man I seek."
    k "A duel... well I guess that would make sense with the state that the room was in, and also the time on the clock. But wait, wouldn't that have made a lot of noise?"
    k "People would have heard a fight wouldn't they? And what does the locking refer to? The study room gets locked?"
    hide hat
    show riu
    r "Actually, the study room is totally sound proofed. The rest of the shrine can get quite noisy, so we sound proofed the study."
    r "It's important that our mahjongers are able to study theory in peace and quiet."
    r "In regards to the locking, I lock the study every night at precisely 10pm."
    r "In fact there's a lot of rooms in the shrine that I lock up. After a room has been locked no one can get in or out of it."
    k "Hmmmmm, there's no way Joseph and the killer could have gotten in then. Unless he knew a way to get in that we don't."
    k "(Let's see what else is around here... ah, a safe. Maybe there's a clue in there.)"
    k "Riu, do you know the code for this?"
    r "Yes, I can get into it for you. As the caretaker of the shrine I have to know these things or else people will bring in troublesome items into the shrine."
    hide riu
    k "(I opened up the safe and saw inside there was a small vial of invisible ink, with a label on it saying 'evidence'."
    k "(There were also a series of blueprints for the shrine's building and layout. I looked over them, but I couldn't find any sort of hidden passage or anything into the study.)"
    k "(The next thing I noticed was a small, clear bit of sticky tape hanging off oo the door.)"
    k "I wonder... could this be the same sort of trick that was used by the famous detective Furuido Erikan? Riu, does Joseph have a lock on his door?"
    show riu
    r "No, he doesn't actually. I had the locks removed from everybody's dorm rooms so that I could come in and tidy up whenever I need to."
    k "I see... maybe Joseph left some sticky tape across his door like this so that he could know if people had ever entered his room? "
    k "With the piece being so small and clear, it's pretty hard to notice."
    k "(Hmmmm... there's no cat hair in this room. It's kind of nice to sit in a room without that gross hair lying around.)"
    hide riu
    show hat
    k "I think we've found all the possible clues here. Can you introduce me to the suspects next?"
label temple_dining:
    scene bg dining with fade
    play music "audio/box15.mp3"
    "Dining room"
    k "(I followed Riu into a dining room, and sitting around its table were five girls. I could instantly tell just from looking at them that they were the top mahjongers of the shrine.)"
    k "(It's hard to explain but, I guess you could say it was like an aura. I could feel this intense pressure bearing down on me.)"
    hide hat
    show riu
    r "Everyone, this is Keikumusume. She's technically a detective. Please introduce yourselves."
    hide riu
    show cat
    c "Hello, my nyame's Ichihime! Glad to meet nya!"
    k "(Upon looking at Ichihime, Riu's comments suddenly made sense. She was simultaneously a cat, but also a girl at the same time.)"
    k "(She had big fluffy ears and a very catlike demeanour. Aaaaa, her ears look so soft! I just wanna pet her.)"
    hide cat
    show nade
    n "Nadeshiko here. Nice meeting ya."
    k "(She's a suspect in a murder case, but she's slouched down in her chair and she even has a beer in her hand.)"
    k "(It's like she doesn't care about what's happening around her. I wish I could be as confident as that.)"
    hide nade
    show hana
    h "*yawwwwn* good morning."
    k "(For someone suspected of murder... She doesn't seem very alert.)"
    hide hana
    show kaavi
    b "Hello, mortal. I am Kaavi, the fortune teller. You've probably heard of me. My mind's eye predicted that we would meet today..."
    k "(This one's a little creepy.)"
    hide kaavi
    show kana
    i "Hello, I'm Kana-chan, the toppu mahjongu aidoru~!"
    k "(Now that's just trying a little too hard...)"
    hide kana
    show hat
    k "I suppose the next step in the investigation would be to interview everybody one by one. Riu, would you mind telling me what happened last night?"
    hide hat
    show riu
    r "Last night, we were having dinner with a group of politicians."
    r "The shrine's mahjongers are our nations greatest weapons, so often the politicians will come around and discuss certain matters with them."
    r "Last night we had one of those dinners, lasting from 7pm to 10pm. Of course I was in charge of serving the food and drinks and other errands."
    r "I was here in the dining room for the vast majority of the dinner. The only time I ever left was around 9:15pm, when I went to the basement to collect some more napkins."
    r "At 10pm the dinner ended and I locked everything up around the shrine, including the study room. Like I said before, there's a lot of rooms in the shrine so I don't normally even check inside the room when I lock it."
    r "I unlocked it the next morning at 7am, which is when I discovered the body."
    r "I also remember the precise times everyone left the dinner table. Hana left at 8pm, Ichihime left at 9pm, Kana left at 9:25 pm, and Kaavi and Nadeshiko both left at 10pm each."
    r "I think Kana said she had to practice her singing, I could hear this dreadful wailing coming from down the hallway."
    k "What was Joseph doing during the dinner?"
    r "Oh, he didn't actually attend the dinner. Before the dinner started he declared that he'd be in his room. He never really liked attending these things."
    r "I think he looks down on the politicians. So the last time I would have seen him would have been at 7pm before dinner."
    k "I see... did you notice anything else strange at all?"
    r "As a matter of fact there was. When I went to take the napkins from the basement I noticed that there was cat hair scattered about the place."
    r "I didn't notice whether or not the katanas were still in the basement at the time though."
    k "(So she notices the cat hairs but not the katanas... she really is a neat freak)"
    k "Thank you. I'd like to interview everybody one by one. Let's start with Ichihime."
    hide riu
$ q1=False
$ q2=False
$ q3=False
label nyagger_int:
    show cat
    c "Ask me anyathing you want nya~"
    menu :
        k "(What should I ask her?)"

        "Tell me about yourself":
            c "I've been playing mahjong for as long as I remember. Before I knew it, I was living at this shrine. I've never really studied it though."
            c "I don't even remember all the yaku. I just play by feel and then I winyaa."
            c "They give me lots of snacks here though and it's fun to shout PONYA and CHINYA and KANYA and especially RONYA so I wouldn't want to live anywhere else!"
            $q1=True
            jump nyagger_int

        "What did you do last night?":
            c "Hmmmm, like Riu said, I left the dinnya table around 9pm. The food was good but talking to those old men was pretty boring nya. So I went back to my room and read manga."
            c  "On my way back there I bumped into Hanya in the bathroom. She seemed really sick so I asked her if she needed any help but she said she just needed to lie down."
            c "Anyway I read manga alllll night. I ran out of snyacks so I got up around 1am togo get more cookies. "
            c "The bag is really tough to get open though so I had to get a knife, and I cut myself a little while doing it."
            k "(Hmmm, there's a bandaid on her finger. Maybe she really did cut herself.)"
            c "But after that I went right back to bed and went to sleep until I got woken up by Riu screaming in the morning."
            k "Does that mean you never went to the study room or the basement?"
            c "I nyever went to either of them! I've nyever studied in my life, so I'd nyever go to the study room. There's no snacks in the basement, so I wouldn't ever need to go there either."
            k "Is there anything else you think I should know about yesterday?"
            c "Hmmm, nope, I think that's everything nyaa."
            $q2=True
            jump nyagger_int

        "What's with all the hair":
            c "That's a little embarrassing nyaa..."
            c "These weird ears, they keep shedding hair. Wherever I go they shed lots of hair. It just doesn't stop. I don't like it nyaa..."
            k "That is pretty cat like of you. Can you turn into an actual cat?"
            c "Why does everyone ask me about that? It's just a medical condition! There's nyathing cat like about me... nya"
            $q3=True
            jump nyagger_int

        "I have no more questions" if (q1&q2&q3) == True:
            hide cat
            k "(I think that's all the information I needed from Ichihime. I'll talk to Nadeshiko next)"

$ q1=False
$ q2=False
$ q3=False
label nade_int:
    show nade
    menu:
        k "What should I ask?"

        "Tell me about yourself":
            n "There are three things I like in life: motorcycles, martinis, and mahjong."
            n "Luck favours the bold, and that's how I got into this shrine. Let me know if you want to go out for a drink after this is over."
            $ q1=True
            jump nade_int

        "What were you doing last night":
            n "Well, I stayed at dinner the entire night of course. They always bring out the really nice alcohol during these dinners. Although I didn't have much of a choice to leave."
            n "The politicians kept lecturing me over this one tiny incident where I had a little bit to drink before the match to settle the Senkaku Islands dispute."
            n "I don't really understand the problem, alcohol is good for your flow, and I still won."
            n "Anyway, after dinner ended at 10pm I went to my room and had just a few cans of beer before hitting the hay around 11."
            n "Although I did get woken up in the middle of the night by what sounded like a dying cat. I think that would have been around 1am."
            n "I just went back to sleep. Then Riu found the body and here we are."
            k "I see. Did anything else happen yesterday?"
            n "Well.. just between you and me, I think I made Joseph mad."
            n "He's the only male in the shrine, so I invited him to come to my room after the dinner and he got really mad about it."
            n "He mentioned filing a sexual harrassment claim but I think that was just a joke."
            n "Ah it's such a shame he's gone. He was such a good hunk of man meat."
            $ q2=True
            jump nade_int

        "Enough for now" if (q1&q2)==True:
            hide nade
            k "(I think I'll interview Hana next.)"


$ q1=False
$ q2=False
$ q3=False

label hana_int:
    show hana
    menu:
        k "What should I ask?"

        "Tell me about yourself":
            h "My name's Hana. I'm not really anyone special, but people praise me when I play mahjong so I like it here. I probably won't be of much use, but ask me anything you need to know."
            $ q1=True
            jump hana_int

        "Are you alright?":
            h "Oh I'm fine. I'm just tired is all. I'm just anemic. I have to constantly be taking all sorts of pills and making sure I'm sleeping lots."
            h "In fact the doctors told me I even have to wear this sleep monitoring thing to make sure I'm getting enough hours of sleep."
            k "Oh I'm sorry to hear that. Would you mind if I checked that monitor for last night?"
            h "Sure. See, here? It shows that I was asleep between 9:30pm and 7am."
            $ q2=True
            jump hana_int

        "What were you doing last night":
            h "Last night I left dinner early, at 8pm. I was struggling to stay awake at the table so I went to my room. It seemed too early to sleep though so I read up on mahjong theory for a bit."
            h "I decided to go to sleep at 9:15pm and went to the bathroom first. I ran into Ichihme on my way there."
            h "Then I slept from 9:30pm to 7am. It was actually a bit difficult to fall asleep with Kana's screeching, but I managed."
            h "In the morning Riu woke me up and here we are."
            $ q3=True
            jump hana_int

        "I have no more questions" if (q1&q2&q3) == True:
            hide hana
            k "(She seems nice. Anyway, I should talk to Kaavi.)"

$ q1=False
$ q2=False
$ q3=False

label kaavi_int:
    show kaavi
    menu:
        k "What should I ask?"

        "Tell me about yourself":
            b "My name is Kaavi. I am the greatest fortune teller in the world."
            b "I have manipulated the laws of fate and probability to create a very simple rule."
            b "My predictions are either correct or incorrect, and thus they're right fifty percent of the time!"
            b "Do not underestimate my power. I could use it to win the lottery fifty percent of the time..."
            b "...if I had any physical desires that is. This plane of reality is not too interesting."
            $ q1=True
            jump kaavi_int

        "What happened last night?":
            b "Last night, fate proceeded as I had predicted."
            k "As you predicted?"
            b "That is correct. Yesterday I predicted someone would die! The others laughed at me, but in the end those mortals were proven wrong!"
            k "(That's insanely suspicious!)"
            b "Anyway, last night I stayed for the entire dinner. I feel that I have a responsibility to inform the government on future events, so I made good use of that opportunity."
            b "After dinner ended I simply went to bed. I stayed awake all night thinking about my prediction. At 1am I heard a screeching noise."
            b "It sounded painful. At the time I wondered if it had to do with my death prediction."
            k "Didn't you think about helping them?"
            b "Of course not. I can't change fate so I saw no reason to bother."
            $ q2=True
            jump kaavi_int

        "Can you predict who will be revealed as the killer?":
            b "I could... for a 50,000 copper fee."
            k "(Aw, I only get 500 a week in pocket money.)"
            k "(I can't even afford a cookie.)"
            $ q3=True
            jump kaavi_int

        "I have no more questions" if (q1&q2&q3) == True:
            hide kaavi
            k "(Well it's time to interview the last person, Kana.)"


$ q1=False
$ q2=False
$ q3=False

label kana_int:
    show kana
    menu:
        k "What should I ask?"

        "Tell me about yourself":
            i " I'm Kana, the nations number one up and coming mahjong idol."
            i "Although to be honest I don't really like mahjong that much. My true passion is singing."
            i "But at school I scored super high on the luck exams and they've drafted me into this stupid mahjong thing. All my poor fans are starved for kana-chan content."
            k "Wow I'm talking to someone famous? How many fans do you think you have?"
            i "...lots."
            k " Lots?"
            i "Yes, lots."
            $ q1=True
            jump kana_int

        "What happened last night?":
            i "Well I went to the dinner at 7pm like everyone else. I hung around and talked to all the government people. It was a little tiring since I received lots of attention of course. "
            i "It was pretty boring, until one of them said that he had connections to the film industry. He said that he'd get me a movie deal after I turn 18!"
            k "That's amazing! What sort of movie?"
            i "Oh I don't remember. He said it was a physically demanding role so I think it was an action movie."
            i "Anyway, I left the table around, like, 9:25 pm and went to my room to practice my vocals. Then I went to sleep around 10pm. Riu woke me up in the morning with that scream."
            $ q2=True
            jump kana_int

        "I have no more questions" if (q1&q2) == True:
            hide kana
            k "(hmmmm, I think I've got a pretty good idea of what happened last night. But one of them has to be lying!)"
            k "Riu, will you take me around the rest of the shrine? There's a few more places I want to investigate. First I want to look into the bathroom."


label bathroom:
    scene bg bathroom with fade
    "Bathroom"
    show riu
    r "Do you see anything interesting in here?"
    k "Nothing yet, other than cat hair."
    k "Actually, there's something interesting here in the toilet stall. There's a ripped piece of paper."
    k "It's pretty small though. There's just one word on it, 'meet' Can you tell whose hand writing this is?"
    r "Unfortunately no. Just like the first letter, I can't tell whose hand writing this is."
    k "That's a shame. Next I'd like to check everybody's rooms."

label kana_room:
    scene bg kana with fade
    "Kana's room"
    k "(Kanas room looks just like what you'd expect of her. It's full of music stuff. Oh there's a speaker system, and an iphone too.)"
    show riu
    k "Hey Riu, can you get into Kanas ipod?"
    r "Of course, I know everybody's passwords here."
    k "(I don't think I'd hire her to be my maid even if she worked pro-bono.)"
    k "Let's see if there's any clues on here... hmmmm. There's just lots of recordings of herself singing."
    k "Well let's move onto the next room."

label cat_room:
    scene bg cat with fade
    "Ichihime's room"
    k "There's nothing particularly interesting here. Just lots of cat hair and a scratched up bed. Ew I think there's a hairball in the corner. Next room please."

label nade_room:
    scene bg nade with fade
    "Nadeshiko's room"
    k "Wow, there's a lot of beer cans in here."
    show riu
    r "Sometimes I wonder why I even bother cleaning up this room."
    k "There's a lot of sunglasses in this room. Although I can't see how they'd be relevant. Oh there's a note sticking out behind her bed."
    k "Oh, it's a love letter? It says some pretty intimate stuff about the way she thinks about Joseph.  It even has a heart at the end of it."
    k "Anyway I don't think there's much else worth investigating here."

label hana_room:
    scene bg hana with fade
    "Hana's room"
    k "This is a pretty plain room. Wow Hana has a lot of medicine. And lots of different pairs of glasses too."
    k "None of the medicine looks suspicious though."
    show riu
    r "Yes, the poor things eyesight really is bad. She has to wear different glasses for reading, going outside, driving, even for playing mahjong."

label kaavi_room:
    scene bg kaavi with fade
    "Kaavi's room"
    k "Hmmmm, nothing particularly interesting here in Kaavis room. Just a lot of fortune telling equipment."
    k "Some of this stuff actually looks pretty expensive. Maybe it's possible to bludgeon someone with a crystal ball?"
    play sound "audio/aba.mp3"
    "*ababababa* *ababababa*"
    k "Oh, uncle texted me again."
    w "It seems like you've been investigating for quite a while now. Knowing you, you should have collected all the evidence you need by now. So now I'm going to explain the shadow trial system to you."
    w "Mahjong crime is huge. There is an estimated 200 mahjong crimes in Tokyo per day. In order to deal with such a huge number of crimes, us detectives have been entrusted with the power to act as judge, jury and executioner."
    w "Essentially we run a trial with all the suspects on the spot. Once you've convicted a suspect, they will instantly be banished to the shadow realm."
    k "(Huh?! What sort of legal system is this? There's no way I can be expected to handle that sort of pressure!)"
    w "I'm sure you're worried about sending the wrong person to the shadow realm. But I'm sure that when you reason it out during the shadow trial, you'll come to the right conclusion."
    w "Oh and don't forget, I've known Riu for years. You can place your complete trust in what she says."
    w "I have placed all of my faith in you. Good luck, and don't forget to have fun!"
    show riu
    r "Before the shadow trial starts, you might want to review some of the evidence you've collected. Is there anything you want to go over?"
label review:
    show riu
    menu:
        r "Is there anything you want to go over?"

        "The times everyone left the dinner table":
            r "Hana left the dinner table at 8pm. Ichihime left the dinner table at 9pm. I briefly left the dinner table at 9:15 pm to get some napkins. "
            r "I noticed some disgusting cat hair in the basement which I had just cleaned before dinner."
            r "Kana left at 9:25pm and from then onward we could hear her terrible singing for the rest of the dinner. Kaavi and Nadeshiko both left at 10pm, when the dinner ended."
            r "I locked the study room at 10pm, and didn't bother to look inside it, like I normally do. It is impossible to open the locked door from the inside or the outside."
            jump review

        "The state of the study room Joseph's body was in":
            r "The study room was in a terrible state. There was blood on the floor, cat hair was scattered around the place, there was a big tear in the wallpaper, books were knocked over."
            r "The grandfather clocks face was smashed and its clock hands were stopped at 1:15."
            r "There were also two katanas in the room. They were a pair of ornamental katanas that belonged to a previous resident. Both were dinged up. One had a bit of blood on it, the other a lot of blood on it."
            r "It's also worth mentioning that the study room is completely soundproof when its door is closed. No noise can get in or out. Or smell for that matter."
            jump review
        "The locations of Ichihimes cat hair":
            r "The disgusting cat hair can be found in the hallway, in Ichihimes room, in the kitchen, in the dining room, in the study, and in the basement."
            r " Do note that I cleaned every part of the shrine before dinner, except for everyone's bedrooms."
            r "The only way to remove all the cat hair from a room would be to use a vaccumn cleaner. It's really filthy stuff."
            jump review
        "The layout of the shrine":
            r "The shrine is very large. But for the purposes of this mystery, only a small portion of it appears to be relevant. You could think of it like a hallway."
            r "At the top of the hallway is the dining room, which leads into the kitchen. In the middle of the hallway it splits and leads into the dorm with the bedrooms and the bathroom."
            r "At the bottom of the hallway is a door to the study room and another door that leads down to the basement."
            jump review
        "Anything else?":
            r "In Joseph's room we found a safe that contained a vial of invisible ink, with the label 'evidence' on it."
            r "We also found blueprints of the shrine's layout. We weren't able to find any hidden passageways with the blueprints though."
            r "There is a small bloodstain in the kitchen, and Ichihime has a bandaid on her finger."
            r "Kana has recordings of herself singing on her iphone, which can be plugged into her speakers."
            jump review
        "I'm ready":
            jump trial



label trial:
    scene bg trial with fade
    play music "audio/classtrialsolar.mp3"
    "The Shadow Courtroom"
    show hat
    k "To be honest with you all, I don't really know what I'm doing. So uhhh, does anyone want to start us off with a statement?"
    hide hat
    show hana
    h "Don't tell me I'm going to have to do the detective work for you. I think that Ichihime did it."
    hide hana
    show cat
    c "What the nyani! Why'd you pick on me?!"
    hide cat
    show hana
    h "It's simple. There's cat hair in every room in the house. Ordinarily you would never go into the study room or the basement."
    h "Not only that, but Nadeshiko told me she heard a noise last night that sounded like a screeching cat at around 1am, the time when the murder took place."
    h "Not to mention that little cut on your finger. You obviously got it during the duel with Joseph."
    h "In other words, during the duel you were nicked on your finger and cried out. This proves it!"
    k "('In other words, during the duel you were nicked on your finger and cried out, which Nadeshiko and Kaavi heard')"
    k "(. . .something about that statement doesn't seem right.)"
    hide hana
label trial_1:
    scene bg trial
    menu :
        k "(I think it contradicts one of these pieces of evidence)"

        "Sticky tape found hanging off of Joseph's door":
            show cat
            c "Thank you for the effort but... I'm nyat sure what that's supposed to mean."
            k "Ahh sorry I'm not sure what I meant either!"
            jump trial_1
        "Closed study room":
            play sound "audio/act_ron.mp3"
            jump trial_12

        "Clock pointing to 1:15am":
            c "Thank you for the effort but... I'm nyat sure what that's supposed to mean."
            k "Ahh sorry I'm not sure what I meant either!"
            jump trial_1

label trial_12:
    scene bg trial
    k "Wait, that's wrong!"
    k "The study room is sound proof! If Ichihime was really injured in the sword duel at 1am, then there's no way anyone would have heard it!"
    show kana
    i "Oh, what if they had the duel outside the study room then?"
    hide kana
    show kaavi
    b "Not possible. If they were clashing swords with each other outside the study room, I would have definitely heard it. I was up all night."
    hide kaavi
    show nade
    n "Ugh, it seems like we're back at square one then."
    n "Right now we need to establish how the murder happened. How'd they enter the study room while it was locked?"
    hide nade
    show hana
    h "Could they perhaps have stolen the key from Riu?"
    hide hana
    show riu
    r "That's not possible. I had the key on me in my bedroom, which was locked."
    r "From the moment I locked the study room to the moment I went to bed, the key was with me."
    r "I had the key with me when I woke up, and had to unlock my own bedroom door to leave."
    r "So unlocking the door to the study simply was not possible."
    hide riu
    show kaavi
    b "A hidden passage is still plausible. This shrine is old after all. We might not have known about it, but the killer and Joseph could have definitely known about it."
    k "(Could the killer and Joseph have known about a hidden passage? I don't think that's possible... )"
label trial_2:
    scene bg trial
    show kaavi
    menu:
        k "and this piece of evidence proves it:"

        "Blood drops in the kitchen":
            k "This proves that you're wrong!"
            b "How?"
            k "Umm, I'm not sure..."
            b "Not even I could have predicted such a stupid statement."
            jump trial_2

        "the two damaged katanas":
            k "This proves that you're wrong!"
            b "How?"
            k "Umm, I'm not sure..."
            b "Not even I could have predicted such a stupid statement."
            jump trial_2

        "Joseph's blueprints of the shrine":
            play sound "audio/act_ron.mp3"
            jump trial_23

        "the letter in Joseph's room":
            k "This proves that you're wrong!"
            b "How?"
            k "Umm, I'm not sure"
            b "Not even I could have predicted such a stupid statement."
            jump trial_2

label trial_23:
    scene bg trial
    show hat
    k "Actually, I don't think that's right!"
    k "We found Joseph's blueprints of the shrine in his room. It's a full map of the shrine's layout, and it doesn't show any hidden passages!"
    k "If he knew of any hidden passages, he would have definitely put them on this map."
    hide hat
    show hana
    h "But wait, that means... the crime was impossible? How the heck did they get into the locked room?"
    k "Well, I think we've been making a pretty big assumption about the time the killing took place."
    hide hana
label trial_3:
    menu :
        k "The truth is that the real time the killing took place was..."

        "1am":
            k "That's the real time it took place!"
            show kana
            i "Amazing! How'd you figure that out?"
            k "Ummm... a lucky guss? ehehehe..."
            jump trial_3

        " before 10pm":
            play sound "audio/act_ron.mp3"
            jump trial_34

        "just after 7am":
            k "That's the real time it took place!"
            show kana
            i "Amazing! How'd you figure that out?"
            k "Ummm... a lucky guss? ehehehe..."
            jump trial_3


label trial_34:
    scene bg trial
    show hat
    k "That's right! The crime took place before 10pm! It's the only way it makes any sense."
    k "There's no way into the locked room, and Riu discovered the body as soon as it was unlocked. So the only way it makes sense is if it took place before 10pm!"
    hide hat
    show nade
    n "Wait, that proves that me and Kaavi are innocent then! We both left the table at 10pm."
    k "That's right. There's only three people who could have done it now. Hana, Ichihime, and Kana!"
    hide nade
    show hana
    h " I see... but what about the clock, and the note?"
    k "It's simple. The killer broke the clock and set it to 1:15am on purpose."
    h "I still think the culprit is Ichihime."
    hide hana
    show kana
    i "Yep, it was definitely Ichihime."
    hide kana
    show cat
    c " Stop bullying me already!"
    k "Hmmmm, why do you two think it's Ichihime?"
    hide cat
    show kana
    i "Well it just makes sense! It's like Hana said earlier. There's hair all over the place where Ichihime wouldn't normally go."
    hide kana
    show cat
    c "Just because I never normally go into the study or basement doesn't prove anything nya...."
    hide cat
    show hana
    h "I think it's fair to assume the killers movements went like this. The killer went into the hallway and posted a note under Joseph's door, or at least told him to meet her in the study."
    h "Then the killer went down to the basement and took out the two katanas. They then met Joseph in the study room and had the duel."
    h "Ichihime's hair is all over the study room, hallway, and basement. She went everywhere the killer went."
    k "(Heh, there's definitely something wrong with what Hana just said..."

label trial_4:
    scene bg trial
    menu:
        "...and this evidence proves it!)"

        "Sticky tape on Joseph's door":
            play sound "audio/act_ron.mp3"
            jump trial_45
        "Cat hair in the basement":
            k "This evidence proves that you're wrong!"
            show hana
            h "How?"
            k "Ummmm... I refuse to explain?"
            hide hana
            jump trial_4
        "Invisible ink":
            k "This evidence proves that you're wrong!"
            show hana
            h "How?"
            k "Ummmm... I refuse to explain?"
            hide hana
            jump trial_4
        "Joseph's blueprints for the shrine layout":
            k "This evidence proves that you're wrong!"
            show hana
            h "How?"
            k "Ummmm... I refuse to explain?"
            hide hana
            jump trial_4


label trial_45:
    show hat
    k "Did any of you go into Joseph's room?"
    "........"
    k " No one claims to have gone into Joseph's room, but I can prove that someone did, with this piece of sticky tape!"
    k "Joseph had a habit of putting a piece of sticky tape on his door frame whenever he left his room."
    k "The fact that we found it hanging off his door frame proves that someone entered his room after he was killed!"
    k "There isn't a single cat hair in Joseph's room, so we know that it can't have been Ichihime who entered his room."
    k "Which means that the killer can only be one of you two, Hana or Kana!"
    hide hat
    show hana
    h "Well it certainly wasn't me."
    hide hana
    show kana
    i "It wasn't me!"
    hide kana

label trial_5:
    scene bg trial
    menu:
        "(Hmmmm... there has to be something that can prove which one of them did it...)"

        "Bloody katanas":
            k "This evidence proves who did it!"
            show nade
            n "Really? Who did it then!?"
            k "Umm, I don't know? Ehehehe."
            hide nade
            jump trial_5

        "The broken grandfather clock":
            k "This evidence proves who did it!"
            show nade
            n "Really? Who did it then!?"
            k "Umm, I don't know? Ehehehe."
            hide nade
            jump trial_5

        "Cat hair in the basement":
            play sound "audio/act_ron.mp3"
            jump trial_56
        "Kanas singing":
            k "The fact that people could hear Kana singing from her room proves that she has an alibi!"
            show hana
            h "Actually, that's wrong!"
            h "Kana had a stereo in her room and recordings of herself singing."
            h "So she could have simply used those recordings to create the illusion she was singing from her room as a fake alibi."
            k "(Kgh, back to square one)"
            hide hana
            jump trial_5

label trial_56:
    scene bg trial
    show hat
    k "The cat hair in the basement proves who the killer is!"
    hide hat
    show kana
    i "What! How?"
    hide kana
    show hat
    k "Think about it. We know that Ichihime didn't do it, and we know that the killer got the katanas from the basement."
    k "The killer must have picked up some of Ichihime's hair from somewhere and spread it around the basement and study"
    k "But during the investigation Riu told me that she had cleaned up the house before the dinner, including vaccuming the basement."
    k "Furthermore, Riu went to the basement at 9:15pm, and noticed cat hair there."
    k "Which means it must have been spread there by someone between 7pm and 9:15pm. Kana left the table at 9:25pm."
    k "Which means the culprit has to be Hana!"
    hide hat
    show hana
    h "That's bullshit! I'm not the culprit! Look at me, do you see how fucking frail I am! There's no way I could have beaten Joseph in a fair sword fight like that!"
    k "(what is this feeling... it feels so...)"
    k "(so...)"
    k "(it feels so goshdarn smug! I'll finish it with this!)"
    play music "audio/pressingpursuit.mp3"

label trial_6:
    menu:
        k "(It feels so goshdarn smug! I'll finish it with this!)"

        "It wasn't a fair fight":
            play sound "audio/act_ron.mp3"
            jump trial_67
        "Hana has been secretly doing steroids":
            k "This will prove it once and for all!"
            show hana
            h "You've only proved your incompetence!"
            k "(Oof, she's right!)"
            hide hana
            jump trial_6


        "Hana used a gun":
            k "This will prove it once and for all!"
            show hana
            h "You've only proved your incompetence!"
            k "(Oof, she's right!)"
            hide hana
            jump trial_6

label trial_67:
    scene bg trial
    show hana
    k "It simply wasn't a fair fight! The reason why you were able to beat Joseph was because you held both katanas! "
    k "Even a man like Joseph could lose in a fight to a frail girl like you if he was unarmed!"
    h "B-but what about the room. There was obviously a struggle! What about the letter huuuh?"
    k "The struggle was faked! After you stabbed Joseph in the heart, you cut up the room and smashed the big clock."
    k "You even clanged the katanas together, chipping them to make it look like a duel was fought with them."
    k "This is also how one of the katanas got a little blood on it. When you banged them together, the one you used to kill Joseph would have gotten blood on the other one!"
    k "The letter is also easy to explain. It was a fake letter of course."
    k "We know about the real letter, beause there was a ripped piece of paper in the bathroom with the word 'meet' on it!"
    hide hat
    show cat
    c "Hanya, is this true?!?!"
    hide cat
    show hana
    h "..."
    hide hana
    show hat
    k "Listen, I'm about to explain how everything went down!"
    k "At 7pm Hana excused herself from the table, using her sleepiness as an excuse. Then she slipped a note under Joseph's door."
    k "It likely said something like 'meet me in the study room at 7:15pm'"
    k "Then she went down to the basement and picked up both of the katanas. She met Joseph in the study room and stabbed him at the time she told him to meet her there."
    k "Of course even if he screamed no one would hear him. The room is soundproofed after all. After that, Hana made the mess in the room and left."
    k "She then proceeded to pick up some of Ichihimes hair from around the shrine, and spread it around the study room and the basement."
    k "However she didn't spread it around Joseph's room. She must not have realised he was using the sticky tape trick"
    k "The reason why Hana went to Joseph's room, and the reason why she killed him?"
    k "Because she knew that he was catching onto her cheating! Hana had been using invisible ink to mark mahjong tiles."
    k "She has multiple pairs of glasses, so it's likely that she had a pair that could see the invisible ink!"
    k "So of course, she went there to try and remove the evidence!"
    k "Hana, can you prove me wrong?"
    hide hat
    show hana
    h "..."
    h "You're right. It was me. I killed Joseph!"
    h "But none of you could ever understand my pain. I had to cheat! I spent so much time learning theory! I have a perfect understanding of mahjong!"
    h "But even so, no matter how much I learned, it didn't matter. I fought so hard to get here, but I always lost to luckshitters like that stupid cat."
    h "So go ahead and do it detective. Ron me and send me to the shadow realm!"
    hide hana
    show hat
#    play sound "audio/act_kan.mp3"
    play sound [ "audio/act_kan.mp3", "audio/act_ron.mp3", "audio/yaku.mp3" ]
    k "KAAAAAAAAAN! Ron! Yakuman! Get sent to the shadowrealm!"
    $ renpy.pause(1.25, hard=True)

label ending:
    play music "audio/itsumonofuukei.mp3"
    scene bg dining with fade
    "Dining room"
    show riu
    r "Well that's that."
    k "Wait, where's Hana now?"
    k "Is she really in the shadow realm? I don't even know what that is."
    hide riu
    show cat
    c "The shadow realm... is a very unpleasant place nya. I think I can understand Hana's feelings now."
    k "I know she killed someone but... I do feel bad about that."
    k "(Although honestly, that was kinda fun!)"
    k "(I don't even know what a yakuman is, but shouting that was a blast.)"
    hide cat
    show nade
    n "Well you do the crime, you pay the chombo. I just can't believe that a girl like Hana could kill anyone."
    hide nade
    show kana
    i "I always did feel like she was kind of stuck up. Still though... I'll kind of miss her."
    k "Well, I guess my job here is done."
    hide kana
    show riu
    r "Indeed. At first I wasn't sure about you, but you proved yourself to be a worthy detective. Feel free to stop by for tea any time."
    k "Thank you! I need to call Watson and tell him all about it!"

label credits:
    scene bg credits with fade
    "Thank you for reading anon."
    "Brought to you by THE WINNING TEAM."
    "Fin"
    "..........."
    "..........."
    "..........."
    "..........."
    "..........."
    "..........."
    stop music
    scene bg watson with fade
    w "Heh... it looks like... that girl really did it. She really is worthy of inheriting... the hat family legacy."
    w "Maybe, just maybe, she could even uncover and expose the Underground Mahjong Repository."
    u "Watson, it's time you gave up. You have lost."
    w "Heh, go ahead and kill me. I've already won."
    w "Keikumusume..."
    w "{color=#f00} I'll be watching you, through the hats eye....{/color}"
    "KEIKUMUSUME MURDER MYSTERY ADVENTURES, PART 2: MIKO'S COUNTERATTACK"
    "COMING OUT 2120"


    return
