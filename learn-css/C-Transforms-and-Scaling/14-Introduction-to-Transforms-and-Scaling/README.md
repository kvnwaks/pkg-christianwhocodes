# Lesson 14: Introduction to Transforms and Scaling

**Section C: Transforms and Scaling** | Lesson 14 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements
- Use CSS transform functions
- Combine transforms for complex effects

## 📚 Key Concepts

- The `transform` property
- Translation with `translate()`, `translateX()`, `translateY()`
- Scaling with `scale()`, `scaleX()`, `scaleY()`

## 📖 Lesson Overview

CSS transforms manipulate elements in 2D space using functions like `translate()`, `rotate()`, `scale()`, and `skew()`. Transforms are GPU-accelerated and don't trigger layout recalculation, making them highly performant.

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
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: fixed;
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
  animation-name: transform;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes transform {
  100% {
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
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: fixed;
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
  animation-name: transform;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes transform {
  100% {
    transform: scaleX(2) scaleY(4);
  }
}
```

### 🔄 What Changed

**New properties applied:**

- `transform: scaleX(2) scaleY(4);`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [→ Next: Lesson 15](../15-Translation/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
