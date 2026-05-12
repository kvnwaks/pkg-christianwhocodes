# Lesson 3: Customizing Transitions

**Section A: Transitions** | Lesson 3 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Understand how CSS transitions work
- Write transition declarations
- Control transition timing and duration

## 📚 Key Concepts

- Using CSS pseudo-classes (`:hover`, `:active`, `:focus`)
- The `transition` property and its syntax
- Transition duration
- Timing functions (ease, linear, ease-in, ease-out, ease-in-out)
- Transition delays

## 📖 Lesson Overview

Transitions can be customized with duration that control the length of time the transition should take, timing functions that control the acceleration curve (like `ease`, `linear`, `ease-in-out`), delays that postpone the start of the animation.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

```html
<html>
  <head>
    <link rel="stylesheet" href="begin.css" />
  </head>
  <body>
    <h1 class="heading">Hover over me!</h1>
  </body>
</html>
```

**CSS** (`begin.css`):

```css
.heading {
  color: darkblue;
  font-size: 15px;
}

.heading:hover {
  color: red;
  font-size: 25px;
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
    <h1 class="heading">Hover over me!</h1>
  </body>
</html>
```

**CSS** (`end.css`):

```css
.heading {
  color: darkblue;
  font-size: 15px;
  transition-property: font-size;
  transition-duration: 0.5s;
  transition-timing-function: ease-in;
  transition-delay: 1s;
}

.heading:hover {
  color: red;
  font-size: 25px; /* On hover, increase font-size */
}
```

### 🔄 What Changed

**New properties applied:**

- `transition-property: font-size;`
- `transition-duration: 0.5s;`
- `transition-timing-function: ease-in;`
- `transition-delay: 1s;`

**Result:** The element now has enhanced styling and animation behavior. The font-size is increased smoothly on hover.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 2](../02-Adding-Transitions/)
- [→ Next: Lesson 4](../04-Transition-Shorthand/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
