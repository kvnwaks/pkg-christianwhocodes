0:00
Hi, welcome back.
0:01
So in this video we're going to be going over a couple other properties that we can use to customize our animations.
0:08
Now these aren't gonna be really focused on timing, but instead it's gonna be focused on how the animation plays out, its direction, and how it really behaves.
0:16
So let's go ahead and get started.
0:18
The first one I wanna talk about is the animation timing function.
0:24
So just like with transitions, this is going to allow us to specify how we want to work with our, uh,
0:33
um, our functions here.
0:34
So what we're gonna do is gonna go through, and we're gonna say ease or ease in, and this is just gonna specify the speed of our animation.
0:41
So let's go ahead and just set it as ease here.
0:44
Now I'm gonna go ahead and refresh, and you can see here that it kind of has that feel.
0:50
You can see it slow down towards the end.
0:52
So the next one I want to talk about is animation direction.
0:57
So this one is new, and it's basically gonna specify how we want our animation to play out.
1:03
So the default is it just goes through from start to finish, no real changes.
1:08
But here, we can actually say if we want it maybe to go backwards or if we want it to to alternate between backwards and forwards.
1:14
So for example, this box could shrink and then grow again.
1:19
So let's go ahead and look at that.
1:21
So the default value for this is normal, so that's basically from start to finish.
1:26
Nothing crazy.
1:27
And then we have reverse.
1:29
So this is going to, well, reverse our animation and basically go from finish to start.
1:33
You can see that here.
1:35
You You can see it starts as a red box and grows to that large blue box.
1:40
We also have two other properties or sorry, values, which are alternate, which which basically just, you know, oscillates between start and finish starting from the beginning one.
1:51
So this starts from, uh, our large blue box, and then we have alternate reverse.
1:58
So this is just like alternate, but instead of starting from the actual start, it actually starts from the finish.
2:04
So it's gonna start as that tiny red box and then grow and go back and forth.
2:09
So if we refresh here, we wait over that delay, and it grows back and forth just like that.
2:16
So the final one I wanna talk about, which is a little bit complicated because it can depend on the, you know, conditions here, is animation fill mode.
2:27
Fill mode.
2:29
So what this is gonna do is basically specify what styles we want to apply to our, um, box here or in any element with our animation, um, after the animation is complete.
2:43
So right now you can see that, you know, the end it looks a little bit choppy after the animation is finished.
2:49
We don't know what to do.
2:50
But in this case, we can actually, you know, for example, finish and apply the styles at the finish line.
2:56
Now the reason this is a little complicated to understand is because it also depends on the direction, um, and the iteration count of our function here or sorry, our animation.
3:08
So for example, if we have alternate reverse and we have the iteration count five times, for example, it could finish at the start, and you may get a little confused.
3:18
But I'd recommend, you know, just experimenting with this a little bit and, you know, really getting the feel for it.
3:23
So just to make things a little simpler, I'm going to remove or comment out the iteration count and the direction so it just goes from start to finish once.
3:32
So just to make sure, let's refresh.
3:35
There we go.
3:36
Now you can see it goes back to that blue box, uh, but what we want to do is if we want it to finish on our final property or our final styles, we set this value to forwards.
3:49
So we refresh, you can see it finishes and it stays there.
3:54
Or we can set it to backwards, which in this case is gonna set it to the beginning.
4:00
So we refresh, it shrinks, and then it sets to the beginning values.
4:06
And then we also have a special value called both, and what this is going to do is follow both rules, but it also depends.
4:14
And this is mainly used for things like alternate and alternate reverse, and this is basically going to depend on where it finishes.
4:20
It's just gonna get the styles of wherever it finishes based on the animation.
4:25
So if I go ahead and uncomment this out, change the iteration count and all of that, and we refresh, you can see it has all of these crazy maneuvers.
4:34
We don't know where it's gonna end, but that both property is gonna allow us to, um, finish it right there.
4:41
And so that's pretty much it.
4:43
So we have forwards, backwards, and both, and that's gonna allow you to specify what we want and basically just, you know, make sure that we can get our animation to finish on the right spot.
4:55
So now it's time for a little challenge.
4:57
I want you to set the timing function of this animation to ease in.
5:02
I want it to alternate starting from the beginning and alternate back and forth, and I want it to finish and retain the same styles that it finishes with.
5:12
Alright.
5:12
Good luck.
5:15
Alright.
5:15
Let's go ahead and get started.
5:17
So the first thing we wanna do is set the timing function.
5:20
So we're gonna use animation timing function and set this to ease in.
5:27
Next thing we wanna do is set our direction to alternate starting from the actual beginning.
5:33
So I'm gonna go ahead and do that.
5:36
Animation, direction, alternate.
5:41
Next thing we wanna do finally is set our fill mode, and I said I wanted these styles to finish on whatever the style is finished on depending on, you know, if it finishes at this actual start or the actual end.
5:54
And, of course, the way we do this is with, first of all, the animation fill mode property, and then we wanna use the both, uh, values.
6:04
So this is going to allow us to set the styles based on wherever the animation finishes.
6:10
Let's go ahead and check this out.
6:13
You refresh.
6:14
You can see it has that ease.
6:16
The iterations play through, and then it finishes on the correct style with the correct timing function.
6:22
Alright.
6:23
So good job.
6:24
You finished that challenge, and now we're gonna bring all of this together and, first of all, use a shorthand to, you know, combine all these properties and then complete a large challenge.
6:35
Alright.
6:35
Let's move on.
