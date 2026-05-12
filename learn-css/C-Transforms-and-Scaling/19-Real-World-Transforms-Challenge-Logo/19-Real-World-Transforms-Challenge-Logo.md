0:00
Hi.
0:00
Welcome back.
0:01
So it is now time for our third and final challenge, which is to use transforms in combination with animations to animate these boxes here and create a little logo animation using CSS exclusively.
0:15
So let's go ahead and check out our animation task.
0:18
Now I've left I've I've really left this up to you to experiment with the values and see what works best.
0:23
So a lot of this is really up to the user or whoever's watching the video.
0:27
So you can go ahead, play around with the values, and you really get a feel for the animation and make it your own.
0:34
So here are some of the base, uh, rules that I want.
0:37
So first of all, what is gonna happen is these boxes are going to be translated to the middle of the page.
0:43
They're gonna be stretched on the x axis to kind of elongate them so they look a lot longer.
0:48
It'll kind of look like a flag at the end of it.
0:50
And they're also gonna be skewed to make the boxes look that they've been tilt tilted about eighty degrees counterclockwise from the, uh, twelve position on a clock.
1:00
So if, for example, the boxes were facing up, what would happen is they would be tilted eighty degrees to the left, so they would kind of be facing around the nine position.
1:09
So that's what I mean by that.
1:12
So the animation should run once, and it should retain all of its styles when the animation is complete.
1:19
So I recommend go ahead, play around with this, and really see what kind of transforms, uh, you can bring into this to to, you know, make the animation look better while also adhering to these rules.
1:30
Alright.
1:31
Good luck.
1:38
Alright.
1:38
So let's go ahead and get started.
1:40
The first thing we're gonna do, just like with any animation, is define our key frames.
1:44
So I'm gonna go ahead and use the keyframes keyword, and we're just gonna give this a name of move, for example.
1:51
Now, again, this is only gonna have two states, and in reality, we only need one state, which is the one hundred percent state since we're gonna be moving these four boxes from the start to the end.
2:03
So what I'm gonna do is just use the two or you can use one hundred percent.
2:07
It's up to you.
2:08
I'm just gonna say two.
2:10
And now here is where we're gonna specify the transforms that we wanna use.
2:15
So firstly, we're gonna use the transform property.
2:18
And now remember, we're gonna have to concatenate multiple, um, transforms together separated by spaces.
2:25
So let's start with our translations.
2:28
So we want to we wanna move this to the middle of the page.
2:31
So we're we obviously know we're gonna be moving with both the x and y axis.
2:35
So let's go ahead and use the translate property.
2:40
Just note not translate x or translate y, the whole thing.
2:43
Now you could use percentages, but the thing is, if you noticed, what's gonna happen is it's not really gonna move, uh, uh, properly because of the way the HTML is set up.
2:53
You can see that we're targeting it may not be targeted properly.
2:57
So instead, we're gonna use the absolute um, view width and view height values.
3:01
So they're denoted by v w and v h.
3:04
So I'm gonna start with fifty v w, so that's the view width, and then fifty v h.
3:11
So what this is gonna do is basically say, um, move fifty view fifty percent of the view width.
3:17
So this is the absolute maximum.
3:20
This isn't, you know, apparent, the width of apparent or anything.
3:23
This is fifty percent, uh, to the right here and then fifty percent down, just like that.
3:28
Next thing we wanna do is focus on our scale.
3:31
So we're gonna use scale x in this case since we only wanna elongate the box.
3:35
We don't wanna completely enlarge it.
3:37
And we can use whatever value, but I'm just gonna go ahead and give it a value of ten.
3:41
It's quite arbitrary.
3:42
You can mess around with it and see what works best for you.
3:46
And finally, we want to work with our, um, our skew here.
3:51
So you can work with rotations, but it may be a little hard to get it right.
3:56
So what I'm gonna do is actually use the skew, and it is specified in the instructions to use a skew, to SKU it.
4:04
Now the thing is with SKU is it may not accurately reflect the rotation unit.
4:08
So if I say around eighty degrees counterclockwise, it won't be exactly eighty degrees if I set it here.
4:15
So I played around with these values a little bit, and I I, you know, I really encourage you to do the same.
4:22
So, um, and I found around sixty degrees would give you the optimal, um, skew to work with.
4:28
So, again, if you wanna go ahead and play around with it, go ahead, uh, see what kind of values work for you.
4:34
And then when you find it or, you know, even if you have an updated value, you can input that, um, through the interactive window.
4:41
So there we go.
4:42
We have the key frame set up.
4:43
Now let's go ahead and apply it to our logo here.
4:47
So the first thing we're gonna do is go ahead and target the box, uh, class since we're gonna be targeting each individual box, not the logo, since if you looked at the HTML, um, these are four separate elements, these four divs, and they're contained inside this logo class.
5:04
So here is we're gonna we're gonna apply the animation.
5:07
So I'm gonna use the shorthand, uh, feature since we have a bunch of different properties we need to specify.
5:12
It's easier to just go up with it like this.
5:14
So let's go ahead and first type out the name.
5:16
So I'm gonna say move.
5:18
Next thing we wanna do is check for the duration.
5:21
So I didn't explicitly spec specify a duration here.
5:24
So what we're gonna do is just go and maybe give it a two second duration.
5:29
Next thing we're gonna do is specify the timing function.
5:32
So this is really important for making animations look good.
5:36
If you set the wrong timing function, it may not play out right.
5:39
Now I think for animations like this, ease in out works best since what's gonna happen here is hold on.
5:47
You you saw that animation one more time.
5:49
What's gonna happen is if you look at the timing function, it kind of, uh, you know, it starts out slow and then slows down towards the end.
5:57
It's really nice to look at.
5:59
So there we go.
6:00
We have our timing function.
6:01
The next thing we're gonna do is look at our, um, uh, delay.
6:06
So we're gonna go ahead and set a one second delay.
6:10
So last thing we wanna do is just a couple of the antics.
6:13
So first, we wanna see how many times we want the animation to run.
6:16
So I'm gonna go ahead and say just run it once.
6:21
Next thing is the, uh, direction we want it to run-in, and since we want it to go from start to finish, we're just gonna set this to normal.
6:29
And finally, the timing function we wanna use, which is just going to be both.
6:36
So let's go ahead and close that off.
6:38
And now you can see our logo is animated.
6:42
So one thing you may have noticed here is that this kind of looks a little weird.
6:47
Now if we actually go ahead and analyze the way that we skewed it, we used a skew, uh, a skew property here that basically skews it on both the x and the y axis.
6:59
So let's go ahead and experiment with that, and I'm trying to show you, you know, what kind of SKUs can really result, uh, how it can drastically change your results.
7:07
So I'm gonna go ahead and start with a SKU x just to see what this does.
7:11
Refresh the page.
7:14
And you can see that that does kind of look the same, but what would happen if we use a SKU y?
7:22
Now if we go ahead and look at our animation, you can see that it looks completely different.
7:27
So this is where you really need to be careful.
7:29
Changing the type of SKU or what axis you're skewing your, uh, objects on can completely change the way that your results look.
7:37
Now if you notice when I use that skew this simple shorthand or just skew x, it completely was off from what I wanted the animation to be.
7:45
It looks a little weird and kind of stretched out.
7:48
But when we use this value, you can see that it does have that curve from the top here.
7:53
It looks kind of about eighty degrees counterclockwise, and everything is working fine.
7:57
So just make sure that you know that kind of distinction and you know what kind of skew to use.
8:03
Now it is perfectly fine to use the x SKU.
8:05
It's just gonna create a different animation than intended, which, again, is fine.
8:09
But for this challenge, it's best to stick to the rules given in the challenge task.
8:16
So that's pretty much it for the animation.
8:18
Now if we want, we can go ahead and kind of make this an infinite looping thing since it's kinda boring to have to refresh the page one time.
8:25
So we can, for example, change this to infinite,
8:30
and we can go ahead and just set it to alternate.
8:33
So what's gonna happen is this is all gonna alternate back and forth just like that, and now we have a nice infinite logo animation.
8:41
So you can see that based on what you set our properties to and what we work with here, We can change the way our animation looks, and we can even change it for different purposes.
8:51
So that's really important to keep in mind.
8:54
Alright.
8:54
So there we go.
8:55
We have finished all three real world challenges.
8:58
So in the next section, we're going to go through, explain a couple tips and tricks, extra features that don't really fit into any other sections, but are still really good to know.
9:07
Alright.
9:07
Let's move on.
