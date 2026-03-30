# Human Activity Recognition - Frontend

A modern, responsive web interface for showcasing the Human Activity Recognition AI/ML project.

## Features

- 🎨 Clean and modern UI design
- 📱 Fully responsive (mobile, tablet, desktop)
- 🖼️ Drag & drop image upload
- 🤖 Real-time activity prediction display
- 📊 Model performance statistics
- 🎯 15 activity classes recognition

## Project Structure

```
├── index.html          # Main HTML file
├── style.css           # Styling
├── script.js           # Frontend JavaScript
├── api.py             # Flask API backend
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Quick Start

### Option 1: View Frontend Only

Simply open `index.html` in your web browser. The demo will work with simulated predictions.

### Option 2: Run with Backend API

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Update the model path in `api.py`:**
   ```python
   model = tf.keras.models.load_model('path/to/your/model.h5')
   ```

3. **Start the Flask API:**
   ```bash
   python api.py
   ```

4. **Update `script.js` to use the API:**
   - Uncomment the `analyzeImage` function at the bottom
   - Replace the `getPrediction()` call with actual API call

5. **Open `index.html` in your browser**

## API Endpoints

- `GET /api/health` - Check API health status
- `POST /api/predict` - Upload image and get prediction
- `GET /api/activities` - Get list of all activity classes

## Recognized Activities

The model can recognize 15 different human activities:
- Walking
- Running
- Standing
- Sitting
- Lying Down
- Climbing Stairs
- Descending Stairs
- Jumping
- Cycling
- Stretching
- Bending
- Reaching
- Pushing
- Pulling
- Lifting

## Models Used

- **EfficientNet** - Efficient CNN optimized for accuracy and speed
- **ResNet50** - Deep residual network with 50 layers
- **VGG19** - 19-layer deep network for image classification
- **AlexNet** - Classic CNN architecture

## Customization

### Update Activity Classes
Edit the `activities` array in `script.js` and `ACTIVITIES` list in `api.py`

### Change Colors
Modify the gradient colors in `style.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add More Statistics
Update the stats section in `index.html` with your actual model metrics

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Notes

- The frontend works standalone with simulated predictions
- For real predictions, connect to the Flask API backend
- Make sure to load your trained model in `api.py`
- Adjust image preprocessing in `api.py` based on your model's requirements

## License

MIT License
