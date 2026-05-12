0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we're gonna be talking about CSS variables and how we can use them to really work and, you know, shorten our styling process and just streamline the whole thing, make everything more efficient.
0:14
So CSS variables are a way of storing values of any kind in some placeholder that you can then use multiple times throughout the, um, throughout your styling process.
0:27
And some of the main advantages of this are, first of all, if you want to change or if you want to use a single value or a color, for example, uh, on multiple elements, all you have to do is assign it to a variable and then use that variable over and over again.
0:41
And the other advantage is that if you want to update something, you don't have to go through and change that value for every single element it's applied to.
0:49
You can just go to wherever you defined your variable, write down, make your changes, or whatever, and it will update for all of the elements that you changed it for.
0:59
So how do we actually define variables?
1:03
So what you're gonna wanna use is something called this, the root, just like that.
1:10
Now what this is is it's basically defining, um, whatever whatever styles or things that you wanna define outside of any elements.
1:18
Because what you wanna do is if you define a variable inside of these elements, they will only be applicable to that element that you defined it in based on the selector, which basically renders the entire thing useless.
1:30
So you need to use this selector right here, the root selector, to define your variables.
1:36
Now to define a variable, what you're gonna do is start with two dashes, and from there you're gonna type out whatever you want your variable name to be, and if you have any if you have multiple words, you're gonna separate them by, uh, dashes.
1:49
So let's say, for example, I wanted to shorten this, um, this right here, this fifty pixels, which is defining our box unit.
1:59
So let's go ahead and call it box unit just like that.
2:03
And remember, we're separating it by a dash for spaces.
2:07
Then we put our colon and then whatever value want we want to assign it, just like that.
2:14
So now what we have done is declare this variable called box unit in the root, and here, this will be applicable to all of the elements here.
2:23
Now in order to use this, you can't just type it in.
2:26
You need to use the var function.
2:28
So what you do is you type out var.
2:32
Oh, oops.
2:33
And then here, you're gonna type the name of the variable.
2:35
So in this case, it's box unit.
2:38
We do the same thing for the height,
2:44
just like that, and now you can see that we have successfully defined our variable, and it works perfectly.
2:51
Now if I wanted to maybe change this box unit variable, all I have to do is go to the top, set it to one hundred, for example, and now you can see it changes both the width and the height.
3:03
Now although it may not seem that all all that practical with just two, uh, uses of the variable, but when you have maybe hundreds of boxes, let's say, and you want to and they all have the exact same width and height, this would come in extremely handy because you only have to change it in one location.
3:22
Alright.
3:22
So now it's time for a little challenge.
3:24
You can see that we have this color right here, this hex code color used two times in our CSS stylesheet.
3:32
What I want you to do is define a variable called main color, change it to this value, and then use that variable to represent this color instead of the explicit value itself.
3:43
Alright.
3:44
Good luck.
3:47
Alright.
3:48
So the first thing we need to do is go through and define the root selector here so that we can use our variable across the entire, um, style sheet.
4:00
Next thing we want to do is use the two dashes to indicate that we are declaring a variable.
4:05
Then we put our name, main dash color again.
4:09
Make sure to space it properly.
4:11
And then we put in our value, which is just gonna be this color code right here.
4:17
Next thing we wanna do is change all of these definitions to the uses of the variable.
4:22
So again, we need to use the var function to make sure that we are getting the variable itself, and then we type in the name just like that.
4:31
Now what I'm gonna do is go ahead and copy this over to the other use of this value, and when we paste it, let's just make sure everything's working, we hover, and the animation is working fine.
4:45
Now again, if you wanted to change this color, so, for example, if you want to just set it to plain, uh, blue maybe, that would also work.
4:53
Now we hover over it, changes to blue, and right here, the animation, uh, is using the blue color instead.
5:00
Alright.
5:01
Let's move on.
