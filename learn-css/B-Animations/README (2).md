# Section B: Animations

**Intermediate Level** | 7 Lessons

## Overview

CSS animations take you beyond simple transitions, enabling complex, multi-step animations using keyframes. You'll learn to create sophisticated effects that can run automatically or in response to user interactions.

## What You'll Learn

- Understanding keyframe animations
- Defining custom animation sequences
- Controlling animation timing and behavior
- Using animation properties: iteration, direction, and fill mode
- Combining animations with other CSS properties
- Building animated landing pages

## Prerequisites

- Completion of [Section A: Transitions](../A-Transitions/README.md)
- Comfort with CSS selectors and properties
- Basic understanding of CSS timing

## Learning Path

### Lessons

7. **[Animations In Action](./07-Animations-In-Action/)** ⭐ _Start Here_
   - Introduction to CSS animations
   - Seeing keyframe animations in action
   - Differences between transitions and animations

8. **[Defining Animations](./08-Defining-Animations/)**
   - Creating `@keyframes` rules
   - Defining animation steps
   - Applying animations to elements

9. **[Animations Timing](./09-Animations-Timing/)**
   - Controlling animation duration
   - Using timing functions with animations
   - Setting animation delays

10. **[Animations Other Properties](./10-Animations-Other-Properties/)**
    - Animation iteration count (loop forever or specific times)
    - Animation direction (normal, reverse, alternate)
    - Animation fill mode (what happens before/after animation)
    - Animation play state (running or paused)

11. **[Animation Shorthand](./11-Animation-Shorthand/)**
    - Simplifying animation declarations
    - Understanding shorthand syntax
    - Writing maintainable animation code

12. **[Animation Challenge](./12-Animation-Challenge/)** 🎯
    - Practice exercise
    - Create custom keyframe animations
    - Test your mastery of animation properties

13. **[Real-World Challenge: Landing Page](./13-Real-World-Animations-Challenge-Landing-Page/)** 🚀
    - Build an animated landing page
    - Create expanding background effects
    - Implement text fade-in animations
    - Apply professional animation techniques

## Key Concepts

- **Keyframes**: Define the stages of an animation sequence
- **Animation Name**: Connects an element to a keyframe definition
- **Iteration Count**: How many times the animation repeats
- **Direction**: Whether animation plays forward, backward, or alternates
- **Fill Mode**: How styles are applied before/after animation
- **Play State**: Control whether animation is running or paused

## Common Patterns

```css
/* Define keyframes */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Apply animation */
.element {
  animation: fadeIn 1s ease-in;
}
```

## Tips for Success

- Name your keyframes descriptively (`fadeIn`, `slideRight`, etc.)
- Use percentage values (0%, 50%, 100%) for precise control
- Start with simple 2-step animations (from/to)
- Use `animation-fill-mode: forwards` to keep final state
- Test animations at different speeds to find the right feel

## Performance Considerations

- Animate `transform` and `opacity` for best performance
- Avoid animating properties that trigger layout recalculation
- Use `will-change` sparingly for performance-critical animations

## Next Steps

After mastering animations, proceed to [Section C: Transforms and Scaling](../C-Transforms-and-Scaling/README.md) to learn how to add rotation, scaling, and skewing effects to your animations.

---

[← Back to Section A](../A-Transitions/README.md) | [← Back to Course Home](../README.md) | [Start First Lesson →](./07-Animations-In-Action/)
