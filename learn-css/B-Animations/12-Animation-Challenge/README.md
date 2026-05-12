# Lesson 12: Animation Challenge

**Section B: Animations** | Lesson 12 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- Defining `@keyframes` rules
- Using percentage-based keyframes
- Setting animation duration
- Controlling iteration count
- Animation fill mode

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
  width: 10px;
  height: 10px;
  background: blue;
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
  width: 10px;
  height: 10px;
  background: blue;
  border: 1px solid black;
  /* Note: 6 animation properties, excluding animation-fill-mode */
  animation: supersize 2s ease-out 0s 5 alternate;
  animation-fill-mode: both;
}

@keyframes supersize {
  50% {
    width: 20px;
    height: 20px;
    background: red;
  }
  100% {
    width: 50px;
    height: 50px;
    background: green;
  }
}
```

### 🔄 What Changed

**New CSS rules added:**

- `100% {`
- `50% {`
- `@keyframes supersize {`

**New properties applied:**

- `/* Note: 6 animation properties, excluding animation-fill-mode */`
- `animation: supersize 2s ease-out 0s 5 alternate;`
- `background: green;`
- `height: 20px;`
- `width: 50px;`

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

- [← Previous: Lesson 11](../11-Animation-Shorthand/)
- [→ Next: Lesson 13](../13-Real-World-Animations-Challenge-Landing-Page/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
