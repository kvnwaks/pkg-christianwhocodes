# Lesson 16: Rotation

**Section C: Transforms and Scaling** | Lesson 16 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements
- Use CSS transform functions
- Combine transforms for complex effects

## 📚 Key Concepts

- The `transform` property
- Rotation with `rotate()`

## 📖 Lesson Overview

The `rotate()` function spins elements around a point (default: center). Rotation values are specified in degrees (deg), and the transform origin can be changed to rotate around different points.

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
    transform: rotate(-180deg);
  }
}
```

### 🔄 What Changed

**New properties applied:**

- `transform: rotate(-180deg);`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 15](../15-Translation/)
- [→ Next: Lesson 17](../17-Skew/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
