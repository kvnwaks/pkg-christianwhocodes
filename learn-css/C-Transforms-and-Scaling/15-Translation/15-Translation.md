0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we are gonna be talking about the next, uh, transform value or method, which is translation.
0:09
So what translation basically does is move the element that you're transforming across, uh, the x or the y axis depending on, uh, the function you're using or both.
0:21
It could be both depending, again, on what the function you're using, um, and can accept any sort of value based on, uh, the element.
0:29
So, for example, it can use pixels.
0:31
It can use percentages, um, any typical sizing
0:37
uh, value or unit that is used typically in other CSS parts of CSS, so for example, font sizes, width, height, things like that, can be used in the translate, uh, method.
0:49
So let's go ahead and get started.
0:51
Now what I'm gonna do is first talk about, uh, the similarities between this and other transform methods.
0:58
So in the last video, we talked about, um, scale x, scale y, and the scale shorthand, and pretty much all of the other transform functions follow this same method.
1:10
You have an x function or an x method, a y method, and then you have some shorthand that combines both axes.
1:18
So So let's go ahead and get started.
1:20
First thing I'm gonna do is translate it across the x axis.
1:24
So translate x.
1:25
Now let's just go ahead and say fifty pixels.
1:28
What this is gonna do is move it fifty pixels to the right.
1:33
And what you're doing here, imagine that you are adding fifty pixels onto, uh, you know, the width from the left of the page.
1:42
So as you add positive values, you're moving more towards the right.
1:46
If you imagine, like, a mathematical axis with, you know, the positive numbers on the right and the negative numbers on the left, then adding a positive value will continue to move it towards the right.
1:56
So if we go ahead and look at this here, you can see that it is moving fifty pixels along this axis.
2:04
So now let's go ahead and try out translate y.
2:08
So when we do that, you can see that it moves down as well.
2:13
So fifty pixels down and just like that.
2:17
Now we can also input negative values to this.
2:19
So if I give it negative fifty pixels, you can see that it'll move the opposite direction.
2:26
And if we give it, uh, translate x of negative fifty pixels, it'll move to the left just like that.
2:33
So now let's go ahead and talk about our shorthand.
2:37
So what I'm gonna do is set it to translate, And here, I am going to put, um, let's just say ten pixels.
2:46
This is gonna be the x axis, and then fifty pixels to the y axis.
2:50
And now you can see that it's going to move ten pixels to the left and fifty pixels downwards.
2:57
So again, this can use negative values, but like I said, it can also use other, um, values or other units.
3:04
So we can go ahead and say we want to translate this by negative ten percent.
3:09
So that's gonna be ten percent of the width because it's the x axis of our element.
3:14
And then we can also translate it maybe twenty percent on the y axis.
3:19
And you can see that it has the same effect, but instead this is using the values based on percentages.
3:26
So it's based on the actual element itself.
3:28
And it all depends on the situation that you're using it in.
3:31
Sometimes you may want to use absolute values such as pixels, and sometimes you want to use relative values such as percentages here.
3:38
It all depends on the situation, but just know that these functions, these transform methods, can support both.
3:44
Alright.
3:45
So now it's time for another challenge.
3:48
What I want you to do is to translate this box here by half of its width on the x axis and a quarter of its height on the y axis.
3:58
Good luck.
4:04
Alright.
4:04
Let's go ahead and get started.
4:06
So first thing we need to do is add our transform property.
4:10
Now I'm gonna go be going as usual with the shorthand method first, and then we're go we'll go the long way.
4:15
So let's go.
4:16
Translate just like that.
4:19
Now what we're gonna do is because we want to translate it by half of its width on the x axis, we're going to input fifty percent here.
4:28
Next thing we wanna do is add the, uh, y axis value, which is going to be twenty five percent because we wanted a quarter of its height.
4:40
And now you can see that that is working perfectly.
4:44
So you can see here that it is moving, uh, just as we intended it to in our translate function here.
4:49
Now if you wanted to split it up into separate parts, what we're gonna do here is say translate x fifty percent and translate y
5:02
twenty five percent.
5:03
So what this will do is, of course, separated by a space, it will add both transform methods and we will end up with the same result.
5:12
Alright.
5:12
Let's move on.
