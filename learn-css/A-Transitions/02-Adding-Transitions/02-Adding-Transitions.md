0:00
Hi.
0:00
Welcome back.
0:01
So in the last video, I talked about what transitions were and how they were applied in the real world, but in this video, we're gonna be going through and creating and applying our own transition.
0:12
So this looks quite similar to the previous video in the setup that we had, except I removed all of the, um, edits and styles that allowed me to create that transition.
0:22
So instead, we are going to be writing it step by step, and I'm gonna be walking you through how to create these transitions.
0:29
So let's go ahead and get started.
0:32
So in order to actually change the, uh, styles that we wanna use based on the state of the element, we need to use something called a pseudo class.
0:40
So the typical formula for a pseudo class is you have the name of the class or the element or the selector.
0:47
It could be an ID selector or class selector.
0:49
It doesn't matter.
0:51
And then you're gonna follow it with a colon and some word that's gonna describe what state you're trying to target.
0:57
So in this case, our class selector that we're gonna use is heading, so we're gonna type dot heading, colon, and then what we're gonna wanna use is hover.
1:09
So what this is representing is whenever this element or any elements with the heading selector are hovered over.
1:16
And then everything just works like normal.
1:18
We're gonna open up our class and start typing whatever properties.
1:22
So remember, these properties are only going to be applied when the, uh, element is hovered over or whatever pseudo class is being activated.
1:31
So let's go ahead and do that.
1:33
Now I'm gonna go ahead and change the color.
1:36
And let's just go ahead and use something simple.
1:38
I'm gonna maybe say brown.
1:42
And then I'm also going to change the font size.
1:46
So let's go ahead and set that to maybe twenty five pixels.
1:49
So what we expect is when this element is hovered over, I'm gonna do that in just a sec, what's gonna happen is the color of the element will be changed to brown and the font size will be changed to twenty five pixels.
2:02
So let's go ahead and do that.
2:04
Nope.
2:04
Refresh the page.
2:06
Yeah.
2:06
There we go.
2:07
So you can see that when we hover over our element, the color and the size are changed.
2:13
So now we have all that said and done, but again, like in the last video, we need to fix it so that it has that nice smooth transition.
2:22
So the way you do that is you use something called the transition property.
2:27
Now the general formula for this is the first, um, part of the value is gonna be the specific property you wanna transition.
2:35
So, for example, I can target color only.
2:38
So I don't have to target the size and the color, but I can target color specifically.
2:42
And then the second part is going to be the time that it takes to transition in seconds.
2:47
So I am going to go ahead and type maybe zero point five seconds.
2:53
So now let's go ahead and check that out.
2:55
So you can see that the the size changes instantly since we didn't transition that, but the color takes point five seconds to transition.
3:04
Now if you wanna target multiple properties, all you have to do is separate them by a comma.
3:09
So I can target color, and I can target the font size, and I can even change the timing if I wanted to.
3:18
So I can set this to one second to change the size and point five seconds to change the color.
3:24
Let's go ahead and check that out.
3:26
So you can see that the font the font size takes one second to change while the color takes point five seconds.
3:33
Now this is good for specific properties, but if you have maybe ten or twenty styles that you all wanna transition, you're not gonna go through and type all that out.
3:42
So the way you can do this is using the all shorthand.
3:45
So all you do is type all, and this is basically going to take all of the properties that are changed based on the pseudo class and transition them.
3:53
So the one downside of this is really that you all have to limit it to the same size, but if you want, you can add extra properties after that to change their timing.
4:03
So let's go ahead and look at that, and now you can see it does the exact same thing, and it takes point five seconds to change the size.
4:11
Alright.
4:11
So now it's time for a little challenge.
4:14
I want you to go through, take this text, and transition it over half a second to change the font color to green, the font size to twenty pixels, and the spacing between the letters to ten pixels.
4:29
Alright.
4:29
Good luck.
4:33
So let's go ahead and get started.
4:35
The first thing I wanna do is talk about the properties I wanna use.
4:39
Now I'm gonna be using this pseudo selector here to when we hover over it, it is going to make all of those changes.
4:46
So let's go ahead and do that now.
4:48
First thing I wanna do is change the color to green,
4:54
then I'm gonna change the font size
4:58
to twenty pixels.
4:59
And in case you didn't know this already, to change the letter spacing or the spacing between the letters, you use that property and set it to ten pixels.
5:09
So now when I go ahead and hover over this, you can see it makes all those changes.
5:14
The last thing we need to do is add our transition property to our base selector.
5:19
So I'm going to go ahead and add that there, and now I'm going to transition all since all of those properties need to be transitioned over half a second, or zero point five seconds.
5:32
Now let's go ahead and view it.
5:33
You could see it makes that transition just fine.
5:37
Alright.
5:38
Let's move on.
