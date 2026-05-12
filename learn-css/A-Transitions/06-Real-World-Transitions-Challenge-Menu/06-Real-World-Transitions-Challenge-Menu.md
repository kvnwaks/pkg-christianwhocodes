0:00
Alright.
0:00
Welcome back.
0:01
So in this video, we're gonna be going through and doing our first real world challenge.
0:06
So you can see here that I've built a tiny website, nothing really much on it, but this is designed to get you familiarized, uh, with the topics and, uh, properties that we've learned over the last few videos and really integrate them into a project that can, you know, really let you know how to use these, uh, properties and topics in the real world.
0:26
So I've left a description down here talking about the challenge.
0:29
Basically, what we're gonna do is add a couple of transitions, one to the title and one to the menu items.
0:35
So the title is gonna be focused solely on transitioning the color while while the menu items have to both grow in size and change color.
0:44
So you can see some of the specifics here.
0:46
And also, both of the transitions need to have a one second duration and an ease out timing function.
0:53
So go through, familiarize yourself with the HTML that's going on here.
0:57
Just look at how things are set up and how you're gonna go through doing this.
1:01
Alright?
1:06
Good luck.
1:08
So let's go ahead and get started.
1:10
Now before we add any transitions, remember we need to add those pseudo selectors so we can tell CSS what we're going to do when these specific elements are hovered over.
1:22
So the first thing we wanna do is change to this color this color when the title is hovered over.
1:27
So the first thing we're gonna do is go and look for the title.
1:31
So it's gonna be this element right here, the h one.
1:34
So we're not selecting the div, of course, since we're trying to change the color of the text, not the div or the box containing it.
1:41
So let's go over here.
1:43
I'm gonna go all the way to the bottom, and now we're going to say dot title and use the colon and add a hover.
1:50
Let's open that up.
1:51
Now we're going to go ahead and set our color to that right there.
1:56
So there we go.
1:57
We've added the pseudo selector.
1:58
We hover over it.
1:59
You can see that it works.
2:01
We didn't get to the transition yet, but don't worry about it.
2:04
We'll do that in a second.
2:05
So now let's go ahead and focus on our menu items here.
2:09
So you can see here that all of our menu text has the exact same class, which is menu link.
2:15
Now the easiest way to do this would just be go, uh, to go and use a pseudo selector with this class to target all of the elements here.
2:22
So let's go ahead and do that.
2:24
What I'm gonna do is use dot menu dash link and then, of course, colon hover since we're targeting the hover.
2:31
Now we're gonna use the color, which is that color that I specified in the challenge description, and, of course, our font size, which in this case is gonna be two point five e m.
2:43
So now we go ahead and just make sure it's working, and you can see that when I hover over it, the text grows.
2:49
So there we go.
2:50
That's one part of the battle done.
2:52
Now let's go ahead and focus on our transitions.
2:55
So we're gonna go ahead and find the base class that these or the base selector, sorry, that these, um, pseudo selectors are applied to.
3:03
In this case, it's just dot title for the title and dot menu link for the menu link.
3:08
Now don't worry about the rest of these styles.
3:10
Those are just to set up the website, but what we really want to do here is add that transition.
3:15
So let's go ahead and use the shorthand property.
3:18
Now for the title, since we're only targeting one property, we're just gonna go ahead and say Color.
3:23
Now you can use All since it doesn't really affect anything, but if we wanna add more things to the pseudo selector later on, it's better to just keep it like this unless you wanna encompass all of those other changes.
3:35
Then we're gonna give it our duration.
3:37
So let's go ahead and say one second.
3:39
That's what I said in the, um, in the challenge description.
3:44
And then, of course, our timing function, which is ease out.
3:48
So now let's go ahead and see what happens.
3:51
You can see that it changes the color right there, and it takes one second.
3:55
Now it may be a little hard to notice the ease out since the animation is quite short, but it is there.
4:01
So now let's go ahead and focus on our menu items.
4:06
So let's oh, sorry.
4:08
Not menu item, menu link since that's the text.
4:11
So let's go ahead and add our transition.
4:15
Of course, I'm you can go ahead and specify the properties individually, but I'm just gonna go ahead and say all to simplify things here.
4:22
Next, I'm going to say set my time, which is one second, and then our ease function.
4:28
Now let's go ahead and look at it, and you can see that that is working right there.
4:35
So now we've added our transitions to the website.
4:38
It was quite easy to do.
4:40
Most of the work was really in just adding those pseudo selectors and knowing where to add them, and once you get that done, it's quite easy to just add the shorthand as long as you know what is going on.
4:51
Alright.
4:51
Let's move on.
