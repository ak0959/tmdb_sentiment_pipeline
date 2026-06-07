# templates.py

# Casual human terms for audience sizes
PHRASE_REGISTRY = {
    "fantastic": {
        "high": [
            "just about everyone who watched it", "the vast majority of fans", 
            "nearly the entire crowd", "almost everyone in the discussion threads",
            "just about every single person who bought a ticket", "the entire fan community"
        ],
        "mid": [
            "most viewers", "a massive chunk of the audience", 
            "a clear majority of people", "the bulk of the fan base",
            "a highly enthusiastic majority", "most everyday moviegoers"
        ],
        "low": [
            "a solid majority", "more than half the crowd", 
            "a good number of people", "a healthy margin of viewers",
            "a decent chunk of the community", "a fair number of fans"
        ],
        "rare": [
            "only a small group of die-hard fans", "just a tiny fraction of viewers", 
            "a few isolated defenders", "only a scattered pocket of people",
            "a minor subset of viewers"
        ]
    },
    "bad": {
        "critical": [
            "the comments are flooded with absolute hate", "the reception is getting incredibly hostile", 
            "people are completely tearing it apart online", "the threads are full of aggressive backlash"
        ],
        "heavy": [
            "most people walked away genuinely disappointed", "a massive chunk of the crowd felt completely let down", 
            "the general vibe is pretty sour", "audiences are expressing a ton of frustration"
        ],
        "moderate": [
            "a pretty decent sized group of unhappy viewers", "a noticeable wave of complaints about the writing", 
            "a fair amount of pushback on key choices", "a steady stream of vocal disappointment"
        ],
        "noticeable": [
            "a scattered handful of negative reviews", "a few loud complaints here and there", 
            "a minor subset of unhappy viewers", "some occasional grumbling about the plot"
        ],
        "trace": [
            "barely a single whisper of negative feedback", "only a tiny handful of minor complaints", 
            "virtually zero critical pushback", "almost no one complaining about the final product",
            "just a few nitpicks that don't really matter"
        ],
        "none": [
            "absolutely no one complaining", "zero negative pushback across the board", 
            "total radio silence from critics", "complete agreement that it worked"
        ]
    }
}

# Real, unpolished audience consensus combinations
TIER_REGISTRY = {
    "FANTASTIC": {
        "intros": [
            "People are completely losing their minds over '{title}', and the massive hype is actually justified for once.",
            "It is pretty rare to see this much agreement online, but the internet is almost entirely united in praising '{title}'.",
            "The general energy around '{title}' is absolutely electric, proving the filmmakers hit a total home run.",
            "If you scroll through what people are saying about '{title}', it's clear this thing completely blew expectations out of the water.",
            "Word of mouth for '{title}' has been stellar, with audiences giving it a massive collective thumbs-up right out of the gate.",
            "The praise for '{title}' is completely non-stop right now, and it is easy to see why it's connecting so deeply with people.",
            "It looks like '{title}' managed to capture lightning in a bottle, getting an incredibly passionate response from the community.",
            "Audiences are completely obsessed with '{title}', and the glowing reviews are piling up faster than anyone expected.",
            "The overall vibe surrounding '{title}' is remarkably strong, leaving almost no room for real debate.",
            "People are lining up to celebrate '{title}', calling it one of the most refreshing and engaging releases in a long time.",
            "The internet is essentially throwing a party for '{title}', with fans obsessing over almost every major creative choice.",
            "From the look of things, '{title}' has struck a massive chord, triggering an absolute wave of praise online."
        ],
        "cores": [
            "The general consensus shows {f_phrase} calling it an absolute masterpiece, obsessing over how well the pacing holds up.",
            "With {f_phrase} staying incredibly enthusiastic, the discussions are full of people celebrating the cast and the pure entertainment value.",
            "A huge part of the fun is how {f_phrase} keep pointing out the standout visual style and the director's sheer confidence.",
            "The main takeaway is that {f_phrase} walked away completely buzzing, loving how the narrative hooks you right from the start.",
            "The threads are dominated by {f_phrase} praising the incredible character arcs and how emotionally grounded the whole thing feels.",
            "It is clear that {f_phrase} felt the film delivered on every single promise, singling out the writing as a massive highlight.",
            "The commentary is highly aligned, with {f_phrase} focusing on how perfectly the climax brought the whole journey together.",
            "According to the text records, {f_phrase} are incredibly impressed by how much care went into the production details.",
            "The feedback patterns show {f_phrase} applauding the movie's energy, calling it an absolute blast to watch on a big screen.",
            "A massive portion of the praise comes from {f_phrase} pointing out how memorable and well-realized the main roles are."
        ],
        "nuances": [
            "Finding anyone talking trash about this is nearly impossible—with {b_phrase}, the positive momentum is totally unchecked.",
            "Even with {b_phrase} pointing out a few tiny pacing issues, those complaints are completely drowned out by the good vibes.",
            "The threads are incredibly clean; with {b_phrase}, it seems most people just sat back, relaxed, and enjoyed the ride.",
            "Any minor nitpicks are basically irrelevant here, especially with {b_phrase} to slow things down.",
            "The broader audience completely brushes aside the detractors, meaning there is {b_phrase} to derail the success.",
            "A few people tried to complain about the logic, but with {b_phrase}, those arguments never gained any real traction.",
            "The overall baseline remains perfectly intact because we are seeing {b_phrase} across the primary discussion boards.",
            "The general momentum easily handles any critical friction, leaving room for {b_phrase} to break through.",
            "Even the tougher critics seem to be taking it easy on this one, resulting in {b_phrase} at the end of the day.",
            "The feedback loop stays remarkably positive, showing {b_phrase} to distract from the movie's strengths."
        ],
        "verdicts": [
            "It's safe to say this one is going to stick around as a permanent favorite that people will keep rewatching for years.",
            "At the end of the day, it's a massive win that proves when a movie connects this deeply, the excitement doesn't fade.",
            "This is the exact kind of reception that turns a standard theatrical release into an instant community classic.",
            "Bottom line: it's an undeniable crowd-pleaser that turned massive expectations into a brilliant reality.",
            "It locks in a stellar reputation, making it an easy recommendation for anyone looking for great filmmaking.",
            "The final takeaway points to a project that hit every single benchmark it set out to achieve.",
            "It stands tall as an absolute triumph, cementing its place as a project that will hold up incredibly well over time.",
            "Ultimately, it's a home run that gives fans exactly what they wanted while winning over casual viewers too."
        ]
    },
    "FAVORABLE": {
        "intros": [
            "The feedback for '{title}' is comfortably positive, showing it easily won over the casual moviegoing crowd.",
            "Most people seem to be walking away pretty happy with '{title}', even if there are a few healthy debates in the comments.",
            "The baseline vibe for '{title}' leans quite favorable, suggesting the core story landed exactly where it needed to.",
            "It looks like '{title}' found its footing quickly, securing a really steady stream of warm, encouraging reviews.",
            "The overarching response to '{title}' is quite solid, proving it functions as a highly successful piece of entertainment.",
            "People are giving '{title}' a very warm reception, agreeing that it makes for a thoroughly enjoyable watch.",
            "The overall footprint for '{title}' looks highly respectable, with the positive remarks easily outnumbering the complaints.",
            "There is a lot of goodwill surrounding '{title}' right now, showing it delivered a satisfying experience to most fans."
        ],
        "cores": [
            "The discussions confirm that {f_phrase} had great things to say about the character chemistry and standout set pieces.",
            "With {f_phrase} keeping things favorable, a lot of the commentary spends time appreciating the overall tone and style.",
            "The text logs show that {f_phrase} felt the entertainment value alone was more than enough to carry the day.",
            "It is clear that {f_phrase} genuinely appreciated the creative risks the script took, even if every single joke didn't land.",
            "The general consensus indicates {f_phrase} enjoyed the solid performances and the sheer charm of the main cast.",
            "Most threads are full of {f_phrase} highlighting how well the movie handles its emotional core without getting bogged down.",
            "Review tracking reveals that {f_phrase} felt the first two acts were incredibly strong and well worth the watch.",
            "The positive feedback blocks show {f_phrase} celebrating the movie's ability to stay engaging from start to finish."
        ],
        "nuances": [
            "That still leaves {b_phrase} picking apart a few predictable plot points or messy editing choices.",
            "We are seeing {b_phrase} calling out a slightly weak third act, but it hasn't ruined the fun for everyone else.",
            "While some felt it was a relatively safe entry, {b_phrase} stays quiet enough to keep the overall win secure.",
            "The broader appeal easily absorbs the friction, despite {b_phrase} targeting the bloated runtime.",
            "There is a parallel conversation happening where {b_phrase} argue that a few scenes felt a bit conventional.",
            "A small pocket of critical pushback exists, with {b_phrase} pointing out that the ending wrapped up a little too neatly.",
            "The positive outlook remains perfectly safe, even with {b_phrase} lingering around the edges of the forum.",
            "Any minor complaints are kept on a short leash, leaving {b_phrase} to actually disrupt the general enjoyment."
        ],
        "verdicts": [
            "It might not be a flawless masterpiece, but it clearly left a strong enough impression to keep fans happy.",
            "Ultimately, it's a solid, reliable piece of entertainment that delivers exactly what you'd want for a weekend watch.",
            "The final reception points to a successful run that completely justified the excitement around its release.",
            "It won't reshape cinema history, but it functions perfectly as a sharp, satisfying, well-crafted story.",
            "At the end of the day, it checks out as a quality film that leaves you feeling glad you checked it out.",
            "It secures a very comfortable spot as a crowd favorite that delivers a genuinely good time.",
            "It's a textbook definition of a solid film—well-made, highly watchable, and leaving viewers in a great mood.",
            "The final verdict is safe: it's a completely worthwhile addition to its genre that holds up under scrutiny."
        ]
    },
    "CRITICAL": {
        "intros": [
            "The feedback for '{title}' faces a serious uphill battle, with a massive wave of negative reviews taking over.",
            "Reactions to '{title}' are trending heavily negative, and a clear majority of viewers are walking away deeply frustrated.",
            "It's safe to say '{title}' completely missed the mark for most people, triggering a lot of vocal disappointment online.",
            "Audience sentiment has sharply soured on this one, leaving the release stranded in a pretty rough space.",
            "The active threads for '{title}' reveal a highly critical baseline, with viewers tearing into the execution.",
            "The response to '{title}' indicates a severe disconnect, with negative reviews rapidly piling up across the board.",
            "People are holding nothing back when discussing '{title}', and the general consensus is looking incredibly bruised."
        ],
        "cores": [
            "The critiques are totally unforgiving, showing that {b_phrase} because of the clunky script and messy character choices.",
            "With {b_phrase}, the active threads are just filled with complaints about a total lack of coherence and vision.",
            "The reality is pretty tough here, as {b_phrase} who felt the final execution was incredibly flat and uninspired.",
            "People are not holding back at all, and {b_phrase} while pulling apart the unearned twists and terrible pacing.",
            "The core discussion is bogged down by major frustration, with {b_phrase} calling it a massive waste of a great premise.",
            "According to the text records, {b_phrase} focused entirely on how boring and predictable the middle section felt.",
            "The main text stream reads like a list of grievances, as {b_phrase} target the unconvincing dialogue and bad structure."
        ],
        "nuances": [
            "Even though {f_phrase} tried to defend the visual effects, their voices are completely buried under the critics.",
            "A tiny pocket of defenders—amounting to just {f_phrase}—is trying to highlight individual performances, but it isn't saving the score.",
            "With {f_phrase} coming back with positive remarks, the broader community is remarkably united in its disappointment.",
            "Isolated praise from {f_phrase} is effectively lost inside a massive wall of negative text reviews.",
            "A small contingent of {f_phrase} tried to argue that the soundtrack was great, but that praise was instantly drowned out.",
            "The critical backlash remains completely unchecked, even as {f_phrase} fight to protect the movie's aesthetic values.",
            "Any positive energy from {f_phrase} is rendered completely irrelevant by the sheer volume of negative commentary."
        ],
        "verdicts": [
            "It's going to face a massive challenge winning people over long-term, leaving behind a pretty troubled record.",
            "At the end of the day, it feels like a project that struggled to balance big ambitions with a cohesive execution.",
            "This is a tough spot for any release, and it definitely won't be remembered as a fan favorite anytime soon.",
            "Conclusively, the project serves as a clear warning of what happens when the execution falls way short of the initial hype.",
            "The final spread points to a major misfire that will struggle to find a welcoming audience anywhere down the line.",
            "It leaves behind a highly contentious legacy, remaining an entry that most fans would rather just forget.",
            "Ultimately, it stands as a massive disappointment, failing to capture the magic required to win over the room."
        ]
    },
    "POLARIZED": {
        "intros": [
            "The conversation around '{title}' is deeply polarized, creating an intense love-it-or-hate-it split online.",
            "Audiences are completely divided over '{title}', and no single opinion is managing to dominate the discussion boards.",
            "The reception for '{title}' is sitting in a classic middle ground, generating a chaotic back-and-forth among fans.",
            "There is absolutely no middle ground for this one; the reviews swing wildly from pure praise to absolute frustration.",
            "The public response to '{title}' looks like a textbook split room, sparking some incredibly passionate debates.",
            "Review networks show that '{title}' has broken the community right down the middle into two stubborn camps.",
            "The feedback profile for '{title}' is a total mixed bag, featuring a direct standoff between fans and detractors."
        ],
        "cores": [
            "For every comment praising a brilliant performance, there is someone else pulling apart a massive plot hole.",
            "Discussions are totally fragmented, with fans fiercely debating whether the unique tone actually worked or completely tanked.",
            "The threads show a direct clash between viewers who loved the experimental style and traditionalists who wanted a clean plot.",
            "Supporters are loudly celebrating the stylistic ambition, while an equally vocal group is tearing down the narrative execution.",
            "One side is obsessing over the incredible visuals, while the other side is completely checking out due to the messy script.",
            "The review space reads like a constant tug-of-war between people calling it a masterpiece and critics calling it a disaster."
        ],
        "nuances": [
            "The metrics show a razor-thin split, where {f_phrase} runs straight into a wall of critical pushback.",
            "With a good chunk of the audience viewing it as a completely average experience, the remaining camps are locked in a tight tug-of-war.",
            "The tone tracking reveals a highly balanced friction point, where {f_phrase} actively match the detractor group line for line.",
            "The final spread is perfectly neutral because {f_phrase} run right into an even wall of stubborn resistance.",
            "The data points display an intense balance, showing {f_phrase} fighting tooth and nail against a wave of localized complaints.",
            "Neither side is willing to back down, meaning {f_phrase} are perfectly countered by the opposing critical commentary."
        ],
        "verdicts": [
            "This exact pattern guarantees the film will keep provoking lively arguments rather than ever settling into a quiet consensus.",
            "At the end of the day, it's a project that refuses to leave people indifferent, which is honestly a win in its own unique way.",
            "Its ultimate legacy is going to depend entirely on what individual viewers are looking for when they hit play.",
            "It defies simple classification, leaving its permanent standing open to a lot of personal interpretation.",
            "It stands as a highly fascinating entry whose actual value is going to remain entirely in the eye of the beholder.",
            "The deep split ensures it will likely achieve cult status for one half of the room while remaining a total skip for the other.",
            "Conclusively, it's a movie that forces you to pick a side, ensuring the online debates won't slow down anytime soon."
        ]
    }
}