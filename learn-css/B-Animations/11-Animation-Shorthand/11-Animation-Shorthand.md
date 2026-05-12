0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we are gonna be learning a shorthand to combine six of these animation properties into one line.
0:09
Just like we did with the transition section, there is a single property that allows us to shorten this whole thing and combine it into a single property.
0:19
So this property is called animation, and it basically goes in the order that you see here.
0:25
So it starts with the name, which is gonna be grow, then the duration, just one second.
0:30
I'm basically just taking all of these values from here.
0:34
Then our timing function, which is gonna be ease in, then our delay, one second, our iteration count, four, and finally, our direction, which is alternate.
0:48
So it does look quite intimidating, but as long as you, you know, get this order down, you will get it in no time.
0:55
Now if you notice, there is no fill mode included in this animation.
1:00
So if you wanna set the fill mode at all, most people don't really it's not really commonly used, but if you want to, you can add it in, uh, on top of this shorthand.
1:11
So let's go ahead and comment this out.
1:14
Now let's go ahead and check out the animation.
1:17
So I'm gonna refresh, and then you see it does the exact same thing as it did before with all the shrinking, and then, of course, we use the fill mode, uh, on top of the shorthand to animate it.
1:29
Alright.
1:30
So now it's time for a little challenge.
1:32
So I want you to use the shorthand to apply this animation to this box.
1:38
It needs to have a one second duration and no delay at all.
1:41
It's gonna have a timing function of ease.
1:45
It's going to alternate, so it's gonna start and then, you know, keep going back and forth from the start, and it's going to run forever.
1:53
Alright.
1:54
Good luck.
1:58
Alright.
1:58
Let's go ahead and add this property.
2:01
So first thing we're gonna do is use the animation shorthand.
2:05
First thing we're gonna set is the name of the animation, which is grow, then the duration, which is one second.
2:12
Then we're gonna go ahead and add our timing function, which is ease, then our delay, which is zero seconds, and then our, um, we want it to run forever, so we're gonna use infinite.
2:25
This is equal the equivalent of the iteration count, and then our direction.
2:30
And since we want it to start from the actual true start and go back and forth, we're gonna use alternate.
2:37
Now notice that we're not going to add a fill mode or a, uh, anything like that because this is going to run forever, and so the animation will never end.
2:48
And therefore, we don't really need to add an end mode.
2:51
Now let's say or sorry, a fill mode.
2:53
Now let's say we wanted to change this to something like reverse.
2:58
Now if we did this, the animation would only run a oh, sorry.
3:02
Well, not the direction.
3:02
We're not gonna change the direction.
3:05
Let's say we wanted to change this, sorry, to maybe two iterations.
3:09
This is a finite number, and it will end at one point, and therefore we're gonna need to set the fill mode.
3:15
But in this case, since it's infinite, it will never end and therefore we do not need to set the fill mode.
3:22
So if we go ahead and look our at our animation here, you can see that it's running through with the properties that we set here forever.
3:30
Alright.
3:30
So that's pretty much it for animations.
3:32
Good job on making it this far.
3:34
Uh, you've learned a ton about all sorts of things to do with CSS animations and transitions.
3:40
In the next video, we're gonna go through and complete a large challenge.
3:45
Alright.
3:46
Let's move on.
