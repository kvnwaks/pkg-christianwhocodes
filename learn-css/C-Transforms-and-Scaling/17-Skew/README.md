# Lesson 17: Skew

**Section C: Transforms and Scaling** | Lesson 17 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Skewing with `skew()`, `skewX()`, `skewY()`

## 📖 Lesson Overview

The `skew()` function distorts elements by slanting them along the X or Y axis, creating perspective effects. Use `skewX()` and `skewY()` individually or combine them for complex distortions.

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

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 16](../16-Rotation/)
- [→ Next: Lesson 18](../18-Transform-Challenge/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
