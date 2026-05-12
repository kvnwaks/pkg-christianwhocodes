0:00
Hi.
0:00
Welcome back.
0:01
So in this video, we are gonna be learning about CSS prefixes and what they are important for.
0:08
So you can see I have a little setup going with some hovers and transitions and, uh, some animations here.
0:14
Now although this may work here, on some of the older browsers, so for example, if you're using old versions of Internet Explorer or Chrome, these newer features of CSS may not be supported.
0:26
And every browser has its own way of interpreting and rendering, uh, this CSS, and sometimes browsers don't work with these normal properties.
0:35
So what you actually need to do is to really have as much browser support and to display those animations on as many, uh, devices as possible is you need to use these things called CSS prefixes.
0:49
Now one common trick is that for maximum compatibility, prefixes are used in combination with a fallback property in case this newer CSS feature doesn't render.
1:00
So for example, if you're using a newer or normal version of an Internet browser, what this transition or animation would render fine.
1:09
But if you're using something like Internet Explorer eight or seven or one of those really old versions, um, you would use something that is simpler and easier to render.
1:17
So for example, this would just, uh, be one solid color or this animation wouldn't happen at all.
1:24
So in this video, we're gonna be focusing on the prefix part of this, um, of this problem of browser compatibility.
1:32
So there are a couple of prefixes that are used for support in different browsers.
1:37
Now the way you write a prefix is whatever property that you want to try and add support for is you go dash and then the prefix, dash again, and then the rest of your property.
1:49
So for example, it could be animation, and you would just paste that in.
1:54
Now although you pasted it twice, one of them is for general support, and one of them is for support for a specific browser.
2:01
So let's go over some of the common, um, some of the common prefixes.
2:07
So the first and most widely used is WebKit.
2:10
So this is mainly used to support um, iOS or tablet browsers.
2:15
So for example, Safari or some Android browsers or Chrome, and this is has a lot of support for mobile.
2:21
So you would include this to add mobile support.
2:24
The next one that we use is MS, and this stands for Microsoft.
2:29
And what this basically is is for support for Internet Explorer.
2:33
So those super old versions of Internet Explorer that don't usually, um, support these typical animations will now be supported, uh, using this prefix.
2:42
The next one that we typically use is m o z, Moz, for Firefox.
2:48
And finally, the last one is for the Opera browser, which is just dash o.
2:55
So let's go ahead and insert that.
2:57
So you can see that this makes absolutely no change to what we're doing here.
3:01
Everything is working just fine.
3:03
But the reason that you need to include this is, as I said, to add browser compatibility because if these lines weren't in here, if you were using something like a phone to view this page, then, um, it wouldn't render properly.
3:17
So the next thing I wanna talk about is where would you use these transitions.
3:22
Now usually, you can search up if you or sorry, prefixes.
3:25
You can usually search up if you need to use these prefixes, but it's usually you usually need to use it with the newer versions of CSS.
3:33
So for example, animations and transitions are relatively new, so you would need to use prefixes.
3:39
So what you would do is for here, you would go with the exact same system.
3:44
So you can go webkit dash, and then what I usually do is just copy this over for everything.
3:51
So we'll go with m s, m o z, and o, just like that.
3:59
And so we've inserted all of these browser web kits.
4:03
So we've done all of this, and we're working with it fine.
4:06
Now, again, make sure to search it up and make sure that you need to include, um, these prefixes.
4:13
Now it doesn't really hurt to include them.
4:15
It won't cause any major errors, but I would so I would recommend to be as explicit as possible and use all of the, uh, CSS prefixes to try and add as much support as possible.
4:27
And this is when those shorthands really come in useful because if you were splitting this up into six different, uh, properties for this animation here, what you would have to do is copy that over four more times for all six of those properties for each prefix.
4:42
So this is where those shorthands really come in useful.
4:47
Alright.
4:47
So now it's time for a quick challenge.
4:49
What I want you to do is add browser support for this transition property here.
4:55
Good luck.
4:58
So let's go ahead and get started.
5:00
Now you may have seen this earlier in the video, but we're just gonna go through with it and do it again.
5:05
So we're gonna use the four main prefixes, which are the ones for tablets and mobile devices, the one for Internet Explorer, Firefox, and Opera.
5:15
So we're gonna start with WebKit, which is used for the tablet and older versions of Chrome.
5:23
So let's go ahead and do that.
5:25
Then we're gonna go with our MS for Microsoft or our, um, older versions of Internet Explorer.
5:32
Again, I'd recommend just copying it over.
5:34
It's a lot simpler and just takes up less time.
5:38
Then we're gonna go with our next, uh, prefix, which is Moz, and then finally, o for opera.
5:46
So there we go.
5:47
We have now added full almost full browser support for this, um, element here.
5:53
Now again, I would recommend also adding a fallback if you're going for a large, uh, site that you're trying to reach as wide of an audience as possible with as wide a range of devices.
6:05
Add some fallback using an older feature or property of CSS just to make sure that, um, this runs smoothly on all devices.
6:14
Even though it may not be exactly what you want, it's still better than having, uh, maybe a broken page that doesn't have the styles you want.
6:21
You can just kinda customize it according to the needs of each user.
6:26
Alright.
6:26
Let's move on.
