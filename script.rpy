init:
    
    $ fade = Fade(1, 0, 1) # Fade to black and back.
    $ lfade = Fade(2, 0, 15)
    $ dissolve = Dissolve(2.5)

    image lounge = im.Scale("lounge.jpg", config.screen_width, config.screen_height)
    image hallway = Image("hallway.png")
    image classroom = im.Scale("classroom.jpg", config.screen_width, config.screen_height)
    image office= im.Scale("office.jpg", config.screen_width, config.screen_height)
    image room = im.Scale("room.jpg", config.screen_width, config.screen_height)
    image mari = im.Scale("mari.jpg", config.screen_width, config.screen_height)
    image badend = im.Scale("bad end.jpeg", config.screen_width, config.screen_height)
    image goodend = im.Scale("good end.jpeg", config.screen_width, config.screen_height)
    image credits = im.Scale("credits.jpeg", config.screen_width, config.screen_height)
    
    image black = Solid((0, 0, 0, 255))

    image Hajime 100 = Image("Hajime (100).png")
    image Hajime 200 = Image("Hajime (200).png")
    image Hajime 18 = Image("Hajime (18).png")
    image Hajime 17 = Image("Hajime (17).png")
    image Gundam 7 = Image("Gundam (7).png")
    image Hajime 14 = Image("Hajime (14).png")
    image Gundam 2 = Image("Gundam (2).png")
    image Gundam 17 = Image("Gundam (17).png")
    image Gundam 5 = Image("Gundam (5).png")
    image Gundam 8 = Image("Gundam (8).png")
    image Gundam 11 = Image("Gundam (11).png")
    image Mahiru 21 = Image("Mahiru (21).png")
    image Mahiru 14 = Image("Mahiru (14).png")
    image Mahiru 20 = Image("Mahiru (20).png")
    image Mahiru 3 = Image("Mahiru (3).png")
    image Mahiru 1 = Image("Mahiru (1).png")
    image Mahiru 16 = Image("Mahiru (16).png")
    image Tsumugi 6 = Image("Tsumugi (6).png")
    image Tsumugi 7 = Image("Tsumugi (7).png")
    image Tsumugi 15 = Image("Tsumugi (15).png")
    image Tsumugi 2 = Image("Tsumugi (2).png")
    image Tsumugi 24 = Image("Tsumugi (24).png")
    image Tsumugi 3 = Image("Tsumugi (3).png")
    image Tsumugi 4 = Image("Tsumugi (4).png")
    image Tsumugi 35 = Image("Tsumugi (35).png")
    image Tsumugi 1 = Image("Tsumugi (1).png")
    image Mahiru 7 = Image("Mahiru (7).png")
    image Mahiru 11 = Image("Mahiru (11).png")
    image Mahiru 12 = Image("Mahiru (12).png")
    image Mahiru 15 = Image("Mahiru (15).png")
    image Mahiru 2 = Image("Mahiru (2).png")

    define L = Character("Miss Lorie")
    define B = Character("Britney")
    define J = Character("Jake")
    define U = Character("Mr. Ulus")
    define W = Character("Willy")
    define P = Character("Police")

label start:
    stop music fadeout 5.0
    play sound "beep.wav"
    scene mari
    play music "casual.mp3" fadein 5.0

    J "Oh, Marianopolis… Such an unfulfilling and unhappy life I lead here…"
    show Mahiru 1
    B "Hey Jake! How you doing?"
    show Mahiru 21
    J "Fine, I guess... I forgot to do my schedule again, so I have a 3 hour break..." 
    show Mahiru 3
    B "Oh, silly you! You didn’t wake up to do your schedule!"
    J "Yeah…"
    J "By the way did you hear anything from Willy?"
    show Mahiru 16
    B "Oh yeah! Apparently he’s having a really bad time!"
    J "How so?"
    show Mahiru 1
    B "From what I’ve heard, his Cal teacher is super unfair to him, and integrating a ton of homework into his course!"
    J "How can anyone derive pleasure from this? That sounds like a pain in the butt!"
    J "Also, what time is it?"
    show Mahiru 21
    B "Ehhh... It’s 8:13..."
    J "..."
    J "Oh ****, I HAVE A CLASS IN 2 MINUTES!!!"
    show Mahiru 12
    B "Run, you doofus! Why do you have to be so disorganised?"
    scene hallway with fade
    
    
    "*runs*"
    hide Mahiru
    J "*pant, pant*"
    J "Almost late…"
    scene classroom
    show Tsumugi 3
    L "Okay, everyone, hand in your assignment!"
    J "NO WAY! We had an assignment?"
    hide Tsumugi
    show Hajime 100
    W "..."
    "{i}Willy looks very depressed{i}"
    J"Willy? What’s wrong?"
    show Hajime 200
    W "..."
    J "{i}Willy really doesn’t look too good… But I have to listen to the class now.{i}"
    "{i}What should Jake do?{i}"
    
    menu:
        
        "Inquire about Willy":
            jump urus

        "Listen to the teacher":
            jump lorie
    return
label urus:
    
    scene classroom
    show Hajime 100
    J "Willy, we can talk if you want."
    W "... Can you meet me outside?"
    J "Sure."

    "{i}The two leave the classroom.{i}"
    stop music fadeout 5.0
    scene hallway
    
    play music "sad.mp3"
    show Hajime 18
    J "So what’s wrong?"
    show Hajime 200
    W "I have a really bad feeling about the cal teacher…"
    J "Yeah, Britney told me he’s a pain in the ass."
    show Hajime 17
    W "Yeah he keeps pinning me down for some reason…"
    J "Oh no!"
    hide Hajime
    stop music fadeout 1.0
    play music "intense.mp3"
    "{i}Just as they were talking, an ominous figure assaulted them.{i}"
    show Gundam 7
    U "HAHAHAR! Skipping class I see, Willy! This is the not the first time!"
    hide Gundam
    show Hajime 14
    W "..."
    J "Sir, we are not skipping, we… just had important stuff to say to each other…"
    hide Hajime
    show Gundam 2
    U "I hope it’s about his last exam, because he FAILED! MISERABLY!!!"
    show Gundam 17
    "{i}The calculus teacher looks down on them like they are some cockroaches on the floor.{i}"
    show Gundam 2
    U"You only got 3 points! HAHAHAHA ONLY THREE PITIABLE POINTS! Enjoy your short time at Marianopolis because it won’t be long before you’re kicked off!"
    hide Gundam
    show Hajime 14
    J "Don’t worry Willy, don’t listen to what he says, we’re going to uncover his evil secrets and make him pay!"
    W "..."
    stop music fadeout 1.0
    "{i}They go back to class.{i}"
    "{i}Then they go home{i}."
    scene room
    "{i}Jake is sitting on his bed.{i}"
    play music "casual.mp3"
    J"Willy is in really big trouble. But maybe… I have a plan…"
    
    "{i}Jake stares at the window.{i}"
    
    J "Yes! If we find evidence that this Cal C. Ulus is treating his students poorly, maybe we can save Willy from a crappy R-Score!"
    stop music fadeout 3.0
    "*The next day*"
    play music "action.mp3"
    scene classroom
    with fade
    show Mahiru 21
    B "Good morning Jake!!!!"
    J "Good morning Britney."
    show Mahiru 14
    B "So what’s up today?"
    J "Look Britney, I need your help."
    show Mahiru 20
    B "Uh… Ok, sure…"
    J "We’re gonna sneak into the teachers’ lounge…"
    show Mahiru 12
    B "What? No way, that’s illegal we can’t do a such thing…"
    J "Look, I know what to do to save Willy…"
    show Mahiru 3
    B "Even if you did, how is breaking into the teachers’ lounge help him?"
    J "If we can find Mr. Ulus’ documents which are probably falsified because he doesn’t act like a real teacher, then we can kick him out of school, definitively!"
    show Mahiru 1
    B "Still, how do you plan on getting there?"
    J "We’ll ask Miss Lorie to get us in."
    show Mahiru 16
    B "That sounds like a good plan." 
    stop music fadeout 2.0
    
    scene hallway 
    with fade
    "*The day passes by quickly*"
    play music "casual.mp3"
        
    "{i}Miss Lorie listens to the two students' request.{i}"
    show Tsumugi 6
    L "Sure, I’ll do it, but only if you can answer this question!"
    "{i}They see an unsolvable problem on the blackboard. Only an excellent chemistry teacher could find its solution.{i}"
    "{i}What should they do?{i}"
    menu:
        "Attempt anyway":
            jump true_ending
        "Bail out of the plan":
            L"I am dissapointed in you two! You will be expelled for plotting against a teacher. BAD END!"
            play music "badend.mp3"
            scene badend
            with fade
            show credits
            with lfade
    stop music
    
    return
label true_ending:
    play music "happy.mp3"
    scene hallway
    with fade
    show Mahiru 7
    B"You can do this..."
    hide Mahiru
    show Tsumugi 6
    J"Emm… Let’s see...."
    "{i}Jake scribbles something he doesn’t understand himself...{i}"
    show Tsumugi 4
    L "Not bad! Actually, this question has no answer, I was just testing your determination! Looks like you really want to help your friend. Since you are so determined, I will lend a hand and provide you a key to open the teachers’ lounge."
    show Tsumugi 1
    "{i}Miss Lorie gives Jake a key.{i}"
    show Tsumugi 35
    L "Good luck exposing Mr. Ulus’ darkest secrets!"
    J "Thank you!"
    hide Tsumugi
    show Mahiru 21
    B "Thank you Miss Lorie!"
    "{i}Miss Lorie leaves.{i}"
    J "So, now we have the necessary tools to investigate the past of Mr. Cal C. Ulus. Let’s go!"
    show Mahiru 14
    B "Yeah!"
    scene lounge
    with fade
    stop music fadeout 2.0
    play music "intense.mp3"
    "{i}The two arrive in front of the teachers’ lounge.{i}"
        
    "{i}There seems to be someone already inside.{i}"
    J "What do we do?"
    show Mahiru 3
    B "You dumb dumb, we just have to pretend that we are taking documents for Miss Lorie! After all, this is her key."
    J "Oh you are so smart!"
    show Mahiru 21
    B "No, you are simply too dumb, Jake."
    "{i}Jake inserts the key into the door and cautiously opens it.{i}"
    "{i}Inside, an old teacher is drinking coffee while correcting midterms.{i}"
    hide Mahiru
    show Gundam 5
    J"Indeed, it is… Their detested transfer calculus teacher, Cal C. Ulus… If only our old teacher didn’t suddenly become pregnant..."
    show Gundam 2
    U "So, ohoho, what are you two doing here?"
    J "We are collecting papers that Miss Lorie asked us to take…"
    show Gundam 5
    U "Oh, go on, go on."
    show Gundam 7
    "{i}Jake and Britney cautiously search for incriminating documents, but since Mr. Ulus is also in the room, it is a lot harder to differentiate between generic bureaucratic documents and those of interest.{i}"
    "{i}At their limits, they do not find anything, and can only leave dejectedly.{i}"
    hide Gundam
    show Mahiru 20
    B "How could we be so unlucky? Any teacher could have been on break, but it just HAD to be Mr. Ulus!"
    J "It’s fine, we can find other way to do it."
    show Mahiru 1
    B "Like what? You seem you already have a plan B in the head."
    J "Sure! The plan is we will wait after 6 p.m. to make sure that Mr. Ulus leaves his office, and then we can find out his secrets."
    show Mahiru 20
    B "Do you think that could work?"
    J "I have 90 percent sure this time. Unless he lives inside the school, but there’s no dormitory in Marianopolis, so he has to leave the school."
    show Mahiru 11
    B "But that includes the students too!"
    J "Don’t worry, I know the janitor. I can explain the situation to him."
    show Mahiru 14
    B "Ehhh… You are not as dumb as usual…"
    J "???"
    "{i}However, when they were about to go back to the room, it seemed as if the principal was conducting a meeting tonight, with all the teachers… There is no way they can intrude after 6.{i}"
    J "Too bad then…we can do it another day."
    show Mahiru 15
    B "Ok, let’s resume our investigation tomorrow. Go home and sleep, we have a long day ahead of us."
    J "Good bye."
    "{i}However, it seems their plan has been heard by a mysterious man in the corner...{i}"
    stop music fadeout 3.0
    play music "casual.mp3"
    "Both of them parted ways and headed to their respective homes…"
    scene classroom
    with fade
    "*The next day*"
    "{i}As soon as they arrived at school at 7, Jake and Britney met up in front of the teachers’ lounge; this time, it was empty since most teachers awake at 8:15 are preparing for class.{i}"
    J "Alright, let’s begin!"
    show Mahiru 14
    B "Yes!"
    scene lounge
    with fade
    "{i}Both of them open the door with the provided key, and start searching through Mr Ulus’ bag for the documents he was working on yesterday.{i}"
    J "Oh! Look at this! His signature seems different from this ID card compared to the one on his insurance card!"
    show Mahiru 16
    B "Look at this! His real name is actually John Smith, a South African who is the leader of the terrorist group ‘Integral Logarithm’ ! Quickly, call the police!"
    J "No way!"
    stop music fadeout 2.0
    play music "action.mp3"
    hide Mahiru
    show Gundam 17
    U "HAHAHA! As if I could be this careless!"
    "{i}Mr. Ulus appeared from behind a door, and quickly closed the only exit door.{i}"
    "With his large body, it is impossible for the two students to escape from the grasp of a grown man, one who is the infamous John Smith as well!"
    J "Call 911! They can track our location!"
    "{i}Jack whispered to Britney, and she managed to dial the number{i}"
    "Britney hid her phone inside her back pocket, and concealed it from Mr. Urus, who already finished kidnapping Jake"
    show Gundam 2
    U "You think I didn’t see that?"
    "Mr. Ulus hangs up the call before 911 could answer."
    show Gundam 7
    U "Hahaha! My plan was to make you all fail, and then just as you drown in despair, with barely a 25 R-Score, then you would join our group of extreme-right freedom fighters out of desperation and hate towards society!"
    hide Gundam
    show Mahiru 12
    B "Stop! I already called the police!"
    U "You really don’t know that? Before you came here, I already changed the IP address of this room, it’s directed to a random region in Australia. Even they are able to find it, they are probably going to ignore your call."
    J "Britney, don’t worry about me! Call Miss Lorie and let her call the police for us."
    U "Lorie? Do you mean Lorie Sue, the philosophy teacher? Unfortunately, she doesn’t have course today, so she can’t come to rescue! Now you have no choice to be defeated by the despair! HAHAHA!"
    hide Mahiru
    stop music fadeout 5.0
    play music "intro.mp3"
    show Tsumugi 6
    L "Unfortunately for you, I am aware of those students being with you!"
    hide Tsumugi
    show Gundam 8
    U "Nani?! Was that a part of your plan?"
    "From behind Mr. Ulus, Miss Lorie appears, with tens of policemen in black uniform behind her, ready to make a sudden attack at anytime."
    P "John Smith! You are under arrest for your crimes of kidnapping underage students, for identity thief and for manipulating the last teacher!"
    "Countless barrels of guns are pointed at Mr. Ulus, and he can only raise his hands in defeat. Unfortunately for him, he had already tied up the two hostages he could have used in a corner, and they were too far to become hostages now."
    show Gundam 11
    U "Don’t forget, my revenge is not over yet. My group will continue to spread the despair of integral calculus all around the world!"
    hide Gundam 11
    "{i}After everything was resolved, Jake and Britney found newfound love towards investigation. The thrill of apprehending a dangerous criminal was impossible to wash off.{i}"
    J "Hey, what do you think about making a new club at Marianopolis?"
    show Mahiru 7
    B "Hmm… Is it the Literature Club you’ve been wanting to join for a while?"
    J "No, I want to make my own club, the Merry Mari Police Club, where students investigate mysteries around the school. There are so many things worth investigating…"
    show Mahiru 14
    B "That sounds interesting! How about we start by looking at the 7 mysteries of the school?"
    "{i}Merry ENDING GET!!!{i}"
    stop music fadeout 10.0
    scene goodend
    ""
    show credits
    with lfade
    
    return


label lorie:
    play music "casual.mp3"
    hide Hajime
    show Tsumugi 6
    L "Jake, please pay attention to class, don’t talk to Willy!"
    J "S-sorry, Miss Lorie…"
    show Tsumugi 4
    L "So as I was saying, the rise of Rome was due because of…"
    "Miss Lorie’s class is always very interesting, so students frowned when they saw Miss Lorie reprimand Jake. After all, any time wasted talking to Jake is time that didn’t go towards improving their R-Score."
    "Jake, however, was paying more attention to Miss Lorie’s beautiful face instead of the subject she was teaching."
    J "Ah, I wish I were born 5, no, maybe 10 years earlier…"
    "Time passed by so quickly when Jake spent it admiring Miss Lorie’s graceful figure."
    
    "*Class ends*"
    show Tsumugi 7
    L "Jake, could you wait a moment?"
    J "Huh! Uh… Sure…"
    "Jake could not help but blush a little when called over by his teacher. After all, her outfit today was a little light, and he couldn’t suppress his brain’s imagination…"
    show Tsumugi 2
    L "You were not very concentrated during class today...."
    J "S-sorry… I had some things in mind…"
    "Miss Lorie casually stands up and closes the door of the classroom, which is now empty except for those two"
    "The setting sun shines its resplendent light on two young people."
    show Tsumugi 15
    L "I wanted… Some advice"
    J "Uhh… I will answer to my utmost…So what the problem?"
    "The face of Miss Lorie was flushed red, but Jake couldn’t tell if it was from the sun or her blood…"
    show Tsumugi 35
    L "Actually… I’ve been in love with a man for a long long time… And I don’t know how to confess my feelings to him…"
    show Tsumugi 4
    J "Ehh… To tell the truth, I might not be the best person to ask, since I have never had a girlfriend for more than 3 minutes…"
    "In his head, Jake was going through the possibilities…He remember one of the three illusions in life: she likes me, but he immediately get that idea out of his head."
    "Jake came to the conclusion that it is probably Willy. His best friend’s peculiar behavior these days, coupled with Mr. Ulus’ strange animosity towards Willy might all because Willy and Lorie were secretly dating…"
    show Tsumugi 7
    L "Even so… How do you think I should confess?"
    J "Uhhh.... Just tell him you like him?"
    show Tsumugi 15
    L "I see…"
    J "If there is nothing else, I will be leaving…"
    "Jake was currently feeling pretty depressed… He already has a broken heart before he expressed his own feeling. His sweetheart teacher actually already had someone on her mind...."
    show Tsumugi 35
    L "I-I like you!"
    J "Don’t tell it to me! Tell it to him! Damn it!"
    "{i}His last two words ended in a whisper, impossible for Lorie to hear.{i}"
    J "Just practice at home a lot, and you’ll be fine…"
    show Tsumugi 7
    L "N-no, what I wanted to say was that… The one I like… It’s you!"
    J "Heh? You mean...that’s not a confession rehearsal?"
    L "Yes..."
    "Jake could not be happier."
    "{i}His dream{i}"
    "{i}Became real{i}"
    "{i}His whole life{i}"
    "{i}He had never seen a more perfect woman{i}"
    "{i}And she turns out to like him as well!{i}"
    "{i}Perhaps it is fate{i}"
    stop music fadeout 2.0
    play music "happy.mp3"
    J "Miss Lorie… Actually, I liked you since a long time ago too!"
    show Tsumugi 15
    L "Jake!"
    J "Lorie!"
    "{i}The new lovers embrace each other in a passionate hug{i}"
    "{i}However, just as it happened, a tremor shook the school.{i}"
    show Tsumugi 2
    J "Lorie, what’s this?"
    L "That’s not normal… Could it be a school shooter?"
    "{i}ATTENTION EVERYBODY{i}"
    "{i}The intercom sounded loudly.{i}"
    "{i}Code 61, I repeat, Code 61, please install security measures against intruders, Co…{i}"
    stop music
    play music "intense.mp3"
    "{i}Suddenly, the intercom is shut down by force, and a new voice picked up.{i}"
    "{i}Hello, ladies and gentlemen, I am John Smith, the leader of the terrorist group Logarithm Integral, who wish to turn all of Earth into a planet where calculus can proliferate endlessly!{i}"
    J "This… Isn’t this the voice of Mr. Ulus?"
    show Tsumugi 24
    L "There is no mistake… This is definitively his voice…"
    U "Today, I planted 2 bombs inside the school. There are clues left all over the place as to where and how to defuse them, and you only have 2 hours to find out and defuse them."
    U "Don’t worry, the police have already been dispatched to a false alarm far far away, and will only come to save you after the limited time… And at that point, hahahahaha, of course, everyone will either be safe or blown up!"
    "{i}Sounds of chaos were already resounding, with a batch of students trying to escape from campus, without realising that all the doors were somehow either blocked, locked, or even welded shut.{i}"
    "{i}From the windows, Jake saw that there were also spikes put under the windows to prevent people from escaping there…{i}"
    hide Tsumugi
    show Gundam 7
    U "Of course, my goal is not to kill everyone, instead, to defuse the bomb, only truly brainwashed people can solve the puzzles." 
    U "Therefore, to be alive after 2 hours means the same thing as joining my terrorist group! Hundreds of aspiring scientists, lawyers and doctors joining my team!"
    show Gundam 17
    U "HAHAHAHAHA!!!"
    J "Quickly, we need to defuse the bombs!"
    hide Gundam
    show Tsumugi 2
    L "Didn’t you hear? He made it so that only people that believe in his propaganda can defuse the bomb!"
    J "Someone has to sacrifice themselves. After all, it is John Smith, the most wanted terrorist in the world that laid this trap!"
    J "There will be no way out if everyone dies! At least I can help reduce the casualties, even if I have to go… To the dark side..."
    show Tsumugi 1
    L "What?! Wait, Jake, are you going to say that you’re gonna resolve those problems alone?"
    show Tsumugi 6
    J "Yes...because I can’t let you and all the students died in front of me. For that, I can risk all my life and my afterlife to protect you!"
    L "I’m not let you doing this without me!"
    "Jake can’t believe it. He’s already prepared to sacrifice himself for this 'game', or this organization."
    "Before Jake declare anything, Lorie interrupts him"
    show Tsumugi 35
    L "We are already a couple, you remember that? How can lovers be separated by only a such terrorist. In fact, don’t you think that would be romantic?"
    "{i}Jake stop to think too much about affording all by himself. Now, he has nothing to worry about, he’s not afraid about anything anymore.{i}" 
    J "You’re right. Let’s stop and take down this John Smith!"
    "{i}There’s no more time to waste, they have to hurry.{i}"
    "{i}They start to join Jake’s friends, such as Britney and Willy. Though they wonder why Jake and Lorie are together, but they know that’s not the right time to ask. Now they have more important thing to care about.{i}"
    "{i}There’s already half an hour past, and they haven’t found any bomb yet, that not a good sign.{i}"
    hide Tsumugi
    show Mahiru 12
    B "**** off that Ulus! Why he did a such thing! Just to make all the students died or what?!"
    "{i}Meanwhile, the school’s broadcast begins to ring again.{i}"
    hide Mahiru
    show Gundam 7
    U "It seems you guys haven’t find anything yet, that won’t make the game interesting, so I decide to give a clue: one of the place is where you pass everyday. Alright, let me enjoy more about your despair’s faces!"
    "{i}And then there’s no other sound made.{i}"
    J "Where we passed everyday? But there’s a lot, like bathrooms, hallways, classes, sidewalk, and etc. Are we going to check all of them?!"
    hide Gundam
    show Mahiru 7
    B "I think we have to do it."
    hide Mahiru
    show Tsumugi 1
    L "But the problem is where to start?"
    J "I think we can start with..."
    menu:
        "Insido":
            "Bathrooms, hallways and classes."
            show Tsumugi 6
            L "Then Britney and me will check all the girl bathrooms, and Will and Jake are going to boys’. At the same time, we can also check hallways and classes. Are you fine with that?"
            J "Yes!"
            "{i}One of Lorie’s personality is her quick reaction to the unpredictable situation. That’s also where Jake appreciates on his lovely teacher.{i}"

        "Outsido":
            "Outside."
            L "Okay."
    scene hallway
    with fade
    "..."
    "...."
    "....."
    scene hallway
    with fade
    "{i}Nothing...{i}"
    "{i}Nothing....{i}"
    "{i}Nothing.....{i}"
    scene hallway
    with fade
    "{i}Still nothing...{i}"
    "How can it turn out like this...?"
    "They already pass through all the school again and again many times. Why they still can’t find any bomb?"
    "They have even gone to the broadcast room, of course it’s tightly closed, the door is very solid, and nobody has the keys, so they have to give up the idea of opening the door by force."
    U "Time’s up!!!! Too bad for you HAHAHAHAHAHAHA!!!! So nobody find the answer? Awwwww that’s too bad hahahahahaha! Well, before I let it explodes, I think I should reveal the real answer...And they were sound of drum rolling … in the wall! Oh, and also some are under the ground." 
    U "Obviously, there are more than two bombs because I had planned to explode the whole school at the beginning! Hmm? Where am I? Well, I’ll let you guess that question, but I’m definitely not in the broadcast room, that’s for certain."
    U "Okay, enough of blablabla I guess. So... it’s time to say goodbye~ in 3, 2, 1. Adio——"
    "The last syllabes cannot be heard, because it’s covered by a big explosion."
    "All of you died in the explosion. Better luck tomorrow. Protect the Earth."
    stop music fadeout 2.0
    play music "badend.mp3"
    scene badend
    with fade
    show credits
    with lfade
    return