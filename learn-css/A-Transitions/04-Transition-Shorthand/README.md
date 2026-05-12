# Lesson 4: Transition Shorthand

**Section A: Transitions** | Lesson 4 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Understand how CSS transitions work
- Write transition declarations
- Control transition timing and duration

## 📚 Key Concepts

- Using CSS pseudo-classes (`:hover`, `:active`, `:focus`)
- The `transition` property
- Transition duration
- Timing functions (ease, linear, ease-in, ease-out, ease-in-out)
- Transition delays
- Transition shorthand syntax

## 📖 Lesson Overview

The transition shorthand property combines all transition sub-properties (property, duration, timing-function, and delay) into a single declaration, making your CSS more concise while maintaining full functionality.

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

  /* transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s; */

  transition: all 0.5s ease;

  /* You don't have to include delay if it's 0 seconds */
}

.heading:hover {
  color: red;
  font-size: 25px;
}
```

### 🔄 What Changed

**New properties applied:**

- `transition: all 0.5s ease;`

**Result:** The element now has enhanced styling and animation behavior.

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 3](../03-Customizing-Transitions/)
- [→ Next: Lesson 5](../05-Transition-Challenge/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
