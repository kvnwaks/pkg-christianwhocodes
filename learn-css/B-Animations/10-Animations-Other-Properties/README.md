# Lesson 10: Animations Other Properties

**Section B: Animations** | Lesson 10 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Create and define keyframe animations
- Apply animations to HTML elements

## 📚 Key Concepts

- Using `from` and `to` keywords
- Controlling iteration count
- Animation direction (normal, reverse, alternate)
- Animation fill mode

## 📖 Lesson Overview

Advanced animation properties control how animations repeat (`iteration-count`), their playback direction (`normal`, `reverse`, `alternate`), what happens before/after animation (`fill-mode`), and whether they're running or paused (`play-state`).

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
  width: 100px;
  height: 100px;
  background: blue;
  border: 1px solid black;
  animation-name: grow;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-iteration-count: 4;
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
  width: 100px;
  height: 100px;
  background: blue;
  border: 1px solid black;
  animation-name: grow;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-iteration-count: 4;

  animation-timing-function: ease-in;
  animation-direction: alternate;
  animation-fill-mode: both;
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

**New properties applied:**

- `animation-direction: alternate;`
- `animation-fill-mode: both;`
- `animation-timing-function: ease-in;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 9](../09-Animations-Timing/)
- [→ Next: Lesson 11](../11-Animation-Shorthand/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
