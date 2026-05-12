0:00
Hi.
0:00
Welcome back.
0:01
So now it's time for a large challenge to summarize up to summarize this animation section.
0:07
So what I'm gonna let you do is create an animation called supersize, which basically takes this tiny box that's on the screen, grows it to twenty pixels, then changes the color to red, and then grows it to fifty pixels and changes the color to green.
0:24
So that's the basis of the animation.
0:27
It's gonna last two seconds.
0:28
It's gonna have a timing function of ease out.
0:32
Uh, there's there isn't gonna be a delay, and it's going to run four times, and it's going to alternate between start and finish.
0:40
Alright.
0:41
Good luck, and I'll see you when you're done.
0:46
Alright.
0:46
Let's go ahead and get started.
0:48
So the first thing I wanna do is define my animation.
0:52
So I'm gonna do it using at keyframes supersize.
0:55
So that's gonna be the name of the animation.
0:58
And because we have three steps, we're gonna go ahead and use percentages.
1:02
So let's go ahead and just define the percentages first.
1:04
So we're gonna have zero percent, so that's gonna be the start, to fifty percent, which is gonna be the middle, and, of course, one hundred percent at the end.
1:14
So at zero percent, we're going to have the width and height and color all the same.
1:20
So we're just gonna use the same properties that we have up here.
1:25
At fifty percent, we said we want it at twenty pixels
1:30
for both the width and the height and the color, which in this case is gonna be the background to be red.
1:36
And finally, at the end, it has to be, um, with a width and height of fifty pixels
1:45
and a background color of green, Just like that.
1:50
So now we have defined the animation.
1:52
Now we have to go through and add it.
1:54
So instead of defining all those properties, we're gonna go ahead and use our shorthand.
1:59
Let's go ahead and set it animation.
2:01
So we're gonna start with the name, which is supersize,
2:07
two seconds, which is gonna be our duration, then our timing function, which is gonna be ease out, then our delay, which is zero seconds.
2:17
Since we said we don't want a delay, we want it to run four times.
2:22
So we're going to say four for our iteration count, and then we want it to start go back and forth between start and finish.
2:30
And of course, since we're starting at the actual beginning, we're gonna use alternate.
2:35
Now just to cover our ends and make sure that the animation runs smoothly, we're also gonna add our animation fill mode and set it to both.
2:46
What this is gonna do is finish with the styles that we finish on, and And the reason I'm using both and not forwards or backwards, depending on how this ends, is in case we want to edit this later on, uh, this will always stay true.
3:00
So let's go ahead and check out our animation.
3:02
We're gonna refresh.
3:04
You can see it does that grow movement right there, and it's gonna run through four times
3:11
and then finish on the correct styles.
3:14
Alright.
3:14
So there we go.
3:15
Now if you chose to not use the shorthand and go ahead and use all of these separate properties, that is also okay.
3:22
Although I do recommend using the shorthand in the future just to shorten things up.
3:27
Alright.
3:27
Let's move on.
