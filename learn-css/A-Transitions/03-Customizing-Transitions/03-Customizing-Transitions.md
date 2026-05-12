0:00
Hi.
0:00
Welcome back.
0:01
So in this video, I am gonna be talking about some more properties and customizable features of transitions.
0:08
So we're gonna be looking through them.
0:09
We're gonna be looking at things like delays and specific timing functions that let us further customize our transition.
0:17
So right now, we ended up at the point that you did the challenge, and we have all of this over here.
0:22
So we have our, uh, changed, uh, font size and our color.
0:26
But now we're gonna go through and really break apart this transition and look at all of the properties that come with it so we can try and get the most out of it.
0:35
So right now if we go to our CSS style sheet, you can see that we have this transition
0:42
property here.
0:43
Now although this is pretty good for basic, you know, usage, if you don't want to really customize it and make it your own, then this is alright.
0:52
But there are a ton of different features that you can use on top of this, uh, to really make the transition how you want it.
1:00
So the first of these that we're gonna talk about is transition delay.
1:05
So what what this basically does is what it says, it's going to add a delay to the beginning of the transition before it starts.
1:12
So let's say we want a one second delay, for example.
1:15
Let's go ahead and open up our site here.
1:17
We hover and it takes one second before it starts.
1:22
So again, this just works with, um, seconds value.
1:25
You can set it to whatever you want.
1:28
The next thing I wanna talk about is breaking up our property and our duration into separate properties.
1:34
So although this is the typical way that anyone would do it, you can break this up into specific properties.
1:41
So we can actually specify the properties we want, uh, in this property here, transition property, and we use a comma separated list of values or we can just use the all.
1:52
So we can say that here or we can specify color and font size just like we did before.
1:58
So for now, I'm just gonna set all.
2:00
Now one thing you need to watch out for is if you use this, you need to make sure you also use the transition duration property because what's gonna happen is if you don't set this and you just have this property here, it's going to set the property, but it no duration will be set.
2:16
So therefore, it will just look as if nothing happened.
2:20
So we're gonna go ahead and set that to point five seconds, just like that.
2:25
So there we go.
2:26
Now we split up that one property into two.
2:29
So the next property we're gonna be talking about is the transition timing function.
2:34
So what this is gonna focus on is how our transition plays out.
2:38
Is it gonna be linear, so it's just gonna go from one point to the other with no really real shifts in speed, or are we gonna have it faster at the beginning and then slower at the end?
2:49
So the property we're gonna use for this is called transition
2:54
timing function.
2:55
I know it's quite long, but this is the property that we're gonna use.
2:59
So there are multiple values that you can put here.
3:02
So the default value that we're gonna use is linear, So you don't actually have to set it since this is the default, but what's gonna happen is this is pretty much gonna say, uh, from start to end, it's going to go in a straight line pretty much.
3:15
No changes in speed.
3:16
We also have ease, ease in, and then we have all of these different, um, properties here.
3:23
So they all have to do with at what point does the animation or sorry, the transition start to slow.
3:30
So why don't we just go ahead with ease here?
3:33
So now let's go ahead and check out our, um, animation here.
3:36
So we have that one second delay, and you can see, although it's not really noticeable, it does have a slight ease.
3:43
If I were to maybe increase the duration to two seconds let's just set the delay to zero seconds for now.
3:50
When we hover over it, you can kind of see that towards the end of the animation, it starts to slow down.
3:57
So there we go.
3:58
Sorry, the transition.
3:59
So there we go.
4:00
There is our transition timing function.
4:04
So those are the four main properties that we're going to be using throughout four, uh, transitions.
4:11
Now I'm gonna challenge you now.
4:12
So I'm gonna go ahead and erase all of this so you don't get to see it.
4:18
So my challenge to you now is we have our, uh, CSS here.
4:22
What I'm gonna tell you to do is I need you to modify this transition so that it only targets the font size.
4:30
It has a one second delay.
4:32
It takes point five seconds to run through, and it has an ease in timing function.
4:39
So go ahead and do that now.
4:44
Alright.
4:44
Let's go ahead and set it.
4:46
So first thing we wanna do is set the transition property
4:51
property.
4:51
So what this is gonna do is because it's only targeting the size, we're not gonna use the all value.
4:57
We're just going to select font size.
5:00
We know that it has a one second delay, so we're gonna use the transition delay property and set it to one second.
5:07
The transition duration, which is going to be how long our animation is gonna take to run through, is point five seconds.
5:15
And finally, the timing function we said was ease in, so all we have to whoops.
5:22
All we have to do is use ease in.
5:27
And it's super simple.
5:28
That's all you have to do.
5:29
And if we go check it out now, you can see we have that whole thing here.
5:34
So there you go.
5:35
That's pretty much it for all of the, um, tasks we have to do with customizing transitions and things like that.
5:44
Now in the next video, I'm gonna teach you a quick shorthand that you can use to avoid, you know, writing all of these different properties down and just condense it all into one property.
5:54
Alright.
5:55
Let's move on.
