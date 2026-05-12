0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we're gonna focus on defining and creating our animations.
0:07
So what we're gonna do is go through and use a special property or system in CSS to create these, um, animations, and then in the future videos, we are going to apply them.
0:19
So one thing that animations that make animations a little different from transitions is that you define them stand alone from properties or elements.
0:27
They aren't dependent on pseudo classes or anything like that.
0:31
So what we're gonna do is use a special little, um, system here to create these animations, and then we can apply them to any element we want.
0:40
So they're not dependent or focused on single elements.
0:43
So what we're gonna do here is type out at keyframes, and what this is gonna do is specify the key frames for a specific animation.
0:53
And what's gonna happen is here is basically we're gonna set these steps that the animation is gonna have to go through.
0:59
So, for example, it changes to the color red and then changes its width and then changes its height, and you get the idea.
1:08
So let's go ahead and get started.
1:09
So once we type keyframes, what we're gonna do is set the name of the animation.
1:14
Now don't worry about any of this.
1:17
Uh, we're gonna cover this stuff in a future video, but this is gonna be the name that you want to give the animation.
1:22
So because I just want to do something simple, I'm gonna call it grow, And then we're gonna open it up with some cur curly braces.
1:30
So now there are two different ways you can go through here.
1:34
You can either use one or two lines to basically set the starting animation, you know, the starting animation properties and the final animation properties.
1:45
So you're only gonna be allowed two steps from start to finish, or you can use percentages to specify multiple steps in the animation, and we're gonna go through and do both of them here.
1:56
So the first thing we're gonna do is do the start to finish method.
1:59
So what we're gonna do is type from, open up some curly braces, and then type to just below that and open up some curly braces.
2:08
So in these curly braces here, next to from, is going to be the starting properties that we're gonna be using and to is going to be the finishing.
2:17
So let's just say from we want the width to be fifty pixels.
2:22
Now the reason that I'm typing this out is sometimes the starting properties won't always be the same as the normal properties that the animation is given.
2:31
So for example, here we have fifty pixels and all of that.
2:35
But let's say, for example, that we want the starting properties to be one hundred pixels or two hundred.
2:41
Maybe we wanna change the color.
2:43
So we'll get more into that kind of stuff in the future videos when we talk about fill modes.
2:48
But for now, let's just go ahead and set the set the width to fifty pixels, the height to fifty pixels, and the color to red.
2:58
Or sorry, the background to red, not the color
3:02
red.
3:02
Okay.
3:03
So now we have our starting properties.
3:05
Let's go ahead and talk about our finishing.
3:08
So whatever we want to change, we are going to include in here.
3:11
And you need to be really careful with this because sometimes, uh, over time things may change that you don't expect them to.
3:18
So, for example, the width could change to a hundred pixels, and you don't, uh, expect it to.
3:23
So you need to be explicit about all the properties that you wanna change here.
3:28
So what I'm gonna do is set our width to fifty pixels, the height to a hundred pixels, and then I'm just gonna set the background to green, just like that.
3:40
So So now what this is gonna do is it's going to keep the width at fifty pixels, it's gonna increase the height, and change the background.
3:48
So there we go.
3:48
This is what you do.
3:49
Now let's go ahead and open up our browser and see how this looks.
3:53
And you can see that it grows just like that.
3:57
Now it does reset, and that's because we haven't specified, uh, a couple certain properties, which we're going to discuss later, but you can see that the animation does work.
4:07
Now let's talk about the second way of doing it.
4:10
So now let's say we wanted to have steps.
4:14
So if you watch the previous video, you'll see that it went and it increased the width and then it increased the height.
4:16
So what if we wanted to do that?
4:21
Well, what we can do is use percentages to specify at what part of the animation do we want things to change.
4:27
So the percentage equivalent of this would be zero percent and one hundred percent.
4:34
But the main advantage of doing this is you can also add other steps.
4:38
So for example, fifty percent.
4:39
And then we can specify things here.
4:42
So let's say I wanted to increase the width as well and add an extra color step.
4:46
What I would do is set the width to one hundred pixels, and again, be explicit.
4:51
You wanna keep the height at fifty pixels and the background to blue, for example.
4:57
Now let's go ahead and run our animation, and you can see it does that change first.
5:03
And this is what I was saying about being explicit.
5:05
You can see let's say we wanted the width to stay the same.
5:08
We need to make sure that it is there.
5:11
So let's go ahead and refresh one more time, and now you can see the full animation runs through with three steps.
5:19
So just to recap, we have this keyframes, uh, we can set the keyframes using this syntax right here, and we can set the name.
5:27
We have two ways of specifying our animation.
5:29
We can use either the from to with method, which allows for two steps, start and finish, or we can use percentages to set certain steps in between the start and the finish.
5:41
And finally, you have to make sure to be explicit.
5:44
The rule of thumb here is just to make sure that you include all the properties you wanna change throughout each step.
5:50
That way you aren't missing any pieces or anything like that.
5:54
So I encourage you to go ahead and give this a try.
5:56
If you want, go ahead and edit this and maybe add some extra steps, you know, see what you can do, maybe mess around with some other properties, and just really get a feel for defining keyframes.
6:06
Alright.
6:06
So for a quick challenge here, I am going to ask you to create an animation called grow.
6:12
You have to keep that name the same.
6:14
And I want it to start with a width and height of one hundred pixels and a color of blue, and it will shrink to a width and height of ten pixels and a color of red.
6:26
Alright?
6:27
Good luck.
6:30
So let's go ahead and get started.
6:31
The first thing we want to do is define our keyframes.
6:35
So we're going to say keyframes grow, So that's gonna be the name of the animation, and because we're only using two steps, I'm just gonna go ahead and use a from to method here.
6:47
So you can clearly see that the starting properties were different from the beginning properties.
6:53
So let's go ahead and set those.
6:55
We're gonna set the width to one hundred pixels and the height to one hundred pixels,
7:02
and then our background
7:06
to blue.
7:08
And then we are going to finish with a width and height of ten pixels.
7:14
So that's going to be inserted into our to box
7:19
and a background
7:22
of red.
7:24
Now let's go ahead and check it out.
7:27
You can see that it does that shrink with the color change as well.
7:32
Alright.
7:32
Let's move on.
