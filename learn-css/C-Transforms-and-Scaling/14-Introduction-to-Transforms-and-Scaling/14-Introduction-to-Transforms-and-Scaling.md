0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we are gonna move on from animations and start looking at some of the effects and special CSS tricks that we can use to enhance our animation skills.
0:11
So in this section, we're gonna be learning about transforms and transform methods.
0:17
So, basically, what these are are certain methods and values that you can combine with a certain property, which we're gonna learn about in just a second, that can be used to change an element, uh, in some way.
0:28
So this could be used to change positioning, scaling, rotation, all sorts of things, and it can really enhance an animation using a simple method.
0:38
So you can see here I have a little animation set up.
0:40
Now don't worry about it.
0:42
This is just to demonstrate the properties that we're gonna be working with, but the majority of the section is gonna be focused on actually working with, um, these transform methods and and the values.
0:54
So what I'm gonna do is throughout the section, we're gonna be using these transform values in here, and then what's gonna happen is the animation is going to run it through.
1:03
And so here, this box will have those transforms applied to it so we can see what's going on.
1:10
So let's go ahead and get started.
1:12
Now what we're gonna use here is something called the transform property.
1:16
And what you do is you type this, uh, sort of function.
1:19
It looks like a function, and you pass some values into it.
1:22
And what this function will do is transform,
1:27
hence the name of the property, the element in some way.
1:30
So you can see that for the box itself, I actually already use a transform to move it to the center.
1:37
And what you can see here is we have this, um, function, so it has brackets.
1:42
And then what this does is basically you give it the you give the transform property this function, and it's going to translate our box by a certain amount.
1:52
So that's a little intro to it, and in this video we're gonna be talking about the scale property or transform.
1:59
So let's go ahead and get started.
2:01
Now the first thing you need to know about transform, the transform property, is the multiple methods that you can use to work with it.
2:09
So typically, you're just gonna be inserting one transform.
2:13
So in this case, it's the translate property.
2:16
But this can also be used in multiple ways.
2:18
So for example, this is translating it on both the x, so the horizontal, and the y or vertical axis.
2:25
But if you wanted to translate it in one axis alone, there's a separate function for that.
2:30
In the case of scale, that would be scale x.
2:34
So if I'm gonna go ahead and type scale x here, and in here we're gonna input the value that we want it to scale by as a multiple of its own size.
2:44
So for example, if I put a two in here, it's going to double in size on the x scale.
2:49
If we look at the animation here, you can see that on the horizontal axis, it is doubling in size.
2:57
We can also input decimal numbers here to represent
3:01
smaller sizes.
3:02
So for example, if I put zero point five, this is gonna represent half its original size.
3:07
We look here, you can see it shrinks.
3:11
Now that's for the x axis.
3:12
For the y axis, all you have to do is input or change this to scale y.
3:18
Quite simple.
3:19
Now you can see you can see now instead of having that horizontal shrink, we're having a vertical shrink while the horizontal distance remains, uh, the same.
3:30
Now what if you wanted to use both of them in conjunction together?
3:34
Well, there is actually two ways to do this.
3:37
Now what you can do with the transform property is use multiple transforms on the same line.
3:42
All you have to do is separate them by spaces.
3:44
So So for example, if I wanted to scale the, uh, our box horizontally by a factor of two and scale it vertically by a factor of zero point five or basically half its, uh, vertical size, we can just write it like that separated by a space.
4:05
Now you can see it doubles on the horizontal axis and halves on the y axis.
4:11
But there is an easier way to do this and it's a shorthand that we can use to combine these two together.
4:16
So what this is called is just scale.
4:19
So what we're gonna do is just type out scale.
4:22
Now what's gonna happen here is we have the x value first.
4:25
So in this case it's gonna be two, and then the y value, which is zero point five.
4:31
And now you can see we get the same result.
4:34
Now this space rule still applies, and you can combine the scale transform with other transforms.
4:41
But in terms of just combining scale properties and transforms alone, this works just fine.
4:47
And again, if you want to use the shorthand, uh, but, you know, avoid scaling in one axis, we can just set a value to one.
4:57
So what this is gonna do is just scale it to the same size that it currently is at, which just doesn't do anything.
5:04
Oh, oops.
5:06
So you can see there what this does is it scales it on the x axis by two, or you can just write this as scale x two.
5:14
Alright.
5:14
So now it's time for a little challenge.
5:16
What I want you to do is to scale this box right here by a factor of two on the x axis and a factor of four on the y axis.
5:26
Now you can do this using either the long method or the shorthand method.
5:31
As long as you get the result, I will show both ways.
5:33
It is fine.
5:35
Alright.
5:35
Good luck.
5:40
Alright.
5:40
So let's go ahead and get started.
5:42
So the first thing I'm gonna do is use the transform property,
5:47
and now I'm gonna go with the shorthand method first.
5:50
We type scale, and remember it is the x scale followed by the y scale.
5:54
So we're going to start with two, which was our x scale, and then four, which was our y scale, and then finish it with a semicolon.
6:03
Now we look at it, you can see it is scaling properly.
6:07
Now if we want to use the long method, what we can do is use the space rule to split split up these transforms into two separate functions, but keep them in the same property.
6:17
So we're gonna start with scale x, which solely focuses on the horizontal or x axis.
6:23
We're gonna set that to two, and then follow it by scale y.
6:29
Remember, separated by a space not a comma.
6:32
That and then we set this value to four, and you can see we get the same result.
6:37
Alright.
6:38
Let's move on.
