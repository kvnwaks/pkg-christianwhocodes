# Lesson 15: Translation

**Section C: Transforms and Scaling** | Lesson 15 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Use CSS transform functions
- Combine transforms for complex effects

## 📚 Key Concepts

- The `transform` property
- Translation with `translate()`, `translateX()`, `translateY()`
- Scaling with `scale()`, `scaleX()`, `scaleY()`

## 📖 Lesson Overview

The `translate()` function moves elements horizontally and vertically without affecting document flow. Use `translateX()` and `translateY()` for individual axis control, or the combined `translate(x, y)` for both axes.

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
    transform: translateX(50%) translateY(25%);
  }
}
```

### 🔄 What Changed

**New properties applied:**

- `transform: translateX(50%) translateY(25%);`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 14](../14-Introduction-to-Transforms-and-Scaling/)
- [→ Next: Lesson 16](../16-Rotation/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
