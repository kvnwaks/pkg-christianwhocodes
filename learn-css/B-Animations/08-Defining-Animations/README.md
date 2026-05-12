# Lesson 8: Defining Animations

**Section B: Animations** | Lesson 8 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Defining `@keyframes` rules
- Using `from` and `to` keywords
- Using percentage-based keyframes
- Animation fill mode

## 📖 Lesson Overview

The `@keyframes` rule defines the stages of an animation. You can use `from` and `to` keywords for simple two-step animations, or percentage values (0%, 50%, 100%) for complex multi-step sequences with precise control over each stage.

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
  animation-name: grow;
  animation-duration: 2s;
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
  animation-name: grow;
  animation-duration: 2s;
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

**New CSS rules added:**

- `@keyframes grow {`
- `from {`
- `to {`

**New properties applied:**

- `background: blue;`
- `height: 100px;`
- `height: 10px;`
- `width: 100px;`
- `width: 10px;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 7](../07-Animations-In-Action/)
- [→ Next: Lesson 9](../09-Animations-Timing/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
