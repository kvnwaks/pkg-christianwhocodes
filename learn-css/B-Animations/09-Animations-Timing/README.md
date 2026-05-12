# Lesson 9: Animations Timing

**Section B: Animations** | Lesson 9 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Defining `@keyframes` rules
- Using `from` and `to` keywords
- Using percentage-based keyframes
- Setting animation duration
- Controlling iteration count

## 📖 Lesson Overview

Animation timing is controlled through duration (how long one iteration takes), timing functions (the speed curve), and delay (waiting before starting). These properties let you create animations that feel natural and purposeful.

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
.box {
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
}

@keyframes first-animation {
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
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
  animation-name: first-animation;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-iteration-count: 4;
}

@keyframes first-animation {
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

- `animation-delay: 1s;`
- `animation-duration: 1s;`
- `animation-iteration-count: 4;`
- `animation-name: first-animation;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 8](../08-Defining-Animations/)
- [→ Next: Lesson 10](../10-Animations-Other-Properties/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
