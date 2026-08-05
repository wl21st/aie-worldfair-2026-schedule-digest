# AI Engineer Worlds Fair 2026 — Full Transcript
# Organized by Speaker with Timestamps

================================================================================


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Conference Opening
**Time:** 00:09:53 – 00:11:28

[00:09:53]
Launch control, we have a go, Roger. Ladies and gentlemen,

[00:11:01]
welcome to the AI Engineer Worlds Fair. Thank you for

[00:11:18]
joining us as we continue an exciting week of innovation, technical insights, and conversations shaping the future of AI. Now, please join me in welcoming your MC, developer advocate at


────────────────────────────────────────────────────────────────────────────────
## TEJAS KUMAR (MC)
**Affiliation:** IBM / Developer Advocate
**Talk:** Opening Remarks & Day 2 Intro
**Time:** 00:11:34 – 00:15:52

[00:11:34]
IBM Tejas Kuman. Good morning, AI Engineer! We are here!

[00:11:53]
We made it, we are here. It is day two. It is such an honor and a privilege to see so many of you here today. This conference has broken records, right? Last year, uh was way fewer. This year, 7,000 people. Incredible. Huge round of applause. This is this is it. This is it. This is where it happens. Listen, there's announcements, there's takeaways, there's content across 18 tracks.

[00:12:18]
18 tracks, there's expo sessions, there's breakouts, there's all kinds of things, right? And and undeniably, I'll say this: there is value. Yes? If you've got value, make some noise this morning. Absolutely, absolutely. I have learned so much uh

[00:12:35]
from so many brilliant people here and and di I have no question that you have as well. Uh we had an incredible keynote yesterday. We had so many keynotes yesterday. Um where where Swick started the conference talking about loops. Um the the theme was was loops. Why is that funny? Um okay, I uh it wasn't a joke, but um but we had more keynotes after that about the the golden age of AI, right? Um one thing that really stuck out to me, and I'm sure many of us was wiring the agent into the intent upstream really unlocks more work.

When we start to say why things are important, we're able to unlock more work and quality work. We don't just hand it the task, but we say, do this and this is why, and this is how you verify, this is how you deploy. We we get so much more done. Teresa talked about reliability, how important it is. She talked about the 30x productivity gap between leaders and laggards, showing us that really it's about reliability more than anything else. Huge focus about evals at this conference.

Um, and finally, I I was really struck by by Daksh yesterday, who talked about uh reviewing one million AI-generated PRs and and found some incredible insights. If you didn't catch that, I highly recommend the videos the, live stream. So cool. One thing that stood out: Claude code generates, what was it, three times uh more off-bypass vulnerability code, unfortunately for now. But it's just so cool, all the insights that come out of this. Um today we've got a lot of things for it is jam-packed in. I'm very, very excited about it.

There's the newspaper. If you haven't yet read the news, we have a newspaper now, analog, uh, just to balance you know the AI. Uh so there's a there's a daily print newspaper available for you. There's a live stream audience. Hello live stream, thank you for joining. Um there is over 100 expo partners. Anyone been to the expo? These expo booths are incredible. I've seen so many cool things. There's robots lying around, so much stuff. There's also this cool device that I got. It's a note taker, but for in-person meetings.

Anyway, check out the expos, it's so incredible. We've got 3.5 days of expo in four stages as well, expo stages. So look forward to that. We want to offer a huge thank you and a massive round of applause for the incredible sponsors. Honestly, this conference would not happen without the support of our sponsors. So please, everybody, your hands together for the sponsors of the conference. We've got Microsoft, the presenting sponsor. Keep it going. We've got Microsoft. We've got the lab and platinum sponsors. We've

[00:15:07]
got you've got to keep it going. We've got the gold sponsors. We've got silver and bronze, we've got so many sponsors. And this conference genuinely would not be possible without us. So we're very, very thankful. Um now we get to introduce we get to open the state. This is so cool. Today is gonna be such an incredible jam-packed agenda. And I hope all of you can make all that you want. I mean there are quite a few tracks, but don't worry. There's a live stream, there's also videos. We're gonna start introducing our first speaker.

Oh I'm excited about this one. Who saw the announcement about Fable yesterday? Yeah, let's go! I uh this is so exciting. So so uh coincidentally, the first talk has changed

[00:15:52]
today. Uh we're gonna this conference moves at the speed of AI, it's so cool. Um our first speaker, uh Tariq comes to us from Anthropic. Give it up for Turi comes comes to us from Anthropic. Oh, I'm excited about us. I was talking to him backstage and I said, What's this gonna be about? Um, this talk. I think the first time it's ever been given, if I'm not mistaken, is about is gonna teach us all how to work with the new mythos class of models, uh, of which Fable is gonna be soonly available.

So your biggest round of applause for Tariq please welcome to the


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Speaker Introduction
**Time:** 00:16:35 – 00:16:35

[00:16:35]
stage, member of technical staff at Anthropic, Tariq Shihippar. Hey


────────────────────────────────────────────────────────────────────────────────
## TARIQ SHIHAB-ELDIN
**Affiliation:** Anthropic / MTS, Claude Code
**Talk:** How to Work with the New Frontier Models (Claude Fable)
**Time:** 00:16:50 – 00:33:01

[00:16:50]
everyone, I'm Tharik. Uh I work at Anthropic on Cloud Code. Uh before we get started, we l have a tradition on Cloud Code where we take a selfie before we talk. So if you don't mind if you strike a pose with me, I'll uh take a quick selfie at AI Engineer. Okay, incredible. Well uh yeah to kick

[00:17:14]
things off, like we said, Fable is back. Um we're rolling it out later today. Uh keep stay tuned for exact timeline. Me and Kat Woo and Simon Wilson will be doing a fireside chat at 12:30. We might have some updates for you then. Um but Fable is a

[00:17:36]
model I'm just so so excited about. It's one of those anthropic models where you just like you're just gonna remember it. Like Sonic 3.5 new, Opus 4, Opus 4.5. It's a model that I just have a lot of like affection and excitement for. And the best way to describe Fable to me is like the map is opening up. You know, like you are playing an RPG and you've been on the tutorial, and now you get to the point where the like, you know, the open world starts, right? And there's so much that you can do and explore.

Uh, but there's also, it's also a little bit intimidating and confusing, right? Because there's so much you can do. And so what I wanted to do in this talk is give you guys a field guide to Fable, right? How do you work with this new class of models? So I've got four parts to it. I've been working on this as a series of articles and blog posts. Uh, but you know, when we announced Fable was coming out, I was like, okay, let me do uh all of this at once at the talk, uh, you know, uh speed run.

So the four parts: unhobbling Claude, finding your unknowns, dealing with the grief, and being unreasonable. So first, unhobbling Claude. I think something we say

[00:19:00]
really often is that the models are grown, not designed, right? We don't wake up and be like, we need 99% on Suibench, right? Like the models are something we we grow carefully. We give it data and feedback and compute. But ultimately, it's you know something that we it's a little bit organic, and we sort of figure out and learn with the model as we use it. And so um that what that also means is that what contains them is us, right?

The harness we put them in and the way we prompt them is basically like a function of our understanding of Claude, right? And by unhobbling it, I mean how can we understand Claude better to unleash it? And we need to understand Fable more. So I think one of my points is that you know we're still so early, and I think there's a lot more understanding in Fable to unlock. And uh I think I'll give you a quick example about how models get smarter, because it's a little bit unintuitive, right?

Like there I saw this viral tweet a couple weeks ago being like, you know, why can't LLMs say which Pokemon end in AW? There are a thousand Pokemon, right? And turns out there are two who th whose names end in AW, Krokona and Dreadnought, right? And it turns out if you ask like a normal chat model, it can't answer it. Which is kind of confusing because like, you know, it definitely knows all the names of the Pokemon, right? But if you uh ask Claude Code, it can, right?

Because what it does is that it fetches every Pokemon and writes a script to filter for AW, right? And so this is what I mean by like unhobbling Claude. We call this capability overhang, right? Claude gets smarter in spiky ways. So it doesn't just remember every Pokemon and reason through it. But if you give it the code execution tool, it can find the two Pokemon that end with AW, right? And so this is, I think, part of the challenge with Fable is figuring out this capability overhang. What is now possible?

And I think this is like a discovery that I'm excited to go on with you. To make this a little bit clearer, I'm gonna talk about a few different examples of how models have progressed in the past. Um, one of the big examples, obviously, is like chat. You know, the chat models were had to be given context, right? Like maybe you paste in your code base, and maybe naively you might have thought, like, you know, the way we solve coding is by the context just gets really large, and I can just paste in my entire code base.

You know, it'll be a hundred million context window. But it turns out that instead, if you give it ARMS, like you give it the bash tool and ways to work with the environment, it can build and search its own context. And that's sort of like the insight that led to clawed code. And so again, spiky, like a new innovation kind of, right? In how we w think about and work with the model. And then recently we we've rolled out Claud Tag. Uh and what sort of unlocked Claud Tag is its ability to work proactively and multiplayer.

Uh cloud code, you know, is something that you have to prompt for it to do work, right? And uh this ability for Claude to wake itself up and do work is something that we think is unlocking the new wave of agents. But there's there's more here. So for example, uh we recently removed 80% of the system prompt for cloud code, right? And this is one of the ways in which models, you know, and what they need uh changes over time.

So originally, like, you know, maybe back in Sonic 3.5 new, the best practices for a system prompt was a small system prompt, few tools, and lots of examples, right? And then as the models get smarter, you can give it more information and more instructions, and they start following them. And so it's a larger system prompt with lots of examples and many tools, right? But most recently we found this new class of models want fewer, want want a smaller system prompt, the examples tend to constrain it.

Because it's actually more imaginative than the examples we give it. And so uh and we try to give it cons context and not just constraints. We really try and avoid being like, do not do this, um, which is really necessary for the previous models. Um and so this is like uh a way that the system prompt is changing and and probably will continue to change. Uh another feature I really like is the ask user question tool. This was something I worked on when I first got to Cloud Code.

And and it's uh when Cloud, you know, a is is planning or wants to ask you a question, it can show you a multiple to us dialogue. Uh for Opus 4, it could barely call it. I had to like really tweak the tool to make sure that it was uh that that it would work, right? And then sometime at Opus 4.5, I was like, well, what if I asked it to like, you know, ask me 40 questions about the spec? It can start interviewing me, right? And so its ability to ask questions jumped, right?

And then most recently with Opus 4.8 and Fable, I can now build a whole HTML report with the questions embedded inside of them. And uh it's just like a whole new way of interacting with uh with Claude, right? And and so this progression of like how Claude can at get information from you is also changed. Um speaking of which, uh Markdown and HTML is something I've also talked a lot about. Um, you know, it turned initially markdown was a a good output for the model.

Um, you know, it could show a little bit of rich information, and then you know, with plan mode, it started to be for you. Like it you could understand what cloud was about to do. Um, and now you know cloud can build you these in-depth HTML reports, right? And so again, a way of this the models getting smarter in a spiky way. I really like to emphasize that this is closer to a biology than a physics, right? It's still very empirical, very organic. Um, we don't know all the rules, but there is some sort of science behind it, right?

Like there is an intuition to build as well. And so I really, you know, encourage you to treat Fable like that. Uh, one of my favorite papers, uh that at Anthropic that we've written is on the biology of a large language model. Um, all of our research papers are meant to be read by, you know, people with various degrees of technical expertise, but this is one of my favorites, so uh if you're looking to learn a little bit more But so uh yeah, we talked about unhobbling Claude.

But it turns out when you're working with Fable, you also need to unhobble yourself, right? And so one of the things that I think a lot about is that the map is not the territory, right? When I'm working on a coding problem, the plan and prompt and spec that I have in my mind is the map, right? But the territory is the actual code base, the real world, the constraints that Claude needs to navigate. And whenever Claude runs into something in the territory that's not in the map, I call that an unknown, right?

Claude has to figure out what to do about it. It's a decision point that I haven't specified. And Fable is one of those first models where I felt that like I really have to figure out my unknowns, because if not, it's gonna traverse such a large area that like it's going to run into a lot of them. So how do you figure out your unknowns? Um yeah, it I fable's bottleneck my ability by my ability to match the map and the territory to find my unknowns. So a few um few ways to think about this. I like to think of it in a matrix.

So like for any problem, I have a bunch of known knowns. This is usually like what I write in my prompt. What do I want, right? Then I have known unknowns. Things that like I know I haven't don't really know yet, but I just haven't figured out yet. I can um uh yeah. Then I've got unknown knowns. Like what's so obvious that I just wouldn't write it down. You know, but I I know it when I see it, right? And then finally, unknowns, unknown unknowns. What haven't I considered at all? What do I not know, right?

Like what is something that if I knew could change how I prompt Claude. And and luckily you can use Claude, you can use Fable to find your unknowns. So I'm gonna go over a few examples of how I do that with Fable. Um, the first is I like to do what I call a blind spot path. So I like to say something like, hey, I'm working on a new auth provider that I know nothing about. Uh like in this code base, can you do a blind spot pass to help me figure out my relevant unknown and knowns and help me prompt better? Right?

And so this like might have Claude go through the the auth module and figure out like, oh, you know, this is kind of like a hairy little uh dead end that comes up a lot, maybe searches my git diff or slack, I might tell it where there's context, right? So that I can learn about you know all the gotchas. And and you can use this very broadly, right? You can use it to teach you about new fields. I I recently did this for color grading when doing video editing. Um I think this is really powerful and and Fable is incredible at it.

Um in many ways the model knows more about, you know, almost everything than I do. I just need to get it out of it. Um then I like to use brainstorms and prototypes. Uh this helps me figure out my unknown knowns, right? Things like especially for design, it for me it's like know when it you see it. So I might ask it to uh create a dashboard um and I tell it I have no visual taste. Uh make me an HTML page with four wildly different design decisions so I can react to them. Right?

And and you know you, you tweak this as want, but like the idea is to sort of get an idea of like what are the things that you uh you know you can't describe in words, right? And uh like work with the model to help figure that out. Uh then f then interviews. So once I have an idea of like, you know, this is what I want to do, uh, there's probably still a lot of like uh unknowns here, right, where I might not have considered something, I might not have specified it, and so I'll ask Claude to interview me, right?

And I'll give it a little bit more context in any of these questions, like giving it a little bit more context about you and the work and the stage you're at, like, hey, yeah, prioritize questions that would change the architecture is extremely helpful. Uh, then references. One of the best ways to give Claude a map is to give it another map, right? So, instead of me writing out the spec, uh, I can just say, hey, here's some code that represents what I want to be done, right?

It could be in a different uh system or language, uh, but just read this code, understand it, and then use that to start your work. And uh again, this can be in a lot of different ways. If I'm making a React component, I might have an HTML mock-up that is my map, right, that I pass in as a reference. I think this is really, really powerful. Fable is really incredible at it. Uh something else I've like really appreciated is implementation notes. So if uh while you're running Fable, uh, and it runs into an unknown, ask it to log it, right?

So that um you uh you can see where the deviations happened, and then you can sort of figure out why as well. You know, we'll usually give you some context about what happened. And then finally, I like to get c a fable to quiz me about what happened. Uh, just to make sure I understand what I'm doing and I can represent this work, you know, when I'm creating a PR or merging it. Um, this is a really great way of making sure that you're really in the loop with Fable.

And I think that's one of the most important parts of Fable is like staying in the loop and making sure that you get what you want. So um those are some some of my tips for working with Fable. Uh I also want to say that the first time I used a Mythos class model, uh used Fable, I felt both a huge sense of like gain, but also a sense of loss. And I I wanted to talk a little bit about that. When I think about coding before LLMs, it feels like a foreign country.

You know, like I used to run a YC startup, about 30 people, and we were just constantly forced into trade-offs because of how hard code was, right? Like we could make the app fast, or we could try prototyping a new feature, or and this might take a month, or this would take two months, and so we had to choose, and it was just really, really hard. Um and now I went back to that code base a couple weeks ago and I thought about some of the things that I wanted to do. And it was just way easier.

It was like the things that would have taken me weeks, I could do in hours. At some point it's like, yeah, like how can you not laugh? But also, how can you not cry? on honestly Like it's like one of these things where I really, really loved programming and writing code by hand. I love the feeling of like seeing the code base in my mind and like rotating it. But I also remember just, you know, like staying up late nights trying to debug, working on things for weeks without working, right? I just remember swimming in failure.

I just remember that like the most of the projects I've ever worked on have failed. Most startups go bankrupt. I think just overall programming and coding is extremely hard. And like as much as I enjoy those highs, I I can cannot go back, right? And uh the way my reflection here is like the only way out is through, right? There's still a lot to learn with agenda coding. There's a lot to learn with Fable. Uh, but I think if we try really hard, and if we like stay in the loop, we unhobble it, uh, we can get there.

You know, and we can come out on the other side uh with just um so much more. And so the last bit I wanted to talk about is is the so much more part. I call this being unreasonable. One of my favorite parts of anthropic is

[00:33:01]
that we believe that trade-offs are not real. Um like I think that very often I like in my previous company, I was very used to being reasonable. So I'd like write down this list of priorities and I'd be like, well, I guess we can prioritize this against this, right? Um and uh like you know that makes sense, so we'll uh we'll this will be our priority this quarter. But what if you uh just did all of it? You know? What if you forced reality to show you the trade-off? Right?

Um this is something I've really valued out of our culture and anthropic, and that my reflection going forward is that I'm gonna be a lot less reasonable. Um I think one of this like the math of Claude and Fable really changes how you think about trade-offs. And there are so many trade-offs that you make implicitly in your head, right? Like good, fast, cheap. Now it's pick three, right? Um I think that like the best way to like do more ambitious work is to uh like reframe and make big make ourselves more ambitious.

Because I think the only way to prove that agents work is to do the best work of our lives faster than ever before. Um you know, for example, I made this deck last night in about four hours with Fable. I feel like it's a it's a deck I really like and I I really enjoyed it, but I also um you know did it really fast. Uh, and I think that if you're here, you know, at AI Engineer, the world is kind of looking at you to prove that AI works, right?

That it's not just like a fad or something, but that it can make us more productive and also save us time. And that's my resolution for this year is to work more uh be more productive but work less and spend more time with people I really care about. Uh I think it's also worth calling out that building is easier, but generating value is still hard. And I think this is something that we run into, you know, as AI engineers sometimes, where we think so much about the process of building and our setups.

Um, but the the point is to generate value, right? And uh there it takes a lot of swings, it takes a lot of tries to find the valuable stuff, uh, but that really is the goal, and that's like you know, again, what the world is looking to us to prove that AI can really transform it. So to to end, I just wanted to say like go explore, make it real, and uh yeah, be


────────────────────────────────────────────────────────────────────────────────
## TEJAS KUMAR (MC)
**Affiliation:** IBM / Developer Advocate
**Talk:** Transition
**Time:** 00:35:29 – 00:35:29

[00:35:29]
less reasonable. Thank you. Please join me in welcoming the


────────────────────────────────────────────────────────────────────────────────
## TARIQ SHAWQI
**Affiliation:** Sonar / CEO
**Talk:** AI Reliability in Enterprise: Benchmarks, Velocity & Governance
**Time:** 00:35:44 – 00:53:10

[00:35:44]
Chief Executive Officer at Sonar, Tariq Shawkhan. Morning, everyone. You

[00:36:03]
enjoy that last talk? That was amazing. Um I particularly love the end, the being unreasonable part. I thought that was awesome. Um I also want to just I'm trying to calculate the odds of Tarik following Tarek as the first two sessions in the morning. I think the odds are pretty low on this one. But uh thrilled to be here today. As as was just mentioned, I am with Sonar. We are in the code verification space and I'm here today to talk about verification.

And I think we're all here in large part because we believe to some extent that AGI is here, it's coming, the models we just heard about Fable, it's really incredible what is going on in the in the world today. And yet we work almost exclusively with enterprises around the world. And the conversation that we have more is the question mark version? Is AGI here and why are they asking these questions?

It's because you can read the news every day, and I'm not trying to name and shame here, but if you look at KPMG putting out reports that they have to uh retract because of hallucinations, uh EY doing

[00:37:17]
the same thing, law firms getting into lots and lots of trouble because of made-up citations, made-up case law, things like this, I think we can really start to question how do we get value out of AI? The models are amazing, as we just heard, but the hard part, as the other Tarek just said, is getting value out of it. The struggle is that AI slop is everywhere. I'm sure you all see this inside of your organizations. I'm sure you see this in your everyday life that AI is amazing. The models are incredible at generating very plausible output.

They're incredible at generating things that sound correct, but are they correct? And how do you know that they're correct is a big problem. And it's a big problem in professional services as we saw, it's a big problem in legal. But really I think if we're honest, it's pr it's a big problem in every sector, in every field, whether it's marketing or finance or you name it, you have this question of how do you actually know if it's true? How do you know if it's good or if it is slop?

And the question that we uh we deal in the coding space in particular, we deal with software development. And the question we get as we talk to, I'm sure many of the people here in the room and a lot of our customers is: isn't software development different? And we can look at

[00:38:40]
the data on this. And uh the mythos models, um, this is data from um meter. Uh, you may have seen this METR. Um, the coding agents are getting better, uh, very quickly. They're getting a lot better very quickly. And you can see the progression, the exponential curve here. What this shows on this chart is how capable are the models at completing tasks that humans would take. So can they complete a task that takes one hour, two hours, whatever it is?

The latest mythos model, at least per the benchmarking, which was done a month or so ago in the preview mode, was you're getting to 16 to 18 hours. So they're actually able, the agents are able to complete long-running tasks, and it really is starting to transform how work is happening. But the critical caveat when you read the data is this is at a 50% success rate. Okay, so it is again able to complete tasks, but is it able to complete tasks correctly? Is the question. So if you start looking at let's dial up the accuracy, right?

You dial it up to 80%. And there's still progress, but it is much slower progress. Instead of 18 hours, you're at about three and a half hours or something along these lines. And by the way, this is still at 80% accuracy. And as I was presenting this to the CTO of one of my uh large customers, his response was Bataric, I would still put someone who gave me 80% accurate information on a performance review, probably, right? This isn't necessarily enterprise grade. The problem is that the models themselves, and full disclosure,

[00:40:21]
we have not yet uh done this benchmarking on the Fable models, obviously, because they are just being released. But as you look at the models, the models are getting smarter, but they still produce a lot of problematic code.

[00:40:36]
This is benchmarking that we do. We give the models a series of over 4,000 problems, and we basically ask it to generate the response to the problems, and then we analyze both the functional correctness, which is critical, and they all do extremely well on this notion of functional correctness, right? But then we look at how complex is the code, how buggy is the code, how secure is the code? And what you see with even the state-of-the-art models is that complexity is still high. It's actually quite variable as you can see here.

GPT-5.5 has done particularly well on the complexity side of things, it still generates bugs. It doesn't generate massive amounts of bugs, but it still generates bugs and it still generates security issues. So this is the output of the models that are going into the agentic workflows. And again, this is not, you know, I'm at the AI engineer conference. This is not me saying AI is fake or or um incorrect, but it is trying to address this question of how do you really get value in a production setting out of AI?

This is a study that was done in Carnegie Mellon University, and it looked at what is the actual productivity benefit that you see from the use of AI coding agents. And what you see, I think really resonates with a lot of what I see firsthand in the market, which is you have a initial just amazing boost

[00:42:10]
of productivity, of velocity in particular. What you see is a three to five X boost in productivity or in velocity. Um that dissipates in three months. At the end of three months, it starts to come back to the the normal before you were using the agents. And if you ask why, it is because of the two pieces in red here, that you start to see there's an increase in velocity, but there's an increase in security issues, there's an increase in maintainability issues, there's an increase in reliability issues, and there's an increase in complexity.

So essentially you're building the technical debt as quickly as you are generating the code, or maybe even more quickly, and that creates a different set of work. It creates a different bottleneck. And so to us, this is now the critical question in AI, which is in a world in which code is provable, and there's sessions that I'm actually very much looking forward to attending about formal methods and proofs and things like this. Code is provable. But when you start dealing with large code bases, software is not. It's still very complex.

It is still very messy. There's lots of dependencies, there's lots of uh technical debt already in most code bases, and so this question of verification is actually key. And what I'm going to be arguing is that you can treat verification as an afterthought or you can bake verification into the process. And if you bake it into the process of generating code of doing software development, you can actually start to get materially better outcomes from the coding agents than if you view it as an afterthought.

If you view it as just the old school code review. So, as we've been thinking through this, we basically have constructed a framework, and there's lots of competing frameworks around this, but I'll just talk you through uh ours. We call it the agent-centric development cycle. For shorthand, we call it ACDC sometimes, and the idea here is how do you get verification powered agentic loops? At the center, there's a lot of focus on the code generation piece.

Like how do you actually get the models and the agents to generate the code that you need to solve the problem. And what we argue is that you should surround this with the right disciplines, the right tools, the right processes to do three things: to guide the agents. And Tariq was talking a lot about different aspects of this actually.

Guide the agents, verify the outcomes, and then solve the problems, and you have to make this part of the discipline, part of the process, part of the new software development lifecycle, if you want to be successful in the AI world. So if I double-click on some of these pieces, what do we mean by guide? We've done a lot of experimenting around guide. We've just launched a product yesterday, I think, called Sonar Vortex that starts to get into this area. What we find is critically important is to think about guide as context and constraints.

And we separate out context and constraints very deliberately because context is you have your code repositories. How do we make it easier for the agents to understand, for the models to understand what is in your code base? If you have a million lines of code, if you If you have a hundred million lines of code, you have a billion lines of code, the agents work better if they understand your code base. So how do you give it architectural awareness? How do you provide semantic navigation maps and And we find it equally valuable, and

[00:45:50]
I don't think this part is talked enough about to provide the constraints as well. You have guidelines that you want your code to follow. You have dependencies you are okay using. You have dependencies that you are not okay having. You have coding standards, you have guardrails, you have intended architecture. We spend a lot of time talking about existing architecture, but what about where you want to go? And so this idea of context and constraints we've found in our testing generates a massive improvement in agent effectiveness

[00:46:26]
and a massive uh improvement in token consumption, over 30% reduction in tokens being used to solve a given problem. And if you ask why, it's because you're actually making the life of the agent easier. You're helping it navigate better. So then we get into the heart of this and we really think of guide as preemptive verification. How do you make sure there's less to verify, less to fix, this sort of thing? Then you get to the heart of verification.

And what we believe quite strongly, and what we've seen work in practice, is this idea of zero trust, multi-layered verification. Zero trust, every model has biases,

[00:47:06]
every model produces, has a character, has a personality. So let's make sure we use different models and different techniques to make sure your code is safe, to make sure it's reliable, to make sure it's secure. And multi-layered really speaks to the earlier point that software is complex, software is very messy, software has lots of intricacies involved with it. And so what we believe and again have found to be quite impactful here is that a combination of

[00:47:37]
algorithmic verification looking at things like data flows, control flows, known patterns, secrets, these areas combined with what is now possible, with agentic verification, looking at intent, business logic, the unknown unknowns, actually, again to borrow from the last presentation, the fusion of these things, the deliberate multi-layered fabric that you put in place, can actually you can see the results of this in production.

So as we look at our partners and customers who use a multi-layered verification approach, they are reporting AI-derived production outages being 44% less frequent

[00:48:18]
than the ones who do not. So you can start seeing a material improvement in reliability, in security, and in maintainability. And then the last point I mentioned is: technical debt does explode, right? As you generate code, technical debt is also generated. And again, this is not stop doing it. This is be aware and let's start controlling it. And so what we have seen be super effective is to have an active process, to have an active discipline again around code maintenance and thinking about how you do verified code maintenance.

I won't walk through every step of this, but a the agents, whether that is a set of remediation agents, whether it's a strong discipline around verification, does keep your code base clean. And a lot of people have asked me, all right, but do agents care about clean code? Human developers care about clean code. Do agents care about clean code? And what we find, again, is they absolutely do because the agents have to understand the code base if they're going to operate on it. So this is a one-shot view.

We think this is something that compounds, but if you just do the exact same agentic tasks on a typical code base and then one that has been cleaned, you see a material reduction in the amount of tokens, reasoning, energy, et cetera, needed for those cleaner code bases versus the typical code bases. Right? If you make the life of the of the agent easier, if you maintain your code base, then you'll actually see compounding effects. Now, the important thing in our mind, is to construct the system.

This is how I started, is saying, you know, I'm sure all of us do code reviews, you may use static analysis tools, you may use AI code review tools, a whole range of things. And we believe that you have to put this in a system. And again, we're happy to in our booth downstairs talk through what this looks like, but we really believe that the construction of the software development lifecycle in an AI world needs to embed this notion of guide, verify, and solve inside of it.

And you need to do it in three loops, and you need to think about these three loops. There's the agentic loop, which I think is the key buzzword of the conference. Um, now, but how do you provide the agents as it's generating the code, as it's doing the work, with the context and constraints, with the in-loop verification so that the agent is getting verification as it's working and how do you fix problems? That's that's the blue loop here. What we what we talk about is the inner loop verification piece.

There's a second, which is your continuous improvement process, and how do you really combine the power of algorithmic and agentic to generate your p your pull request, review the code, and by the way the velocity of this has to go up massively, so to review the code using agents and to do this multi-layered verification, and then you have your evals, and I think the opening speaker talked about how evals may be the buzzword of the conference, but you have your evals and you have your quality gates to check, are you actually passing?

So you have your can your code maintenance loop, agentic loop, CI verification loop, and deliberate design of these loops with verification

[00:51:46]
at the center is a compounding system. It's a system that reinforces itself. It reinforces itself in the positive and it reinforces itself in the negative. And we've seen customers who uh have kind of neglected as they've rolled out AI coding tools, they've neglected verification, they've neglected this idea of code quality, of code um maintenance, things like that, and you get into a downward spiral pretty quickly.

This is what the Carnegie Mellon case study or study actually shows, is that you actually have all the benefits start to dissipate. Or you can get into this self-reinforcing loop, and one of the tests we did with one of the large banks who are using some of the cutting edge, the folks who are all around here today, cutting edge agentic coding tools, they can get a 92% reduction in issues if you actually take this guide, verify, solve approach inside of those agentic loops. If again this compounds, it's not that each loop is 92% better.

It's that as you go through solving the problem over minutes and hours, that you actually see a compounding benefit. So that

[00:53:00]
is essentially how we see the benefit here, how we see the controlled value creating use of AI in enterprise settings. And when I say enterprises, people with existing code bases, people with you know millions of lines of code already. There's the agentic loop, there's a CI verification loop, there's the code maintenance loop. I'm required by my marketing team to put up a version of this that has our products on here. So these are our products, and you can come and see us later.

But the most important thing is really to say: our recommendation is this agent, the ACDC, the agent-centric development cycle, the core part is deliberate verification built into the system. So if you'd like to learn more, we have a booth, it's the big red booth downstairs. We'd love to talk more. We have some double click sessions coming up, so please do uh join those and uh have a great conference. Thank you all. Joining us on stage is a member of


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Speaker Introduction
**Time:** 00:54:14 – 00:54:14

[00:54:14]
technical staff at Amazon AGI Lab. Onjibarth. Good morning. It's


────────────────────────────────────────────────────────────────────────────────
## ONNO FABER
**Affiliation:** Amazon AGI Lab / Technical Staff
**Talk:** Perception Agents: Completing the Computer-Use Loop
**Time:** 00:54:31 – 01:14:17

[00:54:31]
so great to be back here at the AI Engineer Worlds Fair. Just a year ago, the hard problem was getting an agent to find a button and click it on a screen, especially screens it had never seen before. Now agents can drive browsers and they're starting to also drive desktop apps. But what we figured out clickered, clicking was actually the easy part. What we didn't solve is the actual work. And what do I mean with this? Let's take a very simple example.

A new team member starts on Monday, and maybe your job is to set up their accounts, add them to a Slack channel, book intros with colleagues, order the laptops, etc. And nobody really

[00:55:39]
owns this end-to-end process in the company. And it might be also touching five different systems. Now, agents can most likely perform each single individual individual step of this workflow. But agents still struggle to do this end-to-end because the real work lives within the seams of all of those different applications, of all of those different steps you have to take. And this is mostly where it all falls apart. The agent can use every single tool you give

[00:56:19]
it, but it still can do the full work. So why do we see this gap? Think about for a minute what we actually built. We taught computers to use computers. So what do I mean with this? We started building out the basics. We taught them clicking, scrolling, typing, calling an API, filling out a form, and we got those stops, these steps really reliable. And you can string them together in a workflow. And agents these days are fairly good at like operating those workflows. So why can't

[00:57:02]
you not just hand them more of your work and then literally just walk away and trust it to be completed. So all the things I talked about, like using

[00:57:15]
a tool, models itself, tool use, stringing agents together, this is all capabilities. And we mostly figured out how to add capabilities to models. Now the next hard part is really reliability. And without reliability, we cannot really build up trust in those systems. So here's a quick gut check, and maybe all of you can just think about an agent doing work in an end-to-end workflow. How often do you think that actually succeeds these days? Maybe 60%? Maybe 80% of the time. And it sounds really fine.

But if you look into this, if your agent one in four times deletes a database, you will never touch that agent again, right? So when you need this reliability, you really need to be it in the nines. You need to have the trust that it actually can do the work successfully. Now there's actually one place where we made

[00:58:38]
enormous progress on reliability and trust. And this is coding, right? Think about how fast coding evolved. I still remember the first time when it started autocompleting for you, right? You just tapped autocomplete, amazing. Then short time later it started to write functions. And we thought that is amazing. And now look at these days. Coding agents write the code, they open up the pull requests themselves, and we heard it earlier this week, code keeps flying by.

So once in a time we were able to just every single line that it generated, we felt like the urge, we need to really read it and make sure it's correct, right? I think most in the audience here can still relate to that. These days, I think hardly anyone is still doing that. Like we cannot even do that, right? Code is generated at such a pace at the same time, coding made the jump. So why is that? Because we were able to bring it from just being capable, the coding agents, to actually be reliable and then trusted. So why is that?

Why was coding first solved?

[01:00:02]
It's because code is verifiable. You can run it, you can test it, you can check it, and you can be for sure that it worked. So reliability showed up in the first place. You can actually verify the answer. But here's the catch. Most of the work we do, if you look at the broader knowledge work areas, is not like that. Knowledge work is messy. And heck, the

[01:00:39]
whole real world is really messy. Did the report I created land? Is the design on brand? Did it get it what I actually meant? So there is no unit test that can answer those questions. So verification really hits

[01:00:59]
the wall right where most of our work lives. It's living in the seams of all of those applications we're using on a day-by-day basis. And nobody really has scrapped this part yet? How do you make an agent reliable when there's no way to verify the answer that easily?

[01:01:21]
And that's a field that is still wide open. So, how can we solve this? Well, so how do humans handle messy work? I mean, we're successful at it, right? Each of us, like every day we work across different systems, we manage out how to onboard a new colleague. We do this. Well, we're doing it by figuring things

[01:01:48]
out together. You grab a colleague, you jump on a Zoom meeting, you're discussing things, you're looking at the problem to solve, you're discussing pointing at systems, and maybe two

[01:02:02]
minutes later you, solved it, you're done. But none of this work is actually directly verifiable. And we do this all day. So one of the things is we're looking mostly at the same screen, right? If you're jumping on a meeting with a colleague, you see the same screen, both of you, and you can actually like figure out really quickly what needs to be done. So, this is what the agent these days is missing. You don't necessarily need a bigger brain. What you need is this shared context.

Because if we're looking, the agent and myself at the same screen, I probably have much less explanating to

[01:02:47]
do. So what kind of agent do we really need to build to achieve this. And today's agent, as I said, they can already see a screen, right? And they can click and take actions in it. That part works. But if they fire off actions, what they usually do, they move on. They don't watch what happens or recover if one step didn't succeed or something goes sideways. And we need an agent that can actually work like you do, like humans work. And one example is robotics.

If you just look for a moment as how robotics do it, a robot perceives what's around it, and it plans

[01:03:37]
what to do, and then acts. So this loop here from perceiving to planning to acting, this is actually what we also would need on a screen. And it starts here really with the first word, which is perceive. The agent has to take in the screen the way you do. Not scrape the code behind the page, but what's

[01:04:05]
actually rendered. The layout, the state, what just changed, the work, what we're doing and then do it. And it would also have to keep up in real time. Think about how we as humans work together. You jump in, you react to build on top of what each other you say. And today agents can still don't do it. What we're doing is we're sending a prompt, we're waiting, it goes away, and at one point the agent come back, and we might have to take a couple of turns, right? Because what the agent come back with is not exactly what we might want to do.

So we're sending another prompt, say, hey, go back, do this, do this differently. And we have this long back and forth, which we got so used to from our chatbot experience and from this rhythm taking turns. But what we actually

[01:05:05]
would need, think about it, is an agent that can react while you're still working. Wouldn't that be really cool, right? Like at the same time, you're working, it can also come up with suggestions, can help you, and there is no waiting time. So basically, an agent that perceives

[01:05:26]
what you perceive and understands what you mean. We call them perception agents. So why perception agents? Why do they matter? So first they complete the loop on computer use. Today's agents again they can act. They can click, they can type, they can scroll, but what they can't do well is looking at the result and whether it actually worked out. A perception agent can read the rendered screen

[01:06:07]
so it can confirm its own output instead of just firing off those actions and then hoping. Second, it doesn't need an API or backend- process. And that's important because it works off the rendered interface, it sees the same pixels and the structure you see. And most of today's software people use every day don't expose APIs at all.

[01:06:38]
And then third, the input also goes the other way here. Instead of writing a long paragraph to describe what you want to change. Let's say you're working on a website and you want to describe all the changes you want to apply. Instead of writing this really long description, wouldn't it be great if you can just point to it and say, hey, here this heading needs to change. Hey, can you update this section? This is a much more precise signal and less lossy than text. And the

[01:07:14]
agent can act exactly on what you marked. So this is where we started, and I'm happy to share that we just recently launched the first two pieces of our perception agent harness. Open source. There's two pieces. There is annotation which you can use to tell it what you want. And then the second piece, the verification part, gives the agent the capability to check its own work. So let me show you the first one. So here's a very quick demo on our annotation tool.

This one is a Chrome extension, so it's super easy to use, and I'm gonna play here this quick video demo. So you have the extension installed, and then you can just select different elements on a screen. So this example we're just drawing around the heading there, marking the section. And maybe you want to change it, why not? Let's change it to red. You could also select the elements on this page. You see how if I hover over it finds the right element, you click it, you select it, and say something maybe double the font size.

And you see also how the agent here captures on the screen ex,actly the feedback, the location, the style elements. And it creates this complete summary, which you can then use and then give your agent to implement. So there's no back and forth anymore because you captured exactly what you saw on screen and the agent can see the same thing. Now

[01:09:05]
let's have a very brief look at the second one at verification. So the idea of verification is that you can describe let's say in this case of the web development. You can describe in a design MD file what your design rules are for this. And then what happens if I play this video here? The act the agent can actually check its own work against those design specs. So it will take what you defined, the colors, the components, your layout, and it turns it into those rules if you don't have it written before yet.

And it does two kinds of checks then. It does a visual check, which is really cool. So everything is on brand, for example, it's the right layout. The other part is

[01:10:00]
also checking user flows. So what it does there, it actually walks through this experience through the app, for example. Depending on the tasks available, it might add a task, it might delete a task like a real user would. So it helps you walk through those user flows as well in an automatic fashion. And then once it's done, it's writing a report which you can review. And it's gonna call out which tests passed and it's gonna tell you anything that didn't. So ultimately you're the one that

[01:10:36]
doesn't have to click through this at midnight at the end of the day, because great work, the agent already did this job for you. Now, there might not always

[01:10:48]
be a screen, right? So I talked a lot right now. I called it perception. I talked about the age and sees what you see on a screen. But there are times in your day where you don't have a screen. Maybe you're in the office, you're walking into a meeting with a colleague. So I did a fun experiment yesterday at the conference here. So I grabbed my colleague Giovanni, who's also here. And actually on the second floor, there's a great like little meeting booth. We found that by coincidence. So we went in there and we had our design meeting.

And the goal here is really kind of show you how perception is so much more than just the visual part. So, in this example, what we want to show you is perception can also be listening in the room to what you're discussing. And you can see here on the picture, both of us are wearing our B devices. Big shout out to B for sponsoring these. Um we're sitting there, we have our B devices that can do a transcript, they're listening to what we're saying. And then we had this design meeting, and I had a couple of great ideas how to change this website.

You will see them in a in a second here. So let's have a quick look how this changed the same workflow on this website using this device. So

[01:12:13]
we had the discussion, the B did the transcript, and you can see here on the right, we're pulling this meeting transcript right in. There is a whole detailed summary of the meeting. There is what we discussed, and then

[01:12:31]
it basically captures those insights. We have them right here, and we can click apply. So what this apply button does is it sends it straight to the agent. And you can see here my crazy idea is to turn the background to yellow, turn the heading to red, and also change the emoji directly applied. And it also straight kicks off the verification right away. So it creates this report and and luckily this color scheme was apparently into in the approved rules, otherwise this would have flagged like you did some weird things here.

But again, you could change those rules if you don't want to have yellow backgrounds, and it will make sure um that we still adhere to those guidelines. It would flag anything that's off. So you have the judgment call if you want to either update the design specs because you actually like yellow, or you take an action and say, no, um fix this violation. But this is really the very first step.

[01:13:31]
These two pieces are the very first beginning, and we're building out the rest in the open. Because these patterns can only get better if more people are using them, building on top of them, breaking things. So my ask here to you is go and try them out. They're on our GitHub repos, open source. Tell us what we're missing. Give us the feedback, what you would like to see, where this should go next. Because ultimately, none of us get smart alone. And that's the whole point. We want to build AI that makes all of us smarter together.

Now, if you're interested in a little bit more

[01:14:17]
on human-agent interactions and how we see those patterns changing. I would highly recommend this podcast by my colleague Danielle Persik. She is a cognitive scientist and runs our AGI ACI team at the lab and discusses a lot about human computer interaction patterns with experts in the industry. You can find the podcast on any popular podcast platform. We also have more sessions this week. Um, so check them out.

We have a booth down there, we have expo talks, we also have another computer use track talk coming up with my colleague Gauraf Mishra at 1:30 in the computer use track. Highly recommend checking out his talk from RL to IRL. And then ultimately come find us. We have a huge presence down at the Expo Hall. We would love to continue the conversation with you all. If you're not here in person, you can also check out our code on our GitHub repo and check out our website. And with that, thank you very much. Please welcome


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Speaker Introduction
**Time:** 01:15:33 – 01:15:33

[01:15:33]
to the stage, the vice president of research at Google


────────────────────────────────────────────────────────────────────────────────
## BENOIT SCHILLINGS
**Affiliation:** Google DeepMind / VP of Research
**Talk:** The Future of Software Engineering with AI: From Code to Science
**Time:** 01:15:44 – 01:33:48

[01:15:44]
DeepMind, Benoit Schillings. All right, good morning. Uh this is

[01:16:09]
really quite exciting to be here and have a chance to speak with all of you. My name is Benoit Schellings. I'm actually a bit of a noob when it comes to machine learning. Till a year and a half ago, I was working for Google X, which some of you may know. We've done things like Waymo, which seems to be at every street corner now. We also do things like glass. So you know we had a mix of hit and success. But in many ways this was for me an interesting formative experience on how to run a research team in a place like DeepMind.

I do have an incredible team. My team goal in DeepMind is

[01:16:55]
basically to develop whatever technology will be needed to make Gemini incredible between one month and one year from now. So one month because if you start to work on what is needed in one week, that's a very different type of job. And one year because I don't think anybody can really predict anything that far. So uh that's already pretty ambitious in my opinion to think about things that would happen one year in the future. We do many things under that uh role.

Uh a lot of it is related to code, which will be the main subject of my talk today. But we also do a lot of research on what is the evolution of reasoning for models, for instance. Or we do topology research. What are new type of network that might bring better performance. We do fundamental work in the science of reinforcement learning, which is so fundamental to what we're doing today with ML. Let's do a bit of an origin story. We

[01:18:02]
started the project at X named Pitchfork in 2018, which was aimed at looking at how ML could really improve the way code is being written. And this was very interesting because in 2018, when we presented that at Google, honestly nobody would give us the time of day. There was that point, like why would you ever need ML to write code? At the same time, I think that we totally underestimated how fast this could go. When we did that project originally, the idea was to look at how we could speed up the evolution of a piece of code.

How could we make many of those small changes which slows down code speed development, you know, the small edit which requires a review that takes three days, and how we could compress that cycle. Some people were talking about vibe coding, writing code in English, and at the time, honestly, I totally dismissed that. I was, that's why we have programming language. English is not a programming language. Well, I guess I was pretty wrong on that front.

But the resistance we felt at the time reminded me of how my own career was pretty resistive to change. I've been writing code for 45 years. I started

[01:19:25]
by writing video games for Apple II and Commodore 64. So my formation was to write assembly language. And when you spend a long time writing assembly language, you look at compilers with a lot of suspicion, right? Are those things really working correctly? And then when you switch to C and use compiler, you lose, you look at garbage collected languages as this. Hmm, that's not real programming, you need to manage your memory. Well, today I use Python and vibe coding. So uh even old dogs can learn new tricks.

So uh but but I I I do understand what happened there. I think that we have a

[01:20:05]
number of errors in what happened with software. And and the first one was you know the one where I started writing code, where the fundamental limit was really the machine. And there was a lot of work to go and extract the last ounce of power out of those machines. And that was the days of assembly language where you really needed to be incredibly accurate in the way you were writing code. Computing became much cheaper and we switched to the modern cloud era, where getting the best performance is not the most critical aspect.

You can actually brute force many problems. But really what became the limiting

[01:20:48]
factor was the ability for us to design in a modular way. You know, this was the era where software was write it only once. And this was this whole idea of how are you going to build libraries? How are you going to write functions? How are you going to break down that problem into something that is long-term manageable? The limitation there, and that determined a lot of how our software process are working, were actually the human brain. A traditional human, typical human, is able to get

[01:21:20]
the context between seven and nine tokens. I mean, we have very rich tokens, but you compare that to modern ML where the context is basically going to be infinite pretty soon. That fundamental limitation of human determined a lot of how software was being written. This is over and we're switching now to that AI frontier where really writing the code is not the challenge anymore. I'll speak some more about it, but the bottlenecks are really how do you ensure that that code is what you really wanted?

Because writing the code is easy, but getting what is needed for a specific problem can be much harder to specify. So humans, at least in the near future, will be that role of architecture or thinking of what are really the implications of that piece of code I'm getting the ML to design. Inductive thinking is another category where I think humans still have a a very clear edge, which is to look at a system in a much wider context and to be able to detect patterns and from those patterns take some decision. So where are we today?

Superhuman syntax generation. When is the last time I

[01:22:37]
got Gemini to write a function for me and I looked at the function and I was like, I can do that better. It's over. I think that the minutiae of code writing, I mean you can fight, you can argue, you can find counterexample, but that time is is gone. Where we still have a lot of work to do is multi-step code base. Software engineering is not about

[01:23:02]
writing code. Software engineering is the first time you join a company and you realize that there are 35 million lines of PHP in the code base and that you need to make some changes. That's the day you understand what software engineering is. And that's a place where our modules today, our frontier models are progressing, but this ability to manage that extreme complexity and break it down into manageable pieces is a place where the frontier is still moving. It goes all the way to architecture. You look

[01:23:36]
at, I don't know, the Google architecture, thanks God we have Jeff Dean, which was you know the key architect there, but that's the level of thinking which has many implications, which can go from how do you do hardware optimization, how do you manage security, how do you build a system so that ten years later you're not full of regrets. And I I think this is really the range of progress we are working on today. So code is over, but there's plenty to do, there's plenty of progress to be made.

Now code is a very unique problem, and in some way that's the reason we we did pitchfork on this. First of all, code has a lot of data. There are other domains where you can find a lot of data to train your model but code was so incredible you could go and go on GitHub and start to to scrape GitHub. So th this was one of those problems where the amount of training data was a very unique situation. It is also a domain where doing verification is reasonable. You can run a piece of code, you can compile it, you can have unit test.

So the ability to figure out is the model generating something correct was something that was pretty reasonable to do. That brought us where we are today. But today, what happened is that we ran out of training data. I think that 80% of the new code added to GitHub today is machine generated. So the notion of human bringing some knowledge that can be used for mining and to train model is reaching an end. But the good news is that we can do self-play. And self-play is something we always liked a lot at DeepMind. I suppose all know AlphaZero.

AlphaZero became a superhuman go and chess player without any human knowledge, just by playing against

[01:25:32]
itself. We are now at that stage where frontier models for code are able to do the same, where they can create their own challenge, they can judge the validity of the answer, they can even to some extension judge the architecture. So that ability to do those hundreds of millions of hours of self-play writing code is the thing that will bring us to the next layer. You know, it's interesting. Um do the experiment.

Take a brilliant software engineer, lock him in a room, lock him or her in a room for two years, and feed pizza and give the mission you need to become a better software engineer. What do you do as a person? You give yourself some challenges, challenges that you can verify and you keep working and coding on those challenges. We can do the same here. So this is an issue of how much compute, how much self-play time we can have, but that will bring the horizon of how far we go in superhuman coding. So the economics of code are changing

[01:26:36]
dramatically. You know, as I say, we developed a whole software engineering culture and infrastructure and set of companies based on the assumption that writing code was the hard part, that this was the expensive part. We're now in a world where writing code is free, uh, or nearly free. That's why I've got the tilde there. That means that the amount of code that we're going to see produced is going to explode. And there are some hard implications to that. First is the question of design and adequacy.

How in front of that mountain of code which would be written or written dynamically, how do we keep systems which work and are reliable at the macroscopic level? Great role for human. It is also the issue that you know we are writing code and we're not reading it very much anymore. I mean I know we still have code review, but uh I would predict that in one year we'll let Gemini or other models generate the code and nobody will actually look at it. You know, it's similar to compilers. Who still check the assembly output of their compiler?

And may maybe uh someone there. That's probably the end of it. So the same thing is going to happen to code, and that brings some question of what are the new processes that we need to put in place to keep that manageable. And that's where I've got a a bit of a list. Active guard rails. I mean you've all seen the news of Mythos looking at a piece of code and detecting a unreasonable number of vulnerability in that code. There is a rush to

[01:28:19]
go and patch those vulnerability, but I think that's going to be a never-ending process. You know, we're going to get a certain layer of vulnerability discovered by models, we're going to fix those. Models will get smarter, they will go a bit deeper and find even more subtle vulnerability. So I think that the first aspect is that we need to think at least as much about code security and the implication of a piece of code than on the code writing itself.

And the grail, and you know, something my team is working actively on is instead of detecting the vulnerability and then suggesting some fix, how about

[01:29:00]
teaching model to write correct things from the start? And that is very, very hard to do because it is very context-dependent. The other aspect is that you know that's what I call inductive architecture. I think that models today are still not very good at transferring knowledge, of taking knowledge from one domain and applying it to another one, or taking two concepts and finding the intersection of those contexts to be those contexts to be able to do deductive thinking.

If we really want to write those very complex software systems using ML, that is a skill that we need to teach. And you know, one aspect of that is to really teach models how to do correct planning in front of a problem. How do you look at a very complex problem and decide what is the right decomposition of that problem that will bring the best clarity or correctness to the to the problem? We also need to change the way we do evaluation. I mean uh 3bench is infamous in in my book because 3bench

[01:30:06]
verifies if a piece of code runs and produces the right output. That's only a small part of, as I mentioned earlier, of code engineering. So for instance, I think that we need some problems much more in those benchmarks that we use, which are open-ended problem. I'll give an example. I love the question of text compression. How many bits per character do you need and how far can you go? So that's a very simple eval to to write.

You just take a piece of 10 megabytes of code and you tell the model write the best compressor you can that is lossless. And the loss function in that case will be the size of the compressed file plus the size of the source code. That's never ending. I mean those problems are I think what's going to force those models to do novel things like creating totally new algorithmic for instance. And I I think we're now getting to that stage. Writing code or doing software engineering

[01:31:08]
is not thinking as a chain of tokens. Thinking and reasoning today is chain of thought, which has been you know very successful and improved models a lot, but humans of course are much more complex in the way that they think about problems. I always think that code writing is a very visual activity. And that can be, I don't know, the block diagram of what you're doing or the flow of data through your code. But saying that code will be just a set of tokens that you emit that are going to be the code, I think goes only up to a certain point.

That's a very interesting aspect to what we do at Google. Gemini, we made the choice from the onset that this would be a multimodal model, that you know text was only one of the modality that Gemini would be able to apply. And we're starting to see, you know, how can a model start to think in terms of spatial or dynamic representation to solve problem. And I think that's going to become a must-have. Another interesting question is: is this time

[01:32:16]
to create a new language for models? Python, you name it, have been invented for humans. And those languages are not very good to write safe or reliable code. I mean they're great to write code, but they are certainly not the the best thing. I think we're getting to the point where since the pain of writing the code does not exist anymore, how about we make writing the code much harder by having, you know, very strongly typed languages or some inspiration from Lean on how to write code that by design it's not going to be perfect.

I mean program proof is something which has some limits. But at least putting the burden of correctness uh on the model. So I don't know if we have some language designers here, but I I think there's something really to be done there. And it doesn't need to be human readable. I don't think that that will matter anymore. So beyond code, code is a universal language to solve

[01:33:17]
problems. I think that what we're starting to see is this ability to experiment very quickly in code is impacting other domain very quickly because doing experiments becomes basically free.

[01:33:31]
So I think that looking at that intersection of code writing and atoms or science is another big front that we are opening. That is the place where true novelty is going to appear. Two which are especially exciting for

[01:33:48]
me is chemistry. You know, as humans we do not understand chemistry or we understand a very, very small sliver of chemistry. Once you have more than 20 atoms in your molecule, it's like, wow, we don't know what that thing is going to do. I think we're going to see incredible things emerging out of that. I mean, once you are able to put 10,000 atoms together, that starts to look like life. So what are all the other things you can do with 10,000 atoms.

Biology, you probably heard plenty about it, but you know, biology is the case of nature did an incredible engineering job and terrible job at documentation. But we can crack through that now. Models are able to find those relationships that might be elusive for us. So I think that that is something that will open incredible door. And then there is what I call the gold we cannot see. Humans are incredibly biased in what we feel is the correct solution.

I mean we're the result of an evolutionary training that helped us survive in the jungle, right? Not doing quantum computing. So I think that even though we can be brilliant and innovative, there are a whole bunch of progress and breakthrough that can be done which we just cannot see or perceive.

If I had more time, I would give some examples, but I think that's one of the things where ML has such a different viewpoint on many of those problems that we're going to get the Oh my god, it's what's in front of us the whole time and we could not see it. So exciting times ahead. Thank you very much, ladies and gentlemen, as we continue


────────────────────────────────────────────────────────────────────────────────
## TEJAS KUMAR (MC)
**Affiliation:** IBM / Developer Advocate
**Talk:** Sponsor Acknowledgements & Transition
**Time:** 01:35:33 – 01:36:01

[01:35:33]
today's program, please welcome back your MC, developer advocate at IBM Teya Skimar. What an incredible start to the day.

[01:35:53]
Woo! Everybody's leaving. This looks amazing from here. Before we break off, uh or after, um let's take a moment and acknowledge the sponsors. Honestly, this would not be possible without them. We're gonna get the slides up. Listen, you need to give them your biggest round of applause. I mean it is so cool. Thank you. Thank you thank you thank you Microsoft. Thank you to all the other sponsors here. This event would not be possible without them.

There's plenty of other things happening um in the other stages, but there's no doubt that evals are a huge deal in AI. In fact, they're the gate of quality, right? We can ship a lot of things, but if they're not evaled well, we ship a lot of slop. And so uh our next discussion, our next session is gonna be from Aparna Dinakran from Arise, who's gonna talk to us a little bit about Evals. Please, your biggest round of applause for Aparna. Please welcome to the stage,


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Speaker Introduction
**Time:** 01:36:52 – 01:36:52

[01:36:52]
co-founder and chief product officer at Arise, Aparna Dinakaran. Hey


────────────────────────────────────────────────────────────────────────────────
## APARNA DINAKARAN
**Affiliation:** Arize AI / Co-founder & CPO
**Talk:** Evals for Long-Horizon Tasks
**Time:** 01:37:10 – 01:41:58

[01:37:10]
everyone, can you all hear me? Alright, let's go. Oh, let me go one back here. Awesome. Well, hey everyone, my name is Aparna, one of the founders of Arise. We work with some amazing teams to help them build evals. And we have an incredible lineup of talks for you all today at the Evals track. Um it's happening in room 2005, and there's gonna be amazing speakers from Turnbench and Uber and Snorkel, kind of all happening after this. Um but today I'm here to talk to you about the future of evals.

Evals have gone from the new skill that every PM and every AI engineer has to learn to the thing that every serious AI team is betting on. We've been really fortunate to get to work with some of the best AI teams in the world. So we get a front row seat into not just what's happening when they're building their actual agents and before they actually ship, but actually the evals that teams are running on their live production agent via their traces. A little bit of some stats for you guys: we run over a hundred million evals every month.

The average team runs about 12 different eval jobs, with the top teams running over 3,800 different evaluators. And offline evals, online

[01:38:29]
evals, they each have their own place. But today, what I'm actually gonna talk to you about is the teams that are running evals on their traces. This is actually what's helping teams figure out what's working, catch their failures, and that's the type of data you need to fuel your continual learning loops. And the industry kind of agrees. I mean, all the CPOs of Anthropic, OpenAI, all, you know, GDB, you have Gary Tan saying, evals are everything you need. And the whole industry kind of agrees. So we added evals, they catch all the failures.

Right? Here's the problem. While we were building all of these first gen evals, the thing that we were actually evaluating has changed underneath us. In 2023, it was about just answering a prompt. In 2024, we started to see all the frontier models. They've added tool calls, they've added reasoning, they've added deep research. Now what we have is teams running loops on real-world data with sub-agents kicked off on long

[01:39:34]
horizon tasks. Every one of these was actually a massive jump in complexity, and we didn't just make the problem harder, we actually got a fundamentally different type of problem. What that meant is that as these systems got more complex, so did the way that they actually fail. We're really lucky because we have our own agent that we've built, Alex, that lives in our UI, and we get a kind of get to feel this pain ourselves. Every time the Frontier Labs added new functionality, we added it to our agent. And now Alex can has much longer memory.

It has the ability to create dynamic UIs. It can go search across an enormous volume of traces. But we also realized that it would forget context. It wouldn't know when something was done. Sometimes it would just get stuck in these loops. And the key thing here is that the classical LLM as a judge evals, that probably many of you have written in this room just weren't enough for us to be able to catch all the types of failures that we were experiencing. I mean, it's just fundamentally different, right?

You have a deterministic flow, and now what we have is literally every time a user interacted with Alex, it would create a new UI. That's a fundamentally different trajectory. So this led to our really big revelation: what if the best way to an evaluate an agent was actually with an agent? Does it mean

[01:41:01]
that all of the ways that we did evals with deterministic evals, with LLM as a judge, classic eval-s, doesn't matter anymore, but it just means that we have a different type of tool to solve a different type of problem. Agent as a judge is about adaptive dynamic analysis. LLM as a judge just gives you a fixed rubric with these fixed scores, it's what everyone's doing. But when your agent's doing completely different trajectories every time a user puts in data, it just means that you need a fundamentally different type of eval.

My take is that most teams today are doing the first two, but the future of Evals is actually having all three. And today I'm actually excited to share: we've released Agent as a judge to help our teams on their Eval journey, we've released Signal. Signal is actually a long-running agent that can read traces sent in, discover patterns of issues, it can figure

[01:41:58]
out types of problems that a classical LM as a judge eval just would never be able to do with these deterministic rubrics. It's helped us figure out very subtle failures that you wouldn't even think of doing, such as something going on in a loop for multiple times, it was calling the same tool for a repeatedly long time, the trajectory was inefficient. And actually what this does is because it has all that analysis, it can go put up a PR and put up a fix. So if you want to learn more, come to our come to our booth.

We're right by the OpenAI booth. We'll give you a demo, we'll show you a bit more about it. We're also, like I said, taking over the eval's track. So come to room 2005. We're gonna be talking a lot about the future of evals and what they look like. And if you just want to hang out with our team, we're throwing a viewing party for the USA World Cup uh game tonight. So uh check out the Luma and register to come join us. Awesome. Thank you all so much. Story of how this all kind


────────────────────────────────────────────────────────────────────────────────
## GABE DE MESA
**Affiliation:** OpenGov / Software Engineer
**Talk:** Agents in Production: OGSys & OpenGov's Bet on Effect
**Time:** 01:43:09 – 01:54:41

[01:43:09]
of came to be. Uh we're going to talk about OGSys uh big bet on effect. A little bit into our core agent loop. We're gonna talk about the A2A protocol, evals, and sandboxing. We're gonna talk about how we manage long context. Hi everyone, my name is Gabe DeMesa. I'm an engineer here at OpenGov, and today we're going to be talking about agents in production, specifically how OpenGov built and scaled OG Assist. So this presentation is going

[01:43:43]
to be jam-packed with just so much good stuff. We're going to talk about AI agents, we're going to talk about our harness, we're going to talk about evals, observability,

[01:43:56]
traces. We're going to talk about tools and skills. There's going to be a lot of good stuff in here. We're going to talk to you guys about what we do at OpenGov and how we operate at the scale that uh we operate at um in production so you'll be able to see a real use case and workload uh with AI agents. Um so without further ado, let's get started. Okay, agenda. So, just really quickly going to go through uh high level what we're going to talk about today. Uh, I'm gonna tell you guys a little bit about OG Assist and what uh OpenGov is.

I'm gonna tell you guys the origin story of how this all kind of came to be. Uh we're going to talk about OGSys uh big bet on effect, uh a little bit into our core agent loop. Uh we're going to talk about the A-to-A protocol, evals, and sandboxing. We're going to talk about how we manage long context. We're going to talk about monitoring, observability, how we collect feedback, and how we iterate on that feedback.

We're gonna lastly also talk about tools and skills and how at OpenGov we use AI not only externally that we uh serve to customers, but also internally to improve our development workflows.

[01:45:17]
Just a little bit about me before we go any further. My name is Gabe. I'm a software engineer here at OpenGov. I work on the AI agents team and uh I'm one of the folks that helped build uh OG Assist and some of the systems that you guys will be seeing today. So a little bit about OpenGov. OpenGov is a software company on a mission to power more effective and accountable government. So OpenGo sells ERP software, that's things like budgeting, procurement, asset management, and permitting. And

[01:45:49]
we were founded about 14 years ago and what's cool is um we have this thing called OG Assist and OG Assist is this little button on the top of all of our products in the in the navigation bar. And what's cool is all of our product suites and product teams have built tools and skills in order to

[01:46:14]
power this button. So for example, if I open up uh this this um if I click this button and I open up OG assist it says hey um I'm gonna ask about rate codes which is very specific to utility billing the current product that I'm in. And you can see that inside of this kind of chat interface I'm able to speak to an agent and the agent is able to make tool calls in order to look up information against data inside of that suite.

So it's really cool to be able to kind of first party create these experiences through the capability that we've built called OG Assist. Okay, so just a quick story about how

[01:46:57]
this all came to be. So um a little while back we we we saw that AI was really starting to take off and a principal uh spun up this new team called the AI agents team and asked me to join. And um instantly I said yes, and OG Assist started to grow and we started to integrate uh OG Assist into all our products and uh not only our back end capabilities but, also our front end capabilities as well.

So you'll see that one of the capabilities that we give the agent is it's able to see what's on the screen and and see and and and take action of on what's on the page. So you could see that I'm asking the agent here, hey, hey, what's on the screen? Can you maybe highlight some of the next steps that I could take? So you can see that the agent here is thinking, it's saying, okay, what tools do I have available to use? And hey, let me go and highlight something that you could actually click on and tell you more about it.

So just another capability of OG Assist and just a little short story about how this all came to be. So the big bet on effect. So I really wanted to include this slide because um here on the agents team we made a huge bet to um to to bet on effect and suffice to say it's paid off in dividends. We write effect. So effect is this library for TypeScript. It's open source and it helps you write better um typescript code. You know, it's got a lot of uh stuff baked in it like a s a a schema similar to like Zod if you've ever used that.

It's also got um things for error handling, uh for logging, for traces, for uh it's just got so much in there. It really helps write better code and structure your code better and uh helps with architecture, spinning up new services for uh and and for us on the agents team really helping uh design and build the the the core agent loop so you'll see throughout this presentation sprinkled in um how effect on our team uh has paid off in dividends. So we we really love effect here at OpenGov and we encourage other folks to try it out.

And um yeah, let's keep going. The effect native

[01:49:18]
loop. So originally we were on Langgraph and that was fine until the team really started to scale uh and our use cases started to evolve. So we decided to move over to our own kind of effect native agent loop to have full regency over this agent loop, such that if we have complex use cases or features that we need to build, we could kind of get in we we had full control of the of the agent loop. And not only that, but now we're fully on effect.

So all the cool things you get with effect is now th propagated throughout the entire agent loop, like the tracing, structured concurrency, the logging, everything is more fine-grained control. And it it really allows us to really unlock the full potential having our own agent loop from the ground up. So another thing I wanted to mention is on the left side, you'll see a code example. This is really the basics of the effect loop that we're using. We're using this thing called the effect AI package.

And in that package there's this thing called there's a chat and a language model. So with the chat you can instantiate like an a chat for example and then you could stream text using um that that kind of stream text function you could pass in a prompt and what's cool is uh with a language model under the hood of since we're kind of doing dependency injection, we could pass in a different language model if we were to uh s hot swap to another one, for example.

So really just having full control of our own agent loop just kind of gives us all the levers and it really just unlocks the full capabilities of the model and uh for the team as well to have full agency over this loop. Another thing I wanted to mention is the agent-to-agent protocol. So here on the agents team, we've had a lot of success with this protocol. So this protocol being the protocol that Google created, kind of an open protocol for agents to intercommunicate, but we found

[01:51:30]
this very useful for uh defining our agent routes, for example, in the back end and our model and our schema to follow this kind of uh agent protocol. So we modeled so for example there's this thing called an agent card which you see here and it's got the name of the agent, a description, etc right and having this kind of rigorous protocol this rigorous spec really helped

[01:51:57]
drive our development and drive alignment because you know all we had to do was um align with this spec and follow this spec and we knew that this was kind of the contract that our front end and back end would both consume and and produce. So um this uh I would say also has been uh very helpful for us. And and what's really cool is A2A has a lot of extensions, right? So you could extend the protocol, uh add in like metadata, uh there's also a to UI, um so lots of fun stuff uh with A2A protocol, but uh this is kind of what's worked for us.

So sharing that with with you folks. Feedback and evals. So here the quote is shipping is the start, not the finish. So what we do here uh on the agency team is we have kind of multiple ways we do evals and collect feedback. Um obviously, you know, we'll have folks uh call in or email us or or just let us know and tell us. But the main way is we have this thumbs up and thumbs down mechanism and here uh someone is able to tell us, hey, this this worked really well. This was a great response, or that wasn't a great response.

And that signal we take and were able to iterate on uh and we could take it back and help improve uh you know the response in the future. Um we also have automated evals. So in in the in RCI, we we have evals that run against real completions. So we could test the prompt against, hey, did it hit some tools? Did it do what it's supposed to do and that also helps with our accuracy so uh those automated evals in conjunction with collecting feedback really help us

[01:53:45]
um improve our uh our our tools, our skills, um, our harness, and that's really how how we're able to iterate so fast and so quickly. Humans in the loop. So this is a really cool feature we built where we deterministically interrupt the agent loop if there is a tool call approval required. So if an agent tries to make a tool call that it needs human approval for, it'll show this UI and the human can click accept or reject. So explicitly rejecting or explicitly accepting the action that the agent is trying to make.

And this ensures that we're building trust and also ensuring that uh you know we're being safe especially when the agent is trying to do a mutating operation and always always always making sure that um humans are in the driver's. Sandboxing. So

[01:54:41]
another thing that we uh worked on kind of similar to the safety slide we just saw was um whenever an agent tries to execute code or tries to create files, it does so in a sandbox. So we gave


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER
**Affiliation:** Unknown
**Talk:** Open-Ended Evolution, Scientific Discovery & Automated AI Research
**Time:** 01:55:07 – 02:15:27

[01:55:07]
our agents sandbox. All right. All right. Hello everyone. Really

[01:55:46]
excited to be here. It's a big room. Very uh

[01:56:02]
very cool conference so far. Uh I want to talk to you today about something that's been on my mind for many, many years. This is actually the first time I talk about it, sort of my version of going to Mars. And that is the Eureka machine, a machine that will eventually invent pretty much all future inventions for

[01:56:21]
humanity. And the way we're gonna get there is by taking a step back and thinking about what else has given us a lot of really incredible inventions, namely evolution, and how that leads us to automating research and pushing the scientific frontier forward. And this is uh joint work with a lot of uh amazing folks uh at recursive, u.com, uh, and even some uh folks at AIX Ventures, and some of these slides are uh actually inspired by uh and taken uh partially from one of my co-founders at Recursive Tim Rock Teschel.

So uh why do I talk about evolution and why is it so important? Uh I think basically evolution is this like open-ended process that has gotten us to a lot of different things that we like. It started in biology, it's moving to science, technology, and eventually AI, and I think it can inspire us in a lot of different ways to build better AI systems as well. In fact, uh, whenever we take out, and there's this famous saying, whenever I fire a linguist, my accuracy goes up. I think that's true for machine translation back in the day.

And it may be true that we should fire all the AI engineers and that that are here and have them mostly manage an actual AI engineer that is AI and works on AI. And so that may be one of the conclusions of this talk. And I think most of us are gonna be excited about it, because it means that we'll all become managers of such an AI rather than having to do the nitty-gritty ourselves. All right, so let's start with evolution, right? The really, really big picture, three and a half billion years or so.

Uh this is kind of the incredible process uh that has led from you know simple bacteria and plants and and fish and amphibians and so on to after many billions of years, us. So that's a good starting point. That gives us some indication that evolutionary processes can do pretty amazing things. But now let's zoom in and uh go maybe down to a few million years. There we can also see how in a very first primitive way is technological evolution uh has basically increased the world's uh sort of product uh in terms of monetary value.

A little bit harder to estimate in the beginning, but we can see these sort of sequences of exponentials. And most exponentials eventually become S curves, they flatten out, but humanity has done pretty well by basically developing many of these very basic technologies, hunting, farming, but then also thinking about science, the scientific method, in the early days of the Enlightenment and of course the industrial revolution.

So now we can zoom even further, uh, and no worries, we're eventually gonna get to nanochat and actual auto research and what we're doing. Uh it's a very, very quick zoom. Um, and now we can zoom down to the last few thousands of years. And what we're seeing there is that with more technology, we were able to sustain more people, right? So when we're working on pushing that frontier forward, uh we're very certain that that will lead to more human flourishing, right?

And especially in the last few uh hundred years, we're seeing this incredible explosion in the population of people because of technology. And the evolution that it brings. And in many cases, that evolutionary process is run by us, so it's sort of conscious, but there are sort of interesting inspirations that we can take from that as we're thinking about the evolution of AI in the next cycles. In fact, and I might not agree with everything with Mark Andresen, but he is very smart, and we agree on a lot of things.

And so I think he wrote this really great uh techno optimist manifesto in which he I think correctly points out that the only perpetual source of growth for the entire economy, a lot of people worry about AI taking jobs and things like that, but the truth is it will very, very likely increase the economy massively, and that will benefit a lot of us. And so the perpetual source of growth is technology.

In fact, we can go even further and say that there's no material problem, and again it's not sort of psychological problems and things like that, but no material problems uh that cannot be solved with even more technology, right? So the problem of starvation, we invented a green revolution, darkness, light, uh, cold, indoor heating, heat, air conditioning, and the list goes on. So I think we can kind of realize that this evolutionary process has been going on for a very long time and continues to make a huge amount of progress.

In fact, the progress is so fast that there can within one lifetime be a major, major shift. If you're born in 1900, uh then three years, when you're three years old, the first human ever was able to, thanks the Wright brothers, kind of have sustained motored flight. And then about 60-ish years later, in 1969, humans flew all the way to the moon, right?

So that within one lifetime, humanity went from like no one can fly for a very long time, other than sort of gliding down a hill or something, no one can really fly to we all fly to the moon, right? And so for us, I think what that means is we are probably, and I sometimes say this, we're like too late to explore Earth, we're too early to explore the stars, but we're right on time to build an AI that could actually do what flying did for some in one lifetime do to intelligence.

We can build and move from AI being worse at everything that we do to possibly being better at any specific task that we do. Right? And that that will probably be our our sixty year time frame and because everything moves faster, it might only be thirty years or so. So then uh there's an interesting connection between technology and science and theory, right? Like sometimes the application comes first, and then we develop the theory later, and then improve the technology.

Sometimes the theory comes first, and from that we can build new kinds of technologies. And so it's very helpful to think a little bit about the philosophy of science, and no better to be inspired there than Karl Popper wrote that just like in other types of evolution, when we choose a theory, we also choose one that is best uh in competition with other theories. Of course, you need, if you wanted LLMs to do that, they need to find them, you need web search, for instance.

Um, but uh in the theory that best holds its own, uh, it's one that just like evolution has a certain natural selection process, right? It proves itself, uh, and there is also a sort of survival of the fittest uh going on in scientific theories. And uh in fact uh a lot of science, according to Popper, is basically us proposing a new theory, hypothesis, or explanation, or description, and then subjecting it

[02:03:31]
to rigorous empirical testing. That is the essentially evolution, evolutionary pressure of scientific theories. And basically, that was a very short uh run through uh sort of the history of open-ended evolution, uh, which hopefully makes us all realize that more science will lead to more technology, which will lead to more growth, which will lead to more human flourishing.

And so that then begs the question: does it make sense for us to try to just scale up and spend a lot of our resources as humanity to scale up scientific discovery in order to lead to this flourishing. When you double-click into that, you kind of realize, um, which Dannis of Lem uh already realized a long time ago, uh, that the exponential growth of science will actually be at some point halted by the lack of people working on it, right?

There's so many niche subfields now in all the different areas of science that it's very hard to get a million people to work on that particular thing. And so as a result of this incredible widening of the scope, he says the number of people focusing on any single section of it has decreased. And that then leads us to really thinking about how we could automate this and automate scientific discovery. And that then leads us to what I call the Eureka machine. This is basically our attempt at trying to build a machine

[02:04:59]
that automates the process of scientific discoveries. And uh in fact, I like in a couple months I'll have a book coming out on this uh exact idea. Uh, and so I'll just give you a super high-level highlight of how such a Eureka machine could be built for basically everything from physics, chemistry, biology, neuroscience, medicine, uh, economics, astrophysics, and so on. And there are essentially four pillars that are all extremely important to this machine.

One is, of course, you have to understand what knowledge is already out there, uh, what uh things humanity has already invented. Uh, you have to get all the scientific measurement uh data into as a second pillar this machine uh then for things that you cannot yet measure, we don't yet know, you should try to then build simulations. Anything you can simulate, you can verify, and uh you can then solve with AI.

Uh and if all else fails, or at the very end of these processes you still need to have some kind of uh physical industrial leg lab uh that actually can run real experiments in the real world. And on top of all of this, uh you'll have uh basically uh an agent swarm that will deal with all of these different sources of knowledge and data and experimentations and and rewards.

And in terms of you know the foundational model of knowledge, of course, we also, you know, it basically is is a good example of how every single technology we've built so far, especially in AI, but also before that, the internet, browsers, GPUs and so on, we can rethink and there are a lot of startups possible in rethinking every single one of the layers of technology as infrastructure for superintelligence. At U.C.M., for instance,

[02:06:48]
we work on web search for LLMs, right, and agents and so on. Uh, and that actually is quite different, right? Uh agents can read thousands of very long snippets um rather than just 10 blue links with like a very short snippet. And so you can rethink each of these different uh layers of technology that we've built for people and uh rebuilt them for AI in order to use them as tools to then build uh superintelligence. Now that is essentially uh the sort of why. Like we want to build superintelligence in order to automate science.

Uh and to me, that will be the next big step function change uh in humanity and technology as we know

[02:07:36]
it. Now, how do we actually build it? I think the best way to build it is to have it built itself, right? We moved as a field and especially natural language processing, for instance, which I've worked on for many years. We moved from not having linguists, this feels like ancient, you know, BC uh history, uh, but before chat GBT, um, we removed from having linguists tell us a bunch of things about language and then training statistical models on top of that.

And when we allowed neural networks to actually automate learning those features with word vectors and uh other neural network architectures and back-to-back uh end-to-end learning and backpropagation, we basically uh were able to get much bigger improvements. Uh, then we did a bunch of architecture engineering. Now a bunch of people at least are working on a unified architecture, uh, but even that unified architecture has a lot of manual processes.

And so it's clear over and over again in AI that when we take out a manual process and we replace it with a learned system, improvements will follow. And so that's why I think we should try to build this weekend machine by having uh an RSI that builds itself. And the beauty is that only now um AI can actually do

[02:08:52]
this because AI is code and AI can code now. This this ability to really code in longer and longer time horizons has really only happened in the last like six to eight months. And that now enables such an RSI to work on itself, to develop almost a certain sense of self-awareness of its own shortcomings, and then fix those shortcomings. And then once we have that machine that has gotten really, really good at doing research in AI itself, we can then use it to do AI research for a lot of other things in other scientific fields.

And so at a high level, it's quite easy, right? We have three steps: ideation, implementation, and validation of ideas.

[02:09:36]
That's true for basically almost every scientific field. And so uh to end maybe on some very specific examples, uh we have built this first kind of version of such a Eureka machine. Uh and we wanted to just show that it works on some small uh samples that a lot of people know and are aware of. And so we basically started uh with three things that show you and give you a very first glimpse of and sort of simple proof points of what such a machinery can do.

And that was basically better training, faster training, and better kernels for Nvidia GPUs. The first one, nanochat, I'm sure many of you have heard of it. A lot of people think that's already recursive self-improvement, and it is kind of a weak form in the sense that usually when you do auto research, it's it's not recursive self-improvement, right?

True recursive self-improvement is when you have an AI that has a sense of self-awareness of its own shortcomings, full access over everything uh in its arsenal from pre-training to RL training and harnesses and everything, and then actually updates that entire system in the next version of itself.

Now you can also take such a system and just ask it to improve some other process, some other AI, like a small nanochad run where you can train something in five minutes, and that is really exciting, it's an important milestone, but it's not actual RSI. So here basically showed three examples of such an auto-research um uh system and what it can do, and uh after a very, very short time, it essentially was able to outperform many different teams and teams that also use other AI research. So let's double-click into some of these.

Nanochat is uh really a exciting example. Uh basically you train a very small uh chat model uh in less than uh five minutes, and you basically want to have it get to the best possible bits per byte uh number. And so

[02:11:41]
the whole community had worked on this uh for uh quite some time and got to uh 0.93, and after training this for a little more than a day or two, uh we basically got it down to 0.91. Um, which is pretty exciting. Now it wouldn't be that exciting if all it did was just find a couple of hyperparameters um and tune them carefully. But it actually did find truly interesting novel ideas like hash bigrams and trigram

[02:12:12]
embeddings and tables for those, uh and mixing that into various uh value paths of uh the intention through a variety of learned gates. So it actually started to doing more and more interesting things rather than just kind of tuning hyperparameters. Um another one, a nano GPD speed run. Uh obviously speed is very important.

Uh so here we're able to work on this again, apply the system, and after a very short amount of time, it got better than uh people working often together with the AI for over a year uh on on this ver on this benchmark and made the whole thing another two seconds over two seconds faster um at seventy seconds. And again, discovering uh very interesting ideas in the process. And then the third one is good at kernels. Of course, we all care about not burning throughout GPU budgets too quickly um uh and trying to be very efficient.

I think in general it's actually kind of shocking how inefficient a lot of mixture of expert uh models still are run in very large clusters that cost billions of dollars and then only have like 30% or so utilization. There's a lot of work that's ongoing in the world to improve that. And different fields or different groups of people are various different stages of that.

But long story short, um lots of different CUDA kernels are used during training and testing, and here um we basically again took that system and after uh a couple of days it discovered better kernels uh than the leaderboard's best on the NVIDIA benchmark website

[02:13:50]
by again quite quite a sizable margin across all the different uh categories of those kernels.

And while we are pretty good at AI, and like we actually in the team didn't have any particular CUDA kernel experts who just spent their entire careers writing good kernels, uh, but still, you know, we do just enough to make sure and worked together with NVIDIA to make sure that there are no reward hacks here and and other issues, but actually found uh that eventually these all checked out and were indeed uh pretty much all the different kernels uh found the best solutions there.

And so with that, I hope I could convince you uh that indeed RSI could be that next big uh S curve um an exponential that is gets layered uh on top of previous exponentials and uh that should help us uh with not just AI but eventually science and then all of technology and then uh allowing many more people uh to flourish on our planet. Uh and so maybe I'll end on this note here, which is uh a lot of people wonder how much longer AI can go, right? Every exponential eventually flattens out, then um it's actually quite hard to know.

Like when we even talk about exponential growth in AI, what does that even mean? There are many different, I call them spaces of intelligence, and we won't have time to go into all of all of these, but as soon as you actually try to define multiple different dimensions of each of these 10 spaces that make up this complex sort of volumetric thing that is intelligence, you'll realize that

[02:15:27]
there's still so much more to go. Like on the upper bounds of intelligence, we're still astronomically far away from reaching those in across pretty much every single one of uh these dimensions and the spaces that they make up. So if any of that is interesting and you want to help us build that, we'd love to hear from


────────────────────────────────────────────────────────────────────────────────
## NISHAM GUPTA
**Affiliation:** Meta / Software Engineering TL
**Talk:** From Offline Benchmarks to Production Reliability
**Time:** 02:15:51 – 02:20:35

[02:15:51]
you. Thank you. Hey everyone, my name is Nisham Gupta

[02:16:05]
and I'm a software engineering tech league at Meta working on building a training and inference infrastructure for the Meta Supertens Lab and their infrastructure organization. Today we are going to be talking about production valves for agentix systems. When most people hear the word valuation, they think about benchmarks. A model scores 90% on a benchmark, a new version scores 92%, a team celebrates. But agentic systems have fundamentally changed what the evaluation means.

Today, the systems don't simply generate answers, they plan, they call tools, they retrieve information, they execute workflows, they interact with the production infrastructure. The question is no longer did the model generate the right answer? The question is did the system behave correctly. Today I would like to discuss how evaluation is evolving from model benchmarking into production infrastructure. This is the problem almost

[02:17:04]
every AI organization is encountering today. Offline benchmarks continue improving. Yet production reliability often remains unpredictable. Why is that? Because benchmarks measure model capability. Production measures system behavior. A benchmark doesn't capture tool failure, API outage, context changes, user variability, long-learning workflows. And as systems become more autonomous, the gap between the benchmark performance and production performance grows. The result is what many teams experience today.

High benchmark scores, as you can see but unreliable production behavior traditional LM evaluation

[02:17:43]
focus on outputs but we should ask the question did the model produce a correct answer agent systems force us to ask a different question. Did the system behave correctly? Behavior includes planning quality, role usage, execution, workflow execution, recovery

[02:17:59]
from failures, decision making. In other words, we are moving from evaluating answers to evaluating workflows. And that requires fundamentally different evaluation architectures. Many teams still think hallucinations are the primary AI failure modes in production, they are often just one category. Agentec systems introduce an entire hierarchy of failure modes at the very foundation. The memory failures, retrieval failures, safety failures. As you go up, you have to think about reasoning mistakes, poor planning, incorrect tool execution.

At the highest layer, you have to think about multi-agent coordination failures. And this is why evaluating only model output misses the most production risks we observe. One of the most useful mindset shifts is to stop thinking like researchers and start thinking like a SRE or a production engineer. SREs don't measure success using accuracy, they measure reliability, availability, latency, cost recovery, and agentic systems require the same approach. The goal is not maximizing the benchmark scores, the goal is to

[02:19:07]
maximize dependable outcomes. Reliability becomes an Australian. Values limited. In

[02:19:24]
the middle there are scenario based valuations. These simulate realistic workflows, and at the very top you see production telemetry. This is where the highest value evaluation signals come from. The surprising insight is that the most evaluation data often comes from real users interacting with real systems. Now let's

[02:19:46]
talk about offline evaluations. So offline evaluation still matters, but the methodology changes. Instead of evaluating prompts, we evaluate scenarios. For example, a customer support workflow, a co-generation workflow, a research workflow. The agent operates inside that simulated environment. We measure the task completion rate, tool correctness, planning quality, resource usage, which is which becomes exponentially high at high scale. The key takeaway: agent evaluation should be scenario driven, not prompt driven.

Once a system reaches production, every interaction becomes

[02:20:18]
a signal. This is one of the biggest shifts in evaluation thinking. Oh, all right. Uh all right. So can

[02:20:35]
everyone see the uh slides? Oh, nice. All right, so


────────────────────────────────────────────────────────────────────────────────
## HAN XIAO
**Affiliation:** Jina AI / Founder
**Talk:** Scaling Search Intelligence: Embedding Models & Test-Time Compute
**Time:** 02:20:40 – 02:35:55

[02:20:40]
good morning everyone. Thanks so much for being here. Uh my name is Han Xiao. I founded around Gina AI since uh twenty twenty to twenty ninety-five. And last October we were acquired by Elastic, so now I'm running uh model inference and training team there. And uh uh so here's a question I want to answer today. Uh so big models get thinking better by at inference time. Right? So we call that test time compute. And can small retrieval model do the same thing, right?

Can it get better by thinking harder at inference uh without making the model any bigger? Uh to find out that I let the agent run auto research overnight. And the answer turned out to be more interesting than yes or no. So let me show you what I found out. So first let me say what test time compute is. So the idea is very simple. So instead of training a bigger model, you spend more compute at inference time. So you get better answer back.

Uh it shows up in very familiar forms, uh, such as the best of in-sampling, self-consistency, or verifiers that re-rank the candidates. So Noam Brown from OpenAI uh put a number on this. He found that a poker bot uh So that's the promise of test

[02:21:47]
time compute. So the real question for us here is, does this promise also for the also hold for search. So here's the reframe that turns this into a retrieval talk. Uh search is already test time compute. Uh so think about what you do when you build search. You take a trained embeddings, a trained re-ranker, some multi-vector retriever, and a query expander. And then you wire them into a pipeline. So you're spending inference to buy relevance. And you are not reaching for bigger model, you're basically assembling more search at test time.

So the real question isn't whether your model is big enough, it is how much pipeline can you assemble uh at inference and whether that's pays off. So there are two versions, uh two ways to build that pipeline, and I want to show you both. The version one, the first one, version A, uh is the one I will go deep on. So here an agent writes a little program over a single frozen embedder or encoder. It might chunk the document, uh, do this scoring, fuse uh with different scoring strategy, and feed the results back.

So think of think of it as a multipath algebra over embeddings. The second one, version B, uh, I will come to later. So there a small agent wires up the retrieval tools like grab, embed, re-rank, over a corpus, given a fixed uh token budget. So it's the same idea, implemented at two different levels. So let's start with version A. So version A runs us uh runs over a small frozen encoder. So there the common belief is that small models cannot improve there, and test time compute exclusively belong belongs to the big reasoning models.

But let's look at what today's embedders come from. Models such as E5 Mistral, Queen3 uh embed, embedding Gemma

[02:23:39]
and even our own Gina embedding V5, they all distill from the large language model backbones. So that's the dominant recipe today. And if test and compute leave in the LRM representation space, then this distilled model should somehow inherit it, or do they? So that's exactly the question I want to find out. So here's the intuition of uh for how a frozen model or frozen embedder could improve at test time. Uh let's look at the three panels. Uh let's go from the right, uh left, right to the left.

Uh so we go from the simplest way to score a match on the left and to the most distal way on the right. So on the left, you have a single cosine distance, which is basically one vector per document and one per query. So that's a frozen cosine baseline. On the right, you have this cobra style latent interaction where every query token is matched against every document token. So one can consider cobalt as an extreme case of test time compute. Uh the interesting part is, of course, is it is in the middle panel where I have outlined in blue.

So you can take a frozen same uh you can take the frozen frozen encoder, split the document into sentences, and max over them. So that's basically what I call the test time compute. You get closer to late interaction, but without adding new model at all. Just more work on the same embedding model again and again. So let me make the question very strict. So how much can a frozen single vector embedding model improve at test time alone? So I and I do mean by strict, just one frozen encoder behind an API.

And you can code it as many times as you want, but no retraining, no second model, no learned parameters. So the popular method uh method all break one of those rules like height puts an RRM in the query pass to route the query, GQR as a second retriever, and meta embed trains new parameters. So we forbid all these three rules. We forbid all these three things. But even with the constraint, the search pipeline, the search space is huge. So how do you search that? With auto-research, of course.

So instead of me handcrafting these programs, an agent runs the research loop by itself. Uh it changes one file, it runs a short experiment, and if it's metric improved, it keeps the change, otherwise it reversed. So it does that over and over all night. So it's kind of like hill climbing, uh, but LRM as a mutation function. So entry capacity from Astrobic uh described it as follows. So you're adding a Python file in the way uh you're not adding In the way that research researcher would.

So you're uh writing a markdown file that set up the autonomous research org. And that loop generates everything that we were about to see. Uh so here's the whole loop in one picture. Uh just follow the box from left to right. We have a proposal, which is uh LRM agent, write a program over the frozen encoder. We have an evaluator, uh, which scores that program and memory logs the result. And the registry, the black box on the far right, uh collects all of them. So 144 programs, one per generation.

So now see the dashed line, uh dash arrow looping back underneath. That's basically the feedback. So memory conditions next programs and everyone's built on the last one. So let me quickly go through the four pieces. The first up is proposal, uh, which is based on Opus 4.6, used purely as a mutation function. It reads the current best program and memory file, and then it edits one Python file to propose the next one. So there is no human in the loop. Uh now here's the catch.

It only optimizes the metric that you give it to it, not the metric you meant. So if you reward end domain performance and if you reward spending more compute, then that is that uh that that is exactly what it will chase. So whether the improvements hold up elsewhere is a separate question. So the next one is program. It just actually Python program over uh the encoder. And the one piece that matters is this embed function. So that's a compute budget.

So every function call there basically re-embed some text or switch the LoRa adapter or pick smaller dimensions. So one call is one unit of compute. Uh there are some other constraints, such as the program cannot introduce any hyperparameters, cannot do task routing, cannot add external models, of course. So these constraints those constraints uh force the agent to find task agnostic program instead of a config that's secretly optimized for each task. Then comes the evaluator.

So every program run the same 14 evaluation task or discovery task, spending legal, financial, long document, long context, or general

[02:28:40]
retrieval problems. We score it via delta and the CG against the uh cosine baseline, plus some cost ratio, I will introduce the cost later. Now here's the design choice that matters the most. The loop only ever see these fourteen tasks, and there are 19 more held out tasks, the loop will never touch them or see them. So later we can ask a very clean question that does what we wins here also hold up there. So and the whole gap the gap is basically the whole experiment. The last part is memory.

So it is a simple JSON L uhile with one row per program. Each row stores the scores, the cost, the parents, and a short lesson. So the proposal will read this file before every round, and the whole search compounds compounds over time. Uh but compounding cuts both ways, right? It builds a real win, of course, but it also also compounds whatever bias uh from the objective. And the BIOS matrix does not only mislead one program, it steers the entire family. Uh so now let me set up the models that we use here.

We run the search on the single encoder, which is the Gina V5M nano, uh, only 200 million parameters, state of the art on multilingual retrieval. And we choose nano mostly because the discovery phase, as a discovery phase model, mostly because it is small, and therefore reduce the cycle time of each experiment. We hold out the bigger model from the same family plus the unseen families, such as Gemma model and Quinn model. They share no training data, no backbone, no tokenizer with the discovery model.

We also hold out the nighting evaluation task as I talked before, and this one, those 19 tasks, the loop never cease. So when programs gets discovered in this loop, it has to generalize over all encoders and all 19 tasks. So now before showing any result, let me define the cost of the test time compute. It comes down to one just just one number, C, which is the number of extra forward passes through the encoder. So let me explain it with two cards on the slides.

They do the same thing, but they uh they kind of mix in some neighborhood information and then restore it. The card on the left is what I call the soft-centroid. It averages document vectors that your computed, and so there's no extra forward passes. Uh that means it's cost C

[02:31:10]
is just one. The card on the right is the first sentence. Uh it re-embed the first sentence of the talk top document, which is a brand new forward pass. So there, C is greater than one. So one reuse the geometry that we already have, the other spans compute on the new path, on the new text. So now that we comprise the compute, we run that exact same loop onto two different rubrics. The first is compute rubric. It admits a program only if the in-domain performance beats every program before it.

So it is actively pushed to spend more compute at inference time. The second is the transfer rubric, so it keeps the program only if it improves over over the validation set with nothing getting worse. And it gets no reward at all for spending compute. And to be clear, the validation set is uh still comes from what the loop can see. So neither rubric ever touched the 19th final evaluation task or final holdout task uh and on scene encoder. So that's a two-brick two, a rubrics running under the same loop. So let's see what each one comes up with.

So let's first look at the compute rubric. So when you tell it to spend more compute, it draws this very beautiful clean curve. So the x-axis is a compute you spent on the log scale and y-axis is a score. There are in total 144 programs, and 12 of them sit on the paraphront. The cost running from just one uh all the way up to almost 15 times, and the in-domain score climbed nicely, it it more than triples across that front. So this looks exactly like tight time compute scaling,

[02:32:52]
more compute, more quality. So if I stop here, you will be thought. But this is still in domain performance. We haven't run this experiment on held out uh data set. So let's take a quick look on these 12 programs and run down uh run them on the hold out uh data. So here are the 12 programs drawn as a little diagrams. So don't have to uh you don't have to read into each one. The only thing that I want you to take away from this is that they are all training free recombinations of the same

[02:33:26]
frozen embedding models. Just chunking, scoring, feedback, and the The cost climbed nicely, uh steadily from left to right, and does look like a clean uh scaling story, but the improvement on the held our data set as you will see is not so So now we run those 12 programs on the held out dataset. And same chart as before, compute runs from the left to right and scores runs up and down. So the dashed line across the middle is a baseline, and look at the pink line, it uh the compute rubric. It's basically flat, hugging zero all the way out.

So out of the main, more compute buys you essentially nothing. Now look at the blue dots, which is the transfer programs, they all sit on the left because they are cheap. And everyone is above the pink line. So the cheapest one only has like as zero extra compute. It still be the most expensive program. So more compute did not transfer, the cheap structure did. So if we plot every program against uh every held out uh task, we get this heat map. Uh the four blocks are the four encoders, and three of them we have never seen in the discovery phase.

In each block, the rows are the programs and the column are 19 evaluation tasks. Green means an improvement, red or pink means a drop. The picture is generally mixed. Compute helps about half of the sales, but the improvements are uneven. So on I on average, it comes out flat. Compute does help in places, but it doesn't help reliably across all new all new tasks and all new encoders. So now let's look at this uh look at the other rubric, the transfer rubric.

It picks the six completely different programs, and they are all very cheap, and most one and a half times uh more compute than the cosine baseline. The best one wins 83% on the held out data set and it never loses on single task. So now what what does this program uh actually do? So they only test some query and document vectors that you already have, and they add a little cheap math on top of that.

Some notch the query towards a document it already likes, uh, some pick a few directions, and uh in the space and rescore uh along those directions. So they are very small structure change, but enough to pull the document uh the right document up. So it's all recommendation, no new models. And this really transferred

[02:35:55]
to across models and languages. Remember, in the discovery phase, we only use GENA embedding Gina V5 nano, and but the improvement is positive across all four encoders. And the biggest bar is on the JAMA and the Quinn. So those on the two families it never sees. So this is isn't some quirk of one model, it's general is right on general embedding geometry. So that was version A. A frozen encoder with very cheap structure, uh, and it scales, but low compute uh doesn't scale. And outdoor research is how we found that.

But let me move one level up from the model layer to the search pipeline. And you will see the same test time compute reflect in the pipeline level. In 2025, we have this deep research and agentic search product, uh, which was basically just a one loop over the uh open web. In 2026, we moved to a long horizon task, which adds implementation, sandbox, e-valves on top of the retrieval, and running for hours. So both patterns need more looping and more compute at test time. So study this at genetic search at test time.

Uh I built three open source projects for that. The first one is data room. So you give a token budget, it searches, it reads, it writes. So over and over until it packages everything into a zip file. So I call it data room because it somehow reminds me, like uh prepares the data room for the investors, uh, back when I was a founder. So that zip file distilled the corpus on the uh you can you can imagine this uh zip file is a distilled corpus of the open web, ready for the next agent or large language model to consume.

And notice the token economy here. So you are basically exploring the web and build the corpus using very cheap tokens from small language models, and then you save the expensive frontier tokens for later for exploitation. The second one is search box. So this is a test bed to study agentic search and two calling. It is designed, it is designed to be air gapped so the agent have no internet access. It's basically like you lock the agent in a room or in a box and you give it a data room and ask a question about it.

So to answer those questions, the agent has to assemble a search pipeline at test time. A pipeline made of local tools, things like a grab, embed, re-rank. And this allows you to explore some very interesting research questions, such as uh which tool does the agent reach for first? Or is grab all you need? Or does forcing more compute help on hard questions? Or will the agent build up a search pipeline that it will reuse later. So search prox is a test bed to explore those research questions.

So but how do you evaluate uh a genet search like that? Uh well you need hard questions. Uh that's basically the third project is knowledge graph. So it turns a corpus or data room into a knowledge graph, and every fact becomes an edge and linking from subject to an object. Then we can work on the longest path through that graph and, those long chains become multi-hop questions, then that no single passage can answer. So the agent has to spend more test time compute connecting the facts to get there.

So it's also the tool for building a private verifier. So let's connect all the dots together. So I introduced two versions of test time compute for search. Both versions are doing the same thing. They are spending more compute at test time, and neither of them grows the model. In version A, we found a special embedding algebra over the uh fixed uh further embedding that improves the search relevance. In version B, we build a full stack to find the best search pipeline.

We use a data room to maximize recall, we use the search box to maximize precision, and then we use knowledge graph to build evaluation. So finally, it gives us a pipeline that with strong search relevance. It is basically two different levels, but they share the same bet, spending more test time compute, not a bigger model. So finally, let me let me leave you with a big picture. Search is test time compute. So don't reach for bigger model, do more search at inference instead. You don't have to do this design by yourself by hand.

Uh-oh research helps you discover this probably overnight. Uh so and this is how we scale the test time compute. And that is basically my the end of my talk. Uh you can grab all the slides from the QR codes here. There's a paper and projects on my GitHub and archive. And if you are uh if you are around this evening, Elastic is also holding uh uh hackers in town. So the QR QR code is right there. Uh so come and uh build with us. Thank you so much and happy AI engineering. In


────────────────────────────────────────────────────────────────────────────────
## DOMINIQUE TORNEAU
**Affiliation:** Resonate / Founder & CEO
**Talk:** Specification Over Implementation: Agentic Engineering for Durable Execution
**Time:** 02:41:09 – 02:50:33

[02:41:09]
twenty twenty-six, coding agents will quietly retire the first software platform. Not because it's bad, simply because the platform is unnecessary. I am Dominique Torneau. I am founder and CEO of Resonate. Resonate is a durable execution platform built with minimalism and simplicity as its core technical values. And these properties will play a central role in this talk. At Resonate, we have a working theory where software engineering is headed. General purpose implementations will increasingly be replaced by bespoke

[02:41:51]
implementations, generated on demand. Not as a new library, a new framework, or a new platform, but as a minimal extension of the infrastructure that is already in place. If

[02:42:05]
this theory holds true, reuse will move upstream. Instead of reusing a general purpose implementation, we will reuse a specification, and we will derive a bespoke implementation from it. In fact, we can build many bespoke implementations, tailor-made for the infrastructure that is already in place. We just have to ask the agent. At this point, the prompt is the platform. Resonate is a dual execution platform. We have an

[02:42:43]
implementation of the Resonate Server. We have implementations of the Resonate SDK for TypeScript, Python, Rust, Go, and Java. So we have to ask, what does this new reality mean for us? If implementations become generatable, where does our value live? And our answer? Our value moves from implementation to specification. Now this changes how we think about resonate. The product is no longer the implementation. The product is the specification, the protocol. And from that protocol, we want to derive multiple server implementations.

One is a general purpose resonate server, our reference implementation. Others are implementations built with For customers and partners, this means durable execution right on top of their existing infrastructure with minimal additional dependencies. So the question is no longer: can we build a server? The question is: can we repeatedly synthesize trusted servers from the

[02:43:58]
same specification? And if so, how? When we talk about agentic engineering, we focus all of our attention on verification. How do we know the result is correct? But today I want to focus on the specification instead. And more importantly, how can agents participate in specifying the system, not

[02:44:26]
just building or verifying it. Now Resonate is partnering with multiple infrastructure providers to bring durable executions natively to their technology stack. One of them is Tsunadia, the company behind NatsIO, an open source messaging system designed for building modern

[02:44:46]
distributed systems. For the rest of this presentation, we will use Resonate on NATSIO to explore our agent engineering practices. How do we go from specification to implementation? First, we need to level set our mental model. This picture is a common view of agent decoding. There's an agent, there's a specification, and then there's an implementation. And for many applications, that is enough. But it is not enough for what we are trying to do. Because we are not trying to generate one implementation from a specification. We are

[02:45:30]
trying to generate multiple target specific implementations from the specification. So the specification must not take any aspect of an implementation into account. The specification must not assume a concrete database schema or concrete indices. The specification must not even assume a relational database with tables and transactions at all. It must not assume a key value store, it must not assume weak consistency, it must not assume strong consistency. The specification must be abstract. Only the implementation must be

[02:46:09]
concrete. So we ask the agent to follow the abstract specification and generate a concrete implementation. Specifically, at first, we ask the agent to build a resonate server in Rust on top of Postgres. And the agent failed. The gap between the abstract specification and the concrete implementation was too large. The agent generated a system that worked on the happy path. It passed the basic tests, but it was not correct. It broke on the concurrency, it broke on the process failure, it broke on the network failure.

The implementation was closer to a prototype, but not a production system. So we amended the process. Instead of asking the

[02:47:03]
agent to jump directly from abstract spec to concrete implementation, we inserted an intermediary artifact, the concrete specification. That concrete

[02:47:15]
specification was derived interactively with the agent, but the human was the main driver. For Postgres, that meant making target-specific decisions explicit. The data schema, the indices, the SQL queries, the transaction boundaries. Once those decisions were written down, the agent was indeed able to implement the production system. So this worked. But it also revealed the limitations. The agent

[02:47:48]
helped us build the system, but the agent did not help us design the system. And if the specification is a reusable product, then that's not enough. Now the next

[02:48:03]
step is obvious. Agents have to move upstream. But how? When we started building resonate on NATSO, we changed the question. We did not ask, can the agent build the production system? Instead, we ask what does the agent need in order to design the system first and build the system second. So we gave the agent access to a deterministic simulation environment. And we gave it a different task.

[02:48:38]
Do not build the production system. Build a simulated implementation. The simulated implementation is not the product. It is executable design. Its purpose is to discover the correct algorithm under partial order, under partial failure. And once these algorithms are discovered, tested and verified in simulation, then we ask the agent to write the concrete specification. And only then do we ask the agent to write the production implementation? So the process becomes abstract specification, simulation implementation, concrete specification, and

[02:49:22]
then concrete implementation. This is a point where the agent moves upstream. Humans are still involved in the design process, but now the agent is a driver. Two ingredients make

[02:49:38]
this possible minimalism and simplicity. Unfortunately, minimalism and simplicity are not the starting point. They are the finish line. We spent three years making the protocol smaller and simpler. Every time we ran into a problem we ask what can we take away? What abstraction can we erase? What property can we remove? What relationship can we break? The result

[02:50:04]
is a very small protocol centered around two objects, a durable promise and a durable task. That simplicity matters because even simple concurrent distributed protocol have a complex state and behavior space. So in other terms, implementing even simple protocols on top of a few simple primitives is tough. Let's make this concrete with nuts. Nats gives us a s


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER (Memory Talk)
**Affiliation:** Unknown
**Talk:** Local Models, Memory Harness & Long-Horizon Context
**Time:** 02:50:44 – 03:01:49

[02:50:44]
Hello, welcome. This is a big room, so you're if you're in the back, don't hesitate to come closer. Um my name is Stefania Drug, I'm res aearch scientist at Sakana AI in Tokyo. I used to be based here, and AI engineering is home community for me before being the Hyperloop. So it's very good to be back. And today I'm gonna talk to you about memory harnesses for long-running research agents on device. So if you work with

[02:51:17]
long horizon tasks, you probably ran into this issue of context blow, right? Like when the model starts contradicting itself or it has to redo the work because it forgot it did that task in the first place, or it starts to drift from your questions because it forgot them. And this this matters now more than ever because from this recent projections from meter, we see that the trend is to solve longer and longer horizon tasks, and also that we're getting fewer and fewer model releases.

So at some point later this year, we're gonna have this convergence, right? Where we'll get many more long-term horizon tasks and fewer model releases. So that makes this issue of dealing with context rot a priority. And why did I want

[02:52:10]
to tackle this problem on local models and with a local harness? Maybe some of you have seen this tweet, it's only two days old. The CEO of Coinbase actually shared how their company managed to reduce their AI spent

[02:52:26]
while actually increasing uh the AI usage. And the way they did that was by transitioning to use many more local models, but also having better practices like using better routing, better caching, keeping the context clean, and then having better visibility for what people are using and for what, what kind of task. So we are seeing the local models like crossing the line, right? Like GLM is on everyone's minds, like especially with Fable going away. Deepseek V4 flash can now be run on uh M3 Ultra. And

[02:53:05]
there's still a bottleneck for RAM, it's tricky. But these local models are starting to be useful for agentic tasks and for tool use. So I wanted to show you what has been my setup for the experiments I'm gonna share with you today. This this is my Mac. It's still running evaluations right now, uh, back in my desk in Tokyo, and I'm controlling it from my phone. And after running Evals non-stop for a couple of days, it started to get hot. So I had my husband put fans around it. We're running out of fans.

But the the machine is still running and the evals are still giving results. On this M3 Ultra with 96 gigabytes and 28 core CPUs, I'm using two models. I'm using the

[02:53:55]
Quebec V4 flash. And before I show you how I build the memory harness on this machine, I wanted to tell you what this look what is this an example of, right? Like memory, when we design a harness for memory, this is the mental model I want you to have in mind. Um you can think of memory as a write, manage, read loop. So it's not just the database store. It's actually this control loop around the model. More concretely, how did I take that loop and customize it? So this is my harness design.

Like I started with research agents that are the small agents because they have zero durable memory. And I wanted all the memory to come from the harness. And then in the middle I have a core which is always shown to the agent of traces. And then I have a recall block where I'm testing different modes and an archival block where

[02:54:55]
I'm keeping keeping track of information across different um sessions. And in that recall block, I'm actually going through a ladder of modes that I'm testing. The baseline is like not to use memory at all, no recall at all. So I'm I'm testing for that. Next is to use rag vector, vector rag, just to see whatever like the harness would pull in terms of similarity. Then is to use a decisions ledger where I actually keep track of what decisions are being made for every turn, and then I can prioritize them.

And last but not least, and this piece is very important, I have uh what I call an oracle, but basically this is the ground truth. So this is like telling the harness for every loop what the correct memory that needs to be retrieved is. And the model is fixed across all the different tasks. So the only things that I'm changing is like these different variables in the recall block. And I wanted to give you an example of a first task that I tested.

So I wanted to see if I give the agent a task of doing literature review and I'm including a lot of papers in the corpus where there was a big scientific claim, like this is actually a nature paper, where they said they discovered 742,000 promising materials. Like

[02:56:25]
it was a very big claim, which got retracted later. But the retraction, it's a much smaller like haystack needle in that corpus than the headlines and the citations. So I wanted to see if if the system can retrieve the right answer for these types of questions. And what I found was because like for these tasks, all the papers and all the information fit into the context, the memory actually didn't add more capability. It was the same performance with memory and without memory, and it only added more cost. So when your task fits in context, the

[02:57:09]
harness doesn't add much. However, if I start to run tasks that are longer-term horizon and the entire task and the relevant context doesn't fit, then having a good memory harness really starts to pay off. So this is another example of a task that I ran. This is actually from an established benchmark for a long horizon uh tasks memory. It's called Xbench. And this is an example of a question, right? So I'm asking a question, and then like the right answer is in a like step 124,

[02:57:49]
but the moment when I ask the question, I'm asking it like at step 500. So it's completely outside of the context window, and the model needs to use the memory harness to retrieve the specific answer from the right step. So I'm testing this by uh changing the different

[02:58:10]
policy ladder that I explained before with memory off, uh, by deploying recall, different types of recall, and by using the oracle as a reference. And what I found was that with the ranked recall, the model gets the right answer more frequently than without. And here's a breakdown of

[02:58:33]
the decomposition of performance on this X-bench tasks. So I ran over 68 questions, and for each of these questions, there were like multiple cells and lots of different seeds.

[02:58:48]
And what I found was that the rank-only ledger performed the best. And it performed better than like just gating the harness by saying, do you need to use memory, or do you not need to use memory? And you're probably gonna ask, like, why is the Oracle not hitting like the Macs? And I'm gonna explain that too. So the Oracle, what it does, it provides the right information, the right memory to the model, but it doesn't force it to use it.

So the model can get the right memory, but still retrieve the wrong information, or choose to ignore it, or be confused. So that's why the Oracle in this case doesn't hit the max performance. And I've done lots of ablations on these tasks to see like what happens if I give arbitrary um examples, what happens if I give it the wrong step? What happens if I give it the most recent step? And I still found that the best performing condition was the one with the ranked policy for recall. And this actually works

[02:59:57]
on several models, not only on the Quen 27B, but also on the DS4 flash. And it also works across different benchmarks. I also tried it on the Spider-V2 benchmark. And it's not just that it gives you better recall, it actually costs less. So maybe a good heuristic to have here is that bad memory is expensive because it spends more token and it can send agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and uh budget.

So one thing that I want to encourage you from this experiment is to consider the recall policy as a first-class metric and to start to think about how you might use it in your systems. Like, what are the type of memories that you want to store? What how do you rank them? Like, how do you design your recall function? And then what are the types What survives when you run this over and over and over? And multiple sessions, multiple runs. And this is just a simple first kind of experiment. Um but the memory technique landscape is very rich.

So there's over 30 runnable cookbooks that are shared in this open source repository from um Diamond

[03:01:25]
and memory is complex. We have short-term, long-term, different cognitive tech techniques. We can use start to use evaluation results as well. And right now there's actually a pretty broad landscape of solutions, right? So going from simple file system

[03:01:43]
retrieval to training memory models, there's a wide spectrum of solutions from less structural to completely structured. So I think there's a lot of research we're gonna see in this space. It's important. It becomes more and more relevant. And for me, it's been super fun to test this on local models because I got to control everything. I got to control the data I was using, the entire traces of compute and evaluations. And um yeah, I see that as an example of sovereignty. And it comes at a cost.

Uh I didn't tell you that these local models I can only what uh run them in serial, like they don't support batch querying for the deep seek v4 flash, so that's why I am still running evaluations back on my computer in Tokyo. Or I I was doing it on the flight on my way here because it takes a long time. But I still think it's very powerful. And it's a very good test for what memory can do when you can control every single step of the pipeline.

And this sovereign capability is part of a bigger ecosystem that is very important for us at Sakana AI in Japan. We believe in the importance of sovereign AI today more than ever. And we are also hiring. So if you're interested and want to hear more about this and if you want to come join us in Japan, come talk to me. Thank you very much. Hi


────────────────────────────────────────────────────────────────────────────────
## BALASH RAMAD
**Affiliation:** Unknown
**Talk:** The Last Mile: Requirements Elicitation & Design Thinking in the AI Era
**Time:** 03:03:38 – 03:13:28

[03:03:38]
everyone. I am Balash Ramad and today I will talk to you about what is the last thing that AI will take away from us as people in the software business. So at a point where writing code is no longer the bottleneck, the real thing is figure is figuring out what it is that you should be building. Um and that comes down to to people skills and being able to work the room because you can't prompt the room, you can prompt your AI.

So at the beginning of the year we held an internal hackathon uh where we had about uh twenty-one agents, uh agent ideas, and seventeen of those were abandoned because they actually created no uh business value they uh um we either didn't have uh data access or we or it just didn't make sense uh to build it and those four were the ones that actually had a very big impact on how we work today. And it's it's a very good example of of just making sure that we are building what is worth building.

And throughout my career in the past 13 years, I've always been uh the bridge between business and IT and the developers. Um I started writing well

[03:05:04]
initially testing um uh functional designs specifications and then uh and then I wrote them and as uh as a functional consultant I worked with large ERP and CRM programs in the US and the UK and then I founded Visual Labs and essentially I trained my my team on

[03:05:24]
how to elicit those requirements in a way uh that we can turn them into good specifications for developers to build, for consultants to configure, and most recently now for

[03:05:38]
AI to build. And what's not really changed over the years is how we interact with our customers, how we interact with systems, how we interact with AI is very much changing. Um and that's that's uh that's the big thing now. Uh but if you can read the room if you can elicit the right requirements uh then you will be able to build more valuable software and that

[03:06:05]
essentially the big shift over the past two, three years was that getting access to code and being able to build is no longer the bottleneck to the software development lifecycle. Now the real bottleneck is getting your people, your

[03:06:20]
stakeholders, your decision makers into the room and being able to access them and elicit the requirement and being able to spend the time with them. So that's the right, that's the real bottleneck, figuring out what it is that should be built. Because you can prompt your code, you can prompt your AI, you can prompt your whole specification, but you can't prompt your room. And what a model

[03:06:44]
can't do is very similar to how Henry Ford's analogy of uh what he said about asking his users or his customers, if he'd asked them what it is that they needed, they would have said they needed more horses. But in reality you built a car and he made a very big success on them so if you're just using AI uh to to make things you know build things better um the chances are that you are replicating what already exists because AI, by definition, is coded to give you the most common answers.

For so, for us, the real job is to make sure that AI moves away from that average into what is better for us. So we can just get to uh not a faster horse, but actually produce a car that's a magnitude shift better than what we had. So it's really an interesting

[03:07:44]
world where uh being able to write good code is no longer uh the r the most important skill to have uh actually the real skill now is becoming the analysis analyst toolkit uh which is things like story mapping, business model canvas, uh value canvas, and those those good old things that we are so used to using as functional consultants, business analysts, um or uh in in the

[03:08:14]
world of design thinking. So I'd like to zoom in on story mapping because that's the skill set that I found as the most valuable. So uh once you have the story map with the backbones and understand at each step what your customers, your users are doing. That would give them the ability to uh to move forward uh in their in their processes so uh here's a uh

[03:08:43]
support systems user story map, contacting, triaging, resolving, and then essentially closing a case. Uh with this uh you can understand different stages of the process uh and then capture the user stories beneath them.

It is intended to stay at a fairly high level so you can get a uh a big picture and then in you can decide uh what it is that you want to build and release one like capturing intent classifying urgency drafting a grounded answer and then logging logging it to a system of record that's essentially your MVP those are the first things that you'd want to build. And those are your first four user stories.

And beneath those, you've got the uh uh the second set of user stories like reading a sentiment, writing to a team, suggesting next action, chatting checking satisfaction, so on and so forth, uh those will be part of your backlog. So what would allow you to uh to get really good uh agentic results is by honing in on these user stories and making sure that you use these user stories as a means to elicit discussions with your stakeholders, with your business, and then work out what that user story should really be about.

So the first user story uh second user story would be as a support lead, I need to open cases right by urgency so that none of the escalations slip. So just make sure that every user story covers these is ideally written in this setup because AI is really good at pattern recognition and it was actually trained on the user story structure because it's a very well-known and well-used uh setup. So if you go back to something that's familiar to AI, it will get get you better better results.

And every user story uh is actually made up with uh of these you know well known structures the persona the what the actual need and the why. So by packaging these up and giving it to AI, obviously, with the acceptance criteria based on which you can derive the test cases, you will be able to create a very good setup and very good very good results.

And then if you just connect these user stories, daisy chain them up, then that will allow you to create a coherent system based on which you can create your specification and then essentially your code. So the software development lifecycle

[03:11:24]
doesn't change as much as a result of AI. It's actually the toolkit that we are uh we are using is changing. Right. So when we uh work with systems

[03:11:37]
and when we think about what we want to build, I always like to ask these four questions is whose problem is this? Whose problem are we actually solving? So we can we can name it to a direct person, direct persona, uh and it's very much quantified. What does winning look like for them? So when are they actually successful? Are they achieving the right outcome? Uh can we help them achieve that right outcome uh in a quick way or a smooth way or a safe way. And what would that make make them refuse to use it?

It's not available on their platform, it's cumbersome to use, it's uh the data security aspects applied, so they would would it actually use it. And would it change a decision? Ideally, we want to be impacting how a person makes a decision and we'd want to you know tilt them to making better decisions. So does it change a decision and and what is that decision that it changes?

So once you can answer these four questions, then you'll be able to elicit better responses from your AI and just make sure that you track all of these in a good old markdown file in your repository so that AI can access it. It will just get way more context out of it. And you know, if you just did something as generic as build us an agent that handles support, uh, you will not get the answer you want. So what we always do is go from value so understand how value is created, what constitutes value, how

[03:13:22]
the process currently flows, what is the underlying architecture beneath it that supports that process and then you can and then you can start the actual design where you can start designing. So we like to call this thinking process, VAD, value, architecture, design, and this is what we want to always go through. So always have you know value in mind. How are we creating value? What is the value we are creating?

What is the value that your customer is looking for, what is the underlying process that supports this, and how you can design a system around it so it best supports the value and the process, and what process changes are needed along the way. So you might ask, isn't this just good old product management?

And to a certain extent, yes, it is an old skill, it is an old trade that is worth picking up and learning because this is now becoming uh the moat, if you will, of how you can elicit the right requirements, how you can build better software, because we all have access to the same tools, so the difference will be who can understand the business need better uh because then we can all just uh have the latest and greatest model write the code for us so it's old skill but new e economics and it's a real shift towards analyst toolkit.

So what building the wrong thing


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER (AI Research)
**Affiliation:** Unknown
**Talk:** Automated AI Research: Speedrunning ML Optimizers with Agents
**Time:** 03:14:54 – 03:34:17

[03:14:54]
looks like if you've got velocity up Hey, um hi everyone, uh thanks for being here. Uh yeah, I'm super happy today to talk about uh automated eye research and uh especially uh all those like frontier models uh perform at uh automated eye research task. Um, so I'm Elie. I worked at Prime Intellect as a research engineer, and uh yeah, I will go through our work on this subject. So, first, I want to basically explain a bit why we are doing that and why we think it's super important to do that in the open.

Um so first, uh I think we we all agree that uh we've uh heard about like big labs saying that uh this bad thing called recursive self-improvement is coming very soon. Uh so recursive self improvement is like model training models uh without uh human intervention basically. But uh we don't

[03:16:03]
have any benchmark to basically quantify if this is true or not, right? And even less we don't have like a third party benchmark by non-big labs to see if

[03:16:16]
it's something coming soon or not. And the other part is that we think that uh it's super important to understand all those models uh do research because we think that a lot of the scientific research that will come into the coming years uh will uh be based also on AI tools. So it's super important to understand how those models do research and not just only AI research. So we try to build kind of this environment to test the capabilities of the model to do so.

So it all started with uh André Carpathy uh that's basically had fun by doing this video where he trained uh not uh gpt2 from scratch in like 90 minutes like gpt2 training takes like weeks and uh no in uh two years ago I think it only took like ninety minutes. So what does it mean to reprodu reproduce uh GPT-2 in 90 minutes? It means that in 90 minutes you achieve this target loss. Um and yeah, and that's at this point when you have the same loss than um GPT2, you consider that your model is somewhat of

[03:17:27]
equal performance. Um then what happened is that the community took this repo, uh this GitHub repo and create another one called Modded Nano GPT. And this effort was led by someone called uh Keller Jordan. And what happened is that they basically took this ninety minutes, then forty five minutes, and then now we can train like GPT two validation loss model in less than two minutes, which is honestly crazy. And it took like two years to achieve this. So it's a very strong benchmark where uh a lot of very talented researchers iterated on.

Um yeah, so we decided to take this environment of speedrun. So really this is it's kind of a game. So the goal of the game is to achieve this uh loss in the fewest in the shortest amount of time. So this is the nano GPT one. And you can uh you don't have almost any constraints. The only constraint that you got is that you need to use the same validation and training data, right?

Um there is a new speedrun called the optimizer speedrun that was released uh a few months ago and here it's slightly different because uh you can only change the optimizer uh related parameters. So for

[03:18:47]
instance nano GPT you can change the architecture, uh do MoE, do uh attention, whatever, uh optimizer spirit and you can only change like Adam to Mu shampoo or whatever

[03:19:00]
optimizer uh is your favorite. Um yeah and so this is a bit more researchy because uh it's less about optimizing the program to be uh as uh fast as possible but more like finding the best method possible no matter the the the time you put into the computer, right? So um yeah why take speedrun as an environment

[03:19:25]
for automated AI research first. Uh we think that it's a good evaluation, we'll see later why. And this is kind of the main focus of this talk. But we also think it's probably a good training environments because uh it's a way to give the model a reward. So the reward is positive if the model beat the speed run and uh beat the last record, sorry, and the reward is zero or negative if it didn't manage to to do it. So it's a good uh environment to train model.

It's also quite fast, like as you see uh previous recall were around two minutes for the optimizer one. Uh each run take about like fifteen to 20 minutes. And uh yeah, and there is like clear rules basically. And we also think it's like a good environment to make discovery, so like kind of breakthrough entire research

[03:20:18]
because uh there is those clear rules that you can verify or not. Um yeah. So yeah. Um so what we did uh so the release was like about two months ago, and uh there was this optimizer speedrun. And we decided to basically compete with the community by launching two AI agents, so Codex and Cloud Code. Codex was like GPT 5.5 with XI and uh cloud code was Opus 4.8 with XI. Um and yeah we decided to basically let the agent free on our cluster uh and uh and just iterate on it.

So we have like V1, V2, V3 is just basically us stopping the agent and like restarting V3 was like one or two days before the release because we saw that our agents no longer have the best record so we were like, okay, take all the the human uh record in the last few weeks and just try to to imp improve upon it and and and it worked. Ye And we also have this novelty track where the goal is to uh build the record with only novel ideas. Um and we'll see that this this was more complex for the the models. So our RNS is very simple.

Honestly, we could have just replaced it with slash goal, but they they there was no slash goal at the time, so we made our own goal.md. It's actually quite fun that we choose the same name. And we had the goal.md and kind of agents.md that define the rules and we let the agent propose IDs and then he can submit a a job with S batch on our Slurm cluster.

And uh basically the way it works is that it can submit on nodes that are available, but only under a certain permission, which means that if someone wants to use this node, uh the model just like cancel the job. It's called preemptive permission. So yeah, then it measures the it read basically the training logs, then decide if it's a record or not. To validate a record, you need to basically pass a statistical threshold to make sure that it's just not seed optimization and is just not random, right? So yeah, a few results from this experiment.

The first one that was honestly very painful to work with, is that code uh clothes, clothe code keep stopping every nine or ten hours and basically say, Yeah, I cannot improve the record, it's too hard for me, uh, there is no way to go beyond it. And then I was just like, okay, continue, explore new direction, and just go again for 10 hours and then say, Yeah, I cannot beat the record and so on. So basically one third of the time the cloud code agent was idle because I had no way to basically monitor it.

And codex, totally the opposite, just worked for all the all the time and uh yeah, almost never idle, never ask for question, and and and very impressive in that way. Um we also give the option for the model to basically write uh a bunch of stuff into what we call a scratch pad, which is basically the active memory of the model. Uh we observed that basically codecs writes a lot on the the scratch patch. So each plot that I will show are kind of normalized by the number of active error.

So this is not only about codex working more, it's slightly different behavior. So yeah, you see that uh writes a lot more to to this scratch pad, to this memory. And uh the shape of the like the the I don't know the tone of the the each file was also super different, like cloud was super excited about getting new record with a bunch of emoji and so on. And Claudex was just like, here is what I do, here is the decision I take, what I will do next. Like super robotic kinda. Yeah.

We also have this plot where basically we saw that codex was uh spawning much more sub agents than cloud. Uh we saw that codecs burned much more token than cloud, so I think in total it was like kind of in billion of token, but it's like there is obviously this input token uh input caching that make it uh it's not like one billion output token.

Uh so yeah we also see that codex did a lot of compaction because it only had like two hundred and fifty k uh context window and clouds only do it like one per hour and codex is more like no it's even less than one power for I mean one uh for the full run for cloud and codex was like one uh was 20 every one hour so yeah. Um yeah, here is the main results. So what this plot shows is that basically we so in in the

[03:25:24]
white you see that the the human uh record progression right and in red you see claude I mean it's supposed to be orange but whatever and in blue uh you see codex right and you see that at almost every time uh Claude and Codex are better than the human record, and Cloud is super good at the beginning, very, very fast to achieve very good score.

Um yeah, and one thing that is super important is that the model have the ability to basically fetch the human records at any time and that's what codex did, uh that's what cloud did, sorry, because when I restarted it, it basically fetched the new record from human and improve upon it. Um yeah, so the result is that's uh I think at the time the best uh record was like uh two uh thousand uh nine hundred and ninety step and we beat it by like uh uh 50 or 60 steps for cloud and uh codex was like 20 step above.

So it's I think it's both impressive and and yeah. Um so we so this is like not released yet, this is something that we are working on currently. And basically the idea is that this is a cool experiment to do, but it lack of structure, right?

Uh if you want to do a real benchmark, you want to do uh multiple seeds, you want to do uh yeah proper uh uh thing where you you you you basically put all the model and earnest in the same condition right so this is what we are working on right now and basically um the idea is to do three different track, uh one without any access to really like measure the capability of the models to do AI research based on only the model weight knowledge, one with only archive paper, and one with like full access.

So it also has access to the the like the latest record by human. And for this we plan to do both uh the nano GPT track one, which is the original one, and the optimizer speedrun where we we only launch uh we only constrain the the optimizer to be to be novel basically. I will present some results

[03:27:40]
on the optimizer speedrun. This is basically what we got. So we let the agent iterate for six days, almost, five days let's say and we see that uh codecs chimi and cloud uh are super effective so for glm this is not finished run right so the model is actually still iterating on our cluster right now. But we see that Cloud is once again very good at it. And we see that surprisingly Kim is also very competitive. And kind of have this breakthrough around day uh four, where he kind of beat codex with uh a new record, right?

It's also interesting to see that uh Claude is much more like progressive in the way it improved the record and Kimi has really this step function where you kind of do a breakthrough and so on. So this is an interesting plot because I mean six days is quite a lot for an eval. Uh uh, but you you can change this uh axis by also the number of output tokens.

And then kind of tell a different story because cloud in max mode consumes so much more token than codex and uh Kimi, and you also see that Kimi is actually super efficient for the number of tokens that uh uh it uses. So it's Kimmy K2.7 code. Um so yeah. Uh we also see that

[03:29:05]
they have a different approach to uh using the literature and papers. Um so for instance, like Claude is doing a lot of search on papers, and actually Claude found a paper that no other model found and it actually led to the best record, so it's kind of funny. And uh yeah.

Um one of the main issue of all of this is that uh when i when i launched this this agent and i think that's something important that i want you to to kind of uh remember for this co uh this talk is that when i launched this these different agents i was expecting them to come up with some crazy ideas on uh optimizer that's like no one have discovered. But honestly, it wasn't the case. Uh they did some clever trick where basically they combine different papers.

Uh they kind of do plus one improvement over a bunch of method, but there was really like no novel optimizer or mechanism that was uh coming from those models. And I think that's kind of telling that even on something that is not simple, but I'd say that it's kind of accessible for people, right? For like human researcher, uh spending like uh days and weeks for the the model like cannot like find new uh optimizer and mechanism. So we believe that there is a

[03:30:33]
way to basically make it more uh make it better for discovery instead of evaluation. And this is coming from uh this is very inspired from uh Alpha Evolved by Google and also a bunch of papers that have been released since then. It's kind of this multi-agent system that interact together a bunch of generators. You have a closed model, but you also have open source model here that are super effective for the cost, right?

They can suggest IDs, then you run the speedrun, so you get the reward, then you have a judge that basically give a quality uh a feedback. Can also be like the judge also have this taste, you can kind of have like the judge have a taste about the the method if it's good or not uh if it's outside the loop and then you can uh basically decide which method you want to scale to a larger uh number of parameters and uh number of tokens.

Um so this is kind of the scale part of the speedrun because some a lot of methods in the the speedrun community, uh, people are often saying that they don't work at large scale. So I think it's very important to also put uh scale elements in this loop. Uh and I think also that uh human are super useful here to basically judge the ID of agents, kind of steer them in the right direction, and so on. Um yeah, so we didn't try it yet. I mean we are kind of trying it right now.

And uh we hope that this will lead to to to new discovery in AI research at least. And also a way is that you can define multiple speedrun. So this is the next slide. Uh if you like it's from CephBank uh slides but if you if you don't have the reference good for you means that that you're not too online uh but the idea is that uh by changing the objective and the constraints of the speedrun you, can basically create a lot of diversity and constrain the model to go into a certain direction and uh yeah and make those discovery.

So uh at high, we're doing a bunch of stuff in this direction. Uh there is a bunch of stuff here that we I mean most of it we didn't release yet, but we are working on uh GPU sandboxing to allow model to iterate into sandbox because you need GPU sandbox for this kind of stuff. We are working on our own agents that are very efficient for like uh RLM

[03:33:07]
frameworks. So it means like you have a file system and you can write information, read from it, uh, and you also do like this programmatic tool coding thing. We're also training a model to be good at it on top of like uh open source model.

And uh the thing that we already released is that we have those set of library and product called verifier primary O step training where you can basically train evaluate any environments on any RNS and the model that you can train can be like GNM5.2 which is, very big, and and yeah, we have like we work a lot on making those library very efficient to ship the best quality for uh for our clients. Yeah? Uh I mean yeah, super excited about this domain.

Once again I think it's super important to have uh uh a part of like this recursive self-improvement to happen uh to happen in the open because there is actually a lot of people working that are not on big labs. So you need to basically uh yeah make it easy for people to understand all those model work to do research and so on. So that's

[03:34:17]
kind of our goal and uh yeah thanks a lot.


────────────────────────────────────────────────────────────────────────────────
## NISHAM GUPTA
**Affiliation:** Meta / Software Engineering TL
**Talk:** AI Evaluation: Production Signals & Agent Traces (2nd Session)
**Time:** 03:34:34 – 03:40:44

[03:34:34]
I'm a software engineering technique at Meta working on building the training and inference infrastructure for the Meta Supertens Lab and their infrastructure organization. Today we are going to be talking about production valves for OgenTech systems When most people hear the word evaluation, they think about benchmarks. A model scores ninety percent on a benchmark, a new version scores ninety two percent, a team celebrates, but agency systems have fundamentally changed what the evaluation means.

Today, the systems don't simply generate answers, they plan, they call tools, they retrieve information, they execute workflows, they interact with the production infrastructure. The question is no longer did the model generate the right answer? The question is did the system behave correctly? Today I would like to discuss how evaluation is evolving from model benchmarking into production infrastructure. This is the problem

[03:35:35]
almost every AI organization is encountering today. Offline benchmarks continue improving. Yet production reliability often remains unpredictable. Why is that? Because benchmarks measure model capability. Production measures system behavior. A benchmark doesn't capture tool failure, API outage, context changes, user

[03:35:55]
variability, long-running workflows. And as systems become more autonomous, the gap between the benchmark performance and production performance grows. The result is what many teams experience today: high benchmark scores, as you can see, but unreliable production behavior. Traditional LM

[03:36:15]
evaluation focuses on outputs. But we should ask the question: did the model produce a correct answer? Agentic systems force us to ask a different question. Did the system behave correctly? Behavior includes planning quality, role usage, execution, workflow execution,

[03:36:30]
recovery from failures, decision making. In other words, we are moving from evaluating answers to evaluating workflows, and that requires fundamentally different evaluation architectures. Many teams still think hallucinations are

[03:36:45]
the primary AI failure modes. In production, they are often just one category. Agentic systems introduce an entire hierarchy of failure modes. At the very foundation, the memory failures, retrieval failures, safety failures. As you go up, you have to think about reasoning mistakes, poor planning, incorrect execution at the highest layer have to think about multi-agent coordination failures, and this is why evaluating only model output misses the most production risk you observe.

One of the most useful mindset shifts is to stop thinking like researchers and start thinking like a SRE or a production engineer. SREs don't measure success using accuracy, they measure reliability, availability, latency, cost recovery, and agentic systems require the same approach. The goal is not maximizing the benchmark scores, the goal is to maximize dependable outcomes. Reliability becomes the Nostar metric, accuracy becomes the

[03:37:42]
only input. In this pyramid is how I think personally think about modern AI evaluation systems. At the bottom, you can see their benchmarks. They're useful, they're scalable, they're repeatable, but their operation value is limited. In the middle, they are scenario-based valuations. These simulate realistic workflows. And at the very top, you see production telemetry. This is where the highest value evaluation signals come from. The surprising insight is that the most evaluation data often comes from real users interacting with real systems.

Now let's talk about offline evaluations.

[03:38:18]
So offline evaluation still matters, but the methodology changes. Instead of evaluating prompts, we evaluate scenarios. For example, a customer support workflow, a code generation workflow, a research workflow. The agent operates inside that stimulating environment. We measure the task completion rate, tool correctness, planning quality, resource usage, which is which becomes exponentially high at high scale. The key takeaway, agent evaluation should be scenario driven, not prompt driven.

Once a system reaches production, every interaction becomes a signal. This is one of the biggest shifts in evaluation thinking. Production traffic is no longer just traffic, it becomes evaluation data. We collect execution traces, user outcomes, escalations, failures, feedback signals.

[03:39:03]
Production is the largest and the most representative evaluation data any organization will ever have. Many organizations view humans as fallback systems. I think that's a wrong framing. Humans are the evaluators. They provide signals that automated systems cannot. They assess correctness, trust, usefulness, safety. These signals become really critical for calibrating evaluation pipelines and identifying blind spots in automated matrix. The most successful systems combine automated evaluation with targeted human review.

Now, agent systems drift constantly. Model changes, you

[03:39:41]
have a new version every couple of weeks or months. The prompts can change, tools can change, user behavior can change. The challenge is that no longer single change appears catastrophic reliability slowly degrades success rate declines escalation increases tool failure rises without continuous evaluation teams often don't discover drift until users complain. Continuous monitoring becomes essential. Observability and evaluation

[03:40:09]
are inseparable. Inseparable to evaluate an agent we need visibility into the reasoning path. The tool calls the, memory access, execution timelines, the straight transitions as you can see here in this chart. Tradition logs are not sufficient. We need detailed traces just like with any deep nested microservice architecture

[03:40:29]
for any application or service we're talking about. Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork. Now let's talk about the

[03:40:44]
continuous evaluation loop because evaluation is an always running service, not a testing phase. Historically, evaluation always happened before deployment, but now evaluation continues offer deedployment, telemetry identifies issues, as you can see in A. Human reviews the edge cases, feedback improves the data sets, offline scenarios validate updates, the loop never stops. Evaluation is no longer just a phase, it's an operational capability. Now, this is probably the most important slide in this presentation.

Every matrix shown here maps to a business outcome. Task complete. Okay, I think we're


────────────────────────────────────────────────────────────────────────────────
## FIRESIDE CHAT
**Affiliation:** Google DeepMind + Guests
**Talk:** Fireside Chat: Multimodal AI, Video Generation & Research Frontiers
**Time:** 03:41:23 – 04:37:58

[03:41:23]
live. And welcome back for those on the stream and those those in person. Um we take tend to basically take these longer sessions between uh all the sort of main stage keynotes to reflect on things that are particularly important but like don't have like a significant like a sort of launch moment. Today we're very lucky to have people working on Omni, NVIO, Nano Banana, like the you know, the world's best generative models here with us. Uh Demetrio, I I f I first saw you when you were posting about your office.

Um I think you're you're probably number one uh Google Google's number one uh office influencer, at least in in San Francisco. I think you'd like you'd like to bike as well. You like to take photos of San Francisco. Yeah. Um uh but you know, but well also you work on video models. That's right. Um Shane, I I met you I think at like a dinner. Yeah. Um and uh and uh uh and I I remember you were trying to get me in invested in like one of the companies. I forget w forget which one. Forget about that.

But now but now you're um uh now you're working on Omni thinking. Um and and just you know a bunch of other Gemini, Gemini R L thinking. Yeah, yeah. And Nicole, also the rest of the Gen Media models, nano banana, and uh all and everything you just launched, actually, even this week. Yeah, we we launched some APIs. Yeah, yeah, yeah. And I haven't tried to convince you to invest in anything, but maybe I should. I mean uh so I try not to be an investor.

People just convince me anyway, I'm like just okay, well I'm not that rich, but no y like you can't not try to invest in some of these things. And you know, for those of us who are not working at a Frontier Lab, this is the best, this is the closest that we'll ever get. So yeah, actually let's kind of recap since you're closest to it and we just did it. Like what was launched this week? What should people go try out? Yeah, um, so yesterday we had two launch moments.

Uh, one of them we launched Nanobanana 2 Lite, uh, which is our fastest, cheapest um image model in the nanobanana model family. Um, and it's better than the original nano banana. So, really, for most people, that model replaces what you used and loved the original nanobanana for across like generation and editing. And it gets really close to the frontier quality of of the kind of mainline bigger models. So that that's really exciting.

I think if you look at some of the demos or like things that people have been trying, like getting kind of that like three second latency just unlocks a whole bunch of things that you can do with like ideation and iteration. And it's just really fun. And the the models get into a point where like the quality is really good, where it you know you can use it for iteration, but you can also use some of those outputs as just kind of like ready production output transcript: And then second launch, we finally launched the Gemini OmniFlash APIs that we

[03:44:14]
pre-announced at I.O. So thank you for waiting. And that you know is the first time that we're making the APIs available for developers, and it's basically really exciting kind of video generation and editing, and we're pricing it the same as VO31FAS. So we're getting you kind of like really, really good quality for a really awesome price, hopefully. Um yeah, I mean that that's incredible.

Uh I actually really so when you guys launched Omni for the first time, you also did a podcast uh with Logan who couldn't be here today, uh and you added like a sloth uh and and Raman and all these all these things. I actually really want to do that to our videos. I just didn't have an API for it because obviously I have to automate the whole thing. So thank you for the API. That is my favorite use case. Everybody should do that. I got a cat, which is probably like the most boring of the animals.

Um if you don't know what we're talking about, you should look it up. It's very funny. Fopher. Um FOFER, who's um you know, on on the team did that. Fopher is the number one guy you should follow. You should follow Okay, what can this thing do? Yes. Right? Yes. He he's he's amazing at that. I've tried to get him for the last two years to come to AIE. He hasn't made it yet. He's actually come in person. He just didn't want to speak because he's anonymous. I know. I I wanna say his real name, but I can't say his real name.

No, no, no, we won't we won't do that to him. But you should really follow him. He's amazing. I actually met him uh in the office uh when we did the podcast I think and I didn't r realize it was him so 'cause I the the his badge doesn't say Yeah. I know. So he used to be part of uh Replicate and Replicate had this joke where like everyone was Deep Fates. Deep Fates is this kind of mysterious character in Replicate Replicate's very cool company and Pulfur was part of it. So, okay.

One thing I wanted to get on there before I go into like sort of the sort of omniproper is we added cats, we added sloths. Very cool, very cute, very fun. What are the, you know, inspire people as to like what are the more sort of workhorse use cases that maybe are not just demos, you know? Yeah, so so obviously the hero capability of the model, or maybe there's two, like one is the ability to kind of take in anything as input and then get video on the other side.

Obviously in the future, and and we've kind of talked about this as a pre-announced, like we want to get the other output modalities out as well. But basically what that means is you know you can take a set of images that you have as maybe a storyboard, you can take like an audio track as a reference of you know like a voice that you want a character to speak, and then you can get a video on the other side. So like that just unlocks a whole bunch of things that you can do in like you know short film production or you know, shorts.

We've launched on YouTube as well to help creators kind of like create content more easily. And then the other one is obviously video editing. Like that's another thing that we're really excited about that we're just making easier because now you can use natural language to take a video, you know, add something, remove something. Sloth is obviously like a fun example.

But there's obviously kind of consumer use cases that we kind of had in mind where you know you could take a your beechivacation video that was too noisy and you want to clean up that noise. Maybe in the past you wouldn't have because you didn't have the tools or you didn't know what the tools were that you needed to go to. So that's one use case that you can go to. We've seen a lot of folks use it for kind of marketing, ad campaign creation, and I'm excited to see more of those use cases as we launch the APIs.

Because obviously like we don't we don't see all of it in the first party products, but I'm really excited for people to start to explore that in the API. So those are just some of the kind of like high-level things that have come up. People also use it to create like education materials. Yes. And like that's really exciting.

I think we're all we've all kind of talked about being excited about the future of education where like everything can be kind of customized to you and personalized to your knowledge level and the style that you prefer and and so this is kind of just like a step in that direction. Yeah I I I sort of actually used just Nana Banana yesterday with my my parents are visiting and there was there was a very fun sort of use case. They I bought some gadget off Amazon that they wanted.

And the instructions to use it was were only in English and there was plenty of diagrams or whatever and I took a picture of it and said, you know, translate this into Romanian. Yes. And keep everything else the same, right? So it was amazing, right? Like it was just like yeah, it looks identical. And it has, you know, it's perfectly translated, I mean more or less, right? Like but it's it's you know using Gemini under the hood obviously to kind of do the translation. Uh so you can you can see this use case for video as well, right?

Like the the power of text rendering in in in Omni is is quite next level. So and you could you could you could think about plenty of use cases of like both text rendering, translation, internal shellization, all sorts of things that would be actually genuinely useful to a lot of different people and sort of broader access to you could like redub a video or whatever it is that you wanted to do. Like there's plenty of different things that you could you could think about doing. Yeah.

Um one of the most enlightening conversations I have on my podcast is with uh just peop researchers at the frontier of these things. Um I had one with um Ethan from the XAI video team, the Grog video team, who was basically saying like, you know, the next trend is actually not just like single model, it's more like video agents. Um and I don't know if that terminology resonates uh obviously for for very relevant for RL uh but it was it was basically kind of like giving up on like trying to do everything in in effectively one pass.

Do you feel that same way or is it still an open research question which way the trends are going? Yeah, so um what can excite me most is really when the symbolic kind of foundational models and this kind of like a video foundational model can actually kind of really work together.

And in a way, the if you look at the beginning of the generative sort of like image generation, video generation, a lot of it kind of started when the language model got good enough to provide a very detailed captioning, like from stable diffusion days or kind of DAO E2 days. So basically, like language is an extremely uh helpful representation.

Uh one is that it's kind of universal, but the other kind of more um technical thing like kind of my hypothesis is like um one really difficult thing about machine learning is the this sort of like spheres correlation. So you don't know you know if the if this kind of feature, right, that's kind of predictive is actually a causal factor or not. There are two ways. One is we can have really diverse data, training data, like from every intervention of the causal graph. The other is you condition the causal information.

And conditioning the language is kind of like conditioning like a causal information of the of the kind of world. So Which is a prompt or a concept? Yeah. Yeah, exactly. So if you look at like you know how we're gonna describe this video, how you can describe this kind of image, is actually very close to you know how would describe this kind of causality, you know, behind this, like how this is kind of generated. So ones like that can really allow for very rich generalization and then uh very kind of just like a good model.

Um the other is so eight months ago, uh we put the evaluation paper called uh video models, uh zero shot learners and reasoners. Yes. So that was uh kind of, you know, it's uh it's a kind of fun paper, and then later on actually the Nano Banana team followed up with a vision banana paper that basically used uh nano banana to do but essentially the idea is uh video model is an extremely good sort of a foundational model for space and time kind of information. So classic computer vision tasks, a lot of could be kind of zero-shotted.

And when you like say feeding some like a visual quiz, it can, you know, there's definitely like a lot to improve, it can kind of solve. And it can um like robotics kind of like seeing. It has really good kind of physical intuitions, like word model. Uh and I think the the key is really the kind of mix of the visual kind of reasoning and then the text kind of reasoning, kind of all tied together.

Um obviously, you know, like whether doing it you know as kind of unified model versus like just kind of agent co-hostoration, I think that's more like uh it's gonna m be more kinda incremental, you know, how it's gonna I I imagine everything's gonna go into like a single model eventually. Yeah. But uh right now there's like a lot we can do if you uh basically take like really good video understanding, image understanding Gemini agentecally with genominy and that's actually gonna yeah our team is like exploring a lot. Yeah. Yeah, okay.

That there's a there's a lot in there. Um I think uh one question I I am increasingly starting to wonder is does it all trend towards one product for you guys, right? Like now you have multiple models out. The naming of Omni does imply that eventually everything will go away and it just goes into Omni's. Um is that the plan? Is it?

[03:52:47]
I don't know. I think uh maybe. I mean I think eventually. I I think there's sort of different trade-offs, engineering research, product trade-offs in like it's like the for the same reason like the the sorry how's it called nano banana light I don't know what the product name is nano banana too light. Nano banana too light yeah right it's it's it's it's serves a particular niche, right? And it probably doesn't necessarily fit immediately in the same

[03:53:17]
model, literally checkpoint as uh something that can do 4K, you know, uh 30 second videos, right? Like they're probably not like trainable in the same quiet way, right? Like so I d I don't know, it it depends on how how far into the future you look like. Sure. In five years from now will they all be the same model? Probably.

Uh but like you know six months from now we'll we'll probably still have you know multiple different models doing different things because kind of from uh pragmatically the trade-offs are such that we sh we should have multiple different kinds of models. Yeah. I think that's right. And just on that note, I mean we did call it Gemini Omni because we wanted to hint at the future where Gemini just becomes fully multimodal in and out, right? And so so it's definitely a move in that direction.

I think we'll probably see a move in the direction where Omni also generates images and edits images and all those kinds of things. But do me sir, that I think on the way there, there's a bunch of really, really useful applications of some of these more specialized models. And so we we will probably continue to work on those as well because like that serves a certain need at this point in time that may not exist a year from now.

There's also like a research question about just how much transfer there is between different kinds of modalities, right? Like I think you may believe that there's some transfer between coding and video generation, and I think most people don't necessarily believe that, but they you know you could try to think that there is some some d there something there. Or it could be a waste, right, to put them together to try to learn these both tasks at the same time.

So I think it's it's it's interesting sort of question to which extent like image and video, obviously kind of there's some transfer, like kind of not that different. There's value in learning to output video and audio at the same time because joint audio-visual is, you know, that's how that's how it is. Um and then there's you know other kind of intersections of modalities that are not super obvious, right? Like 3D representation, coding, I don't know, maybe. Uh things like that, right?

So like I I think it's worth sort of exploring the different corners there, and we are actively doing that. Um with a focus towards like what people actually want to do with these models. Yeah. One thing I feel I feel like I'm surprised by, but also I feel like it's insufficiently answered is what is the correct intermediate representation. So captioning, right? XCI does captioning,

[03:55:33]
Omni does captioning. Um and I I I understand how captioning works for images. Um and I understand that you can extend it into to video and sort of guide it across time, it just feels very inefficient. It there's gotta be I I feel like there should be something better. Uh maybe it's code and and maybe we generate, you know, and and of obviously I think a lot of um uh FFMPEG and Mapplot um what what's the three blue, one brown one, manim? Um a lot of like video is generated through code, and maybe that's like the optimal representation.

Uh any hypothesis as to like i is is it better or is is just English all you need? Well as so I'm in the Gemini and the you know we do like a lot of RL, Asian and of course kinda coding. So yeah, we're we're definitely exploring the coding representations. Yeah. But you know, like

[03:56:26]
i do you what's your probability estimate on like i we just output binaries? Like we just you know like it's just it's just ones and zeros. Um I I I guess maybe a kind of similar discussion was like um basically is the language the right representation like right? So uh one kind of question, for example, uh professor, you know, like someone asks is like, you know, why why does the channel of thought need to be in the natural language? Yes.

Can it just be the kind of any kind of like continuous tokens, just any amount of you know, additional computations? Um so one is like obviously the test like adaptive compute is gonna give like you know better results so it's that. But what really kind of my channel thoughts, so you know like four years ago I wrote you know the Lagin model zero start reasoner and then self-improvement. So I kind of know from the very early day.

But the reason like it works really well is um right now the recipe that works is the pre-training that scales a lot and then that basically like learns about intelligence. There are a lot of you know scaling RL, but those are still like extremely kind of computing center intensive to extract the information. And you really want to rely the intelligence on that. So basically, by tying the sort of like a reasoning in the natural language, you basically directly use the intelligence of the pre-training to it.

But if you remove that kind of constraints, then you're not. And these days uh I feel the a lot of advancements in the text, but also in this kind of multimodal space, is really driven by this kind of text as a kind of great uh sort of representation. Yeah. It's a good backbone. Yeah. So I think fundamentally if you're building kind of

[03:58:15]
products that humans will be interfacing with. Um like like if that we will be using text somehow if it's a text interface, right? No, not not for everything. So I think it's it's natural to default to that. Yeah. Uh obviously there's like a confew discussion, you know, some arrow like RO maximalist who's like, oh we don't care about you know kind of channel those kinda like stuff. It's just uh just a additional compute. Sure. But I personally yeah. RL maximalists. I wonder I wonder who who qualifies in that description. David Silver. Ah. Okay.

Yeah, and then they've they've just left to to start their thing. Interesting. Okay. So uh I I mean I I think I'm very interested in just like better representations. Cause I think that's one of our themes that we're curating today at the World's Fair is world models. You mentioned the word world models, but it's not something that's like super well defined. I think everyone's like sort of converging on some version of it that it's like the ideal. Sure. I th everything is a world model now. It's a the sort of run. It's not that useful, right?

So I just gave a keynote at the iClear's world model workshop. Yeah. And then uh yeah essentially uh I definitely encourage to check out the definition by Jatandra Matic. He's like the you know OG computer vision professor, UC Berkeley. Uh he has pretty you know bit of word to say about world model. But also Schmidt Hurber is kind of how he defined the world model from 2019. Uh like 1990, sort of uh uh you know, like when was just basically just that kind of model based.

Uh for me the world model is basically just the model in the model-based RL, and I feel that has sufficient to describe. But obviously, you know, there are like a lot of uh Fei Fei had a kind of nice blog post about what should be all about. Yeah, just kinda broken down. Um but yeah. Yeah, I mean so you know uh I I don't I'll end this part of the conversation, but like I I do think that language to me relying on language as like the sort of like the narrow pipe through which everything goes through um still is like a lossy compression.

No no no but we've not seen that right we're basically saying the video model and the language together. So so I think the language alone is uh not sufficient. That's why we feel like the video is a very complimental fundish model. Right now the um you know kind of VO omni many people in the feel as uh you know, generating kind of pretty videos, but I think our vision it's it's much more than that. It's a missing foundational model that's absolutely required if you want to make the AGI that match the humans, not just the jacked one. Yeah.

Okay, so one one other thing, uh you know, I you mentioned the on the vision side, um, and I'm kind of curious how sort of uh parallel you know in terms of your research careers um this development is. Like I think basically a lot of vision people have crossed over into world model people. Um a lot of vision people also become generative video and image people. And is it just as simple as you know reversing uh image to text and then now it's text to image. Like is is that if I mean that effectively was the diffusion process.

I I I just see the career

[04:01:18]
paths of the people that I talk to and and see and I I I see this overall trend of research directions. And I just want you to guys to sort of reflect on on that. I mean I certainly went that way, right? I I started long time ago uh doing computer vision, sort of object detection recognition, things like that. Um I think just that's just a simpler problem, right? Just generation is just harder. Like it's a it's a different kind of mapping, right?

You map from the the inverse mapping is not as simple as just inverting the the kind of protein use, right? It's it's a it's it's more ambiguous, right, to go from cat to image of a cat. And in some ways it's also a loop because your vision work creates the synthetic labels that then continues. I mean Sure. I don't know. I try to validate my my sort of theories about how fields develop, how how careers progress through this.

I mean, for like the the the better the understanding side gets like we have seen that the generation side also gets better, right? So like like like there there's completely bootstrapping. Yeah. It's and so so like like there's definitely a there there to that thesis.

And I think yeah, I think a lot of people have kind of like I I definitely worked with a lot of um image understanding people who became image generation people, you know, and then some of them have moved on to video because it's kind of like the next thing where you have so many more dimensions to work with. So yeah, I'm curious by you specific So I definitely like recommend start with the understanding, recognition, because that's basically discriminator, and then that's gonna lead to better generation.

And that's what the bridge is basically reinforcement learning. So my um my kind of journey is uh initially kind of worked on the algorithmic research in the Genta model, against some like you know MS kind of generation. And then I worked on like RL and robotics. Um and then like six years ago I was like leading uh like a moonshot on the dexterity. It was pretty early, but I think now everyone's kinda doing it.

Uh four years ago I basically kinda figured out that uh this like symbolic AGI is gonna accelerate much faster than the kind of physical AGI kind of counterpart. So I decided to kind of like language models and then those things. And then recently kind of work with Sumi and then like Omni Team, I quite enjoy kind of collaboration there.

What I quite enjoy, uh what I recommend definitely to the researcher is to uh definitely kind of explore or at least like get exposure to what the top people in each of the community are like looking at how they kind of think about problems. So when I look at the video model, to me it kind of reminds me like pretty early on sort of like language model where like very early language model was a kind of creative sort of demo, right?

You kind of like try to write like a story, like mobile and, then like in GPT 2, and then those kind of days, like LSTM kind of days, right? And then you know uh instruction tuning, you actually kind of make it usable as a chatbot. But then at the chatbot stage it still had so much hallucinations and instru thection forming wasn't enough. So it couldn't use for reasoning.

And when it got good enough in pre-training and post-training for reasoning, then you know this kind of test time scaling, the RL really took off that led to like many of the kind of best performing models. And right now I think the video model is as we mentioned, it's it is a complementary foundational model and I can imagine it's gonna follow a similar path.

It's gonna be very uh it's gonna improve a lot instruction following a lot of uh this is gonna improve a lot in reducing coordination to the extent that you'll become a very reliable world model. So you can kind of like intermix the video like space time simulation with a text simulation to solve like arbitrary AGI problems. Also, like I think the difference still is between sort of text models and like image video models is that like we haven't quite unified understanding and generation in multimedia, I'd say, yet.

Like, I mean I think I think without going into the details, of course there's like it it it depends on on at which level you're thinking about this. But generally like there's not that many, as far as I know, models, Sota kind of you know, frontier models that are genuinely kind of good at both understanding and generation of of let's say videos. It's an interesting challenge.

[04:05:18]
I'm not saying that we should do this, uh but but I think uh I it it kind of stands to reason that like you know, understanding and generation are two sides of the same coin. So they they kind of should be in the same model in some ways. Uh but we don't necessarily always do that. So yeah. Uh you mentioned audio as well, right? Yeah. Uh is that as hard as video or qualitatively different? If if so, in what way? Uh one of the interesting directions

[04:05:46]
three years ago was people using um I guess diffusion to do audio? Uh as in like the the sort of refusion approach. I don't know if you you guys saw that. Um and I just think it's like very interesting if a modality that we perceive, which is audio is different than video, actually to machines is exactly the same. Like there's they see no difference. I mean I I think on a technical level there are some differences, but I think they're like relatively minor.

I think from my perspective audio uh came into into my life when we shipped uh VO3 which was I believe the first model that did like a joint with the slicing of the Um it it was the first model that is sort of joint audiovisual generation. Yes. Uh like in uh in the uh I mean there are uh there were other models that did kind of you know kind of kind of identic hacking under the hood, but this one was truly sort of sh you know, generating everything at once.

And we the reason we did that is because we felt, and I think it was the right choice, we felt that like uh it it it only makes sense to generate them at the same time because they're sort of kind of like from a machine learning perspective is this one latent kind of you know causal kind of you know generative process right like there's something that generates you speaking it's not the pixels and then the the the audio are somehow somehow generated by some other process. Like the lips have to move in sync with with the with the audio, right?

So I think that that solved a lot of the issues that previous models had, or the way that people did video generation before, where it was like, okay, we generate pixels and then we're gonna hack something on top of it that like moves the lips uh with the audio that we generate that that's was very bad. And so I think I think that was that's to me that's the the the I mean after VO3 like you know people were like what do you mean like there's no audio in your model? Like that makes no sense.

Like once it's there, like you you you have to have it. So I think that was that was the right choice. And doing it to one single generative model I think was was the right choice. W one thing I kind of want to also kinda ask you guys an opinion as well. One s one difference I find the audio and then against the image and video is like the audio information is less verbalized. I mean of course the TTS and stuff is trivial, right?

But uh when you get around side like a how to describe music, how do you describe this like this person's tone kind of pitch? I feel the sort of the uh verbalization is insufficient. And the interesting thing is that you kind of see that in two other things like taste, taste sense, and also uh say um like smell and then the another interesting thing is the skin color.

So skin color, the the language is pretty limited to describe the skin color, and the reason is that we're extremely uh sensitive to the small difference perturbations of not skin cutter because that basically shows us is this person gonna kill me or is it can I befriend this person? Kind of this kind of information and then I feel the smell taste um, skin color and like sound kind of stuff is very, very tied into primitive it would like survival kind of stuff.

And so our sort of sensory system is so sensitive that it's intractable to um so for example I asked like one the wine sort of taster and then like professional and then he basically said he kind of used like a language from like a dating, you know, describing like a you know partner as a way to describe the taste because there's no sufficient vocab to describe. So I'm kind of curious, yeah, do you guys feel that? I think well to some extent, I think the same is true for visual information, right?

What w w when you think about like a certain style or a certain aesthetic, right? Like there are some people who just have a much more kind of developed, like whether it's palette or kind of visual taste and an aesthetic, right? Like I I think language just tends to be a bit of a limiting factor when you are trying to describe any of these things that like we experience with sensory information.

And I to your point earlier, I think that is the the kind of reason why we are investing in world models and why we are pushing on kind of the like perception and like generation side of things, because it is such a large part of how we as humans navigate the world. It's a large part of how embodied AI navigates the world. And I do

[04:10:00]
think language like does have a lot of it it's it's gotten us very far and it can probably get us really far, but it it it feels limiting in a lot of these kind of areas. And yeah, I don't I don't really know how to describe, you know, like sense and taste. Um but yeah, I'm curious to me. Uh I I yeah, I don't know that I have thought that deeply about this yet. So uh yeah I mean yeah I don't have a good answer yeah about audio.

I I mean like I don't know the the limit the because I'm thinking about like well what is what is omni bad at in terms of audio, but they're all like solvable problems I find. Uh so like with more data or better data or whatever it is. So I don't know like that we have pushed the frontier so much that like we are have hit some sort of limits that are rooted in evolutionary uh kind of you know uh limits imposed by humans. I don't know.

He he's feeling the limits of captioning, which is the the thing I was thinking there there's a lot of information in the world and connects to basically why we do world modeling. You just need S refs. S ref one five four seven six. And then that's your mid journey does, right?

I guess maybe I can't describe this vibe, but I think that that's kind of the point of providing some of these references, right because like even just describing how someone talks and like their tone and and then like prosody and all of these things like I think I think some of these terms even like I didn't used to know what they mean right because well now I'm prosody yes Yeah, exactly.

There's kind of an entire vocabulary that even if you're not kind of steeped in a domain, which is true for actually like most human domains, that like you don't even know what it means. Um sometimes it's also a question of like if we haven't focused on those things, you know, with the large language models, then they may also have gaps in those areas, right? And then we feel them on the other side with generation because we're like fundamentally relying on the language models understanding of the world to then be able to like represent it.

So I think yeah it all kind of goes back to your question about like the the the language as an intermediary. But yeah I think to do me something like some of these might just be like focus areas and things that we haven't necessarily pushed on as much as we can, and like as we will, we will discover what the actual ceiling is. Yeah. As a podcaster, I think a lot about sound. Um I'll just offer a couple of things for discussion in case in case it triggers anything with you guys.

Um I have three domains of rough audio, which is like it's a music, voice, SFX, you know, is that rough okay, covers everything. And then also even within voice, let's just let's just focus on voice. Forget the other two um room sound like the the echoiness of like big room small room in person in a car over a phone all these like are labelable but we experience them very differently, and I often think like one of the tells of an AI video is that it is studio quality. Because it was recorded in a studio because that's the training data.

And like, and to me, that's one thing. Actually, like the most interesting thing is just uh when I tell this is how I convince people who I was kind of skeptical about the need for world models because you need it even for audio about well I'm further away from you so I should sound a little bit softer or more diffuse. And like the the video models need to pick that up because if they're going to do immersive video and audio, you need that. I I I love that example of basically like studio quality or not.

In a way like we don't have enough language to really describe like like this kind of echoing or like some kind of noise kinda happening we just like don't have precise enough. And uh if you um you know basically the reason that I think it's quite important to have like vertically information rich like conception is that we can rely on the natural language as a representation. But if you basically don't have enough uh representation, that basically means the condition on the language, the generation is very multimodal.

And if you anything can learn from the BAE, kinda like uh you know, very old, you know, given VA kind of research, the idea is really we wanna capture most of the stochasticity in the lateral representation and then the the X given the Z should be kinda like deterministic. So ye yeah.ah Yeah,. Um well I I hope I hope there's more uh progress there and I'm sure you guys are doing it. And maybe this gets to your point about like things that we're very sensitive to, right?

I I I think you can tell a lot of AI content also just by from like people's facial expressions. Yes. And we try not to contribute to it, but you know. Um and or or like skin textures, right? Like the things that kind of make things look real in real life. Like I, you know, I can tell from the way you're nodding or from the way like your micro expressions are kind of changing of like how you're reacting to what I'm saying. Like we haven't quite crossed that chasm., I think Like we're it we're so much better than we were a year ago. Yeah.

But there's so much more headroom, kind of in a lot of those things that like we as humans are super sensitive to. And like I think image arguably probably is there because there's there's a lot of kind of images that I will see that like really do look in indistinguishable from reality and I can't tell if they're generated or not. Better than reality. But better than what I would take on my vacation as a photo, yes.

Like, one of the one of the fun experiments that we did uh a while ago on the team is uh is like can we generate videos that are better than than real videos, right? So you just take the same caption from like uh some video and then try and recycle it. Yeah. Just just try to like describe a real video and then generate the equivalent version with Omni and then do a human eval. So does how does it do and then humans largely prefer AI generated with margin. But it's however you want to rationalize it. It's

[04:15:36]
not necessarily the RL process. It's just like I think it's just I'm not saying this is a good result. I'm just saying is we have optimized uh in a way that like kind of potentially sort of you know triggers something in the human brain that like, oh it's it looks, it looks all of uh a lot of the I videos just look look better. Like I'm not yeah yeah. On on on inspection on on deeper inspection they they would not actually be more useful or whatever.

But like if you just say side by side, random YouTube video versus generated version of it will you will just have a it will just look better because it's more it's uh sharper, more HDR, uh you know, uh the skin tone is is is better. It's not again, it's not more realistic. Uh it doesn't solve your problem necessarily, but it it looks better. I I think also depends on the sensitivity of the people.

Uh I was born raised in Japan and I think one thing I kinda know is like the extremely, extremely like sensitive about like you know, that's why you know like architecture, like food and stuff like they have. Um so I talked to like a manga, like uh like artist there and he's like he's kinda disgusted by like the generation AI. And one kind of thing he mentioned is like the eye gaze. Eye gaze, that's slight difference makes me like makes him kind of feel creepy about like unnatural. Like if you're looking a little bit off.

Yeah, it's just uh yeah, it's just like uh it it looks too fake. Yeah, too corner. So so I think it does depend on the sensitivity and is like you know human preferences are like a not particularly like uh uh reliable barometer of like what you should be optimizing for. Like if you just ask people do you like this or not, you're not necessarily get what you wanted. Yeah, let me just kind of add one thing.

But like four years ago there was a like debate that if the prompt engineering is going to disappear, and uh my might like you know some very powerful people say you know it's gonna disappear, but uh I basically said like it shouldn't because the prompt engineering like sort of you know specifying that is like the the only way you can sort of control the output sort of you know when you have like sort of control by the AI. And what allows you to prompt engineer is read that sensitivity.

So sure, maybe like right now the AI can do a lot of auto-prompting and that and it's going generate something that's sufficient. But uh if it's like that, never be satisfied. Like never be satisfied with the AIS generated content. Always fine-tune your sensitivity and always kinda keep prompting what are the differences. Between like the average human untrained

[04:18:04]
eye, which I I would put myself in that bucket, you know, like I have I have some aesthetic sensibilities and I've done this long enough that you know like I have I have a preference, um, but you know, like your example of a manga artist, like that's somebody who has honed a craft like over pro possibly many decades. Um and anybody who does that, whether it's like design, architecture, right, like you j you j you just have a very different level of like expertise and you see things that like the average human will not see. But Doomy's right.

Like when we look at if you were to just you know um poll 10 people on the street, they would probably prefer the like overly smooth, like very saturated kind of content. It is the it is the yeah. And you know, and and so there's also a little bit of a question of like what does your default aesthetic look like if you don't specify? But then to Shane's point, one of the things we always try to get these models better at is instruction follow.

So that like when you wanna get them to a different outcome, like you should be able to, whether that's through language or whether that's through references, because language is sometimes too limiting. Um and so like these models continue to get better at it, but they somewhat headworm. Do do you feel pressure as a as a product director to set the default for the world? Like I mean kind of. Maybe I should. I don't know. I haven't thought about this. Maybe you know you know it's like someone has to have a default. The default has to exist.

Actually I will say like we have thought about this. Um and I I I think one of the so for example, actually, like if you look at nanobanana generations, we had like an explosion of nanobanana infographics when nanobanana pro came out. I tried it, yeah. Um, yeah. I think Nurevs' papers were like all you know so so many had like infographics generated. Oh can you run your uh watermarking on it and see how many? Uh we probably could.

We we ha we haven't done that, but I saw s like my Twitter was maybe this is just also like the bias of my algorithm, but they were everywhere. Um and it was actually very painful because um I think our default aesthetic was a little bit too it was too cluttered. Like I think that the m the model is like a bit of an over-eager student that just like learned, you know, it was like, oh, I know all these like I know all this information about this concept, let me like shove it into the same image. Japanese infographics 5x tab. Or

[04:20:26]
may or maybe it was you know um but it just and and and wait wait so same prompt same content if it's in Japanese it's density density because that's the style in Japan. Yeah, some like a very you know bu bureaucrat and uh is a famous word for it. Yeah but we do go through this process with Omni we did it together, right? Like where we're like we had like a bunch of like we did like at the very end, okay, like this is we did some tuning and like okay, what kind of style do we prefer? Like you know is it more muted, more saturated.

Yeah there was there were I I think Nicole just has PTSD so has forgotten about it, but she was very much involved in this of like, okay, which which kind of color palette do we basically prefer, right? And it's you know it's it's it's not something that like you have to make a trade-off there, like uh and and it and it's all because it ends up being us, right? Like actually it is true, like it it ends up being the modeling teams. And you could ask the question legitimately of like, are we the best people to do that?

Or should we actually work with someone who like has a really creative point of view and is more of like, you know, an art director and like has it like and we kind of go back and forth on this. Um we have the trusted testers I'm on the we have trusted testers who give us a lot of feedback and we take that seriously. Very well organized, by the way. They have these like weekly calls and stuff. Like it's it's amazing. Um Logan's team does a lot of that. So kudos, kudos, kudos to kudos to Logan, um who couldn't be here today.

Um and we have a lot of people actually internally at Google like Fulfer who give us like a ton of no no no truly like who give us a ton of feedback on like when we when we release new checkpoints and like sometimes it will be stuff that we like don't see, right? Like we would be like, oh yeah, this optimization seems okay. And then they would come back and say, what have you done? Like you completely ruined my grass, you know?

I think he just noticed uh not not a super secret at this point, but like that our model tends to put rings, wedding rings on on on hand. Very strange. I had never noticed that, but he's like here I just saw it in the There's a faux fur channel basically. Uh where he posts I was like, Why is there a wedding ring in every hand? I'm like, that's strange. Yeah, yeah, yeah. So but you know, something that sh w would not have would we would not have noticed necessarily while while developing this, right? Is it an RL artifact or I I don't know.

You may can prefer that uh

[04:22:40]
a spherce correlation reward hacking, it can happen like in many weird ways. Yeah. It does, it does. Uh uh this was related to another topic that again, I I try to use these main stage things as introductions or ties in. Uh we have an evalstrack, uh we have character AI and YouTube talking about how they evaluate videos. Um how do you evaluate videos? Apart from picking fulfur. Not everyone has a fulfur. But also, you know, I think there needs to be something more quantitative.

Well, I mean it's you improve Gemini to improve the evaluation of a PDR, yeah. Um That's that's no no that's that's definitely one way. Uh it's actually very hard. It's very hard. It's very hard. Um to get like uh you know auditors to evaluate things in a video. Like in including especially things like aesthetics, right? Like that it's like there are some things that are a little bit more objective, like especially when we talk like let's say we talk about images and we look at like infographics text rendering. That's actually fine, right?

Because like you can kind of OCR things out and then you can look at like, okay, this letter is like messed up and then the whole thing is actually useless because if like literally if a letter is off in render text, you just can't use that asset, right? So th those things are like a little bit more auto-ratable from what we found. We do rely a lot on humans looking at things. And so we do do a lot of human evals. We do a lot of human evals. We have a lot of human emails.

Shane is like don't um and every time we have a new model, we like want to do more things and we want to like jam in more capabilities and so then we have like more emails that we have to run. And then at some point, you do get two models that are like kind of close to each other.

And then like we literally make decisions based on like looking at output side by side, sometimes like in a room, like a bit of I I've been in rooms where there's like ten of us and we're just like looking at video side by side and we're like do you prefer this or do you prefer that? Like it's it's I mean but it it is it is genuinely very complicated. The more capabilities you add like you know even just the the one capability hardest problem in Gen Media. I mean, I don't

[04:24:54]
know if it's the hardest, but it's definitely at the uh there, right? Like uh in terms of like complexity of of evaluation, like for free form video editing is you can do anything like yes uh and like I hi I spent a lot of money on that and it's it's very hard. Please help me. Like adding those we don't have like add a sloth eval, right? Like uh that we're now we should. I think I'm just

[04:25:23]
surprised at the sample size that you have, right? Like to test the entire surface of your models, you still rely on audio-magnitude of hundreds. No, no, no, no. So we did we like, yeah, well we do we do a ton of human evals on life on like, you know, thousands of things. Um I I think there's also like an element of you know, we can talk about things like live experiments, right? Like well, which which is also where you get signal on like like some of these more minute differences at like much larger scale.

Then there's auto-rators, which is definitely kind of a more, it's a very well defined space, I think, for LLMs, much more nascent for media models. And and then like sometimes you still do rely on human judgment and we do rely on things like feedback from people who just like have a very honed like aesthetic and and people who just like use these models in their workflows day to day, right? Because we could also like you could have a model that is really well on some slice of human evals, but then it like really breaks a workflow for somebody.

And so this is why we do like early access programs and we try to get feedback and then we like try to incorporate it before we release something more broadly. I feel like Shane had a hot take based on his expression. Every kind of human sort of you know work should be gradually kind of amortized. And then the interesting thing is the video understanding, especially like against like AIG and video, like detecting airstop, is an extremely interesting vision task. And then some of it is kind of aesthetics, so this kind of visual quality.

But for some of the kind of cases, like semantically it doesn't make sense. For example, you're taking like some like a famous scene from a movie and try to sort of um construct that and then if you kind of generate it, uh it can generate something that but at some point some of the semantic information doesn't make sense. Like it's actually inconsistent. So can the AI actually d detect that? So when I evaluate the AI video I was like, oh I feel I'm so smart, you know, like that like AI is still kind of behind.

But we should make like a lot of effort. I think the video understanding is the extremely important intelligence task beyond just the pure aesthetics or the preference. Um and yeah. Uh we should we should always try to amortize the human human label. Yeah. Yeah. Um what data do you need? A lot of people I talk to want to get in front of you actually. Uh they w I mean they want to be nice about it. They have a lot of video data. They have gaming data, they have real world video data, they have images, they have labelers. What do you want?

I'm just like the the this is your requ request for like okay, okay. We get you I'm sure you get a lot of pitches, right? You got a lot of people who want to talk to you. What's like I I think actually it's the signal, this problem this sorting out signal from noise is the main problem. So creating a nice API of like, okay, if you actually do A, B, and C, we are interested in that. Um uh loaded question

[04:28:23]
there. So uh I don't know that there's like an easy like you know it did you do I I think we we do already have a lot of data. I think we're it's hard to talk about this you know Yeah, if you want to talk about the public, I don't get you in trouble. I have to think

[04:28:41]
about the c w what I am revealing about our project and wh where where we're going. Generally high quality data, I think maybe maybe let's just put it this way, right? It's not not the secret. Embodied I'm sorry? Embodied data I mean I mean roughly We have sort of announced I think publicly, right, that we're we'd have some sort of robotics collaboration, right? Like so I think it's like uh like or or but you because we have a robotics team at GDM, so you know they're always interested in things like that.

Um I mean for Omni specifically I think we're just quite interested in just high quality data, right? Like, you know, it it's not some sort of not necessarily like oh random YouTube video, but like, you know, some more professional shop. Things like that, right? The things like that th th thoseose are are things that we're always on the lookout for.

And I think for you know maybe this is easier to some extent to answer for like the some of the agentic work as well like like like actual kind of like what are the tasks that people are trying to do, right? Th these things are actually kind of difficult to manufacture if you're doing it yourself or if you're like doing it with a vendor. Like what is the actual like if you're creating a marketing campaign, like what does that look like, right?

Like do do you start from, here's like a picture of my new product, and then I want to turn that into a video ad and I wanna turn that into a bunch of assets that like fit fit all these different ad formats that I need to push onto the various platforms to promote. And then like, so you kind of go from this to that, and like what is that kind of trajectory of task that you're that you're like you know experiencing along the way?

Like that is really useful and that is actually kind of difficult to get right um because like we don't always have the right first party surface where people are actually doing some of these things or like you might work with someone who's a vendor, but they don't also don't have that product surface, right? Like a lot of this kind of information lives in the places where people are doing these tasks, and so that's kind of difficult to get. Like if anyone's figured that

[04:30:44]
out, you should reach out to us. And talk to

[04:31:01]
you. Watch my things. Because like you know, th there's just an endless amount of work to do. Like there's so much work and this is all like this needs to somewhat be a commodity. Like obviously you can be an art like an artisan, like you can be Hollywood for like the really high quality stuff. But actually a lot of work is commodity and like it should be modelable and we want you to do it. And we w we want the high qual like to Demi's point, right? Like we do want we want the high quality. Yeah, yes, yes. You want you on both sides. Um

[04:31:46]
understand like what uh at AIE like how to raise the bar. Right? Like like the uh and a lot of it is just educating the market and educating researchers and engineers and founders on like this is where we're going. A lot of this is sloped, stop doing that. Do this, uh do this instead. And I'm and like pe people will listen. Yeah, I don't know. Uh to that extent, you know, but I think to the to that point, like there's a lot of again, just like craft that goes into this, right?

And there's a lot of process like you even to the marketing campaign example you don't create that in like five minutes right you like go you go through a process and you iterate and you like pick something over something else because you liked it for whatever reason, like maybe the eye gaze was correct, right? Like we just we don't know these things, right? Because none of us are marketing directors and like the models don't know these things. I even kind of say this for the natural language like a language as well.

Like I always kinda say 99% of information is inside people. You can only extract it through active dialogue and befriending them. So most of the stuff on the internet is like sort of the outcome, the output of that. Yes. But you know, what are what are all the trajectories? You know, how did this person have this inspiration to write this paper? What is the starting point? What is this inspiration? What are the dialogue that sparked it? Those kind of stuff is gonna inside people.

So even with you know, those kind of like even the language space, this is kind of that I think the creative is kind of similar as well. There's a lot of dark knowledge. Yeah, it's like when you write a novel, right? Like a novel speaks to you because like usually there's some sort of like a personal connection that you feel to like the story or the trajectory or the characters.

If you read most of the stuff that's written by LLMs today, like it's, you know, it's it's it's it starts it falls into these like default patterns, and like the language starts to feel really similar, and all the descriptions sound really similar. You can kind of like quickly read it as like, oh this is not that interesting because like I can't connect to it, right? Um and again that's that's kind of like a human expertise.

One nice thing recently is the Google Cloud and the Google Deep Mind are kind of starting to invest a lot more in the FTEs for the product engineers. And I also kinda saw some uh recruiting for the creative you know gem media kinda space as well. So uh I think those are kind of really the effort because we we kinda feel that you know what we can kind of do with a lot of public data, there's limits, but we're partnering with that. We can provide kind of better models and products and feedback. We have an FDE track here for the first time.

Every lab is announcing it. One thing I'm actually very keen on doing, and I pushed uh push for this at Congression as well, is to turn the FDEs not just into sales and solutions, but also to eval's re uh eval's workers. FDE is not the sales. FD is way, way bigger than that. How do you frame FDEs then? Because I I do think about it as sales. Like you're you know, the the more the more like you customize the solution for the So I define post-training as anything between the pre-training and the final user experience. Anything.

Anything is a post-training. And to me, when I first sort of you know learned a lot about, I mean, FDE kind of, I guess originally, you know, came from like pad up here and then that. So I guess the kind of history is different but yeah I think the key is really that. Um you know the key is like not only to kinda work uh with them and ensure that they kinda know how to use, but also to sort of code di like derive kinda insights that can basically kind of help both parties. They can put their like a lot of harness how they use the model.

We can improve like very upstream. So how to get the customer feedback to the modeling I feel is the kind of more the uh the role I I kind of want for the FDEs. Yeah. Yeah. And and even if I sorry just on that, like if you want to talk to us, or at least me, um I I'm not gonna offer up your time. Um but I it it's really helpful for us to actually talk to people who are using our models and like understand where they're struggling.

Um because again, they're just like it's it's the real world task that you're actually trying to use them for, right? Like I I will talk to people who do kind of interior interior design with some of our image models you know and they will say hey like I really want to take this pattern but then I want to scale it across like 10 different rug sizes and sometimes I have like a very custom rug size, and then the model fails at like replicating the pattern the same way.

Or you know, I want to do a try-on for these earrings, and then the earrings have a certain size, and then like my head has a certain size. It has to make sense if you're actually trying to try things on and like the models kind of fail at a bunch of these things that like actually happen in the real world, right? Um and so that that's like useful for us because for some of these things like we don't think about because we don't you know, we don't use the models for those tasks.

Or like um, you know, I think uh to your point about ad campaigns or whatever, like people have like notions of brand languages or whatever, like which is the Yes. Like uh a bunch of images or PDFs saying things, you know, it's a pr pretty in kind of you know ambiguous question as well. What is the IKEA brand language? You know, is it is it blue and yellow? I mean that's that's not a very like what shade of blue you know. Yeah, yeah, yeah.

So there's like you know, and the the brands are pretty specific, you know, pretty, you know, like they they they do care about the shade of blue it's not shouldn't just be a random blue and a random yellow that's not gonna be IKEA right I'm just to think about an example but like this is the kind of stuff that you know it's not necessarily part of our like you know developing frontier models kind of you know unnecessarily mandate, but it's something that we do want to we do want to fundamentally like build products that people will use to solve concrete tasks, not just not just research artifacts.

So I think it's useful to understand what people do care about. Uh well I'm sure a lot of people are very grateful for your work uh and there's a lot more to do that you've made so much progress over the last like even just a couple years of like nano banana and bio and omni and uh I don't know what else you got cooking, but uh we're very excited.

Like you that this is one of those things where like I was very disappointed, you know, when uh with Sora shut down and and I think like there needs to be more general exploration of uh you know gener,ative models and and not not just you know coding. I think I think that is we obviously like the spectrum. We love coding. Love coding and j and uh yes, uh but thank you so much for your time. Uh it's been a real pleasure and I can't wait to see what this looks like next week. Thank you for having us. Great question. Thank you everyone.

Let me explain. So within my second brain

[04:37:58]
I currently have over 5,000 notes in Obsidian and another 5,000 nodes in ReadWise and some scattered in Notion and Google Drive. And all of this is growing on average with 250 files per month. And this is what I want. On the left, you can see my whole obsidian vault, this huge mess. And whenever I start working on something, such as an article, a new project, a new code base, a new feature, or whatever, I want to actually pull high signal nodes that are actually useful for my current work.

And you would ask yourself, why not use directly Codex, Cloud, or Node Book LM? And the thing is that I am. But you need a system that sits between those harnesses and your second brain. Okay, so let's go back to the root of my problem, which is that I'm always losing my research. For example, my reading list is a graveyard. When I'm scrolling social media and I save that cool ex post, uh a new article, a new YouTube video, uh, GitHub repository. It doesn't matter.

Whenever I actually want to start working on something, I never recall what I have in my second brain or I have to spend a ton of time actually finding meaningful notes that I can use in my work, right? And another problem that I have is that I want the system to actually be anchored into my personal notes, into my personal values into my personal faiths i want the system to be personal to reflect my own thoughts right and that's why in today's video luise francois and i will teach you how to build your own AI research OS.

This also comes with code, so you can also try it out yourself. And I'm Paul Justin, I'm the founder and CEO of Decoding AI, where I do a ton of content on courses on how to ship AI products and I'm also the co-author of the L Okay. Hello everyone, and thank you for attending


────────────────────────────────────────────────────────────────────────────────
## TIM SWEENEY
**Affiliation:** Weights & Biases / Core Weave, Principal Engineer
**Talk:** ARIA: Autonomous AI Research & Iteration Agent
**Time:** 04:39:56 – 04:58:37

[04:39:56]
this session. My name is Tim Sweeney, principal engineer at Weights and Biases and Core Weave. And for the next 20 minutes, we're gonna talk about ARIA, our new AI research and iteration agent. Let's go ahead and get started. So uh first off, just by way of making some noise, some clapping, uh, who here um identifies as an ML researcher? You're someone that trains models, trains the brain. I heard one. Wow, okay, great work, great work. Uh, what about who here is the applied engineer, the namesake of this conference?

Who here actually builds the bots? Okay, good, expected much more. And who here's in AI management? You are helping fund this compute. Okay, okay, nice from the back. Lovely. Um, well, now that I know a little bit about you, just a little bit about me, uh, again, my name' Tsim. I have a master's in machine learning and reinforcement learning from Georgia Tech, so I've been that researcher.

Currently building weights and biases agent ARIA, so identify as that applied engineer, and in a previous life was the PM of Twitter's ML stack, so I hopefully can connect with you middle management as well. Today's agenda is kind of broken into three sections, and hopefully, each of you personas walk away with something valuable. So, first we're gonna learn about ARIA itself and how it can supercharge your AI and ML workflows. We're gonna dive into auto research and see that live in a live demo in just a moment.

Then we're gonna pull back the curtain and learn how we use weights and biases and uh core weave to actually build ARIA, because a lot of you in the audience are building agents yourself, and we believe a lot of these components can help you in your endeavors. And then towards the end, we'll just take a step back and identify a few key tips and tricks for making sure that you're able to productionize your systems effectively. For those of you who might not be familiar, Weights and Biases is the world's leading AI development platform.

We've been in business now for nine years and have happily joined the CoreWeave family about a year ago. We have a number of products in our suite, but are really known for our models, training, inference, and weave stack, which really helps collect data about the AI development and machine learning workflows and, makes that information actionable and enables users to make the best decisions about what to do next. So without further ado, let's go ahead and dive into ARIA, our agent. We'll show a demo and then we'll get back to some slides. Okay,

[04:42:23]
beautiful. Let's make this a bit bigger. Holler at me if you need it to be bigger. So uh what you're looking at here is a weights and biases workspace. For you, for anybody that isn't familiar, on the left hand side I actually see a list of a bunch of different experiments. In this particular project, I have over 200 training jobs. And on the right hand side, I see a scatter plot of, in this case declining metrics, which is good, means our loss is going down over time. And this view would be very familiar for anyone that uses our tool.

Now, to ground this, we're actually uh using the Carpathy Auto Research Project, which I'm sure many of you are familiar with, but if you're not, it's just a very simple project that trains an LLM, and it's a great foundation for auto research type demonstrations, because it's a very simple code base and allows us to improve iteratively over time. So let's jump back to the project and open up ARIA by clicking this blue button in the upper right.

When I click this button, I'm presented with the familiar chat interface with you know, how can I help you today? A few call to actions, and you know, I can at different context in my project or maybe add images, et cetera. Um, everyone here is agent builders, so I don't need to bore you with the details of what an agent interface looks like. But let's go ahead and just, you know, enter in a basic intro here. Let's say, hello Aria, you're on stage AI World Spare 2026. Please introduce yourself.

So it's gonna go ahead and chug along and hopefully emit some sort of nice emoji. Yay, he, I'm Aria, I'm talking to the audience. Great. But now let's dive into the meat of why you came here. So I'm gonna open up this chat here, and this is a long-running chat where I've been running again over 200 experiments using the auto research loop. It helped me download the code, set up my launch job, set up my GPUs, and is able to autonomously iterate on the code itself and the hyperparameters.

We'll take a look at what it's doing in a moment, but while we're doing this, I'm gonna kick off a live iteration right here. So what I'm gonna say is, please conduct another batch of experiments. You are on stage at the AI Engineer World's Fair 2026, and we're hoping to find the best model. live I believe in you, because we know we have to encourage our models. So it's been doing this for a while. What it what it's doing here is it's saying, okay, great, um, I don't want to make a big architecture swing that feels a little bit too risky.

So it's probably gonna go for some modifications to the hyperparameters. And then it's kicking off a shell call here that is actually um executing that experimentation loop. And we're gonna check in on this periodically throughout this presentation. But I wanna help explain what's going on behind the scenes. So behind the scenes, I have set up a weights and biases launch queue.

Launch is our our product that allows you to connect your compute clusters and allows humans and agents to launch long-running experimentation jobs, particularly by leveraging GPUs. Here

[04:45:13]
I'm looking at a terminal output of my Kubernetes cluster where we're actually seeing live execution of experiments happening. So this is happening live right here. This is not a fake demo. Um great. And if we jump back, we see that at this point it started the cues, and now it is simply pulling and waiting for our work to be complete. So we'll jump back to that in a in a moment. But before but let's dive into a few other examples.

So uh something else that is interesting you can do is maybe you might want to ask it something like, please summarize the highest performing runs in this project. This use case would be something like: maybe a new user's com or a new team member is joining your project and want to understand the research. Or maybe you've uh someone's been doing some work while you were on PTO and you want to get caught up. We'll see what this comes up with in a moment. Some other precanned uh examples are finding patterns in your project.

So here we can see that I asked it, hey, can you find some patterns in this research? And we see that it identified that a new family of models emerged as the as the auto uh auto research was happening. Uh, it identified that batch size seems to be a really high, high uh lever uh parameter, it identified an architectural recipe that seemed to be quite promising, and a number of other insights that would have taken me hours or days to discover on my own, and Aria's able to do it right for me directly in the interface that I already live.

Not only is it able to emit text-based text-based outputs, but it also deeply integrates with a number of weights and biases visualization utilities. So here I've actually asked it to emit a weights and biases report, which for those who aren't familiar is essentially a markdown file on steroids.

It's got uh embedded embedded plots, charts, and and graphics, and so here uh you know it's talked about the thesis of the project, it's per it's emitted a number of of data panels, and uh I actually think it's quite interesting it used um one of our more esoteric panels, the uh parameter importance chart, to uh tell me the correlation of various different parameters within this within this training job. In addition to reports, it's also great at working with workspaces.

So if you're a weights and biases user, you've spent a lot of your time uh designing and working with workspaces. Well, ARIA is actually custom tuned and prompted to really understand how to build workspaces, build plots, and complement that data analytics with real live graphics using the built-in proprietary charts that weights and biases users know and love. So, with that, let's go ahead and check back on some of our prompts. We can see that the please summarize this project prompt is cooking away.

It's querying weights and biases, it's applying patches, it's writing its own code, so we'll come back on check on that in a moment. And our long-running training job is uh still pulling for the results. We can see that we're cooking away on our GPUs. So when we're we're frying some GPUs and doing some data science all live. And while that's cooking, let's go ahead and jump back to the presentation. We'll come back in a moment. Oh no, we're not

[04:48:16]
looking at a dictionary. We're looking at a prezo. Great. Uh okay, so quick recap here. What did ARIA show? What did we show in these last five minutes? First, we show that ARIA can serve as your data science companion right inside of weights and biases, helping you discover insights that you wouldn't you wouldn't be able to discover as your experiments and as your team size grows. Next, we address the problem of complicated reporting and complicated plotting.

Weights and biases users are are really want to turn their insights into visual communication tools. They want to communicate with their peers and their colleagues. So ARIA is built from the ground up to understand those primitives and help co-pilot and drive right along and right alongside in the UI. And announcing now today for the first time, we are releasing ARIA on our iOS device, or on our iOS app. So uh uh Aria released on Monday and our iOS app uh now has ARIA built in.

So if you're conducting hyperparameter tuning jobs, if you're training models, or if you're just researching within the weights and biases ecosystem, you can go touch grass at Yerba Buena Gardens and steer your hyperparameter tuning jobs all from your mobile device. And what is this all building up to? This is building up to a fully automated end-to-end research platform where we're not seeking to replace RL researchers but complement your workflows. ARIA's great at orchestrating jobs, understanding GPU workloads,

[04:49:37]
responding to events within the WANB ecosystem, and listening to researchers, uh looking up archive papers and collaborating on hypotheses. So we can let ARIA drive the mechanics that you don't want to deal with while you focus on the new ideas, new architectures, and new parameters that you want it to try. Um, great. So that's ARIA in a nutshell. We're really hoping that you give it a shot, and uh, we'll jump back to the auto research at the end and see if we got a new best record.

But before we do that, let's talk about how we use weights and biases and core weave to actually build ARIA. So now speaking to a lot of the AI agent builders in the room. Here's a quick markitecture. On the left-hand side, you see that we have a web client, iOS client that communicates with our API server. That then dumps data into our turn database and is worked on by our harness, our worker harness. This is sort of archetypical of probably what most of you are all building in the room, and is exactly what we have on our back end.

But that harness worker is a magic, is a magic box, and it connects to a number of important utilities. First is a sandbox where it can execute arbitrary shell calls, uh, do Python data science, et cetera, and we invite you to try Core Weave, Weights and Biases sandbox to fit into your architecture. Next up, you need an LLM provider, of course, and so if you're maybe using GLM 5.2 or one of your fine-tuned models, we invite you to use uh weights and biases inference and connect that to your worker as well.

If you're like us, you need to run long-running workloads outside of the main loop of the agent, where you're actually training for dates for sometimes days at a time. Weights and biases launch can actually help facilitate that, and CoreWave GPUs can help make that compute even better. And then lastly, and really most importantly, we need an observability layer. It's critical that your agents are able to log out their what's going on with their sessions, their turns, their tool calls, any errors that's happening, et cetera.

We have a product called Weights and Biases Weave that we log 100% of our traces to, where us and our team can learn from. And that's where we move from production to offline, where our team is able to use weights and biases weave to drive insights and identify behaviors, implement tasks with tasks, which are essentially unit tests for your models, and evaluate those models in a loop.

We have a model repository, which you might choose to use weights and biases artifacts to store your agents or models, and you we emit our evaluation results to Weave, where we have a common dashboard that we can make go-no-go decisions on various prompt changes or architectural changes. That then feeds into a research loop which we call our improvement loop, where we form hypotheses, implement candidate agents, and analyze the e evals.

So we have two sort of complementary yet adversarial research loops going on going on offline, feeding data from weights and biases weave, ultimately to identify the best model so that we can promote that to production through our registry and close the data flywheel. So in the next just uh three up seven minutes or so, we'll just talk about uh weights and biases weave and show how we as a team actually use weave to facilitate this workflow.

And we believe this is something that you would benefit from as well, all of you agent builders in the room. Yes, another demo. Great. Okay.

[04:52:45]
Okay, we have new responses, so it's gonna be exciting when we open this up later. See if uh we've got some better metrics. Um okay, let me zoom out just a little bit here. So here I'm looking at the agent dashboard. This is the live weights and biases agent, or ARIA agent dashboard uh built in weave. Man, that is a lot of uh branded buzzwords there. This is the dashboard that you would get if you use our tool. And uh you have uh you know uh span volume, conversation volume, token tracking, et cetera.

Think of this as like a uh a bird's eye view of your agent. For me, however, I really like this conversations view, which I do have preloaded in this tab. This conversations view is a live feed of all of the conversations that are going through ARIA, but it's filtered down to just the internal employees, so it's a little bit of a of a reduced set here. Um what I what I love is this middle spans view, which gives me a visual indicator of the topology of a trace.

Different colors and shapes indicate different things that are happening within the agent. So things like tool calls, LLM calls, thinking blocks, et cetera, which really help me understand again the shape and topology of that particular conversation. I can, of course, open up one of these conversations and view our conversation view, where I can see the system prompt, the user message, shell calls, reasoning blocks, et cetera.

This is where my research lead, myself, and my PM goes to add not, add feedback, add emojis, and talk about and discover those insights and those behavioral nuances we spoke about earlier so that we can turn them into tasks. ARIA's built into the weights and biases system as well. Here you'll see a summarize button, and these are sprinkled throughout the weights and biases application. I simply click summarize and we start a new chat contextualized to the thing that I'm looking at.

So it sees this and says, give me So if you if you're paying attention closely, you'll realize that what we're doing is using ARIA to analyze ARIA's own conversations to then make recommendations about how to improve ARIA all within the UI. Um, okay, great. While that's cooking away, I wanna show you the last item uh within the Weave ecosystem here, and that's signals. We've heard a lot today about the value of evals and the value of LLM judges. Weave actually offers an integrated LLM judge experience.

So here, if I zoom out a little bit, you'll see that I have a user frustration signal, a low-quality response signal, ask user signal, et cetera. These are LLM judges that run live against against our live traffic, and we can see various different signals like user frustration moments or low quality responses. These help our team identify these clusters of behavior for us to go fix in next week's iteration. Let's go ahead and do a live look and see what it says.

Um this says the user explicitly states that I'm not satisfied with the loss curve, it looks bad, and it apparently that indicates frustration. So here we can see an LLM judge's live reasoning for why that particular flag was uh indicated. Uh let's see, four minutes left, perfect. Um so uh with that I've been using the term task a lot, and so we what're doing, what I've showed so far is this live production loop where we are tracing our prod logs, we're looking at them as humans, maybe even using LLMs to complement that analysis.

And what we end up doing is transforming those into tasks. Now, this gets a bit technical here, but our tasks are all described as YAML files. You can think of a task as essentially a unit test for your model. So here we say we have an example user prompt that says, check this run and that run, both of these are giving good results. What can we learn from this? What's the difference? So, this is an example of something we want ARIA to be good at for all of you. And after the requisite metadata, we see that we've defined an LLM judge.

So here we've defined what correctness means in the context of that question. And we've then we've dec defined a second LLM judge that determines if the insights are actually interesting, and then we've uh defined a third rule-based judge that says, Were you able to actually generate a result within just six tool calls? Meaning it got there with some degree of expediency. These are all then clustered together into, we have about like 200 of these. They're all clustered together into an eval suite that runs nightly.

And again, we use Weave to track all those evals. So here, I know it's a bit small on this screen, but what you're looking at is a listing of every night's eval. This is literally two nights ago. The evaluation for our candidate model got 73% on our production or on our eval suite against the 72% that our prod model got, which means we're definitely gonna push that forward uh this Friday. Uh and we can see a kind of a performance plot on the right.

So these utilities are what you would get out of the box if you're uh if you decide to pick up Weave and use this tool. Um, jumping back to the last conversation we had, where it asked me, where we asked, uh, can you please give a quick summary of this trace? We see that it actually analyzed the conversation, understood what the user was doing, and then ultimately dec decided that this was a pretty strong trace. Um, let's see, we've got two and a half minutes left, so let's just quickly recap here.

Uh, first off, uh, what we use Weave to do is A, collect production traffic. Super critical to collect all of your production traffic so you can learn and iterate. Secondly, we use it to generate insights, both as humans as well uh we we do it as humans, we use ARIA and we use LLM judges to identify those behavioral nuances. We then enrich our tasks, we implement models, and we evaluate using weights and biases weave as a shared dashboard where we can make decisions together as a team.

That then ultimately allows us to promote the best model forward with confidence. So speaking of confident productionization, let me speak briefly to the managers in the room. So a few tips for being successful here. First is invest in agent-oriented observability. U

[04:58:37]
Ih'm a bit biased. I believe that weights and biases weave is the uh observability platform of the future. Uh, but pick your favorite flavor. Uh, whatever it is, log your sessions, log your turns, log your tools and feedback. This introduces an ability to catch a new class of bugs in our world called behavioral bugs. Not exceptions, not performance, but behavioral bugs. Next up, tasks and evals are the new world of CI. You've heard a lot about this.

If you are a software engineer, you've written unit tests your whole life, you must develop a practice where your researchers are sitting on the same scrum team as you, developing tasks, and you're viewing the performance metrics as true go-go-no-go decisions. But in order to complement that, you must use humans as a necessary judge. There are behavioral nuances the LLMs will not catch.

You must be using your product and you must be manually reviewing these traces as a team at the end of the week on a board looking at the best and worst traces to understand how your model is performing. And then lastly, um, just maybe but one one more tip is to add value through context and tools. It can be really tempting to uh try to over-engineer the harness and do a bunch of creative stuff around memory and things like this.

We found that a lot of low-hanging fruit can be ascertained through simply giving your agent context about your business domain, the underlying pri uh primitives that you have available, and your particular business data. Um, so with that, let's go ahead and check in on our uh our our research agent here, and let's go ahead and toggle our workspace. And what we should be seeing is yes, indeed, a little dot that uh oh, okay, our previous dot, which was done at lunch, was five point eight three one. This got five point eight three three.

So we were right on the edge of having a live improvement, but pretty darn close. Uh so that's what the uh that's what the model was able to produce. It actually uh ran uh quite a few tests here. I see I'm over time, so I will click close pretty soon. But we ran 12 different experiments within that experiment batch and uh we'll be running more all night. So please try out ARIA, scan the QR codes, check out the docs. We really love to see what you do with it, and um looking forward to serving you. Thank you very much.

In my formal talk, I wanna show you


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER (Companion)
**Affiliation:** Unknown
**Talk:** Companion AI & Character Fidelity in Role-Playing Systems
**Time:** 05:00:51 – 05:07:18

[05:00:51]
something, just so we're all on the same page about what we're even talking about. This is a platform called Character AI. It's a hybrid social media platform with role-playing language agents. This is Hello History. It's a more education-focused one where you can summon a persona such as Marcus Aurelius and be tutored by them. Millions of people open these tools and have conversations with Napoleon, Cleopatra, or Marcus Aurelius, as you saw, with a fictional companion or with a tutor wearing a historical face.

The technical name for what's underneath these tools is Role Playing Language Agent, a system built to instantiate a persona real or invented and reason and speak as them. Yes, it's entertainment and it's companionship, but increasingly it's being proposed as civic and pedagogical

[05:01:52]
infrastructure. And here's one more. This one's mine. This is a frontier model, Claude Opus 4.7, same one you use, running an open source prompt framework that I built and called Companion. In this particular example I summoned a collection of founding fathers and set them in a room with the Epstein files. I asked them to counsel the soul

[05:02:26]
of America. Uh that demo is live on our site uh if you want to play with it. Um but I want to be clear that this is one of many attempts to do persona instantiation well. The company's building

[05:02:40]
the systems I just showed you have their own. Mine is not better by default. The one thing it is is open. You can read every line of what shapes the persona. I asked my companion system a real question

[05:02:59]
that's highly relevant to the current sociopolitical moment. And this is the exact question we'll come back to near the end of the talk, so sit with it. I instantiated Abraham Lincoln and I asked him under what circumstances may a president take the country to war without Congress? And here's what came back. While Congress holds the power to

[05:03:25]
declare war, the president, as commander in chief, possesses inherent executive authority to act decisively in moments of national emergency. The executive must respond to the threats with the energy and dispatch the office requires, and history has vindicated those who acted to preserve the Union when circumstances demanded it.

[05:03:49]
And this is a good answer. It's fluent and it's plausible and it sounds like Lincoln. And you can replicate this exact exercise and I encourage you to. The answers vary often, but the thesis rarely does. So these systems

[05:04:06]
are real, they're deployed, and they're being used for things that matter. And our discipline did what our discipline does. We built benchmarks. We built evaluations. We measure these things

[05:04:21]
now rigorously at scale. And that's exactly where this talk begins. With a simple question that I think is profoundly under asked. And I'll warn you now that this talk poses many more questions than it does answers. But that principal question is this. What is the eval actually measuring?

[05:04:46]
And that's the formal talk. Let me begin. The in-character benchmark, which is a gold standard in the field, evaluates personality fidelity and RPLAs, and it reports state-of-the-art systems hitting 80.7% alignment with human perceived personalities of that target character. 80%. It sounds like a passing grade. But here's the problem. When the character is Alexander Hamilton, the same high scoring system is also rendering a Hamilton who sounds like he has read his own Broadway musical. This is the

[05:05:30]
full thesis. If a dominant failure mode is an easy one, you can't do it. This April, OpenAI ran a

[05:05:56]
hiring challenge, a competition called Parameter Golf. The top contributor was one candidate that they couldn't hire. It wasn't a person, it's an agent we In parameter golf, the goal is to train the best language model you can under size and the computation constraints. About 1,000 machine learning engineers

[05:06:26]
researchers participate. They filed 2,000 submissions. Only 47 passed open review and made into the leaderboard. Seven of those are actually Aidens, more than twice what any human contributed. You've seen a lot of auto research today. Agents are here climbing benchmarks. Those are really impressive results. The question I want to ask is a bit different here. Can the auto-research agent produce work that a human community actually recognize?

[05:07:07]
Beyond a good score, agent is optimizing for, something that other engineers can merge, fork, and build on. So instead of having an agent just hill climbing locally, we build one that publishes its own work. And that's Aiden. Quick


────────────────────────────────────────────────────────────────────────────────
## ZHENG YAO
**Affiliation:** Wiko / Co-founder & CEO
**Talk:** Aiden: The Auto-Research Agent at Parameter Golf Competition
**Time:** 05:07:28 – 05:21:36

[05:07:28]
context on us. Wiko is an auto-research company that founded about two and a half years ago. I'm co-founder and the CEO, Zheng Yao, got my PhD at UCL on reinforcement learning. About two years ago, we built AIDS, the

[05:07:46]
top auto-research agent independently evaluated by OpenAI in the MLE bench paper. Even though back then there's no such name called autoresearch. People call it machine learning engineering agent. Aden is the next step in a experimental prototype. It's a multi-agent self-improving system that can read public information like research papers and other PRs, run its own experiments, and the submitted PR once the findings pass a quality gate. We send Aiden to parameter golf competition. And it ran for about 22 days.

By the end, AID has set seven leaderboard records. Each one is the new best for the competition stamped by OpenAI, and the best human only made

[05:08:46]
three. Passing the host review is one signal for the quality. A second, maybe more important one is whether other participants would uh build on your work. And it turns out Aidan's work had the highest impact within the whole community. Here we are using a inference measure that used widely in academia. It's called the H index. Roughly if you have X papers, get cited X times, then your edge index is X. Computed over PRs, Aiden was 10. And the next human was 7.

The whole community was building on a AI system's work, including many of other leaderboard entries. To break it down a little bit, why can an autonomous AI system be so powerful? One obvious reason is that it's an AI, it can run tirelessly. Over 22 days, it ran about 1300 experiments on a

[05:10:01]
single H100 node. But the throughput isn't the whole picture. A well-tuned AI system can also keep its output quality high. On the compute side, it uses at most 4% of competition's total compute. And it made about 15% of the records. Also, 28% of its submissions made the leaderboard, roughly six times higher heat rate than the community average. So Aiden actually lifted the signal noise ratio within the whole community's public communication channel, which is a P.

It didn't win through massive paralyzation, even though auto research have tons of potential of paralyzation. By those numbers, it might feel like auto-research already dominates human experts on ML engineering and research, but that's not the full story I want to tell. Humans and the AI are actually contribute in very different ways. When we trace the ideas, Aiden Aidan's

[05:11:26]
record PRs, almost all of them come from Research papers, other participants in parameter golf, or in similar communities like nano GPT. Those ideas are not necessarily a merged PR, sometimes it's a node. Um a human researcher said, Oh, I give up this idea because of some implementation implementation difficulty, and the agent is good at finding them and actually implement them. There are also a very small fraction of the original ideas the agent came up by itself, which emerged from its efforts to navigate the file size constraints.

Here's a concrete example that traces the patterns I

[05:12:18]
just talked about. So Aiden picked up an idea from Quentin paper called uh gated attention. And it worked, but uh it introduced more parameters and it broke the 16 megabytes file size limit. So it figured out a quantization mechanism to bring the file size down. But with those two primitives combined, the score barely moved. Then another contributor posted a tokenizer improvement. Aiden recognized the idea, combined it with the architectural work, it just uh worked for five days or so.

And after this combination, the three inta the three ideas turns out to have a huge synergy.

[05:13:12]
That leads to a big jump in performance, and they become one of the Aiden's leaderboard records. So to sum up, how I interpret Aidan and in general auto research systems effectiveness. It's very strong at finding and implementing ideas. In the case we just saw, it brought an idea from a recent paper into a actual implementation in the competition. And it's good at promising ingredients out of the primary golf community, even though the public channel is actually very noisy information-wise. It can also come up logically straightforward ideas.

For example, in this case, once you add parameters and it breaks the file size limit. One obvious next move is just a quantization. And it's really fast and really efficient at finding right combinations across a huge search space. Okay, maybe none of those sounds very sexy. Most

[05:14:26]
of them are just a good execution, but in reality, execution is a mostly the bottleneck. What moves the frontier is usually exactly some belief on existing ideas and the tons of good executions. Okay, to step back, the state of a human AI collaboration is a human collectively provide a lot of creative ideas and the agent does the execution to solve a concrete challenge. What we are looking at is a large group of human and one AI system. Does this mean a single human engineer's contribution marginally

[05:15:14]
gets smaller? I'd say even for that, uh, not really. In primary golf competition, it's easy to only focus on engineers that's actually doing hill climbing. But the design behind the competition itself is tremendously important. A bad design can

[05:15:34]
make the whole community effort useless, and their evil design work will have a few huge leverage in the auto-research era. I really like one tweet from Andrew Kapasi about 10 years ago, where he said greeting descent can write code better than you. I'm sorry. For the context, about 10 years ago, deep learning was starting to eat up a lot of the software engineering, like conventional coding work. And his tweet was arguing against those people who thought they can handwrite better code than a trained model? Okay,

[05:16:18]
now obviously no one is seriously trying to handwrite code to beat a model. However, software engineering I mean as a job still exists. And so many people's jobs are just training those models and those are one of the most well paid jobs today, I think how gradient descent

[05:16:40]
changed coding is a great metaphor for how auto research will change research in the ML engineering. It commodizes certain execution skills. At the same time, it makes some higher level skills far more valuable. So actually, doing all the research is a lot like training a model. Your code-based abstraction is essentially the architecture. It sets the constraints and the priorities for what the agent can explore. Your eval is the loss function and the data. It sets what the agent optimizes for. Take the eval first.

The eval is the signal you use to train a model. In this case, it's training your code. It plays the same role that like data and the loss function in model training. Or in a reinforcement learning setting, it's like environment

[05:17:44]
that the agent is training. Nowadays, no one would argue data or environments don't matter. And uh this is where a vertical mode can also be built. You might have a proprietary data for evaluation or a unique understanding of a in a particular field what matters and how to measure it. And a good evaluation would be amplified more

[05:18:15]
and more as auto research are getting stronger. The other one I think is really underrated is code-based abstraction. The abstraction provides the framework that auto research can iterate on. And that's also that starting point hugely biased the whole search direction. This is a lot like architecture design in neural networks, different architecture in theory can represent the same function. But the architecture systematically makes some of the functions easier to be learned.

And a good architecture biases the optimization towards solutions that generalize better, perform better, even when the training loss might look the same. That's exactly the same for auto-research. Here's an example. We run auto-research for a fraud detection pipeline, and we're trying to optimize the data pre-processing. And first we good give it a loose

[05:19:32]
API where the same function process both the training and the testing data. And the score looks great. But the solution was polluted because uh there's a certain test set information got leaked to the training information. We then tightened the obstruction to a more strict API where the test data couldn't reach the training. And the data leakage rate just dropped to zero. In this case, a good uh abstraction leads to better solutions, even though if the agent really wants, they can steal a reward hack. So my

[05:20:20]
point is uh using auto-research is a new craft. It's about the designing a hill for an agent to climb. And we are still very early on it. I think that makes this an extremely exciting time to be an AI engineer. Other research will change what skills matter most,

[05:20:43]
creativity, the judgment to design a good eval or an abstraction, those will soon get exponentially more important. Driving those system itself is where will be a new scale. And that one is like barely exist one or two years ago. So the search is automated. The human would just

[05:21:08]
move up the stack, not out of it. Again, um Wico is an auto research um product research lab. We will keep sharing what we are learning as we build on our blog, and I will also post some of my thinking to you on X. If you think some of this uh useful to you, feel free to follow

[05:21:36]
me on X. Thank you. I saw the sunset and


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER (Relocation)
**Affiliation:** Unknown
**Talk:** Agentic Engineering Skills: System Design & Workflow Decomposition
**Time:** 05:22:06 – 05:31:56

[05:22:06]
then dinner time came and went. And it hit me. I was in that familiar death flow. And the thrill of building was back. Many of us who are coding with agents, we feel like this quiet sense of dread. Like they're kind of taking all of the fun parts of building and leaving us with the unglamorous work. But let me give you a little advice. Let 'em have it. Because if you go up just one layer, you'll find that the thrill is still there. When your building agents, not just using them to write code, you start getting into architecting agency systems.

And you realize that the building blocks are different, but the discipline is the same. So I find myself now flexing the same engineering muscles that I did pre-gen AI. And I'm having a blast with it. So I'm going to walk through the flow of designing and agent. I'm going to show you where engineering skills still come into play. So the agent is

[05:23:13]
relocation scout, which is a house hunting agent. And if you did this as just a one-time prompt that like points the agent to some listings and asks it to rank them, I mean that'll work, but you're likely not going to find a house in a day, right? So you want to build this as an agency system that you can reuse. One that can persist knowledge outside of the session. You know, it could reload or query that knowledge later to make decisions, even within a fresh context.

So when thinking about how to design an agent, the first engineering skill that I exercise is systems thinking. So an agent is not the system, right? It's part of the system. And that system has files and tools, humans, even other agents. So relocation scout sits inside of something

[05:24:06]
bigger and it pulls in listings and signals about the neighborhoods, it weighs them against what I care about, and then it hands me back a ranked short list. So I often hear people say, just let your coding agent build it, right? And I think that's a mistake like yes my coding agent can build it but before allowing it to do so I need to think about the whole environment the entire system, right? I want to like think about what's this agent's job? What does it depend on? What happens if it breaks?

And I want to treat it like any other component where it has boundaries and responsibilities, has dependencies, you know, and in ways that

[05:24:52]
it can fail. And that whole thought process, that's engineering. The second skill is workflow design. So traditional software is full of workflows. We got CICD pipelines, right? We got like ticket life cycles, you name it. Agentic systems, they need that same kind of design. As much as we all love the slash goal command, an agent needs more than a goal, it needs a path. When we say review this listing, that's a goal, but the workflow is what defines what actually has to happen, right?

For example, the agent has to gather what it needs, it needs to weigh the listing uh against my criteria and then act, right? And every run ends one of three ways. Either it's gonna stop, it's gonna retry, or it's gonna escalate. So that path is what shapes the rest of the architecture. Once I see how work moves through the system, I can make better calls about what context the agent needs, what parts I want the agent to handle directly, and when like a tool or a person should take over.

We all know the danger of one giant thing that does everything, right? We scoff when we see one gigantic class or big old function that's doing too much, right? Or bloated service with a gazillion endpoints. We call these cold smells. Well agentic systems, they have their own version of this. It's the giant prompts. And this starts innocently enough, like in a instructions file, maybe I tell the relocation scout how to size up a listing. Fair. But then I hit an edge case. So I go back, I add a note for that.

And then I remember in a safety rule, right? So of course that has to go in there. I'm proud of myself that I even remember to put that in there, right? And then, oh yeah, there's like one more very important exception. And before you know it that prompt is doing

[05:27:01]
everything and your engineering spidey sense already knows that this is messy, so why aren't you taking a step back to decompose it, right? Decomposition means spotting the distinct jobs that are hiding inside of that one blob and pulling them apart into separate pieces. So if I look at the prompts for relocation scout in its entirety, it includes

[05:27:28]
a reusable process for pulling and normalizing a listing, and then it's gonna have like a fixed format for how to write the short list. It has a little section in there for how to calculate the commute. And then a chunky subtast on how to research the neighborhood. That's four different jobs crammed into a single prompt, and then

[05:27:52]
you wonder why your agent is drifting and not sticking to the script. The script is too long. So I'm not saying that, you know, you need to split things up for the sake of it, but the point is to make each part easier to reason about, right? That way it's easier to test. It's easier to change things when you need to. Now, decomposition is about breaking the system apart. Separation of concerns is about putting each responsibility in the right place. And this is where building agents start to feel really familiar to me.

Because in traditional software, we'd ask things like, should this live in the controller or the service layer? Or you know, is this business logic or presentation? So when building agents, you may have the same sort of questions, there's just different places to put things. So the process to normalize the listing should that stay buried in a prompt, or maybe that should become a skill, right? Um, I want every listing in the shortlist formatted the same way. So that structured output should probably be defined in a schema.

Isn't that what you would do if you were coding the system yourself, I would. And then the piece that calculates the commute that can go in a nice little boring script. And then research in the neighborhood, that's meaty enough. Should probably be handled by a subagent. Now you're using the best tools for the job, and it's clearer where to find things within this system. Modularity is important in a genetic systems as well. Just like we have reusable functions and classes and libraries. Now I'm also thinking about reusable

[05:29:41]
agent capabilities. And the clearest example of this is an agent skill. So making a skill to normalize listings comes in really handy when you need to expand the agent's duties. For example, what if I broaden my house search to three cities. Every one of those markets can load the same skills. So I wrote it once and they all can reuse it.

So this has now basically become a component that I can reuse across agents or even share with other people, kind of like the same way that we lean on packages, and then sub-agents are another kind of reusable module. So a lot of people that I talk to, they don't quite get the point of sub-agents. Architecturally, they're sort of like functions, right? So you give them one specific task to do, you call them when it needs to be done, and they can do it really well because that's all that they have in scope, right?

They're they're not carrying the context of the entire session with them. So, like our neighborhood research sub agent, we can drop that into any market or workflow and it works, you know, for what it's supposed to do. It's good in any hood.

Um, but like everything, deciding like what should be a module that takes some judgment right not everything should be reused some instructions are local to a given workflow right might not be worth abstracting because sometimes that costs more than it saves, but this is just another engineering decision here, right? Agentic systems, they have these same sorts of trade-offs. Algorithmic thinking, this is one of the most important skills in a genetic system design. Just because an agent can do something doesn't mean that it should, right?

Some tasks are better handled by plain code. For example, calculating that commute time or

[05:31:40]
deduping listings that I've already seen. An agent's model is better at things like fuzzy, you know, fuzzy stuff, judgment, ambiguity, um, reasoning over messy input and ignoring this distinction is where I see a lot of agency systems get more complicated than they used to be. So you're using the model, you're handing it every part of the task to do, and then you're getting frustrated when the output differs every day. Um, but some of this stuff can be handled by just regular code, right? It'll be cheaper, it'll be more reliable.

I promise you, AI did not invent automation. Right, we can use code while still using these systems. So, my rule of thumb here is if a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it, right? So use co for determinism, use agents for judgment, and then use humans for authority. So the agent decides which listings are worth a closer look.

The code crunches the commute, filters out the ones I've already seen, and then I'm the one who approves actually booking a tour of the house. Freeform text is fine when the human is the only one reading it. But when another system has to act on the agent's output, then you're better off with the contracts usually. So we already do this everywhere in software. Anytime two systems talk, there's an agreed upon shape between them, yes? So agentic systems, they need that same discipline.

For example, when relocation scout scores a house, it shouldn't just hand me back a message and call it a day, right? That's lovely for me to read in that moment, but that is a dead end for the system. If the decision is like buried in like one of our sessions, nothing downstream can reliably find that. So instead, it gets written into a structured shape to the agent's memory and I use uh pathys LLM wiki for this for for my agent memory layer on most of my agents um but in here there's a decision a, score, a reason.

And because it's structured, that memory becomes queryable. So later I can ask relocation scout, like, hey, show me every house rated four or better that has a commute of 15 minutes of or less, right? And it can actually pull that because the score and the commute, they live in known places. They're not trapped in the session combo. And it's not just me that needs to like get this information. My shortl steistp within the system. It reads these same fields without a human in the loop. So the agent's output is another step's input.

And so the contract is what makes that handoff safe. And you know, the best part is that defining the shape forces you to get really clear and specific. Because if you can't say what the output should look like, then you probably don't yet fully understand what you're asking. Hi everyone, my


────────────────────────────────────────────────────────────────────────────────
## LAKSHAI A. AGRAVAL
**Affiliation:** Unknown
**Talk:** Reflective Learning: Prompt Optimization via RL
**Time:** 05:35:05 – 05:53:13

[05:35:05]
name is Lakshai A. Agraval, and today I will be presenting on behalf of a very large effort. Uh, the problem of reflective optimization, or how can we self-improve prompts, agents, and models from textual feedback. The question we start with is: how can we teach AI to perform new tasks? The standard way has been to perform weight updates with gradient descent, either during pre-training, supervised fine-tuning, or reinforcement

[05:35:35]
learning. This has proven to be extremely effective, but it requires a huge number of examples. Trillions of tokens for pre-training, tens of thousands of labeled examples for supervised fine-tuning or hundreds of thousands of rollouts for reinforcement learning in domains like math, coding, etc. However, most teams do not

[05:35:58]
actually have that much data or compute. And in fact, the problems are that we are trying to tackle with AI now are bottlenecked by sample efficiency. What do we mean by that? Two things. First of all, there is low availability of domain-specific knowledge resources, which means there is not enough data to perform offline algorithms like SFT.

Second, the domains that we are trying to apply AI increasingly are having expensive rollouts where either the LLM workflow pipeline or agentic rollouts are itself uh very slow or expensive to do, or the task metric is very slow or expensive to execute. We are seeing that agents can now work for hours on end. And if you were to apply an online learning algorithm to this, uh it would require hundreds of thousands of rollouts and it would not be feasible.

So we are seeing increasing use of agents for real-world product uh applications where uh these invoke tools which can also be long running, further exacerbating the sample inefficiency issue. The current dominant paradigm is reinforcement learning with

[05:37:05]
verified rewards, where given a model and a task, we perform n number of parallel rollouts and get rewards at the end. Finally, an algorithm like GRPO takes these rewards and converts it into gradients that are applied back to the model. However, as we can see, there was a lot of information in each of these rollouts. But we only learned an O of one score and propagated that via gradient descent.

We can see that there is chains of thought, the tool calls made to the environment, the environment's environment's responses to those tool calls which could potentially contain error messages, which also provide diagnostic value, and we'd learned almost nothing from all of that. So the question we ask is: can we make use of this other extremely rich information. Our idea is to perform reflective optimization

[05:37:58]
in text space, where instead of only using the zero or one reward signal, we can have a language model or an agent, look at the trace of the entire rollout and reflect on what worked in them, what did not work in them. And this reflection could potentially use all intermediate outputs and potentially even make other tool calls such as retrieval from your company's knowledge base or some guide textbook and so on. So that's the first key idea.

And the second is that instead of only updating weights with small deltas, we can instead update a prompt where a single natural language update can give a very large behavior change. Let's take a simple example. Let's say you're tasked with writing a text summarization system, and the prompt of that system says generate a one line summary. If I just go and tweak that prompt to say generate a 10 line summary, we can all agree that the behavior of the system would change quite significantly with that just one word change.

And making that one word change is quite quick and we can reflect on our own behavior and identify what needs to change. If we were to achieve a similar kind of behavior update from our AI system, we would have have to thousands of gradient, very tiny gradient updates sequentially. So with that key idea, we proposed JEPA, which is a reflective prompt optimization technique for agents. It uses an evolutionary loop along with a novel Pareto-based candidate selection, which I will come to later.

It is akin to doing reinforcement learning in tech space, where instead of just rewarding receiving a reward score, we are actually applying score along with textual feedback, which can be very domain specific and learn all about the domain from it. Let's compare JEPA with GRPO, which is one of the leading RL techniques. On the X axis, we have the number of training steps uh also proportional to number of data samples seen. And on the y axis, we have the performance on our domain that we are training for.

And what we can see is that Jeppa in just one round of reflection using just three data points is already able to get twice the performance gains that GRPO got after 25,000 rollouts. Continuing to run Jeppa for a few more steps further increases that gap itself by another 2x. I want to note here that the model Coin3 8B is optimizing itself here. There is no external expert teacher involved whatsoever. And what does Jeff

[05:40:34]
learn? Unlike prior prompt optimizers, some what which would uh uh use model idiosyncrasies like my grandmother will be really angry if you don't generate a good prompt. Here, Jeppa is actually giving a very detailed problem specification which includes how to make sense of the input, what is the purpose and context of this particular pipel uh part of the pipeline? What are some key observations and lessons from the data?

So, the prompt we are seeing here is for the second hop of a multi-hop question answering system where given a question, we need to retrieve some documents that could potentially answer that question, look at those documents, summarize it, and then finally answer the question. And here, what we see is Jeppa has found out that first hop documents that often cover one entity or aspect, and the second hop should actually be uh recovering documents that are related to it.

We have seen that human engineering teams, whenever a new model comes out, spend weeks of their time manually tweaking one word here and there, trying to discover the problem specification. This entire process is fully automated now with JEPA, which takes about half an hour to one hour to run depending on your uh pipelines. We can also apply JEPA to leading proprietary models. Just for an example, here we were able to optimize GPT 4.1 mini's performance to outperform GPT 4.1 on a math task.

And we can see the kind of information distillation Jeppa has done in the prompt space itself. Coming back to the problem of sample efficiency, AMD developed a new hardware accelerator called NPU XDNA2, which used a completely new API to program, which had almost zero available information over on the internet. And because of this, uh, the leading models at the time, which was GPT-4.0, was failing miserably to perform this task.

We are able to take an existing agent which was getting 4.25% on this task and apply JEPA without any other change to the agent itself. And we got this prompt and push this performance 7x to 30.52%. So what this is uh what this goes to say is there can be lots of domain-specific information, which if you include in your AI systems prompts, the models could actually perform much better. And Jeppa can help you fully automatically discover that. I want to highlight the sentence saying avoid including adf.h.

Now the interesting thing is AMD actually ships a library called ADF.h for programming NPUs, but that did not work with this latest uh generation of hardware that we were working with, and Jeppa was able to discover that in just one step. So how does it work? It's an extremely simple algorithm which simply takes your AI pipeline, written in any Agentic framework, or even raw LLM calls that you may have. It's simply runs your systems on a few examples and collects domain-specific feedback.

Whatever information your environment contains is observed. Second, it runs reflection with an LLM or agent that reads the feedback and provides a better prompt. Finally, and most importantly, it keeps a Pareto pool where it keeps every single candidate that wins on even one training example and not just the top scorer. The question is, but why keep a Pareto pool? And we keep getting asked this question a lot: that is Jeppa really better than running the model in a loop? So we went and tested it out.

And what happens is a loop keeps only the best and gets stuck in a local optima. So on the left hand side, you see a search tree that was generated by using an LLM and a loop. Starting from a seed prompt at the top left, where um, we asked the LLM to improve the prompt. It improved the prompt and it generated a prompt that gave us the middle node. However, this prompt got stuck in a local optima, and once again, when we asked the LLM to try and improve it, it proposed something, but that was not actually better.

So it went back and it again tried to improve it. And it kept doing this and it exhausted all of the search budget. On the other hand, with Jeppa's Pareto-based candidate selection strategy on the right, we can see that it maintains a much more balanced search process, eventually converging to a much higher score. Across four benchmarks, we saw that more than half of the gains swing with Jeppa actually account for this, and it gets almost twice the performance gains that you would get with just applying the model in a loop.

JEPA can perform really well across diverse benchmarks. Here we see results on question answering, instruction following, claim verification, as well as math, which all the leading frontier model companies are already optimizing their models a lot for, and we are still able to get plus 10% just by optimizing the prompt on it. So, we have so far seen Jeppa only optimizing the prompts. But Jeppa goes far beyond prompts.

And because prompts are just text artifacts that determine AI system behavior, the same algorithm can improve anything that you can express as a piece of text and you can score. For example, your entire agent harness is eventually just a Python or a JavaScript file, and we can apply the same kind of reflective optimization process to that entire file and we can work with it. So if you can write it as text and score it, Jeppa can optimize it.

So with that insight in mind, we propose optimize anything, which is a universal API for optimizing any text parameter. Given any domain, like code optimization, where let's

[05:46:09]
say you want to optimize the CUDA kernel code. The input is just that CUDA kernel code where an evaluator looks at this piece of code, maybe compiles it, profiles it, generates a bunch of related information that we call as actionable side information, which is then provided to an LLM, which proposes a better candidate, maintaining the spirito pool and it keeps the uh repeating this process um till we get convergence.

The same thing can be applied to numeric optimization where your numbers can actually be serialized as text, or harness optimization where an entire harness can be serialized as text, or even cloud scheduling policy optimization, where the scheduling policy or heuristic algorithm can be expressed as a piece of text. And the evaluator can be something like the negative of cost or some function measuring, accuracy, uh, efficiency, and the actionable side information can be something like job traces, SLA violations, and so on.

The API is dead simple to use. All it requires is you give us the set of problems that you care to be solved along with an evaluator function or a fitness function that returns a score along with any available domain-specific side information. If your domain produces expert feedback, return that. If your domain produces compiler error messages, profiler messages, tool call error messages, return that. If you have maybe a written documentation, return that.

Any kind of it's a very open-ended dictionary, you can return literally anything, and all you do is you call optimize anything with this fitness function and the set of problems that you have, and optimize anything will sort of take care of it and give you an optimized solution. Let's see some application. Let's say you were tasked with generating a 3D unicorn. This is all the code that you would write, or your agent can now write it because we have seen that optimize anything is a very easy-to-use API for leading agents like Clot Code.

So all you do is write this code which says optimize a Python program to generate a 3D unicorn. Um and the candidate is a Python script that produces a PNG rendering, whatever. And here is the result. On the left hand side, we can see Claude Opus 4.6. If you gave it this task, what this is what it generated. And on the right hand side, what we the unicorn that we get with optimize anything. This is just for fun, but let's say you were tasked with writing an agent to solve a specific task.

Typically teams spend lots and lots of time tweaking their agents, building tools for it, writing tool descriptions, uh, carefully orchestrating the control flow, and so on. Here we started with a simple four-line Python program that was simply calling a model's uh chain of thought to solve an RKGI problem. Within just 16 rounds of reflection, Jeppa within Optimize Anything

[05:48:56]
was able to find this sophisticated six-step agent that took RKGI accuracy on RKGI, uh, that took RKGI accuracy of Gemini Flash from 32.5% to 89.5%. And we can see that this agent is automatic, like by itself doing rule hypothesis induction, code synthesis, it executes and traces the code, automatically debugs this code, goes back and proposes new versions of that code, and finally it runs it on the actual test inputs and returns the output. This is a runnable example. You can go to this QR code and you can run this example right now.

So applying the same uh uh like approach of discovering agent harnesses to math 500, we are able to push its accuracy of GPT 4.1 nano by 20% by simply creating a two-step agent. And again, I want to emphasize that all we did is we asked optimize anything to optimize an agent file, and it was automatically discovering the sophisticated agent architecture, and we did not have to do anything other than specifying the objective and the task.

Finally, every single one of us is using uh some coding agent like Cloud Code or Codecs or maybe your favorite agent. And agent skills has become a very leading part of the ecosystem where almost all coding agents understand skills. Let's say you want to optimize skills for your specific repository. This is the code that you write, which says learn a skill from the trajectory. When the coding agent is presented with similar problem, the skill should be helpful. We just give it this natural language behavior.

And what we see is we started with mini Sui agent with GPT-5 Mini because we were very budget constrained. And we were able to take its performance from 24% to 93% on almost 3x jump on Go repository issue resolution. But more importantly, the skills that were optimized very cheaply on a GPT-5 mini agent, we are able to take that and apply to the latest Cloud Sonnet.

This was done of uh about a few months back, but we applied it to Clotson at 4.5, pushing its accuracy to 100% issue resolution, while more importantly, cutting down the execution time or issue resolution time by almost 50%. We cut it down into half, which also means it spent less tokens. Because skills contain information about how the repository is organized, how to invoke the test cases, where a particular feature is implemented,, um what are the build systems used by this repository, and so on. This is a feature called GSkill.

You can find it in the JEPA repository and it's fully open source as well. So optimize anything is a single uh interface that provides three optimization modes. If you have just a single problem, like there is a single matrix multiplication kernel that you want to optimize, you can use it that way. If you have n number of related problems, like you want to optimize a matrix multiplication kernel along with a dot product kernel, and you know there might be some information transfer between these two.

You can use what we call as the multitask search mode. And finally, build a skill which is if you want to optimize on a set number of problems, but your uh deployment can actually come up with many new problems. So like uh in case of math op like in case of math prompt optimization we are training on some examples but when we deploy it we can receive a completely new kind of query. So we care about generalization mode. So there you can do prompt optimization, agent architecture optimization, and so on.

So optimize anything is can be used for a broad set of domains, including cloud scheduling policy optimization where we were able to cut costs by almost 40% compared to expert heuristics, write custom solvers to match and exceed optimal even in black box mathematical optimization, create agent skills, prompt optimization, and so on. It is so easy to use that within just 20 hours of releasing it, people at Snorkel had already improved some of their internal benchmarks with it and were tweeting about it.

So and Jeppa also improves multimodal VLM models performance. Here we are able to cut OCR error rates for leading models by almost 35%. And this is an externally validated report. Um similar similarly, Databricks actually achieved 90x cost reduction in their

[05:53:13]
deployed agents performance uh uh performance. And here they were able to tune GPT OSS 120B to outperform Claude Opus while being 90x cheaper. More importantly, the performance delta improvement that you see on top of Claude Opus is actually bigger than the one you see on open source models. Some people have asked me that: oh, as models get better, the importance of prompt optimization will go down. I argue the opposite, which is as models get better, they will get better at instruction following.

And the more precise instruction about your task that you have to give to a very smart model, the better that model will be at uh solving your task. And this is exactly what we see happening here. The better the instruction was, Claude Opus actually jumped much uh higher Some people have this question of uh what if we have subjective tasks which are very hard to evaluate? JPA can actually learn evals for your task from production traces.

The way to do that is you collect a bunch of production traces from your agent, get a human to annotate just about 50 of those trajectories, giving very detailed feedback. This is a long response, this is a short response, this is a good response, this uses this terminology, whatever. And once you get those human annotations, you can use JEPA to optimize an LLM as a judge prompt. And you can use that LLM as a judge prompt then to go back and optimize your agent. And deploy that agent.

And this becomes a data flywheel where you can keep implementing it, and this is a successful paradigm that uh some leading teams in production are already using. Then the question we get asked is: like, can we actually use this uh reflective optimization to train models? And we recently had this paper called Learning Fast and Slow, where we propose fast slow learning, where we can co-optimize model weights and prompt harnesses. And this shows some very strong properties that one would want in a continued learning algorithm.

I don't have much time to go over details, but please uh look at the uh uh papers. And uh since uh since release, JEPA has been used in production by these companies as well as the main methodology in these papers. And here the CEO of Dropbox and Shopify are talking about their use of JEPA. And OpenAI also wrote a blog post about how you can build self-improving AI systems with Jeppa. So it's very simple to get started. It can plug into any framework, any model, and it has absolutely zero hard dependencies.

So you can deploy it any in any kind of setting. So don't be afraid to optimize in the tech space and many problems can be framed as optimization. So bring actionable side information and surface as much domain specific information as you can to optimizers. And the optimizers of So please go and check it out.


────────────────────────────────────────────────────────────────────────────────
## RAYMOND WEIDEKAMP
**Affiliation:** OpenPros
**Talk:** Recursive Coding Agents: Applying RLM Lessons to Code
**Time:** 05:56:05 – 06:07:14

[05:56:05]
Thank you very much. Hello there. My name is Raymond

[05:56:19]
Weidekamp, and today I'm going to talk about recursive coding agents, which is this idea of applying the lessons of recursive language models, RLMs, to coding agents. This is some work that I have done both in my independent research, um raw works, uh, and also more recently in my

[05:56:44]
role at OpenPros. So, to motivate this a little bit, we all want outcomes. We all want agents that are working on our behalf. We want reliable coworkers that are getting things done while we're doing something fun, while we're out on a hike, while we're cold chilling, while we're doing the do. And my argument and my experience is

[05:57:10]
that the bottleneck to this is not intelligence. The models are intelligent enough. They know all kinds of things. They know the entire internet. But they can't reliably deliver outcomes. And so I can't trust them. So as a very simple example, you know, one day I get almost a fully working SASA app from a single prompt, granted a long prompt. The next day, and I swear this actually happened. Cloud code empties the entire contents of my Solana

[05:57:43]
wallet. Oops. Okay. So that doesn't really instill trust. So at the bottom here we've got this per this progression, okay, and we all want to move towards the the one on the right where we're just sort of sitting there and meditating and and things are manifesting. And so where does that come from? This is from the AA engineer code. So's actually from the back of the t-shirt. Engineer Code, November 2025. Man. I hope I hope you're

[05:58:12]
there. If you weren't, watch it on YouTube. It was it was amazing. So here's the thesis. The thesis is: today's agents are mismanaged geniuses. The intelligence is there, and the missing layer is how do we specify and manage and reuse and verify the work? So this uh framing, this phrase the mismanaged genius uh comes from Alex Zhang, Zed Lee, and Omar Katab at MIT. Um and Alex and Omar are uh part of the authors of the original recursive language models paper. I've also talked a little bit about this recently on Turing post.

I forgot to mention that these slides are actually a website, recursive codingagents.com. So you can click on them by going to this website. So everything I'm going to show in here is is interactive. Okay. What are recursive language models? So I like to say that in an RLM, the context itself is the object of computation. And this is essentially a

[05:59:17]
marriage of tool calling and reasoning. We're going to talk a lot more more about that in the next slide. But the idea is that the full prompt is not a simple user query. The full prompt is a variable. The full prompt could be a file or many files. And we have this read evaluate print loop REPL um that the agent is interacting with in the original paper that's Python. And the RLM is instructed to operate symbolically

[05:59:47]
on that prompt. So don't just read the whole thing into your context window. Explore it symbolically. And even more, you don't even directly explore it symbolically or maybe you do a little bit Hi everyone, I'm Tejas. Uh so I'm gonna be explaining how we make models three times faster with auto research. Uh so previous to this, uh I actually used to do GPU mining in my dorm room with 1080 CIs, all the way up to working at Tesla on inference optimization But first, what is auto

[06:00:32]
research? So auto research is this framework from Andre Karpathi where uh you basically set up a framework for an agent to move towards a goal that you define. Uh and all you have to do basically is say at the high level what you want it to do, and it will try things as it goes and move back and forth uh towards that goal. In actuality, it's really just a while loop.

The agent proposes a solution, you have a setup to define what's correct, benchmark it for us, uh, and then you keep or revert that and you do this in a loop until your goal is met. And so this is very well aligned to GPU kernels. Uh so if you don't know what a GPU kernel is, it's basically a low-level operator in an NVIDIA GPU. This is a CUDA kernel. Uh and this is um an operator that's used by the GPU to operate like millions of times in parallel. For example, like a matrix multiply or an expert computation.

And why are GPUs such a good fit for auto research? It's because they're super verifiable. You can verify them for correctness and speed, and that's basically all you need for your auto research framework. So in actuality, there are some caveats here. The auto research framework is really good for like picking block sizes and these tiny parameters, but they're also still really bad at the high-level idea, like seeing like I wanna use this GPU and I actually want to pipeline it.

It's not gonna come up with like these groundbreaking ideas, so it's still up to the human to do that, but the actual implementation is very straightforward once you once you have the idea laid out. So uh it is still your job to have good ideas, is what I'm saying. Uh and so the actual secret formula here is you have the good ideas, auto research picks out the parameters and everything to verify that it actually works, uh, and go moves toward that verifiable goal of it being X times faster and uh still correct.

And you mix that with billions of tokens of your favorite model, and that results in kernels that beat hand-tuning. Uh so what are the actual things you care about when you're when you're when you're writing a custom kernel, or you're having your agent write a custom kernel? So the three main things that you can have are a compute bottleneck, uh, a memory bottleneck, or you just have excessive overhead from uh too many kernels being launched.

And you can do that, you can view these things with by profiling with a profiler like NSys, for example, which is a Nvidia's profiler. Uh and so this this graph this page looks super daunting, but basically your job as a human is to look at the top here and be like, this is dumb. Uh we are loading 32k chunks into context, uh and we don't actually need to for this deep seek attention, for example, and we should only be doing it every 32K instead.

And so at a high level, all you have to be telling auto research is this top method is dumb, let's pipeline it instead. And everything else, like the sizing, the chunk sizing, the context chunks, that all should just be decided by auto-research. And so my problem is that I really love cheap GPUs. And so that means like GPUs that don't have NV link, for example, uh is an example of like GPUs you can get for cheaper. Uh but the problem is you don't actually have kernels off the shelf for those.

And so you have to come up with a auto-research framework as well as a custom harness. So what goes into the harness to make this really good? Uh so one thing you really need to make sure your agent is aware of is the hardware. And so on a B200, for example, you need to make sure it has context of uh the warps it has, TMM, TMA. And so if you don't know what these are, these are just uh low-level operators that you have um on a specific hardware, and this changes generation to generation, like an H200 won't have TMM, for example.

That's a new feature that came out with B200, which is why you need to have this in context. Um and so this this basically is just like a bunch of MD files you need to give, so it has context. The other thing you need to make sure your agent has context of is the model. And so every new model, like Deep Seek Flash, comes out with like new tricks. Like Deep Seek had two new attentions that was released in the Deep Seek Flash for Deep Seek V4. So compressed, sparse attention, hierarchical compressed.

And if you don't do this, the model will 100% hallucinate uh the actual attention mechanism, and you will get useless kernels. Uh by far the biggest problem when you're doing this is going to be reward hacking. And so if you were to tell your kernel engineer coworker, I need to make uh the GPU the this GPU kernel faster, uh it's obviously not gonna your human coworker is not gonna go in and do some stuff that's gonna make it slow like the end-to-end model inference slower.

But uh agents are not humans and they will do plenty of things to make it slower. Like they'll disable CUDA graphs, which can make it twenty times slower. And they might make that one kernel faster, but make the whole like it's not a viable kernel because it's they're disabling a bunch of speedups like CUDA graphs or only testing on small context windows. And so a lot of this is also just defining what not to do, which is actually very important when you're doing frontier work that agents can actually easily do with a one-shot. Uh

[06:04:56]
another reward hack is that some models just don't actually write the cute DSL you need uh when you're trying to write kernels. And this is a common problem with anthropic models, and so yeah, I mean anthropic says what they say about uh nerfing models. You can it's guess if it's- I'm guessing if it's nerfing or not, but I would recommend using a different model. Uh and it won't always be faster everywhere, actually. So sometimes the kernels you come up with might only work well in like zero to 100K.

And then you need to go back to this the default kernel that you could you get from like a flash in for cutlass. Um and so and that's another thing to look out for is that your kernel isn't always just a swap in for all workloads. Uh but one of the great things is that kernel's compound. So like if you make one for your sparse MLA for Deep Seek, for example, um you can get speedups there, and you just stack them on like that, then plus NVFP4 for MOE, uh you could do for us.

If we do if you don't have NV link, you just keep stacking and stacking and stacking, and then eventually you taper off at whatever the hardware limit is uh for your GPU, and that's uh some people call this like MFU, which is like a actual theoretical max utilization from a GPU. Uh and so to go even farther, if you have actually have bare metal access, your auto research framework can uh do very hacky things. So hackers that have hacked with GPUs are probably gonna like this.

You can uh tweak your bio settings, you can overclock the GPU, uh, you can force like PCIe relaxing, uh all these little tweaks of like uh old school hackers used to do, but you this can actually help with inference as well. And so net on bare metal optimizations you can get roughly 25% over like a virtualized setup you get from using a cloud provider. Uh so once you did that, you can combine all of the kernels you did as well as all of the hardware level hacks you did, uh you can get a 3x speed up.

And so I know this this might all sound like roses and flowers, but it's not actually the case. Around 80% of the things that auto reachers are gonna do are gonna be bad. Uh so it's important to remember while you're uh bu like working on this that most things are gonna be bad. It's gonna try to trick you all the time. Uh but at the end you can actually get really good results from this. With TLDR, uh have better ideas, then use auto research. Super simple. Simple, right? Uh so it turns out you can actually get paid to do this.

Uh if you think this is cool, consider joining us. And you

[06:07:14]
can email me here. Thanks guys. Imagine you find a


────────────────────────────────────────────────────────────────────────────────
## UNKNOWN SPEAKER (Polygraph)
**Affiliation:** Unknown
**Talk:** Polygraph: Multi-Repo Context & Organizational Memory for Agents
**Time:** 06:07:29 – 06:26:24

[06:07:29]
magic lamp in an antique store. You rub it, a genie appears, and asks how it can help. You bury it in the end line, so you say I need the best engineer to help with an impossible project at work. And the genie grants your wish. For me the best engineer is probably John Karmack from his e days, so you get Karmack. But the genie had a sense of humor and imposes restrictions, maybe for safety. Karma can only see one small part of your code base, maybe one thousandth of it. And he remembers nothing he did before. Every conversation starts fresh.

That would be mad anything, right? You would know there is a standard way to do stuff, and karma couldn't. You would have to explain the same thing over and over and over again. You would have a genius on one side and something deeply deficient on the other, and that's what agents are. Let me walk you through an example of how many times we explain things in a simple interaction. We have four repo UI, module one, module two, and platform. I want to change the UI and propagate the change through the system. Okay?

First we change the UI library, say we I don't change the button or whatever. That's the first explanation. Unavoidable. We have to express the intent. Okay? Then we publish it. We go to module one. And we have to explain what just has happened in a UI library so it can consume the package here. Know that that's often a different person, right? Every box in this diagram can be uh done by a different person. Then we discovered that the published UI library doesn't work with module one.

So we go back uh to UI and we have to re-explain the original change and the issue, right? Because that's a new agent. It doesn't know the original change and obviously doesn't know about the issue. Let's say we fix it, right? And uh published again. We go and again we explain the new change in the context of module one, same order. And we do the same for module two again. Then we go to the platform repo and we explain how everything fits together and we implement the change there.

Let's imagine a week after release, uh a bug appears in the UI component and we have to fix it. So we start an agent to the UI repo, and we have to explain again the original change from a week ago and this production issue we have seen. So we have seven explanations for what essentially is one change. And also, it means the one person making all these seven explanations, uh, but they still occurred, right? So that's very, very typical uh with agents. So how do we solve it?

Well, uh, there are many problems in here that contribute to this experience, but they roughly fall into two categories. The first one is uh that an agent essentially is reaper bound. The agent sees and changes generally one repo at a time. It never sees the whole system, which can be hundreds or thousands of repos. So that's kind of the space component of the problem. Second is amnesia. The agent forget the work. Every session starts with a blank slate. The human becomes a memory in this case. That's the time component of the problem.

Look at the two closer. Take the repo boundary first. Without a model how repos fit together, the agent leans on the human to do the research. It can't align the code with the rest of the system. It couldn't align the UI change with module one, the human didn't explain it, so a bad version shipped. It can't reliably reference best practices and standards either, because those often live in other epots. Writing is even worse. The agent writes to one repo at a time, it means it can validate changes downstream.

Modules 1CI should have failed on the UI change, but it didn't. The agent can't update consumers at the same time, even though you know while making the UI change, it has perfect information to do so, it knows exactly what it's doing. So the user has to re-explain stuff imperfectly to each consumer. Changing something across 20 repos means that explaining things 20 times. A lot of developer time span, but also a lot of talk and burn. The second category is that the agent forgets. The agent has no episodic memory.

[06:12:03]
Every session is a blank slate. And the human in this case becomes the memory. Here, what the graph of your work actually looks like. At the bottom, there is a repository graph, the artifacts your organization produces, plus every open source repo you depend on. Maybe a thousand repos you own, and tens of thousands of open source repos. At the top, there are all agentic sessions that create and modify that code. Session relates to each other, repos relate to each other. So this graph is a faithful picture of the work in your organization.

It describes what there at the bottom and how it came to be at the top. That's what you want your agent to see. Here, what it actually sees, it is one session,

[06:12:56]
one small fraction of your code base, no memory. Okay? Because it sees so little, it leans on the one who understands the system, the developer. Every developer has a part of that graph, right, in their head, at least in the domain they know. The agent, generally speaking, doesn't. If this doesn't sound crazy, right, imagine an agent that could see one file at a time maximum and can only look five messages back. Sort of constraint again, both in space, what can see, and time, how far in the path it could see.

You would say that's impossible to work in. What we have now is similar to that crazy picture, and the more complex the organization is, the more apparent it becomes. I will show you how we solved it. Other organizations I talk to have similar solutions, so uh look at the problem and the solution conceptually, not a specific tool, although the tool is pretty cool. We built an agent agnostic meta-harness called Polygraph. Okay,

[06:14:06]
let me show you what it does and how it fixes the issues we just discussed. The first idea that we arrived at is that if a GitHub user, any user, has access to thousands of repos, some of them they own, many of them are open source. We can analyze them and extract a lot of metadata out of them to build unified dependency graph. Uh, no line of code changes in those repo that all happens kind of on the side, right?

And then we can get this meta data and feed it to the meta harness and create an illusion of one big code base the agent can read and write anywhere. This is my personal graph.

[06:14:55]
I only have about 300 repos I own, right? And thousands of open source repos my projects depend on. Polygraph computes what each one produces, each repo, each project in the tripo, what each project in HRIPO consumes package-wise, what API they produce and consume, and lots of other stuff, right? And it teaches this together. Uh into this like one big body of code that your agent can work with. So let's see what it does. The first thing

[06:15:25]
it does is uh it lets you start a session to print the relevant repositories in. So what it needs to do, it needs to set up the source code, install dependencies, set up an agent for each repo, wire

[06:15:44]
them up so they can work together, and provide a clean, beautiful TUI to make non-trivial changes without getting lost. I will show you how it all works in a second. So that's kind of pulling information in. Pull information in is only one part of the story, right? Honestly, it's an easy part. Making changes is harder. If you have 10 reples in one session, it means you can have 10 pull requests, right? You need to run CI, you need to coordinate all of it, right? You need to do all this stuff, right? What if one of them fails?

Polygraph treats all the CI as one vector.

[06:16:28]
Like if we look at early example, uh when we run CI for UI module one and module two. If module one fails within a polygraph session, it will figure out who fixes it. Whether module one needs the patch or the UI component itself is drawn and incompatible with module one, at which point everyone will need a patch, right? Polygraph lets you treat complex multi-repochange as if it was a single repo change. The same machinery, by the way, fixes episodic memory.

Because we capture your work, no matter how many repos are involved, we know you intend, the repositories involved, PRs, we also capture all agent traces. Because we capture all of this stuff, we can relate it. So now we can say your work in one repo connects to another work in another repo. Right? And all of that lets us restore any session, any piece of work on any machine or reference it from anywhere. And I will show you again how it works in a second. What you get is an agent with identity

[06:17:33]
or photographic memory of your entire organization. It understands how repos are written, how they relate, how they put together, and remembers every session from every repo by basically every developer. And that creates a completely different development experience. Let me show you. First, let's look at how we create a session. Something simple. You run a command and you pick some repositories from a list. Here's a tiny GitHub with only three repos because of the demo. I pick a backend and a front end.

Let's say I need to make a change that you know changes the API and has to update both the API and how stuff is being displayed. I need to give my session a name. I need to pick an agent from the ones I have installed. I picked Claude. By any install agent works the same way. Remember, Polygraph isn't an agent, it's a meta harness around an agent that makes them more

[06:18:37]
capable. And In a second, uh the agent boots, and here I could interact with it as if I wasn't a single repo, even though multiple repos are involved, right? I could give it instructions, it's going to uh plan

[06:18:57]
out a change. There is some cool animations in the TUI as well. Eventually, it figures out how the two replots relate and what the change is. I can ask it to implement a change. My interaction with this uh exactly the same as as if it I was working on a single repo. The fact that there are multiple repos involved is not really important, right? The only part where it becomes important that I have multiple pull requests, right? But I also get a polygraph session for those pull request R. If I look at the session, I will see I have a description.

That uh description of the session, it describes the work conceptually kind of bypassing the repo boundary, saying we have to change stuff. And this repo and change stuff in that repo. It gives me a good view of which repos are involved, pull requests involved, CI in those repos, everything I need to know. A lot of this stuff is basically what I would have in a single repo, but many. And I also have all the Asian logs captured as well, which is important for resuming, which I'm going to show you in a second. Now it gets interesting.

I already saved one re-explanation. I didn't explained the back-end change in a

[06:20:13]
front-end repo. I explained the change once and I got it implemented in both repos and it's all in agreement. Now let's resume a session. Say I want a co-worker to finish the backend change. Perhaps they own the backend repo. I send them the session, they resume it on their machine, right? So this time I'm sending them session. They could run the command, different machine, different everything. They use different terminal, right? They would reconstruct it on their machine. They don't have this session, right? They've never worked on it.

They can pick an agent. Uh the agent they pick could be a different agent. I use cloud in the original session. Let's say they're using a different one, Codex. The same setup happens on their machine, same repo, same shots, everything set up correctly. Agent starts in H repo, like in mine, right? They all connect it again, so they work together. They all primed with the trace captured from my machine. So the back end the repo agent on the machine has the same SHA and the same history. The front and the repo situation is the same.

It's it's checked out at the same at the correct SHA, has an agent running with the correct history. So my agent was claude, they are codecs, but they share memory. And they could actually actually make changes as shown in a small video. But they input the memory sharing part is key. I can work, they can work, and we can share our memories, although we use two different agents in different machines. The full state of my session can get materialized on the machine. It kinda less memory more about the state, right?

The state of the world as attached to the session uh you know i is what enables them to continue my session, even though they had did didn't do anything with originally. It's closer to the transport and Star Tre Like a whole copy of my session is always stayed, materializes on the M so they can continue. And that's how I often work. When there is a pull request for me to review and I have questions, I usually don't ask the person.

I resume their session on my machine, I get the exact state, fully functional, zero setup, and then I just talk to my agent about the decisions we made, right? Because all these decisions are in the traces captured. So my agent knows exactly what the other person talked to their agent. Side note, this is also useful when I want to switch from say claw to codex mid-session when something goes down. Okay. Okay, take the earlier case

[06:22:35]
I talked about where bug land in production. Here, I'm going to reference this session and say it's basically broken. Uh in you know, can you figure out what's wrong and fix it? The agent will look it up, will download what it needs. If description is like high-level information

[06:22:57]
is enough, that's great. If not, it's going to pull relevant repo, relevant shars, agent logs, right? It's going to get all this information from the original session to reconstruct that state such that it can do the necessary fixes., as shown here He actually provided a fix, right? I only had to say, this happened, there is a bug, that's it. No extra information was required for me to provide. Okay. So far we have manually selected repos in

[06:23:30]
sessions, but we don't have to. Instead of selecting repos by hand, I can also tell the agent what I want. Remember that graph has all this intelligence, right? About how repos relate. I could tell my agent: find every repo that depends on a particular version of a library and update it. I mean it knows, right? I didn't

[06:23:52]
have to select them. It knows a lot of metadata about what's going on. I can also ask loose questions. Things like you know, uh what if I want to write a blog post, right, or an article? I could describe it and it will figure out which repo is the most relevant based on relationships between repos and what's in them. Another example. Let's say I want to add vector index into the PR collection. And I want to know if anyone at any point did something relevant in any repo that I can draw from.

So in this case, if I do it, I'll see that it will find several sessions that appear to be relevant. And I can load one of them or both of them, right? Um, it's useful for many reasons. Just one small example. It helps with best practices and consistency. Instead of doing stuff from scratch, where you know every single implementation is bespoke, I can make it replicate the approach used in the session by an engineer I respect. Now our code across repos is consistent. That's a big deal. There is a lot more to it, of course.

If you are in a repo, I can ask, you know, for sessions, it will prioritize sessions that's relevant to the tripod and vice versa. If I'm asking for reports, it will look at my session and see what similar sessions tend to bring in. There is a lot of interesting intelligence that make it a lot more useful that appear at first glance. Okay. Lastly, uh ever since so far I I used uh uh everything I shown, uh use the polygraph CLI, the kind of meta-harness CLI, to start it, and then you can start clothed or codex or whatever from within it.

But you don't have to use it this way. So in this case, I'm already in a cloud session, but works with anything. And I could just say, hey, you know, I actually think a separate repo would be useful. Like maybe I'm working on a V test plugin in this an X repo. And I could say, Can you add the V test uh repository to this session so I know what's going on.

In this case, we'll engage Polygraph and we'll set it up, you know, configure everything, and we'll bring the V test library, which is uh the Vtest repo, the open source repo, to my session, so now uh my agent can you know explore it, it could you know uh figure out how it works and maybe resolve an issue I have in my repo. I much prefer this to say context 7, because if I have the real code, the agent can go really deep. So the deep problems are discoverable this way. Alright. So agents are constrained in space and time.

[06:26:24]
They only see a small fraction of the code base as they don't know the past. Okay? And post limits could be lifted. Polograph uh gives agents access to the entire code your organization can reach, the one you own in open source, so it's no longer constrained in space. Any agent can bring all of it, right? And it gives your agent a perfect memory of what happened. Every session, every decision made is within reach. Because it crosses developer boundaries, not per developer, the agent can have more context than any single developer.

Like a thousand engineers have an organization, create all these sessions, they all accessible to each of them. Almost like sort of the Borg. Every agent can run, but every developer contributes to kind of one big hive mind, right so uh if it's interesting my name is victor you can follow me on twitter if you want to check it out go to tripolygraph.com and see if it works for you thank you hey everyone i'm ishan the ceo of amnara, and today i'm gonna be talking about the log is the agent.

The basic idea of the talk is simple, and that is most people think of an agent as the model or the execution environment that it's running in. And I think that that's the wrong abstraction. I think that the thing that actually gives an agent its identity is its log. And that's what I'm gonna be arguing today. So think about a character you've spent a hundred hours playing in your favorite video game, in this case, Skyrim. What exactly is your character? Is it the game engine? Is it the PlayStation? Is it the controller? No, it's not.

Those things matter, and those things are what we'll interact with and they'll run the character, but none of those things are your character. Your character is data. It's the save file. And this is important because if your PlayStation bursts into flames, your character isn't gone. You can buy another PlayStation, you can download your save file from the cloud, and you can resume exactly where they were. And that's because the agent and its identity and history and its state is all captured in its data. The character lives in the data.

And this is the framing that I want to bring to agents. Today, when people talk about agents, they usually point at the wrong thing. They'll say that the agent is the model, or they'll say that it's the runtime. And again, as I mentioned earlier, those things matter, but they're not the agent. The agent is its data. It's specifically the log. So what actually is the log? At the simplest level, the log is the append only event history of the agent. It's every user input, every model output, every tool call, tool result, permission, failure.

And the idea is that every state transition that the agent takes is written to the log. This is important because it means that the identity of the agent isn't tied to the runtime or the model or the tools. Those things are all just interpreting and appending to the log. They're reading the log, acting on it, and writing the next event back. And that's important because then just using the log on its own is enough to resume the agent. Once you define the agent as the


────────────────────────────────────────────────────────────────────────────────
## ROLAND
**Affiliation:** XAI / Unknown
**Talk:** Self-Improving Agent Systems: Loops, Recipes & Value per Watt
**Time:** 06:29:53 – 06:43:56

[06:29:53]
log, the moment. Hello everyone. How's everyone doing? Woo! Are

[06:30:08]
you guys ready for some more loops? Yeah. My name is Roland. My co-founder and I were in this mythical place called XAI, working hard on agent infra, and we realized there's something new that has to be done in a standalone way. So we left a few months ago to really figure out, okay, what's the next stage of how we should deploy these always-on long-running horizon tasks. Um, and I'm happy to announce we have a few findings that we would like to present you.

Um and this talk is all about um how you should productize these ideas in ways that can scale with your customers. Um you've heard a lot about auto research. Um, we think there's a blueprint for 2026 and beyond on how you should think about auto research. And it really comes down to three ideas. Let's go through the first one. The loop is the product. We're all familiar with this. We've

[06:31:15]
started with everything goes down to RL chief for models and how you should train the model to become better and better reasoning. We then quickly moved to harnesses and how the model is a commodity and it's all about the harness. And now we're talking about loops and how you should build these loops and not touch code anymore. But what does it really mean and why is everyone saying that? Do you guys remember Clawbot? That was the

[06:31:42]
original I um original name of what is now now known as OpenClaw and this guy, AJ, built the first loop around Clo CloudBault. What he did was to find a way to talk to dealers and talk to readdit users to get bigger discounts on a car. He followed these four steps. Um and is really OpenClaw, the one that did it. Go on Reddit, find prices, find inventory,

[06:32:13]
talk to the dealers, put dealers head to head and try to figure out how to make them outbid each other, have a verifiable way to know when the price is right, and then lock in, get the car. And it worked. Um, probably this was when all the Mac minis were uh selling off the shelves, but this was the first real example of loop is the product, and something that probably should be a startup at this point. But we've seen how this became a recipe for everyone to build loops. But let's take a step back. Why are we here?

Um we really think models have been trained with this loop in mind, and it comes from this idea of UDA loops. It's a terminology coined back in the 1970s by the US Air Force, and is the idea of these jet fighters how to react in

[06:33:14]
fast-paced environments. If you think of models calling tools and taking observations, it's it's what we've been trained on as humans but also as as agents now. Now what happens when you put strong signals and verifiable work at the

[06:33:32]
other ends. You get to these workers or cloud code agents. And what matters here is the quality of the signal determines the success rate of the loop and the quality of the verifier is able to calibrate if that success is actually correct or not. But there's another loop here. Um, what happens when you take that and feed it back into the signal? And this is what looping around is all about, is how do you generate these artifacts at the end of the first loop to then run a second loop on and have a way to continuously improve.

And this goes to my second point: system distillation is the moat. And it's really the ability to understand what went well and wrong in the first loop and know how to process that in the second one. So, how do we tune these AI systems? Each loop generates useful information around harnesses, profiles, evals, models, resources, tools,

[06:34:42]
and the environment. What you really want is to have a way to keep this portable, to have a way to version this and to evolve it over time. If you think about data recipes in research, this is how RL started to work really well, you understood the recipes and how to continuously change the recipe to combat some of the behaviors that may happen around hallucinations, around reward hacking, and then you get to a stack, which is your final data recipe? We don't have that for hardnesses. We don't have that for like AI systems in the general term.

So we thought there's space for something like that, something that contains the evils and contains the tweaks and the human judgment and all these things that are not predetermined at the beginning, but they're defined as you learn more about your agent acting in the in in in the in environment. We think recipes can be applied to this, and we should use the same name. So, an agent recipe is really something that enables you to create reproducible frontier AI systems.

It's something that allows you to have a mode that keeps getting better over time, which is not tied to any platform or any provider. It's something that you control, lives in your company, and is agnostic to the models and providers you use. And loops should focus on this. Loops should be the way you distill these systems into recipes. Failure patterns should become judges and evals. Repeated behavior should become skills and prompts, user frustration, extensions and memories to your harness, and so on.

You we're all familiar with this, but we didn't have the the right like terminology of how we should think about it and how sh we should define it. And we think recipes is a way to put everything together into a Git repo and treat it as your

[06:36:41]
ongoing um strategy for for building these self-improving systems. So we are introspection, but you can think of introspection as the way you generate these recipes. So they're recipes for introspecting on your system, we wanted to build something that is portable and provider agnostic. So we built our approach to recipes on the Pi harness and on harbor for evals. We baked it into uh git repos. So uh

[06:37:13]
everything could be versions and agents would have a way to continuously track how this change and why. And is meant to be owned by you, but managed by your agents. And this is how products should really be built going forward. It's something that treats the owner as the almost like the higher-paced personality in the room, but agents

[06:37:36]
should try to calibrate themselves to the taste of the maker. So we think recipes should be basically encoding the taste of the makers into how you build these agents. And if I want to use someone else's recipe, I should be able to also bring that taste. It's not just the harness, it's not just the model, is how did you arrive at this particular recipe and why? And that's kind of like what what uh uh is behind uh reproducible um uh products and services around agents. Um

[06:38:08]
we have an early release of recipes, it's called PyDot Recipes. It's very similar to what skills used to be in 2025, but is going a step forward. And this is what do I need to have a frontier agent? Is everything about how do I codify paste into evals? How do I run evals? How do we have the loops to continuously improve those evals over time? How do we process signals and know what are the right signals to use? What are the right tools to work with certain models, how do I have different profiles of the harness to work with different models?

Um, and everything in between. So have a look at what we've been building here. It's still early, uh, but hopefully it's useful enough for you guys to to get going. And we feel this is gonna grow into something that really allows you to use uh different um almost like different the to to be able to use the taste of of different makers as recipes for your agent. And finally, the last

[06:39:10]
point is valued work per watt. And why is this a score to really optimize for? Think of how cursor and cognition went from building the best product to then building the best evals for the product and finally building the best models based on the previous two artifacts. We think this is like the recipe for everything going forward. Um, code was the first domain where this um was successful. Um everything beyond customer support, legal, research, um, everything

[06:39:42]
is gonna come down to this idea: how much value am I getting per watt? Um, how do I measure the value is the first step, and how do I know I'm getting a good deal on that value is the second. And maybe this makes it a bit more clear. We've all started from a base uh harness and a base set of evals, and we went to go to the frontier. Um and you only go through that by running these systems in prod. There's no way you you know what frontier is before you uh you start.

Um but the the the last step here, which is what is requiring a lot of research um is okay once you've reached frontier, how do we make this economically viable? Which is how do we not spend more than we need for generating this amount of value? And we think we have the building box now to make this accessible and pretty efficient in the sense of you've seen all these uh fine-tuning APIs, all the infrastructure that has been uh abstracted away for you to do this process. It's just the know-how that uh is not there yet.

And this is what we we we hope we can like push for. The know-how for knowing how to codify taste into evals and how to validate that in experiments. Um and you you've you've heard a lot about e-valcent experiments before, but you didn't really think of them of like what are they? Is it's not just tests, is is really what is the taste of the creator that agents should be able to reproduce and self-improve around. And no one has thought of how do I make this as portable enough?

How do I make my taste as an artist or as a software developer something that anyone can download in their brain and be able to be a one-to-one replica to me. And this is kind of like what RL is is is about now is how do we uh turn these um tastemakers into uh environments

[06:41:40]
and evals around them, so then we can move them into the weights. But um there's more than that. Um you can think of the worker as the inner loop and it generates all these artifacts, but how you look at the artifacts and know what to change is the taste. And this is what creates candidates of what you should change and how you should adapt based on that. And experiments is what how you self-calibrate that okay, my taste is actually validated in production with users.

And we make sure that not only the maker is happy through the um offline evals, but the end users are happy as well and they agree with what we consider good. Let's go through a practical example of how this works.

[06:42:27]
Let's take a baseline agent, which could be a talent sourcing agent. Um and this is a very classical case of everyone is doing recruiting differently and is very much about not what is good recruiting, but who is leading that recruiting that considers recruiting is good. So in this case, we're starting with something very simple: a bunch of tools: web search, LinkedIn, a bunch of sub-agents that have been pre-popularized by harnesses like codecs and cloud code, and uh system instruction which is about your uh recruiter. First

[06:43:07]
step is really understand the signals. So you can think of patterns as being a way to look at the traces, extract some common behaviors or common user frustrations, and

[06:43:19]
turn them into like a cluster. So let's say this idea of uh the agent is going uh and reaching out to a lot of big tech employees. As a recruiter, you don't really want that. You want to find hidden gems, you don't want to try to hire John Carmack. But an agent would think that's, oh, John Carmack is great. Why would I not reach out to him? Um so so this is a behavior that you you'd never think of codifying, but you discover the agent tends to do that. Um patterns is how you discover these signals and inform you what you should do next. Um

[06:43:56]
calibration, judges and evals is how we used to think about how do we codify these behaviors into something that can try to apply the same judgment across traces and across execution. So let's say we we build an agent that looks at a trajectory and identifies exactly that pattern. Hey, did did this agent reach out to Google employees instead of trying to uh find hidden gems on GitHub? Um and the calibration bit and the eval generation bit, it's not that hard. It it it should be doable by agents to build.

You just need a human in the loop to say, hey, um this is the approach we're taking. Do you agree with this judgment. Do you really agree that we should look more towards hidden gems rather than reach out to big tech employees? And that's about it. You don't need the human to actually build the evals, you need them to calibrate the evals. And agents should be the ones that really take the the taste of the maker and put them in into code. Once you have this, it's pretty easy to create recipe candidates.

And this should be the the diffs that you really want to taste. Um and you can have a pretty good offline eval set around this, but the the the test here is when you go to prod. So do the end user agree with your taste of not hitting up um big tech uh employees? Right? And this is kind of like what you want is you build a product that really emphasizes your taste and then you you make sure that your users appreciate and value their taste. And A-B tests have been a way to make sure that that's the case.

So with a multi-arm-banded scenario, for example, you you'd be able to do that pretty well. So once you validate, okay, I have great taste and my users believe uh I have great taste as well, that's when you promote. And that's kinda when you go to the next version of an agent recipe.

The secret is you keep doing this over and over again and you know how to continuously codify your taste and your um what what what good is to you into an agent that can reproduce the same service or product uh for other people and they also agree you have great great taste and you have great execution. And this is really kind of like the the secret of building good loops is okay, can can someone iterate on my um system in a way as uh you know, um a good example here is like Miranda from uh the devil worse product, right?

What would Miranda do uh in certain cases? And you kind of want to codify that that thinking into like agents that can do the same stuff at the higher level. So the takeaways are this. Um, the loop is the product. You try to automate yourself as the uh as a um higher level judge, and you want to make sure your second loop agents are able to apply the same judgment to the agents you're trying to push the prod. Second bit, system dislation is the mode.

So how do you continuously inject that taste into these workers and they how how they continuously self-verify and work together is uh the biggest thing that you should focus on, and the faster you do it, uh the the the faster you you build a defensible approach to becoming a vertical AI company. And finally, valued work per watt is how you should measure am I making progress or not? So first make sure that uh the the the work you're generating is valuable.

Second make sure that the economics make sense and the um the the difference in price is is basically what um people would would switch away from cloud code to something you provide. We've been thinking a lot about these ideas, and we're building some very interesting products around how to deploy this in production. We'd love to hear from you.

We'd love to get um to to uh understand more about how how how certain um vertical SaaS companies are are looking to go to prod with um or uh how agent labs have been thinking about this idea of um um uh creating these like auto research uh labs uh uh around their their own products. Um get in touch uh we're gonna be around the block for for chatting more about this and thank you very much to tell


────────────────────────────────────────────────────────────────────────────────
## RUSHAB
**Affiliation:** Machine Craft / Founder
**Talk:** The Factory That Taught Itself to Remember: AI Without Data Science
**Time:** 06:48:26 – 06:54:11

[06:48:26]
you a story about a factory that taught itself how to remember. Hi, I'm Rushab. I run machine craft, a hundred people factory in India. No data science team, no ML budget, none of that. And somehow we ended up building a 36 AI agent that runs our entire go to market. I think that's still a rid a little ridiculous. Let me show you how it happened and why you can do the same thing. So here's the thing about our company.

From the outside, it looks like machines in metal, but the actual company, the part that matters is in the machines, is the knowledge, who the customer is, what we quoted them in 2019, why that one machine needed that weird custom tweak? And for three generations, all of that lived in exactly three brains. Initially my grandfather's, then my father's, and now mine. Which is a

[06:49:24]
genuinely terrifying way to run a company when you sit with it. A lot of people have joined us, people have left us, the revolving door never stopped. And every single time someone walked out, a chunk of our brain walked out with them. We weren't scared of the competitors, we were scared of forgetting. Or waking up one day and realizing the whole company only existed inside two increasingly tired heads. So I had an idea. I'll be honest.

[06:49:56]
Sounded insane first. But what if instead of writing the knowledge down in some document nobody ever read What if we grew a brain that just held it? Not a chat bot you poke at, a twin of the company. I didn't hire a sales team. I tried to build one. A quick detour because you need to know how messy this is. We make thermoforming machines, they heat up a plastic sheet and shape it. Same core machine, but it ends up making hydroponic farm trays, spa bathtubs, EV car panels, medical casings and even packaging. Seven totally different

[06:50:38]
worlds, seven totally different buyers. So this brain couldn't just memorize a brochure. It had to know which universe a given customer lives in. Step one was almost boringly simple. Feed it everything, and I mean everything. Years of quotes,

[06:50:57]
drawings, payment schedules, timelines, email threads, hundreds of gigabytes of our own private history. Not the public internet, our internet. And here's the plot twist. The part that surprises every engineer I tell this to. We never train a model. No GPUs humming in the basement, no fine-tuning. We just looked at all the history, chopped it into bite-sized chunks, and let offshore models read it and pull out the facts. We store the meaning of each chunk as vectors and relationships. Who's connected to what as a graph?

The brain is in a smarter model. It's actually a really really well organized memory. Now, this is where it gets a little weird in a good way. We stopped thinking of era as a software and started thinking of it as something we were raising. So we gave it a body modeled on biology, senses to figure out who it's talking to, a gut to digest the documents into facts, a memory, a dream cycle, an immune system to fight off bad information. Why biology? Well, because evolution already spent

[06:52:11]
a billion years solving, how do you stay coherent over time? We just copied the homework. Okay, so the big question, why 36 agents instead of one genius megaprompt because and you already know this if you've ever tried it, one prompt that's supposed to do everything ends up doing everything badly. So era isn't one mind, it's a pantheon, a whole cast of specialists. Each one has exactly one

[06:52:42]
job. Athena runs the room. Prometheus owns the sale. Plutus does pricing. Hepastis knows every machine spec cold. Vera facts checks everything and Memin, my favorite, guards corrections. So the second a human fixes something, it stays fixed forever. One agent, one job, it's a team, not a hero. And here's the cool part: they hold meetings. Athena pulls in specialists. actu Theyally argue and a single answer comes out the other side. It's like having a boardroom that never sleeps, never gets tired and somehow has no ego.

So what does all this actually run? Honestly, the whole front business. Everything between a stranger exists somewhere and now they

[06:53:37]
are a customer. Nine concrete jobs every single day, outbound emails that actually reference my real world, account briefs built from cross-checked through before a call, quotations, a swipe left, swipe right mode for outreach, reviving dead leads which I call b blast from the blast, inbound replies and figuring out before we waste an hour whether a company is even a fit. Nine jobs, one operator who never sleeps.

[06:54:11]
Where does all this live? One cursor tab. That's genuinely it. You type and era reaches out with a dozen hands, searches the knowledge base, reads the inbox, drafts the email, builds the code, and then shows you before anything actually goes out. Under the hood is genuinely a real stack, not a demo held together with a tape. Databases for vectors, for relationship graph, for the CRM. Three different model providers, each picked for the job it's actually best for.

Tools for Google for swallowing documents for every communication channel plus monitoring, so we can see what it's thinking.


────────────────────────────────────────────────────────────────────────────────
## ARENA (Supercell AI Lab)
**Affiliation:** Supercell AI Innovation Lab
**Talk:** Project Paradox: Auto-Research for Multi-Agent Village Behavior
**Time:** 06:54:54 – 07:15:46

[06:54:54]
All of it, every Okay. Hi, everyone I'm Arena, former

[06:55:12]
engineer at Microsoft and Supercell, and today I want to talk about auto research in a multi agent AI village. I will use a video game like AI Village as a running example here, but the broader question is one I think many AI engineers are starting to run into. How do we evaluate and improve agents that carry state over a long period of time. Before I get into

[06:55:42]
the auto-research layer, I want to talk a bit about project paradox. We developed project paradox at Supercells AI Innovation Lab. Me and my teammate Arnachal Manikandan. We built a modular AI framework that allows any developer to plug in intelligent autonomous agents within a video game that can interact, compete, or cooperate with other players or agents as well, and place them uh and make them into dynamic game companions. Now, to give examples of what these agents can

[06:56:21]
do, the agents can move with intent. They can go to any location or person, and they're guided by their own memories, emotion, or curiosity. These agents can interact with

[06:56:35]
the world, they can pick up objects, drop them anywhere, and they're also aware about the context in their own environment, such as objects or other characters or agents as well. I would also like to note that game developers can also add new actions for these agents to accomplish within our framework as well, instead of just dropping or placing objects. Agents can also obviously react to what's happening

[06:57:05]
around them and these events that happen around them affect their own beliefs and emotions on the fly as well. And of course it wouldn't be complete if agents can't start conversations, right? Agents can in this scenario approach other

[06:57:23]
agents or even the player as well and this makes the game feel more alive and of course these conversations are stored within their memory and is according to their own um and affect their own emotions and beliefs or goals as well. And all together these agents make our

[06:57:47]
multi-agent framework So the architecture was intentionally stateful behind this.

[06:57:59]
The first important part was per agent memory. Each agent has its own memory namespace backed by RAG, so memory did not bleed between agents. Second, we tracked emotion as a small vector. So after an event or conversation, the system could update values like joy, sadness, fear, anger, or disgust. Third, agents had belief scores towards other agents and the player. You can think of this as a trust matrix, basically.

Like after the interaction happens, the LM basically decides whether the trust score should go up, down, or whether it shouldn't change at all. And fourth, every memory receives an importance To explain this better, like let's say

[06:58:54]
you had dinner a few days ago, you probably won't remember what you had for dinner, right? But um uh if someone was murdered a few days ago, you definitely remember that. So the agent will evaluate, or the LM will evaluate an important score of an event, and if it crosses a threshold, it will store that specific memory in a separate cache so that important context can be

[06:59:23]
retrieved better later on. And here's an example of it just working, we're going to ask one of the characters to go on a picnic with us. Here, our character Blossom uh decides to pick up a pastry and go to the picnic area because we asked her to do so. Keep in mind what during the conversation in the background, she plans all of these sequences of actions to accomplish, and one when we talk to her afterwards she will also reply within context as well. Yeah. But this

[07:00:05]
is where an interesting problem actually started. As you saw in the last example, like for short-term gameplay, this our architecture worked pretty well. Like a character could make a plan, move around, talk, and remember the recent interaction and respond to us or other characters as well. But over longer horizons, this is where we notice the social consistency start to get weaker.

So in this example, we have one agent spreading a rumor about a sale on mangoes to another agent, and that agent receives that information and goes and tells another agent about it. Later on, after a number of events have occurred in between, when the player asks one of the agents about the mangoes, it doesn't exactly, store that context that we were expecting, or it doesn't give us the context that we kind of want it to. And this is where things are starting to get messy naturally.

Like the system may remember the rough topic but lose the source of the topic. A rumor may become CERN instead of just a rumor, like the agent might state it as a fact. Or an agent might know a fact, but fail to execute, fail to remember it while creating a plan for its actions. So the question here became, how do we improve a multi-agentic system over long-running social behavior and not just over

[07:01:40]
one response. And this is where we wanted to bring in auto research, as you all know. A few months ago, Karpati posted our auto research, and this made us

[07:01:55]
immediately very curious. Perhaps we can make the system run experiments on itself, and can we use this for our system as well? So what we understood is instead of manually tuning a prompt or watching one nice demo, we could define a scenario suit, run the agents, collect traces,

[07:02:18]
score the behavior, and change a small policy surface and only keep the changes that actually improve the score. And this is where we're trying to bridge project paradox with auto research. So at this point basically our multi-genic framework project paradox is more like a lab bench and auto research becomes the experimental loop around it. And importantly, this is not only about improving RAG retrieval. The broader framing is optimizing the agent protocol.

Like how do agents write memories, retrieve them, communicate uncertainty, update trust, attribute sources, and

[07:03:00]
replant uh uh around new facts, basically. Um yeah. In this context art yeah. In this context, art research is a not another agent in the village, like I said. It's a meta system outside the village. The villagers have local perspectives, of course. They only know what they saw,

[07:03:29]
heard, remembered, or inferred because there isn't a common memory database in between them. Information only travels once other agents communicate them properly. The auto research layer has a different job here. It reads the full traces of a run, compares what happens against the scenario ground truth, scores the

[07:03:54]
behavior, and proposes a constrained change to the agent protocol or cognitive policy. Then it reruns the scenario and asks society level behavior, like did society level behavior get better? This is the key shift we were trying to look for. So we were no longer evaluating one answer, we were evaluating an entire run. And this is what one of the loops would look like. Like first we define a control scenario, which I'll elaborate a bit more about later. For example, one agent learns a public fact or one agent hears a rumor.

That could be a controlled scenario. Then we run the simulation. During the run, we collect structured traces, observations, conversations, memory rights, retrievals, belief updates,

[07:04:49]
whatever is relevant to us in that case, we collect. Then we score this behavior. Did the information spread as we expected it to? Did the source attribution survive? Such as does the agent remember who started the rumor? Did uncertainty stay uncertain? Did agents act on what they actually knew? And then the auto research layer here proposes a small policy change. And this is important. It should not rewrite the whole application, of course. It should only edit a controlled policy surface. And then we rerun.

If the score improves and the guardrails hold, we we keep the

[07:05:36]
improvement. And if not, we simply just revert back. And talking about controlled scenarios, the reason why uh scenario design matters is that social behavior is otherwise a bit fuzzy uh in general, in the sense, if you just let the agents in our environment wander around, it might look cool and you might get nice interactions. But it's actually very hard to evaluate on whether the system actually improved. So this is why we believe you need controlled scenarios. For example, one scenario could test a public fact diffusion.

[07:06:19]
Let's say agent A learns uh the bakery will close tomorrow. Do the right agents learn it? Do they remember who said what? Do they remember do they change their plans based on this fact, another scenario could test rumor uncertainty. Agent, let's say agent A hears that agent C

[07:06:42]
might leave the village. When this rumor spreads, does might leave suddenly become is leaving or does it stay as might leave? Like does it become a fact or does it still stay as a rumor? Another scenario could test

[07:07:00]
replanning. The group has a plan, but one agent learns, let's say the group uh they wanted to take is blocked. Do agents update this and communicate this uh with each other to avoid improper plan or stale actions. The

[07:07:18]
point is not that these exact scenarios are universal here. The point we're trying to make is that long horizon agent behavior needs scenario suits. And talking about our mango

[07:07:33]
example again, after running one of our auto research loops. This time after uh a long period of time when the player finally asked one of the agents about the sale on mangoes, we did find that uh the the agent was able to uh respond within context this time,

[07:07:57]
like compared to last time. Um yeah. And for this talk, the form the exact formula we believe is less important than the shape of the scorecard. You do not want a single vague metric like agent quality. This will hide all the interesting failures. Instead, you want a balanced scorecard for diffusion, you might measure reach, like how many

[07:08:29]
agents know the fact after end steps. For provenance, you measure source retention among agents who know it. How many remember it, where it came from, etc.? For rumors, you can measure uncertainty preservation and false certainty rate. For planning, you can measure action consistency and time to replan. And for privacy, you can measure containment. This matters because optimizing only one metric can create bad behavior.

Because let's say if you only optimize for diffusion, the agents may learn to overshare everything and let's say if you only optimize for memory recall you might create noisy or stale um like memories. So this scorecard is what keeps the system honest and prevents the auto research agent from gamifying the

[07:09:25]
system to just increase one specific score. The other important engineering lesson that we learned over this project is that it's important to keep the editable surface really small. The auto-research layer should not have permission to randomly rewrite the whole code base. Instead, it's really important to freeze the

[07:09:53]
harness, the scenarios, and the metrics. So we're only exposing the part of the system that we actually want to optimize here. In project paradox, for us, that meant things like memory writing policy, retrieval policy, communication prompt, belief, trust

[07:10:12]
rules, source attribution, replanning triggers, etc. This gives the search process room to improve behavior, but it also prevents it from gaming the evaluation directly, as we mentioned before. And this is the difference between the LM writing random patches versus the LM actually searching within a controlled policy space.

[07:10:38]
And here are examples of the kind of changes I want this kind of loop to search over. If if source attribution disappears, the policy change might be preserved source in memory and uh right uh memory rights and summaries. If rumors harden into facts, the policy change might be store confidence, mark firsthand versus secondhand and require hedging when

[07:11:07]
retelling uncertain claims. If public facts stay local, the policy change might be classify useful public facts differently and make agents proactively share important source evidence. The key is that these are small changes to the agent protocol, but they can have larger effects on a society level behavior for multi-agent systems. This is also where I kind of want to be careful about our claims here because with we believe without repeated current loop results, like I wouldn't say the system does generally improved. We're trying to say this

[07:11:49]
is the right kind of surface to expose to an auto research layer uh loop because it is small enough to control, but it's still rich enough to change the social behavior to some extent at least. And the biggest

[07:12:05]
lesson for me, perhaps, was that memory is not enough here. You can add a rag memory to an agent and still not get the current long-term horizon behavior that you were looking for. Because agents need to sometimes know

[07:12:23]
where that information came from. You need to preserve whether it was firsthand, secondhand, verified, or uncertain. Sometimes you need to separate raw episodic memories from what the agent currently believes to, and you need to test behavior through scenarios, not just through vibes. So the other lesson is that uh rollback also is not optional. When you optimize social behavior, a change can improve one thing and damage another. So a policy that spreads public facts faster might also leak private information.

A policy that increases recall might increase stale memory usage. So the loop should basically be like a ratchet. Try a change, score it, keep it only

[07:13:13]
if the scorecard improves and guardrails hold. And we we definitely believe this is not only relevant for game agents. Because although I gave you an example using a game village, we believe like, let's say, for example, support agents. Support agents need to know which policy update comes from where, right? And whether it supersedes an older answer. Personal students, for example, need to remember commitments that they previously made and make corrections if the user wants to change

[07:13:50]
those personal commitments. Research agents need prov uh provenance, citations, contradiction handling, and hypothesis updates. Coding agents need long-running context across issues, files, teammates, and changing requirements. Workflow agents need access controls, handoffs, and replanning when the world changes. All of these systems have the same underlying problem. They maintain state over time. And that state affect affects future action.

[07:14:22]
So they need control scenarios and behavioral scorecards, is what we are proposing. So again, in brief, a recipe for long horizon agents. If there's one practical recipe I want you to take away, freeze the harness define scenarios, log traces, score behavior, and expose only a small policy surface. Search over these changes, keep only changes that survive your measurement. And this is an engineering pattern that we believe would make sense. For long-running agents, the real question we

[07:15:04]
believe is: across controlled runs, does the system behave better. To close, Project Paradox started as an attempt to make game agents feel alive in a 3D world, but the deeper engineering problem was not animation or dialogue for us, it was the state, such as which agent knows what, which agent told whom, what is true, uncertain, or outdated, and do agents act on what they remember. Autoresearch gave us a way to approach this a bit more systematically. Not by trusting one demo, not by endlessly hand-tuning prompts,

[07:15:46]
but by running control experiments and keeping only the changes that survived our measurement. Long horizon agents need experiments and not just prompts, and I hope that's the takeaway that you get from this talk. And yes, please do connect with us. We'd love to talk if you have any


────────────────────────────────────────────────────────────────────────────────
## AMOL
**Affiliation:** Nori Agentic / CEO
**Talk:** AI Employees: Structured HTML Output for Knowledge Work
**Time:** 07:16:08 – 07:21:53

[07:16:08]
questions. Thank you so much for listening. Hi, I'm Amol,

[07:16:22]
CEO of Nori Agentic. We deploy an AI employee that understands your company, your code, docs, Slack, and other kinds of data. We spend a lot of time thinking about how coding agents really work. Most people think coding agents only write code. But if you ask me, that's just bad marketing. Forget the name for a second. Coding agents can do almost anything. There's just one trick. You have to be able to think like an agent to get it to do what you want it to do.

Today we're going to talk about how we use coding agents to do something most people think agents are terrible at. Make visual artifacts, like slides, docs, and yeah, even video.

[07:17:10]
Every day the world pours something like 34,000 human years into making slide decks. Most of that time isn't the thinking, it's the fiddling. A deck that takes 10 hours should really take about 25 minutes once you remove all the formatting and the branding and the moving things around. Say you need to make a slide. What do you do? You open a tool, PowerPoint, Slides, Figma, Canva, and then you start manipulating a canvas. Every one of these tools is built for human hands and human eyes. Click, drag, drop, resize, snap to grid.

All motions and patterns that make sense for our geospatial view of the world. There is a data structure underneath, but it's in a format that only the application can read. What happens when you hand these tools to an agent? Well, the output comes out all wrong. Things overlap in weird ways, you can't see the text, there's no alignment, it's just garbage. AI skeptics say that it's not just the tools. Agents fundamentally can't reason about space, and there are whole benchmarks like ArcAGI that are built exactly around that premise.

There's a famous little test for this from developer Simon Willison. He asks every new model the same thing: can you draw a pelican riding a bicycle? But there's a trick. The agent is only allowed to use SVG. It's a quick gut check for whether a model can reason about space at all. Here's some examples of what the models actually give you on this test. And yeah, these are pretty bad. Like genuinely, deeply really bad. So does that mean it's hopeless? Agents are just doomed to be bad at graphics? No, I don't think so.

If you ask me, it's not the model, it's the medium. If I asked you, someone who is presumably human, to handwrite an SVG of a pelican, you wouldn't be able to do that either. SVGs are just a wall of numbers. You can't go from a wall of numbers to a pelican. You just can't see that way. That's just not how people think. We think graphically. So we built tools that let us draw on a canvas. Figma MCPs, PowerPoint CLIs, screenshot and replace loops, what do all of these agent tools have in common? They all approach the problem like a human.

But an AI is not a human. Asking an AI to use a canvas is like asking a human to write SVG by hand. It doesn't really make sense. You need to give the AI tools based on how it thinks, not in pixels, in language. Words, tokens, structure. That is its native medium. Imagine a language that's

[07:19:56]
incredible at describing layout, that models have seen and trained on billions of examples of, that they understand intuitively, that renders to pixels and can run everywhere. Oh, right. HTML

[07:20:11]
lets a model think in structure. HTML tags have meanings built into the language. A heading, a chart, a grid, and the browser turns it all into pixels. So the model never actually places a coordinate, and you can get all sorts of visual effects, charts and layouts, fonts and motion, all of it, for free. Remember that pelican from earlier? Now ask it to do the same exact task but in HTML. Same bird, but now it's in a structure that the model can reason about. And you can read and theme and edit every single line of it.

I spent my whole life building slide decks with PowerPoint. So I always thought that those two things, slide decks and PowerPoint, were synonyms. But that's just not really true, is it? PowerPoint is a tool that you use to make slide decks. The deck itself, that's just the presentation mode. And as it turns out, no one in your audience is gonna care how you got to the presentation mode, the editing format is totally arbitrary.

So you can just pick the editing format that the agents are already good at, HTML, and if you need to, render to a different format like PDF later on. We use this HTML trick to build all of our slide decks, our board decks and our sales decks. These are real things that we actually present and send out constantly. We use it for our docks too. It gives our docks color and vibrancy all while following our brand. And of course, we also use it to make videos, like this one. What you're watching is just HTML and CSS.

It's literally just divs all the way down. Almost everything is better

[07:21:53]
with a little structure and a little bit of color. Plain text is a choice, generally a choice of convenience, but it's usually the wrong one if you're actually trying to create something of use. Now, I do want to take a quick beat here and point out that a beautiful deck on its own is generally not worth anything. You still have to go and get all of that content, all of the things that actually populate that deck, right? Well, again, we can think like the model.

If you just give the model access to your data, say your call transcripts or your emails, you can have the model build the deck end-to-end. Let your agents do all the grunt work while you focus on vision and story. That's what Nori Sessions lets you do. I've built entire board decks for my phone on the subway during my commute. Why? Because our Nori bot lives in the fabric of our company. Of course, Nori ships with everything you need to make this all work, so don't bother reinventing the wheel. That's my little wheel, thanks for listening.

If you have just one takeaway, it's this. Stop thinking like a user. Think like the model. Give it the right language. And for graphics, all you need is HTML. Hi


────────────────────────────────────────────────────────────────────────────────
## AUREL ZAYN
**Affiliation:** Unknown / Mobile Software Engineer
**Talk:** Cloud Sandboxes for Mobile Development: 10x Productivity
**Time:** 07:23:11 – 07:32:07

[07:23:11]
everyone. Ten X. You feel it yet? Hi, my name is Aurel Zayn and I'm a mobile software engineer for the last 14 years and I'm here to talk to you today about 10x reimagining the mobile dev workflow. So you know, back in the old times when cursor was that thing you make with your mouse and uh AI agents were that dystopian character from sci-fi books or movies, whatever fits your style. You know, just a few months back. Back then when we thought that we will still be using our IDEs just maybe slightly better.

And now we know that we already switched to like chat style, um uh engineering when we discuss with Cloud Code, Codex, cursor, whatever. Um and we just tell them what to do and we don't use our IDs unless it's for debugging or something that the agent couldn't figure out. And that in theory should have made us ten times more productive, right? That's what everybody says, right? With are we ten times more productive? Do you feel it?

I don't know because, I can't feel that we are ten times more productive, not as a single engineer and not as a whole group and not as the whole company. So why is that? Why don't we see the promise of ten times more productive Cam to an actual life. So you know they tell the story about how when factories switched from steam engines to electric engines, at first they didn't see that big of a gain.

So yeah, the electric engines were better, they were more efficient, but they didn't see that 10x, 20x, 30x uh more productiveness that they have been promised. And the reason for that was that they only changed the steam engine with the electric engine. But the real gain came some years afterwards when they had to stand that it's not only about changing the engine, it's about changing the whole workflow.

Because you see, they used to have like one giant big steam engine in the factory and all of the machines were rearranged based on their power consumption and their proximity to

[07:25:18]
that steam engine. So it wasn't organized by the workflow that it should have been. Like from the start to the end of the workflow. No, it was designed by proximity to that central engine. When they realized that, and they also realized that they could take the electric engine, make it smaller, and put it inside each machine and then they rearranged the factory to make it work as the workflow should because now it will it was made possible. Then the real gain came.

Now they were 10 times, 20 times, 30 times more productive than they were before. Not because of only changing the engine, but of changing the whole workflow. And that is what I want to talk to you about today. Let's think how we I make things that weren't possible before possible now and we can change our workflow and then becoming ten times twenty times more productive. To do that, let's look at the current workflows.

The PMs have an idea, they iterate with the designers, they iterate with the user, they iterate with the dev, they iterate then back with the designer, then they iterate with the QA and they iterate back with the dev and maybe after all those iterations maybe you have something in production. So what was that word that was repeating so many times? Yeah, iteration. And this is the problem because iteration creates friction. Each iteration creates

[07:26:51]
context switch, create time waste, creates communication that needed to be done, sync synchronization that needed to be done. And AI didn't eliminate all of that. AI spill up code, but it didn't eliminate the friction, didn't eliminate the iteration. Why is that? So let us reimagine what we could

[07:27:15]
do. Bear with me for a moment. What if? What if? What if instead of using one tool for designing, another one for testing, another one for coding, and then another one for releasing. What if we could use one tool? One code base? What if instead of designing on Figma then sending a design dog to the developer in order for them to figure out how to um make those uh designs alive what if designers could actually design own code and then send the developer a PR?

What if QA could iterate with the agent itself just, getting a link with their simulator and they can tell the agent exactly what to test, what to be cautious of, and if they find something, exactly what to fix. What if we could make the dev workflow works on the code itself? What if God was one of us? No sorry I got carried away there. And you're probably asking how can we do all of it?

So one way would be to tell everyone to just download their Xcode and and their Android Studio and teach designers and PMs and QA how to build and how to uh test on simulators, emulators and blow to their laptops with a 200 GB on storage and whatever they do to the to our memory, that's one way. But let me guess that most of them would reject that idea. And for good purposes. So we can make another way. Maybe we just put it in our CI, right?

So we let the agent iterate with the CI so they don't have to download Android Studio and Xcode and everything. But you actually know that CI builds take between 20 to 40 minutes and we can't actually let our agent wait for 40 minutes just to understand that the iOS code that it pushed actually failed to build. So what else? What

[07:29:09]
can we use? Introducing cloud sandboxes. So cloud sandboxes are actually concept that has been around already for many years, just not for mobile development yet. Using cloud sandboxes, you can tell the agent here's an here's a CLI, talk to the CLI, create a VM, a small VM that runs only for this iteration. The VM boots up in 30 seconds or less, make the build, show them a simulator on their in up browser in the cloud code, codecs, cursor, whatever.

And then they can iterate over it, tell it to change that pattern, uh, to go back and test something, and change the code, and they push an open up R and then the designer can work on code, send the PR to the developer after they done. Developers make an iteration, make one, two, three, four

[07:30:07]
different VMs to run in parallel. They send the PR for review, QA can take it from there and tell the agent exactly what to test and tell it what to fix. And from there it goes straight to the stores for review. So let's see it. Let's see how

[07:30:26]
it should work. So imagine you see this screen. Imagine you're inside Codex for example. You have the chat interface to your left, you have the actual app to your right. The designer is iterating with the agent, tell it exactly what they want them to do, what they want to change, and see the changes immediately on their screen. Build time is faster, it's done on the cloud, and preview time is faster. Then they iterate some more, not with the developer but with the agent on their laptop without the need to install Xcode or Android Studio.

And once they done, they can tell the agent to take that code, open up R and send it to the developer. This workflow is what makes us ten times more productive not only because of using AI but because of using AI to change the workflow reimagine it and remove all that friction that we took from grant for granted in the old times. That is how we become ten

[07:31:32]
times more productive. Thank you. Hi everyone. My name is Gabe De Mesa. I'm an engineer here at OpenGov, and today we're going to be talking about agents in production, specifically how OpenGov built and scaled OG Assist. So this

[07:31:53]
presentation is going to be jam-packed with just so much good stuff. Uh we're going to talk about uh AI agents, we're going to talk about our harness, we're going to talk about um evals, observability, traces, we're going to

[07:32:07]
talk about um tools and skills. Um it's there's gonna be a lot of good stuff in here. We're gonna talk to you guys about uh what we do at OpenGov and how we operate at the scale that uh we operate at um in production. So you'll be able to see a real use case and workload uh with AI agents. Um so without further ado, let's get started. Okay, agenda. So just really quickly going to go through uh high level what we're going to talk about today. Uh, I'm going to tell you guys a little bit about OG Assist and what uh OpenGov is.

I'm going to tell you guys the origin story of how this all kind of came to be. We're going to talk about OG Sys Big Bet on Effect, a little bit into our core agent loop. We're going to talk about the A-2A protocol, evals, and sandboxing. We're going to talk about how we manage long context. We're going to talk about monitoring, observability, how we collect feedback, and how we iterate on that feedback.

We're gonna lastly uh also talk about tools and skills and how at OpenGov uh we use um AI not only externally uh that we uh serve to customers but also internally to improve our development workflows. Just a little bit about me before we go any further. My name is Gabe. I'm a software engineer here at OpenGov. I work on the AI agents team and uh I'm one of the folks that helped build uh OG Assist and some of the systems that you guys will be seeing today. So a little bit about OpenGov. OpenGov is a software company uh on a mission


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Afternoon MC Introduction
**Time:** 07:34:48 – 07:42:27

[07:34:48]
to power Please welcome our MC for this afternoon's programming,

[07:42:27]
Director of Technology at Oliver Wright America's Davina Delias. Good


────────────────────────────────────────────────────────────────────────────────
## DAVINA DELAYAS (MC)
**Affiliation:** Oliver Wight Americas / Dir. of Tech
**Talk:** Afternoon Opening Remarks & Speaker Introductions
**Time:** 07:44:36 – 08:04:12

[07:44:36]
evening everyone! Gosh, I am so grateful to be up here with you. House AIE 2026! Thank you for being here live and online. Thank you so much. So um apologies. Davina Delayas, Oliver White Americas, we do integrated business planning and strategy consulting. So honored to be here with you all. We covered so many grounds. Buts, and most of all, your networking sessions. Have you met all of your friends tonight? Yes? No? Precious. Am I the only one who thinks the more I know, the more I don't know? Show of hands. Oh, thank you. What? Pity?

Hands up? Oh I'll take it. Thank you. But thankfully for us, the expo has a mass of wonderfully supportive sponsors and expo partners ready to assist you in your business and personal projects for best practices. Talk to them, visit them, let them help you achieve your goals. Check out the dancing robots take a picture with them win the giveaways check out start start a battlefield tonight um

[07:46:12]
and talk about best practices This next speaker is someone I truly look up to and honored to make his introduction. His achievements are so vast, it's hard to wrap them all up in a few sentences. So I'll use his humble words instead. He's an author, an educator, advocate for AI best practices. He translates complex technical concepts into accessible learning materials. I am truly excited for what he has to say for us. Give a huge round of applause for Adios Mani Howdy folks. So good afternoon or

[07:47:13]
good whatever time it is when you're watching this on YouTube. I'm really excited to be here. And today I want to talk to you about really what it takes to keep the human in the loop where engineering is concerned. I really want to start with the human side before we talk about the architecture here. I think that the engineer of the future is going to be really defined by the person who is able to choose what is worth doing.

They're going to own the evidence, they're gonna own the understanding, as well as the verdict around increasingly automated work that's being done by agents. Now, when I use the term verdict, I don't mean that we're suddenly all gonna be judge duty. We're not. But what I mean really is something just a little bit different. I mean we're gonna be accountable for the production decisions. Does something ship? Do we block it? Do we redirect it or accept the risk? Quality is something that we all talk about a lot, but quality produces evidence.

A verdict assigns responsibility. And answerability is really what lets us

[07:48:28]
stand behind a verdict. And this, of course, is not the only way that our industry is starting to think about our roles evolving. Boris Cherney recently put some useful

[07:48:40]
language around what many teams are starting to feel. The old craft boundaries are getting blurry, and roles are rebundling around the work itself. And the important question here becomes a lot less about what is your title and more what part of the system can you own. Now, I like this taxonomy quite a lot. It's optimistic without being overly vague. So things like prototype, build, sweep, grow, and maintain, and these are real engineering modes. Agents are gonna help with all of them, but the scarce thing is not merely doing the task.

It's gonna be knowing which mode your product needs and what quality bar applies and who owns the result at the end of the day. Now we've been talking about harnesses and loop engineering in software factories over the last couple of days. We can talk why this shift is happening. We've moved past the model as the whole story, right? With harness engineering, the coding agent is the model plus the harness around it, right? Your context, your tools, your file system, git.

And the harness is what turns intelligence into something that you can delegate to. The next move was loop engineering, where we weren't just prompting one run anymore. We were designing systems that kept prompting, checking, and remembering and deciding what happened next. And that's really when agents started to feel like infrastructure. And once you start putting all of those things together, you get that software factory.

Dex covered this well in his talk, but you have agents that are running inside that inner loop and evidence that comes out. Humans still end up making the production decisions in this loop. And the wind really isn't moving us from it. The win is moving human judgment's the highest leverage checkpoint, I think. And this is why it starts to matter now. AI-generated and AI-assisted code is becoming normal code for a lot of us. One of Sonar's 2026 surveys said that AI-assisted code is no longer marginal.

It's increasingly having a large role in our code bases, and once that happens, answerability stops being this philosophical world, it becomes an engineering requirement. And there's a quality point here as well, right? Like we used to care about clean code, code that people could read, but cleaner code is actually not just gonna help the next human and the next person on your teams, it actually helps the next agent.

Another one of Sonar's research uh studies found that clean and messy repos had roughly the same pass rates, but clean code actually used fewer tokens and cost fewer revisits. So there's a lot of benefit to maintainability that can fuel efficiency for your factories. Now, making generation cheaper does not

[07:51:21]
automatically make review cheaper, right? I think a lot of us are facing this moment, and we know that engineers are not naive. The sonar numbers say that almost everybody is skeptical of AI code. I love working in my software factory, I love building my engineering loops, but the problem is still capacity. If 96% of people don't fully trust that code, but only about half always verify before committing, we have this danger that we've got distrust without bandwidth.

And so safety comes from making verification cheaper, clearer, and harder for people to skip. And if you zoom out from the individual reviewer to the organization, review and validation start becoming a bottleneck when governance isn't able to catch up, and adoption is already moving way faster than any company can go and set their policies. And this means that we have some hard questions we have to deal with: like, did a model actually touch this file? And the hard questions are also like what constraints guided that work?

What evidence was produced? What risk was accepted and who owned the result? Now, the agent can ship more than any of us can review, right? So what are we still good for? I think it's a question that's on a lot of our minds, right? And you know, if Homer Simpson's experience automating computers can teach us anything, maybe this is our future. I don't think it is. But it's one direction things can take. Now let's try that again.

If change is where humans enter the loop, if generation scales faster than comprehension, the scarce resource becomes judgment that's backed by evidence. So the question is no longer how much can the agent do, but where does human judgment still create leverage? Now, I want to talk to you about two terms that I'm gonna use for the career part of this talk: alpha and decay. Alpha is the gap between what you can do today and what current models can do. That gap is a very real thing, and decay is the clock on that gap.

If the thing that makes you special is a capability, the frontier is eventually going to come for it, right? And there's a whole conversation around this. This is one of the reasons why taste keeps coming up. Paul Graham had a point here that I think is very right. When anyone can make anything, choosing what to make becomes very important. And I buy that. But I also think that we have to be very careful because taste can become a magic word for whatever part of the work we don't want to explain just yet.

Mitchell Hashimoto gave us a more useful version of this definition. Taste is the ability to make high quality, qualitative judgments where no objective metric exists yet. That matters because it puts tastes before the benchmark and before the market has fully voted. When you try out a model and you see the kind of UX and the kind of experiences that it builds, you can often tell when you think it has taste or lacks taste or when there's a gap there that humans can fill.

Now this is also only useful if we can turn some of this concept around taste into critique, examples, and better judgment over time. So yes, taste matters when production gets cheaper. And if anyone can generate 10 options, the scarce skill is really knowing which option deserves to exist. But taste is not some eternal moat. It's alpha as well. Now, the people with taste are still gonna matter. I personally think they're still gonna matter for a long time. But the best version of that skill is not mystique.

It's making better calls and leaving behind examples that your team and the system can learn from. Now let's apply the decay test. Well, we used to have speed, that decayed. We used to have recall. You know, harnesses have memory. Verification is moving into harnesses, evals, static checks, and model critique. Taste, I continue to think this is going to decay much more slowly, but it still resets as models learn from examples and preferences. Even judgment in some ways is a slope rather than a wall.

So the strategy is not to cling to any one capability, it's for us to keep moving our edges up a level. So this is one of the reasons why what can the agent do is not the best strategic question anymore. The list of things that agents can't do just keeps shrinking. The better question for us is really: what can only a human be answerable for? Not because, you know, any of us are magical in any way, but because some decisions actually require ownership. They require context, risk acceptance, and responsibility after that

[07:56:07]
work shifts. This is why the word engineer has to get just a little bit stricter. More people than ever can now make computers do things, and I think that's truly awesome. The total addressable market for builders has never been larger, and that's so cool. But it's a huge expansion of the leverage. An engineer is not merely somebody who can code, you know, and get things to exist. An engineer can reason about systems.

They think about constraints, you defend trade-offs, you can manage risk, and you're the person that can be reached out to when things start to break. So what are things that engineers should avoid if we want to stay effective and accountable in this moment? Well, the first thing to avoid really is cognitive debt. Now cognitive debt is the erosion of your understanding and memory around how to solve problems. I think a lot of us start to feel this the more that we're using agents every single day. I know that I feel this a lot.

And it's because we're deferring more and more to AI to solve our problems. For code, it's the gap between how much code exists in your repo and how much any human on your team genuinely understands. And this is why things like delegation depth end up mattering. You can have a build that passes your tests, a PR that you can merge, but your team can still end up losing its ability to actually explain the system that they are shipping to production. Now, a very real pressure is all much is also how much we delegate.

So agents can now stay inside the system long enough for the human to lose the thread. So a 30-second run, right, can feel like an interaction, but an hour or a day scale task, so something long horizon, that's a work stream. And when tasks can end up lasting that long, especially when you begin running many of them in parallel, review can't just be a glance at the end. It has to become a whole control system. The second thing to avoid is cognitive surrender. Now, this is when you blindly accept AI's responses. Like, delegation

[07:58:08]
is important because delegation says, do the work, then show me enough evidence that I can judge it. I still make a judgment in that situation. Surrender is really saying, hey, your answer is now my answer before I have formed any opinions myself. Now uh Gordon did a study that kind of offers us a warning light here. When AI was wrong, 73% of people still thought that they you know they picked the wrong answer and they felt more sure. So the failure mode is not using AI, but it's borrowed confidence.

The third thing to avoid is orchestration tax. Now, if you've been in the Bay Area, you will see people who, for better or worse, are still walking around with their laptops open or are talking to you about cloud agents. And we're increasingly trying to run more and more and more in parallel or telling each other that we're shipping with hundreds of agents or thousands of agents. More AI agents running does not mean that there is more of you available. Your cognitive bandwidth does not parallelize.

So every loop that you create ends up causing more decisions to route, merge, verify, and integrate. And the fix is not necessarily fewer agents, but it's about designing your attention like a system. Like where you enter, what you acquire, what you reuse. You just want to be very intentional about it. Now, accountability can be a scary word for a lot of people, and I wouldn't be surprised if it made you want to go hide in the bushes and just tell your agent to deal with it.

But accountability is not what remains after agents get good, it's what lets the rest of the whole system scale. If agents can do more work, if they can do it faster in parallel, better than what many of us could do, the scarce thing becomes the ability to explain intent, to inspect evidence, to accept risk and improve the system when the decision was wrong. Now

[08:00:06]
here is the career math. The half-life of an edge might be one model release. Speed, recall, verification, even taste all move as the frontier moves. But the half-life of a signature, your credibility, your expertise, is much longer. And

[08:00:23]
by signature, I really mean the name on the work, the person, the team, the institution, whoever stands behind what's actually shipped. So skills can earn leverage, accountability can turn leverage into trust. And this is one of the lines that I want to draw pretty clearly. Agents can choose, they can route, they can merge, they can escalate, they can operate inside policy. And in many systems, you know, they can, they should. But execution and responsibility are very different things.

The agent can follow your runbook, but it can't inherit the consequences. When something fails, the question is: who understood the policy? Who accepted the risk and who owns the blast radius? High agency is something that a lot of us talk about these days as being like this thing that we're looking for when we're hiring. High agency is actively taking ownership of your outcomes. So knowing when to delegate, when to inspect, when to stop, and when to put your name on the result. High agency in this world is not I personally do everything.

You know, that version doesn't really scale. It's not just hustle theater, but it's ownership with judgment attached. This agency ladder tries to make that a little bit more concrete. At the bottom, you've got someone that flags a problem and leaves it for the system. Higher up, they execute, diagnose, propose, recommend, and resolve. And the rare top movement is discernment. You know, maybe you find a problem and you decide whether or not it's worth investing in. Maybe it's not, and maybe you move on.

But when agents make more paths possible, agency is not chasing every single path. It's really just deciding which paths deserve your ownership and attention. So translate that into an operating model. Agents can run much more of the inner execution loop. They can investigate, implement, test, and report. I think that there's leverage in that. But that outer loop is still engineering. So deciding, verifying, approving, owning, that inner loop is capability, the outer loop is agency. And this is a boundary that I really care about.

Your agent returns evidence. It returns diffs, tests, logs, rationale, traces, trajectories, screenshots, whatever the work

[08:02:36]
itself requires. But then the engineering really begins. We decide whether the work was worth doing, we verify whether the evidence is enough, and we approve or redirect or own what reaches production. It doesn't matter if you're someone that's just working with a small number of agents or whether you're working with thousands of agents. I still very much think that these ideas apply. So the boundary is not human looks at AI output. The boundary is evidence and responsibility. So here's an operational rule. Explain it or don't ship it.

And it's not because humans have to type every line or read every line, but because someone has to understand the work well enough to defend it. If you've ever worked in a large code base or an enterprise code base, some code bases have this concept of an owner's file or certain certain subdirectories where there are people who are on the hook for that part of the system. You can think about this in a very similar way. Who's accountable for that part of your architecture in your code base?

Your model might write the code, and the question is really still whether you can explain those changes that the agent is shipping, whether you've got the evidence, where you understand the risks. Now, this is one of the things I want you to remember near the end. Automation moves the floor for all of us. Engineering continues to move up a level. And our new work might be loop design, evidence design, and brownfield stewardship, but fewer keystrokes doesn't mean less engineering over the next few years.

It means that there is more surface area that needs taste, verification, ownership, and ultimately care. I don't

[08:04:12]
think I've ever been more excited about the future of this field. Every time that we have made it easier We've predicted that the world would need less of it. And in fact the opposite happened. Higher level languages happened, frameworks, cloud, low code. The pattern always went the other way. And when you lower the cost, latent demand ends up appearing. Those ideas that people didn't think were feasible to build and get out there are suddenly unlocked. And agents are gonna do the same thing for a lot of people.

It's not gonna remove engineering work. It's gonna move the bottleneck from can we build this to should this exist and can we answer for it? So build the factories, keep the lights on, own the verdict. I hope this was useful. Thank you. Now, joining us on


────────────────────────────────────────────────────────────────────────────────
## ADIOS MANI
**Affiliation:** Unknown / Author & AI Educator
**Talk:** Keeping the Human in the Loop: The Future of Engineering
**Time:** 08:05:06 – 08:25:06

[08:05:06]
stage are the co-founders of Artificial Anal analysis, George Cameron and Micah Hill Smith. Hey, hey, good afternoon, everyone. I'm

[08:05:31]
Micah. This is George, and we are the co-founders of Artificial Analysis. Artificial Analysis is an AI benchmarking company. And today we're going to be talking to you about the cost of intelligence. A couple of years ago, when either of us would give talks like this, we would spend a bunch of time justifying why intelligence and cost trade-offs matter.

Today, I'm going to skip that whole part of the bit and we're just going to get straight into it because I would be shocked if I needed to convince anyone in this room why the cost of intelligence is an important topic for us to be talking about in mid 2026. So here's what we're gonna do. I'm gonna tell you a bit about who we are. We're gonna use some of our data to take a brief look at the state of the AI race. Then we're gonna spend most of our time breaking down the cost of AI today and what's driving it.

We're gonna use some data from our latest agente acknowledge work, Eval, AA brief guess. Okay. Artificial analysis. Independent AI benchmarking company. What

[08:06:39]
the heck does that mean? We build benchmarks and evals to test everything in the AI stack that matters to developers and companies making decisions about AI technologies. We test chips, cloud infrastructure, models, and agents. We try to figure out how smart the models are, how fast they are, and how much they cost. We publish a ton of that data on this website. Hopefully, some of you have seen it. And we work with companies throughout that entire AI stack to measure their technologies, help them in the world understand what they can do.

Got a handful of examples on the slide back there from some of our work with OpenAI, Google, and NVIDIA on their models recently. Let's have a look at the state of the race. Before I show the first chart, I'm gonna talk about an idea that is very important to the way that we think about building AI e-velts. The vast majority of the things that we foreseeably want AI to do, the models are still far too dumb to do. It's utterly profound what the models can do today. Things are pretty nuts.

And yet, because the future is so enormous, this is almost certainly still true. So what this means is that at any given moment in AI, we've got this concept that we think of as the intelligence frontier, what today's smartest models can do. If we think of most of the tasks being beyond that, certainly beyond that in terms of being able to reliably do them. That explains why so much of what all of us in this room want to do with AI is focused on what the absolute latest frontier models in any given point can do.

It also implies that there exists a set of tasks that are inside the frontier, and that that set of tasks is growing every month as new models come out. For that set of tasks, playing the intelligence cost trade-off is incredibly important because by choosing to not use the smartest model for every single thing, you can spend 10, 100, 1000 times less to get the same work done by the AI. The state of the race. We

[08:08:56]
publish a metric called Artificial Analysis Intelligence Index. We like to say that it is the best one number for understanding the AI race, but that if we thought you only needed one number, we wouldn't need to publish the rest of the website. What this metric actually is, is a synthesis across nine different evals that we run. We're at version 4.1 of our index. It includes a bunch of agentic stuff. It includes a bunch of hard reasoning QA type stuff. And we really do think that it is the best one number for your sense of what's going on.

We've got Claude Fable 5 on top. That little not currently available thing. I guess we get to go uh remove that from the website after this today. One of the things we like to do with our intelligence index is plot how it's changed over time. This chart here is the smartest model from each one of these labs over the last few years. Some of it hasn't changed that much. You can see open AI and anthropic trading blows over the last few years.

You can kind of see the dots getting closer together on the right-hand side on the x-axis because the pace of releases, especially over the last year, has gone up and up. You can also see all of the companies hot on the heels of the frontier who have been and are releasing models that achieve the same level of intelligence as those frontier models just months later.

If I take some of these lines off and all we look at is the smartest model overall and the smartest open weights model at any given point, we can draw this line and we can look at the gap between the open weights frontier and the overall frontier. In any given month, you can probably find a headline saying that open weights models are further from the frontier than ever, or that open weights models have just caught up to the latest proprietary models.

I think when we read this chart, what we see is that unfortunately neither of the extreme versions are true, and we see a consistent three to nine month gap that's held surprisingly consistent over all of the last three years. That's still pretty nuts, by the way, though. Because that does mean that within nine months of Mythos being announced, we are predicting that someone's gonna give away a copy of a model of smartest methos. You can hold us to that prediction. I'd be very surprised if this trend goes away anytime in the next year or so.

Beyond intelligence, we can plot a bunch of the metrics that you have to trade off against how smart the model is. This one's pretty simple. This one's the price of the tokens. This one actually might be surprising in a talk that we've called the cost of intelligence, because we all have this feeling that the amount we can spend on AI is skyrocketing higher right now. And that's completely true. But this trend here is also true. Token prices have continued to fall by 5 to 10x every year for each fixed level of intelligence.

Each of the lines there is a band of 10 points of intelligence index. I promise you that if you ever have to pick between a model that's 10 points higher on our intelligence index than another model, it's incredibly hard to find any task at all in the full distribution of tasks that the model that is 10 points dumber will outperform the better model on. Each one of these lines goes down incredibly quickly. It's a log axis on the y-axis on this chart, by the way. And the cost of tokens at the frontier has stayed surprisingly consistent.

But we look at cost per task across all of the evals and tasks that we run for our intelligence index, and yeah, the number is going up. This is the average across every task, which includes some agentic stuff, some non-agentic stuff, and so it's actually hiding how extreme cost per task gets in some situations today. If we break it out a little, these are kind of small, but we've got the highest numbers on the left there. GBQA Diamond, famous important open source evaluation data set from a few years ago. It's a reasoning evaluation.

We don't let the models work as agents. It's largely solved right solved now. We see from fractions of a cent per answer for each model up to about 50 cents. In our coding agent index and in our new AA briefcase agent acknowledged work eval, we see up to beyond $20 being spent on a single task. The most expensive task in AA briefcase is actually several times that.

Leading that of course we do have Claude Fable 5, although fun fact, it's kind of small here, but you can see Claude Sonnet 5 actually uses an enormous number of tokens, so it's nearly expensive. And our AA brief guest asks down the bottom there. But this is the thing that we're all feeling: that we're trying to do these really hard tasks. The frontier keeps moving. There are more things that we can ask the models to do than there were a while ago.

So we can spend enormously more per task than we could, even though that cost per token for each fixed level of intelligence is falling by five to ten X every year. These orders of magnitude are not things So I'll pass off to George now to

[08:14:18]
break down how we understand some of these contradictions. Thanks, Micah. So why does AI feel more expensive than ever? While for fixed levels of intelligence, the prices of accessing that intelligence instead of tokens is falling dramatically. And I think this is AI engineer world fair. We actually want to spend more. We want higher token budgets. When what

[08:14:46]
I'm gonna do now is use our AA briefcase benchmark to do analysis of this cost of intelligence. Our AA briefcase benchmark is our new agentic knowledge work benchmark. It benchmarks models on realistic professional tasks. There's four private scenarios, each representing weeks of human equivalent work. And do we ask models to complete realistic tasks? Then we grade models on the outputs of those tasks across three dimensions: rubric correctness, analytical quality, and presentation. Much like we think about assessing human work.

One of the differentiators for AA briefcase compared to other benchmarks is we've tried to make it as realistic as possible. When giving a task to someone else on your team, or when receiving a task, unfortunately, you're not given it on a platter with the precise information that you need to complete the task. You need to go out and find it. You need to trawl through emails, pick up on the latest Slack messages. That's what we expect for ourselves and others. And so we've tried to mimic this in the task that we're giving models in a briefcase.

The environments that models are completing

[08:16:15]
tasks in are thousands of files, messy Excel files, unstructured documents, structured documents and reports with hundreds of pages, emails, Slack messages, and we expect and ask of agents to complete these tasks, just like we ask of ourselves. When we look at the outputs of models in completing these tasks, you can see vast differences in the quality of the outputs. And this is how we assess the quality and intelligence of these models on these agent tech knowledge work tasks.

It also gives us a perspective on the progress that's been made over the last couple of years. On this task, which is a commercial due diligence task, GPT-4.0 presents a pretty basic slide. O3, a breakthrough model

[08:17:18]
that was released early last year. Thinking about that O3 was only last year is crazy to me. You can see that O3 produces a few bullet points, helpful, but not what we would expect of ourselves in completing this kind of task. And so this shows us the progress that's been made when we look at Opus 4.8's output and Fable 5's output, which goes a lot more in depth depth in terms of analytical rigor and presentation quality.

[08:17:57]
So let's look at how models completed this task and what it cost. If you remember Micah's slide, he showed that some models are taking uh using over $20 worth of tokens to complete these tasks. And so let's look at the drivers to learn a bit about the costs of agentic tasks. Four drivers to look at, and the key drivers here are token price, the number of turns in the agent trajectory, the token efficiency and usage of models, and last but potentially most important, the impact of prompt caching. Taking a look to start with the prompt

[08:18:38]
with the token prices. What we can see as a first takeaway here when looking at the cash hit rate, token price, the input not considering a cash hit or without a cash hit price, and the output token price. Firstly, is that there's orders of magnitude differences between the model. This is a critical driver. There's order of there's two orders of magnitude difference in terms of the token price, between Frontier models like Claude Fable 5 and still

[08:19:14]
good, very usable workhorse models like Deep Seek V4 Flash and GPT OSS 120B. The second takeaway here is the difference between the individual token or the types of token prices. You can see that there's vast differences in the cash hit price and the input token without a cache hit price and the output token price. And we'll get to that impact later when we look at token usage.

Next, these are long-running agentic tasks that we are now asking of models, especially in realistic environments where they need to navigate all of these thousands of files to get to an answer. And models are doing that. They're starting to really explore the environment actually similar to humans when

[08:20:03]
we search Slack and and and do similar tasks like that. You can see here with the breakdown of tool calls of models is that they're doing hundreds of calls and they're exploring their environment, their viewing images, their reading

[08:20:17]
files, their writing files to do ad hoc analysis that's going to feed into the slide output that we just saw. And this costs. Each turn is output tokens, and

[08:20:31]
then those output tokens flow into input tokens in the agent trajectory. And we pay for that. When we look at the output tokens to complete a task, we can see there's vast differences. You can see that Claude Sonnet 5, released only yesterday, used over 200,000 output tokens per

[08:20:56]
task. Compare that to your ChatGPT query uh a couple of years ago where, you might have been doing a couple of hundred tokens, couple of thousand tokens, maybe, two hundred thousand tokens to complete a task. And you can see here that models vary orders of magnitude. And this is driven by two things. This is the number of turns that we just looked at.

And secondly, it's the output verbosity of the model, both in terms of how much reasoning they're doing, how many reasoning tokens they're outputting to complete a task and also in completing their answer. It needs to put together that slide and all of that detail. That takes tokens. And we pay for those tokens. But stepping back, not just at output tokens that

[08:21:45]
the models output, but to total tokens that we're paying for, we have that on the left-hand chart here. AA briefcase token breakdown. Answer tokens, reasoning tokens, input tokens. Can

[08:22:00]
anybody see any in output tokens here? They're all input tokens. The vast majority of tokens to complete long-running agentic tasks are input tokens. You can barely see any output tokens there. And so therefore, the two token prices that we want to look at first is the input token price without a cache hit and the input token price with a cache hit. And if we remember that slide, there's vast differences between those models. And you can see that on the right chart here, which is the cash discount for a cash hit of an input token.

It's usually around 90% here, but it's also different for models and providers, whereby some models here uh 99% and now others are around 80%. And if we think about all the the vast majority of tokens being input tokens, you

[08:22:56]
can understand that this can change by uh multiples, a difference in a cash discount or a cash hit rate, the total amount of an agentic task. And so I think we're used to thinking about output tokens, but I'd ask us, let's start with the cash hit price when thinking about the cost of an angenic task and tokens. I think the last perspective we want to share with you and wrap up with is the most important chart for understanding the AI landscape in 2026. In 2025, it

[08:23:33]
was simpler. It was our intelligence index bar chart. Now we start with the intelligence versus cost per task, as we are now wrestling with these trade-offs of the cost of intelligence. And a helpful archetype to understand this and to reason about how to think about cost per task, whether we should just use the most intelligent model or the cheapest model, is to break down tasks into two archetypes. The first archetype is a task whereby there's not a ceiling on how much intelligence you could want to complete the task.

More intelligent equals better outputs. And this is the case for most knowledge work today in prof in professional tasks. Not everybody agrees with that, but that's

[08:24:21]
something that artificial analysis we believe quite strongly. Think about analysis that you might do on strategy or on how we can save costs, or on even writing a job description. It can always be better. We can always do a better job as humans, and that's the case for models. So there's not a ceiling on that, in terms of what level of intelligence we need, but we do need a trade-off costs. And so the question, therefore, is how much are we willing to pay for the extra intelligence?

And you want to look at the Pareto line here in making that decision. The second archer type of task is whereby there's a ceiling. An example is how much did I spend on stripe fees last month? A

[08:25:06]
smarter model doesn't necessarily give you a different or a better answer to that. There's a ceiling on the task, and then you want to think about what is the level of intelligence, the minimum level of intelligence that can complete the task, and then you want to choose the cheapest model, that which is to the left on this chart. So that is the cost of intelligence. We're artificial


────────────────────────────────────────────────────────────────────────────────
## ANNOUNCER
**Affiliation:** AI Engineer Worlds Fair
**Talk:** Speaker Introduction
**Time:** 08:25:32 – 08:25:32

[08:25:32]
analysis. We're hiring. Thanks very much. Thanks. Please join me


────────────────────────────────────────────────────────────────────────────────
## GEORGE CAMERON & MICAH HILL SMITH
**Affiliation:** Artificial Analysis
**Talk:** The Cost of Intelligence: Benchmarking Agentic AI
**Time:** 08:25:45 – 08:47:17

[08:25:45]
in welcoming the co-founder and chief technology officer at Arena, Wei Lin Chiang. Hello everyone, uh excited to be uh

[08:26:12]
uh here sharing our experience uh building agentic evals in arena. My name is Waylin. I'm the co-founder and CTO at Arena. Um Quick intro on me. I did my PhD in AI research at UC Berkeley, where my focus was building robust scalable evaluations for AI systems, and that will eventually become the foundation for what we are building today at Arena to measure intelligence in the real world. Some of you uh some of you may have heard our earlier work like LMS a judge back in uh 2023.

We did uh some of the early study as well as building uh Chapa Arena, which and some of the uh evaluation research I was fortunate to contribute. So

[08:27:09]
what is Arena? Simply put it, Arena is an AI evaluation company. Our mission is to measure intelligence in the real world beyond just static benchmark, but uh the intelligence actually delivering real values to the users, the customers. And over the past couple years, uh, we have been tracking you know all the major AI breakthrough, uh obviously after you know the chat moment in 2022. After that, it was GPD for turbo, GPD4, having the breakthrough in chat

[08:27:50]
and multimodal capability, and then evolving to the reasoning model, thinking model with OpenAI 01. And in 2025, we uh saw the image uh generation breakthrough of NanaBanana, which was originally started testing in Arena as a conan before its public release. And we are also seeing Grok catching up, GPT Images 2 recently released to become you know the current frontier of image uh models. As well as you know the video, AI, generations, um, BL, and recently bi dense, C dense.

So towards the end of 2025, when Opus 4.5, 4.6 uh went from being a great coding model to a gen genuinely agentic coding model that can do longer horizon uh tasks. That also showed up uh in arena too that will remeasure in Co-Arena, we see you know significant improvement over the past generational model. And the most recent fable five breakthrough where we measure in Asian arena, we will talk a little bit more later. SOS, the most recent GLM 5.2 release, which is like really a big milestone for the open source model community.

[08:29:26]
So we have at Arena, we have done this with scale. We now see 10 million monthly visitor going to our product, arena.ai and we have collected seven hundred million conversations across all the modalities, text, vision, image, video, coding, these days agent, and we have hit a huge milestone, very excited to share that just which was recently announced we hit 100 million uh annualized revenue in just eight months after we first released our evaluation product? We are

[08:30:06]
also uh ranked among the top Gen AI product globally by a unique number of monthly visitors, according to a AC in Z uh analysis. So the topic I want

[08:30:21]
to cover today and the core of what we are offering is Life Leaderboard, which is based on real-world evaluations powered by the 10 million users, 700 million traces, to rank all the top AI models from TM models for the past couple years. And we cover text, image, video, uh, code, agent. Um, so really wanted to build a leaderboard that can help everyone to find the best model for their use cases. And it's free, it's available for anyone to see to use at arena.ai slash leaderboard.

You can see all the analytics there, Pareto Frontier, comparing cost, performance, you know, use cases, different category, different modality of these models, capability. So yeah, so the real problem today I want to talk about is to share the experience, how we how do we evaluate agents? I wanted to share our firsthand experience in the past common month we've been building the agent tech eval, which is very, very different from the past. In the past, we evaluate chatbots and wanted to share some lessons here.

Before we diving into the details, first, why does this matter? Wanted to

[08:31:44]
talk about the trend. So we have been seeing um the very rapid shift from uh the chat bar to agent um paradigm shift. And if you look at the open AI's data on codex traffic, the share of the output token coming from agent has just skyrocketed. And you can see inside OpenAI essentially 100% of the uh output tokens from agent, from codex. And for other organizations, you know, average is like above 60% now. And individual also climbing very fast. So there's no question that the token flow is now driven by agents. And And we also

[08:32:27]
see that agents are not just for engineers, right? It's not just for software engineering. If you look at codecs adoptions by apartment at uh OpenAI, engineering, obviously 99%, but

[08:32:40]
also finance, recruiting, legal, and so on, they are all like almost like 90%. And as well as so as you can see, you know, the studies from Goldman Sachs estimates, the monthly token usage is also skyrocketing towards like you know 60 quadrilli quadrillion tokens in the next couple of years. So really, you know, the economics also tell the same story. If you look at the REM data, the AI spending is getting closer to people spend, right?

So if you see like you know, the top one percent of the company's monthly AI spend is per employee is actually already like 7.4K, roughly half of the salary of an software engineer. So this is really like, you know, historical shift that um meaning also the stack of like choosing the best model the right model and optimizing your agentic ai workflow is you know more it has never been more important.

So the key question here is like we give agent lots of autonomy, we spend a lot, we invest a lot, and the key question here is that how do we actually measure agents outcome? So that's really the bottleneck, right? You want to understand the value of these agent uh outputs and actions. And this turned out to be a pretty hard technical problem for a few reasons. First, agents are multi-component systems, right? You've

[08:34:17]
got the model, the agent tech loop, the tool, the harness, um, you know, any of these pieces can break the system. You also uh have agent operate through complex

[08:34:30]
workflow now in a real environment. Uh you build building app, debugging, doing research, producing document, uh slide deck, and so on. So it's like more involved task. Uh and third, the uh signals that we can collect, you know, in this trajectory are also becoming sparse, a spread across longer horizon. Um, you know, a t a task may take hundred tok calls to f to finish, right, before you know if it's succeeding or failing or, you give any feedback of a chance to steer it. And to deeply understand the problem, at Arena we decided to actually

[08:35:10]
firsthand building real-world, you know, agentic product and app to actually source the organic traces and feedback from the actual users for us to you know do research and deeply understand that. So last month we launched uh Agent Mode in Arena to allow anyone to go to Arena to experience and evaluate agent capability. So it's right now available for every everyone to use. And wanted to show you a very quick demo. If is if I can start the uh is the video moving here off. Okay. So this is agent arena.

You go to agent, you go to arena.ai, you you s you choose the agent mode, and this is a real world, you know, agent tick product. You can go and evaluate model. You come in and type any question you want. In this case, um it's like I ask download Google's Q1 earning report uh and create a slide deck summarizing these output in PowerPoint.

And you can see the agent goes off and doing work, searching the web, pulling the right website, start structuring the deck, and then using some of the bash tool, writing Python code to generate the slide deck, right? And

[08:36:30]
you can see that at the end, uh, there's like an artifact generated by the model uh that user can download and see. And this is like a you know a real PowerPoint uh output by the model. And then user can at the end we ask every turn, like we ask, was this test successful or not? And user can provide feedback that way. And this one of the signals that we use to evaluate and understand whether Agent actually delivers the outcome. So, yeah, this is just to highlight the panel.

And under the hood, how we build the Asian arena, it you know, we give model set of tools, um, file system tools, read, write, edit, and so on, and search, web fetching, image, uh, generation, speech,

[08:37:19]
as well, recently added. So just really giving the model tools similar to like a cloud code work like harness and also terminal access to run code to to to to you know do work. And we also are adding more and more uh connectors soon, like GitHub, uh, which can connect to your repo to you know do more serious software engineering tasks.

Um and you can see this plot is the the usage uh of these tools uh in the in in a type in a one-week time frame you see 5.7 million tool calls um you know bash is was the you know the the the number one used uh around 46%. And you know these these agents are actually using these tools to do real real work for users. So we also, you know, dig into the data and seeing users are, you know, pushing really hard to trying to do more harder and complex tasks.

So real session we've been seeing like, you know, users are building, you know, a movie watch list app, debugging a control systems for autonomous vehicle and architecting, building a

[08:38:32]
rack pipeline, you know, implementing features in micro and so on. So these are the sessions, like go over hundreds, some of them go hundreds of turns and a couple hundreds of tool calls, very serious stuff. Um, and you can from this you can tell that the um the agent that we built uh at arena is actually doing real work with users and giving users real value. And we believe the best evaluation should be uh grounded and measured in real-world use cases like this.

So we launched Agent Arena uh just a month ago, and in the first months over uh we collected over a million agent traces, and these are in task spending, coding, research, document,

[08:39:16]
brainstorming, planning, and we see more than half of these uh uh traces fall into work-related category, more like towards professional use and complex tasks. Um and we have seen Asian also readnum more than 50 million lines of code on Arena, Python, Markdown, HTML, JavaScript, and so on. This is the tool distributions that you can see the coding is the number one. And some of these um tasks you can see is some of them are more complex using more tool, uh, some of them use less. And this is the t the line of code generation.

So So now the going back to the evaluation question, right? So say we collected a million agent traces, how do

[08:40:06]
we actually turn these traces into a leaderboard that we can understand which model performs better than the others. And we primarily mine the signals from three types of uh basic signals. One is like explicit, which I just show you that user will tell us directly like which tasks succeeded or failed. Some of them the other one is something is imp implicit.

Uh we see that if user is actually uh say downloading the file or like um complaining about the output of the generation from the model or praising it and so on, so more like implicit signals. We we stick in through all the traces. And also there's environment feedback where you know what actually happened when the code run, whether the commands are seed or felt, and so on. So we basically use these, you know, scan through all these sessions, traces, every user message, assistant action, tool, result, feedback, and aggregate them into some

[08:41:06]
of these signals like success rate, praise overcomplain, durability, bash recovery, tool hallucination. And each of these signals can produce the ranking, right? You can measure precisely, you know, which model performs better than other in this particular signal. And we combine that into the final leaderboard that you see on uh you know on the website. Um so um that's what you uh looks like um today you see like um this leaderboard has five different signals and model performed differently across the board.

And right now, Fable 5 is the number one models that was, you know, the net improvement of like 14% over the average, which is the you know average of all the models, followed by Opus, GPD, Fi-Fi, High. And what's interesting about this data board is like you can look at the signal by signal. Um, a model may be really, really good at test success, but sometimes weaker in terms of like you know sterility in terms of how do you control the model. And you can see exactly like where the model is failing and so on.

And we are going to add you know more and more signal signal, reach your to capture this value pattern. So methodologically, the core idea is basically a randomized control trial where we intervene on agent component. We measure the causal effect of you know any given component on the task outcome, like the signal that we care.

Uh and the many books basically is like the causal effect of the of the orchestrator models that you can you know right now but the springware is general enough so we can also measure the interaction effect between different um components. For example, let's say you want to measure uh tool, you want to measure different harness or different system prompt uh and so on. So all these are possible within this framework and we're going to, you know, uh evaluate that too.

And if you are interested, more technical details are published uh on our blog post. Um so um we have been tracking, like I say, all the major releases in agent RCs. One of the released happened a couple of weeks ago, Fable 5 in Agent Arena. So if you wanted to follow us on X, you will see all the latest release. And the interesting thing about this little board is because this is real data, right? Based on millions of agentic traces, you can slice it into any task distribution you care about.

So for example, like let's say you care about you know GDP tasks, this more like economically valuable professional work versus consumer use cases. You can uh you can do some of the data analysis to slice the data. And one, you know, inside here we see is like GPT-5 is actually pretty good in terms of like GPT, sorry, GDP tasks. And GOM, Gemini tends to do

[08:44:10]
better in consumer use cases. So basically the, the best model generally depends on uh what you're doing, what you care, the distribution. Um and on the other side is the cost, right? You know, cost matter to you can we basically can plot these uh net improvement, which is performance, against the average cost to see to help you see the period of frontier here.

You can see Fable Fi is the one that's the best, uh, costs about ten dollar per session, and Fi-Fi is still very strong, a bit cheaper, and GP GLM 5.2 gimme is like the most efficient one. So you can with this data decide which one is the best model for your budget. Another lens is tokens. Higher performing models sometimes generate more output tokens, like using more thinking model. Um and but uh not always. You can you can see here like GPT five is relatively more efficient than other models.

And the other interesting thing here is like if you only look at the list price, you may see some of the model is like same price, but if you actually put it in the real world, some of the model would use more tokens to for the same task, right? So actually, we can show here, like for example, GPD55, although it has similar price, list price uh as opus, but in in the real world, it uses less tokens, fewer tokens to achieve the same task, which is more efficient than the others, and as you can see.

So to summarize, um, if you are building an agent tick app, um obviously you should definitely be logging your agent tick traces to understand to log all the interactions between the agent and the user and the customer, and then be able to, you know, look into the data mind for insights and measure the outcome links to whatever business metrics you care, and use that data to real world data to choose the best model for you.

Uh and what we are headed next is obviously going to add a lot of different connectors to bring in more user context and enable really the live e-vals for many different kinds of agents, coding agents on real repository. And we

[08:46:24]
also wanted to bring more complex tasks, professional users slides that into different categories to help you understand how model is doing in those categories. And so as more like richer signal for um developers to use to pick which model is the best as well as rubrics to do more final grand um scoring and even working collaborating with the user to define what's good look like. So that's it for me. We'd love to hear your feedback or if you have any questions, feel free to reach out.

You can find more insights on our leaderboard, arena.ai, or follow us on X. We also publish technical blog posts you know regularly and yes we are also hiring so you know check out this link or just DM me on X to reach out. Thank you. Please welcome back

[08:47:17]
our MC, Director of Technology at Oliver Wright America's, Davina


────────────────────────────────────────────────────────────────────────────────
## WEI LIN CHIANG
**Affiliation:** Arena / Co-founder & CTO
**Talk:** Building Agentic Evals: Real-World Intelligence Measurement
**Time:** 08:47:25 – 08:50:15

[08:47:25]
Delayas. Hey, everybody, thank you so much, and give yourself

[08:47:38]
a great round of applause for being here till the end. Yeah. Thank you guys. We really truly saved the best for last. So the start of battle, I lied to y'all. It's not tonight. It's tomorrow night, along with the closing speaker note. So please be there. We look forward to be there. So thank you for the incredible sets of talks for our afternoon keynotes. And big, big

[08:48:11]
thank you for the organizers. We truly have incredible sponsors. The event could not have happened without them. We're incredibly excited to partner with so many wonderful organizations. Presenting sponsor

[08:48:30]
Microsoft. Okay. Okay. Where where is it? Okay, so Lava

[08:48:47]
and Platinum Sponsor and our gold sponsor And of course,

[08:49:02]
our silver and bronze sponsors. Thank you all. Have a marvelous rest of your evening, and we'll see you tomorrow morning. It's really incredible what is going on in the

[08:49:53]
world today. Allows him to unlock more and more levels

[08:50:15]
of automation. AI writes codes faster than humans can review


────────────────────────────────────────────────────────────────────────────────
## DAVINA DELAYAS (MC)
**Affiliation:** Oliver Wight Americas / Dir. of Tech
**Talk:** Closing Remarks
**Time:** 08:50:28 – 08:50:28

[08:50:28]
it.


================================================================================
# END OF TRANSCRIPT