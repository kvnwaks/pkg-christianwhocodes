0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we are gonna be going through and performing a challenge that not only combines all of the features and methods learned in this section, but also some of the animation skills that we learned in the previous section.
0:14
So the challenge goes as follows.
0:16
You need to create an animation that lasts two seconds and runs infinitely.
0:21
It has default timing functions, and everything else is default.
0:25
The only things you need is that the name of the animation are is transform.
0:29
It lasts two seconds and has an infinite run time.
0:34
So it runs forever, basically.
0:37
So this this animation is going to scale our, uh, box here that we have in our screen, and it's going to take it and scale it down by a factor of two, which means it's going to half in size.
0:53
This box is going to be translated fifty pixels to the right here and zero pixels down.
1:00
So it's just going to be translated fifty pixels to the right, and it's also going to be rotated by forty five degrees.
1:08
Alright.
1:09
Good luck.
1:12
Alright.
1:13
Let's go ahead and get started.
1:14
So the first thing I wanna do is define the animation.
1:17
So I'm gonna write keyframes and then the name, which is transform.
1:23
And then since we only really wanna end up in a destination and we don't have any starting values, we're just going to put one hundred percent.
1:32
So this is just going to define the end of the animation.
1:37
We don't need to define a start point since we're not changing anything at the start.
1:41
So before I write anything down, let's go ahead and add this animation to our box.
1:46
So I'm gonna go animation name.
1:49
This is gonna be transform,
1:52
and we said it's going to last two seconds.
1:55
So animation duration is gonna be two seconds, and then it needs to run forever.
2:01
So we're gonna go animation iteration count infinite.
2:06
So there we go.
2:06
We've added the animation.
2:08
Now let's go ahead and talk about some of the transforms that we need to do.
2:12
So first thing we're gonna need to use is the transform property.
2:16
Now I'm gonna start at the super low basic level.
2:19
We're just gonna start from, you know, individual axes like scale x, scale y, and then we're gonna work up and combine them using shorthands.
2:27
So let's start with our scaling.
2:29
I said I want it to half in size.
2:32
So what we're gonna do is use the scale x and scale y functions.
2:36
Remember, separated by a space since, uh, if you want to use multiple transform methods, you need to separate them just like that.
2:43
And because we want to basically have it in size, we're gonna use zero point five, just like that.
2:50
Next thing we want to do is rotate it by forty five degrees.
2:54
So what we're gonna do is use the rotate method here, and then forty five degrees.
3:01
Now I did not specify whether it was supposed to be clockwise or counterclockwise, so either way could have been fine as long as it's forty five degrees.
3:09
If you did it counterclockwise, it would look like this.
3:12
Again, both methods are acceptable.
3:16
The last thing I wanted to do is translate it by a certain amount, which I said fifty to the right.
3:22
So what we're gonna do is use the translate x method and use fifty pixels here, just like that.
3:30
Now we didn't say we wanted any y translation, so we don't need to include a translate y.
3:36
So there we go.
3:37
That's what we're doing.
3:38
And if we look at it, it's being translated.
3:40
Everything is working fine.
3:42
Now, of course, the translation may not work exactly as we want due to our transforms here, but if I go ahead and, uh, comment them out, you can see that it is now being translated fifty pixels, scaled down, and rotated forty five degrees to the right.
3:57
And just to clear things up, this the reason it wasn't translating maybe perfectly before is because of the code I put in here to center our box in the middle of the page.
4:08
Um, so don't worry about that.
4:09
This does work perfectly.
4:11
So now let's go ahead and actually combine these because there are some things we can do here to shorten it up a little bit.
4:17
So the first thing I'm gonna do is combine the scale x and scale y, uh, transform methods into a single method.
4:24
So we're gonna use scale, and of course this takes the x value and the y value just like that.
4:31
The rotate method doesn't have any shorthand since it's only doesn't have multiple axes, um, so this is fine.
4:38
Now we can also shorten this down into a shorthand.
4:41
You don't really need to since we don't have both translate x and translate y, But just to, you know, show you how it will work, I do it now.
4:49
So what I'm gonna do is erase this.
4:52
We're gonna go and use the translate method, and of course no x or y, just translate.
4:57
Then we're gonna start with the x value, which is fifty pixels, and the y value, which is zero pixels.
5:03
Since we didn't have anything, we don't wanna move it down.
5:06
And there you go.
5:06
It works fine.
5:08
Now this is the shorthand form of it.
5:11
Of course, you can also keep this as translate x fifty pixels, and you don't need this zero.
5:17
It is all up to preference and how you want to order it, um, but as long as you end up with this result where it's shrinking, rotating, and translating, then you should be fine.
5:27
Alright.
5:27
Let's move on.
