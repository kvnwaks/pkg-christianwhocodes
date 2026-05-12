# Lesson 21: CSS Variables

**Section D: Good to Know** | Lesson 21 of 3

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- CSS custom properties (variables)

## 📖 Lesson Overview

CSS custom properties (variables) let you store values that can be reused throughout your stylesheet. They're especially powerful for animations, allowing you to change animation parameters from a single location or dynamically with JavaScript.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

```html
<html>
  <head>
    <link rel="stylesheet" href="begin.css" />
  </head>
  <body>
    <p class="hover-text">Hover over me!</p>
    <div class="box"></div>
  </body>
</html>
```

**CSS** (`begin.css`):

```css
.hover-text {
  transition: all 0.5s;
}

.hover-text:hover {
  color: #290000;
  font-size: 20px;
}

.box {
  position: fixed;
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
  animation: size-down ease-out 0.5s infinite alternate both;
}

@keyframes size-down {
  100% {
    transform: scale(0.3, 0.3);
    background: #290000;
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
    <p class="hover-text">Hover over me!</p>
    <div class="box"></div>
  </body>
</html>
```

**CSS** (`end.css`):

```css
:root {
  --main-color: blue;
}

.hover-text {
  transition: all 0.5s;
}

.hover-text:hover {
  color: var(--main-color);
  font-size: 20px;
}

.box {
  position: fixed;
  width: 50px;
  height: 50px;
  background: red;
  border: 1px solid black;
  animation: size-down ease-out 0.5s infinite alternate both;
}

@keyframes size-down {
  100% {
    transform: scale(0.3, 0.3);
    background: var(--main-color);
  }
}
```

### 🔄 What Changed

**New CSS rules added:**

- `:root {`

**New properties applied:**

- `--main-color: blue;`
- `background: var(--main-color);`
- `color: var(--main-color);`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 20](../20-Prefixes/)
- [→ Next: Lesson 22](../22-Custom-Timing-Functions/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
