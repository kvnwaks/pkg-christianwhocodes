0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we're gonna be talking about using something called a cubic bezier function to basically customize our timing when it comes to our transitions and animations.
0:13
So what are cubic Bezier functions?
0:16
Well, to think of it simply without going too deep into technical terms, two points from zero to one on both the x or horizontal and y or vertical axis are used to define a curve.
0:28
Now this curve is defined so that progression is on the y axis and the time passed since the start of the beginning of the animation or transition or whatever is going on on the x axis.
0:41
So basically what happens is over time the progression, is going to change.
0:47
Now this may sound a little bit complicated without putting it into words, so there's this really cool visualizer that helps you look at cubic bezier functions, um, to sort of visualize it and see what you're getting yourself into.
1:00
So here's an example of one of the pictures.
1:02
The website link is up here.
1:04
It's cubic bezier, cubic dash bezier dot com.
1:08
So what you can see here is two points, and these two points are placed around this this, uh, plane here from zero to one on both axes.
1:18
And what happens is this curve is defined, uh, based on wherever these points are placed.
1:24
Now what happens here is you can see that, um, you know, as time goes on, it the progression is quite slow, and then it speeds up, speeds up, and then slows down.
1:35
So this is kind of the equivalent of an ease in out function.
1:38
If you kind of look closely right there, you can see that's kind of what the function looks like And it goes, you know, the progression is quite slow at the beginning and then it increases and increases and gets faster and then it slows down towards the end.
1:53
So that's kind of how you can think about these things.
1:56
So I'll show you an example of another one.
1:59
So here is another image based on these points right here.
2:03
You can see the points are placed differently, and now the progression curve kind of happens differently.
2:08
So you can see it starts to progress really fast in the beginning and then gets slower and slower.
2:13
So you'll notice that all of these points here are between zero and one, but what happens if we go over that limit?
2:21
Well, here's an example of something that where it does go over that.
2:26
Now although it looks it is acceptable in terms of CSS, you can put it in and it won't cause an error.
2:31
What happens is the progression goes over a hundred percent.
2:36
So it actually goes beyond what the animation is supposed to be finishing at.
2:40
So for example, what would happen here is it progresses, progresses, and then it gets to one hundred percent and then jumps over so it it extends beyond the animation and then kind of bounces back.
2:51
It goes back downwards.
2:53
So what would happen here is for example, if you're trying to scale something up from, you know, a scale of one to a scale of two, what happens is it would scale up to two, then scale a little bit beyond two, and then shrink back down to the completion, which is at, uh, one hundred percent or the scale of two.
3:12
So we're gonna go ahead and write a couple of these cubic bezier functions in CSS, and we can basically define them just like we've used those words to define timing functions.
3:22
So things like ease, ease in, and ease in out.
3:25
So let's go ahead and do that now.
3:27
Now first of all, if you look at the top here, you can see, um, a sort of CSS definition of the cubic bezier function based on where your points are, uh, in the visual the visualizer.
3:39
But in case you're wondering what it stands for, the first point is gonna be the x coordinate of this pink point or the beginning point, then the y coordinate, and then the x and y coordinates of the second point respectively.
3:52
So let's go ahead and try and implement some of these, uh, cubic bezier functions and just see what they do.
3:59
So I'm gonna go ahead and use this first one right here.
4:01
So what I'm gonna do is go to our animation, and where it says, uh, when it gives our timing function, which is ease out right here, we're gonna turn this into a cubic Bezier,
4:15
and then we're gonna start defining our numbers.
4:17
So first it's gonna be the x and y coordinates of our beginners beginning point, which is point sixty two and point fifteen.
4:25
Point sixty two and point fifteen.
4:29
You can put zero point.
4:31
It won't really make a difference.
4:32
And then we put point four and point nine for our second point.
4:36
So point four and point nine.
4:40
So now let's go ahead and check out how our animation looks.
4:43
You can see that it looks drags drastically different from before.
4:46
It kind of slows and, you know, it's kind of like an ease in out cycle instead of just an ease out where it slows down towards the end.
4:54
So in my opinion, this does look a lot better.
4:57
And, you know, you may wanna customize it to something completely weird that you wouldn't find, um, in any other typical normal animation, uh, timing function.
5:08
So you wouldn't find it in an ease or an ease and out.
5:11
And this is honestly the real power of cubic cubic bezier functions is you can really customize your animations beyond what's available in just the normal CSS set, uh, progression curves.
5:23
And so this is where cubic beziers really come in handy.
5:27
But it's not just available to you in animations.
5:31
You can also use it pretty much anywhere that a timing function is used.
5:35
So for example, if I go ahead and that define the timing function of this transition here, I can also use this cubic bezier function in CSS right here.
5:47
And now when we hover over it oh, gotta refresh the page.
5:51
We hover over it, you can kind of notice how it speeds up and slows down.
5:56
Uh, it speeds up only in the middle.
5:58
So if I actually extend this, it'll make a little bit more.
6:01
Uh, you can see it a little bit better.
6:03
So let's go ahead and check that out.
6:06
So you can see that it speeds up and slows down towards the end, and it's also quite slow at the beginning.
6:13
Alright.
6:13
So now let's go ahead and start a challenge.
6:16
I want you to use that, um, that little website there to create or kind of visualize a cubic bezier function that starts off quite slow and then progresses and speeds up all the way towards the end.
6:30
So it starts off slow and then speeds up and go gets faster and faster and faster.
6:35
So it does not slow down towards the end.
6:37
It's kind of like an ease in.
6:39
So kind of think of it like that.
6:42
Alright.
6:42
Good luck.
6:44
Alright.
6:44
So let's go ahead and get started.
6:47
So what's gonna happen here is I am going I'm not really gonna show the visualizer, but what I got is a cubic bezier that looks similar to this right here.
6:58
So it doesn't have to be exactly like that.
7:00
It could be a variety of things, but as long as the this value, the second value is quite small and these other three are quite large, uh, relative to each other, then you should be in the clear.
7:14
Now the real tell comes in actually looking at the animation and seeing if it looks similar to mine, um, but we're we're gonna go ahead and look through that in just a second.
7:23
So let's go ahead and implement those cubic beziers.
7:27
So what I'm gonna do is go to my animation here, and I'm gonna replace this timing function with our cubic bezier.
7:34
Now if we look at it, you can see that it starts speeding up towards the end.
7:40
Now it's a little hard to tell since it's infinite and alternate.
7:43
So what I'm gonna do is just, uh, change that out.
7:47
So I'm gonna go to we'll go one iteration and keep that as alternate just so we can see how it works.
7:54
We refresh, and you can see that it starts off slow and speeds up towards the end.
7:59
So if it looks something like that you are doing it right, I recommend going around and playing with this a little bit so you can really get the feel for how cubic bezier's, uh, cubic bezier functions work and just, you know, interact and how they play into animations like this.
8:15
Alright.
8:16
So this pretty much concludes the course.
8:18
Unless more tips and tricks are added after this, as of now, uh, this course is complete.
8:24
I hope you learned a lot about CSS animations and transitions.
8:27
You really have come a long way and learned a ton of advanced CSS that can help you in your future web development career.
8:35
Alright.
8:36
Thanks for watching, and good luck.
