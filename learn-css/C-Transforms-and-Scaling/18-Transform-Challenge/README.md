# Lesson 18: Transform Challenge

**Section C: Transforms and Scaling** | Lesson 18 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- The `transform` property
- Translation with `translate()`, `translateX()`, `translateY()`
- Rotation with `rotate()`
- Scaling with `scale()`, `scaleX()`, `scaleY()`

## 📖 Lesson Overview

This practical challenge allows you to demonstrate mastery of the concepts covered. Work through the requirements methodically, building and testing your solution incrementally.

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
  /* top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); */
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
    transform: scale(0.5, 0.5) rotate(45deg) translate(50px, 0px);
  }
}
```

### 🔄 What Changed

**New CSS rules added:**

- `100% {`
- `@keyframes transform {`

**New properties applied:**

- `/* top: 50%;`
- `animation-iteration-count: infinite;`
- `animation-name: transform;`
- `transform: scale(0.5, 0.5) rotate(45deg) translate(50px, 0px);`
- `transform: translate(-50%, -50%); */`

**Result:** The element now has enhanced styling and animation behavior.

## 🎯 Challenge

This challenge tests your understanding of the concepts covered. Work through the requirements systematically:

1. Review the starting code
2. Plan your approach
3. Implement the solution incrementally
4. Test frequently in the browser
5. Refine and polish your code
6. Compare with the solution when complete

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 17](../17-Skew/)
- [→ Next: Lesson 19](../19-Real-World-Transforms-Challenge-Logo/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
