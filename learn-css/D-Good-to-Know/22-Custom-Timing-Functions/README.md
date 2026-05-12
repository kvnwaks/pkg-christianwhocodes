# Lesson 22: Custom Timing Functions

**Section D: Good to Know** | Lesson 22 of 3

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- CSS custom properties (variables)

## 📖 Lesson Overview

Custom timing functions provide precise control over animation speed curves. Use `cubic-bezier()` for smooth custom easing, or `steps()` for discrete, frame-by-frame animations perfect for sprite sheets.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

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

**CSS** (`begin.css`):

```css
:root {
  --main-color: blue;
}

.hover-text {
  transition: all 3s;
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
  animation: size-down ease-in 0.5s infinite alternate both;
}

@keyframes size-down {
  100% {
    transform: scale(0.3, 0.3);
    background: var(--main-color);
  }
}
```

### Completed Code

**CSS** (`end.css`):

```css
:root {
  --main-color: blue;
}

.hover-text {
  transition: all 3s;
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
  animation: size-down cubic-bezier(1, 0, 1, 1) 0.5s 1 alternate both;
}

@keyframes size-down {
  100% {
    transform: scale(0.3, 0.3);
    background: var(--main-color);
  }
}
```

### 🔄 What Changed

**New properties applied:**

- `animation: size-down cubic-bezier(1, 0, 1, 1) 0.5s 1 alternate both;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 21](../21-CSS-Variables/)
- 🎉 **Congratulations! Course Complete!**
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
