# Slack GIF Creator: API and Animation Reference

## Available Utilities

### GIFBuilder (`core.gif_builder`)
Assembles frames and optimizes for Slack:
```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)  # Add PIL Image
builder.add_frames(frames)  # Add list of frames
builder.save('out.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

### Validators (`core.validators`)
Check if GIF meets Slack requirements:
```python
from core.validators import validate_gif, is_slack_ready

passes, info = validate_gif('my.gif', is_emoji=True, verbose=True)
if is_slack_ready('my.gif'):
    print("Ready!")
```

### Easing Functions (`core.easing`)
Smooth motion instead of linear:
```python
from core.easing import interpolate

t = i / (num_frames - 1)
y = interpolate(start=0, end=400, t=t, easing='ease_out')
# Available: linear, ease_in, ease_out, ease_in_out, bounce_out, elastic_out, back_out
```

### Frame Helpers (`core.frame_composer`)
```python
from core.frame_composer import (
    create_blank_frame,         # Solid color background
    create_gradient_background,  # Vertical gradient
    draw_circle,                # Helper for circles
    draw_text,                  # Simple text rendering
    draw_star                   # 5-pointed star
)
```

## Animation Concepts

### Shake/Vibrate
- Use `math.sin()` or `math.cos()` with frame index
- Add small random variations for natural feel
- Apply to x and/or y position

### Pulse/Heartbeat
- Use `math.sin(t * frequency * 2 * math.pi)` for smooth pulse
- For heartbeat: two quick pulses then pause
- Scale between 0.8 and 1.2 of base size

### Bounce
- Use `interpolate()` with `easing='bounce_out'` for landing
- Use `easing='ease_in'` for falling (accelerating)
- Apply gravity by increasing y velocity each frame

### Spin/Rotate
- PIL: `image.rotate(angle, resample=Image.BICUBIC)`
- For wobble: use sine wave for angle instead of linear

### Fade In/Out
- Create RGBA image, adjust alpha channel
- Or use `Image.blend(image1, image2, alpha)`

### Slide
- Start position: outside frame bounds
- End position: target location
- Use `interpolate()` with `easing='ease_out'` for smooth stop
- For overshoot: use `easing='back_out'`

### Zoom
- Zoom in: scale from 0.1 to 2.0, crop center
- Zoom out: scale from 2.0 to 1.0

### Explode/Particle Burst
- Generate particles with random angles and velocities
- Update: `x += vx`, `y += vy`, `vy += gravity_constant`
- Fade out particles over time

## Optimization Strategies

Only when asked to make file size smaller:

1. **Fewer frames** - Lower FPS (10 instead of 20) or shorter duration
2. **Fewer colors** - `num_colors=48` instead of 128
3. **Smaller dimensions** - 128x128 instead of 480x480
4. **Remove duplicates** - `remove_duplicates=True` in save()
5. **Emoji mode** - `optimize_for_emoji=True`

```python
builder.save('emoji.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

## Making Graphics Look Good

**Use thicker lines** - Always `width=2` or higher. Thin lines look choppy.

**Add visual depth**:
- Gradients for backgrounds (`create_gradient_background`)
- Layer multiple shapes (star with smaller star inside)

**Make shapes interesting**:
- Add highlights, rings, patterns to circles
- Stars can have glows (larger semi-transparent versions behind)
- Combine shapes (stars + sparkles, circles + rings)

**Colors**:
- Vibrant, complementary colors
- Contrast (dark outlines on light, light on dark)

**Complex shapes** (hearts, snowflakes):
- Combinations of polygons and ellipses
- Calculate points for symmetry
- Add details (highlight curves, intricate branches)
