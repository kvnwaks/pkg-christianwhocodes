# Lesson 5: Transition Challenge

**Section A: Transitions** | Lesson 5 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- Using CSS pseudo-classes (`:hover`, `:active`, `:focus`)
- The `transition` property
- Transition duration
- Timing functions (ease, linear, ease-in, ease-out, ease-in-out)
- Transition delays
- Transition shorthand syntax

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

  /*transition-property: all;
    transition-duration: 1s;
    transition-timing-function: ease-in;
    transition-delay: 1s;*/

  transition: all 1s ease-in 1s;
}

.heading:hover {
  color: green;
  font-size: 10px;
}
```

### 🔄 What Changed

**New CSS rules added:**

- `.heading:hover {`

**New properties applied:**

- `/*transition-property: all;`
- `color: green;`
- `transition-delay: 1s;*/`
- `transition-timing-function: ease-in;`
- `transition: all 1s ease-in 1s;`

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

- [← Previous: Lesson 4](../04-Transition-Shorthand/)
- [→ Next: Lesson 6](../06-Real-World-Transitions-Challenge-Menu/)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
