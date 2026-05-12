# Lesson 20: Prefixes

**Section D: Good to Know** | Lesson 20 of 3

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Vendor prefixes (-webkit-, -moz-, -ms-, -o-)
- CSS custom properties (variables)

## 📖 Lesson Overview

Vendor prefixes (-webkit-, -moz-, -ms-, -o-) ensure animations work across different browsers. While modern browsers need fewer prefixes, understanding them is important for supporting older browsers and production code.

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
.hover-text {
  transition: all 0.5s;
  -webkit-transition: all 0.5s;
  -ms-transition: all 0.5s;
  -moz-transition: all 0.5s;
  -o-transition: all 0.5s;
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

### 🔄 What Changed

**New properties applied:**

- `-moz-transition: all 0.5s;`
- `-ms-transition: all 0.5s;`
- `-o-transition: all 0.5s;`
- `-webkit-transition: all 0.5s;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [→ Next: Lesson 21](../21-CSS-Variables/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
