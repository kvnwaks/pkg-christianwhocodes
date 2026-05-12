# Lesson 11: Animation Shorthand

**Section B: Animations** | Lesson 11 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Using `from` and `to` keywords
- Setting animation duration
- Controlling iteration count
- Animation direction (normal, reverse, alternate)
- Animation fill mode

## 📖 Lesson Overview

The `animation` shorthand combines all animation sub-properties (name, duration, timing-function, delay, iteration-count, direction, fill-mode, play-state) into one declaration for cleaner code.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

```html
<html>
  <head>
    <link rel="stylesheet" href="begin.css" />
  </head>
  <body>
    <div class="box"></div>
  </body>
</html>
```

**CSS** (`begin.css`):

```css
/* Apply animation to box. 1s duration, no delay at all, timing function of 'ease', alternate, run forever  */

.box {
  width: 100px;
  height: 100px;
  background: blue;
  border: 1px solid black;
}

@keyframes grow {
  from {
    width: 100px;
    height: 100px;
    background: blue;
  }
  to {
    width: 10px;
    height: 10px;
    background: red;
  }
}
```

### Completed Code

**HTML** (`end.html`):

```html
<html>
  <head>
    <link rel="stylesheet" href="end.css" />
  </head>
  <body>
    <div class="box"></div>
  </body>
</html>
```

**CSS** (`end.css`):

```css
.box {
  width: 100px;
  height: 100px;
  background: blue;
  border: 1px solid black;

  /* animation-name: grow;
    animation-duration: 1s;
    animation-timing-function: ease;
    animation-delay: 0s;
    animation-iteration-count: infinite;
    animation-direction: alternate; */

  animation: grow 1s ease 0s infinite alternate;
}

@keyframes grow {
  from {
    width: 100px;
    height: 100px;
    background: blue;
  }
  to {
    width: 10px;
    height: 10px;
    background: red;
  }
}
```

### 🔄 What Changed

**New properties applied:**

- `/* animation-name: grow;`
- `animation-direction: alternate; */`
- `animation-duration: 1s;`
- `animation-iteration-count: infinite;`
- `animation-timing-function: ease;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 10](../10-Animations-Other-Properties/)
- [→ Next: Lesson 12](../12-Animation-Challenge/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
