# Lesson 2: Adding Transitions

**Section A: Transitions** | Lesson 2 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Understand how CSS transitions work
- Write transition declarations
- Control transition timing and duration

## 📚 Key Concepts

- Using CSS pseudo-classes (`:hover`, `:active`, `:focus`)
- The `transition` property and its syntax
- Timing functions (ease, linear, ease-in, ease-out, ease-in-out)
- Transition shorthand syntax

## 📖 Lesson Overview

To create a transition, you need two things: a CSS property change (often triggered by pseudo-classes like `:hover`) and the `transition` property that specifies which properties to animate and how long the animation should take.

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
  transition: all 0.5s;
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
  transition: all 0.5s;
}

.heading:hover {
  color: green;
  font-size: 20px;
  letter-spacing: 20px;
}
```

### 🔄 What Changed

**New CSS rules added:**

- `.heading:hover {`

**New properties applied:**

- `color: green;`
- `font-size: 20px;`
- `letter-spacing: 20px;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 1](../01-What-are-Transitions/)
- [→ Next: Lesson 3](../03-Customizing-Transitions/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
