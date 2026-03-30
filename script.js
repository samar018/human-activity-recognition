// Activity labels (15 classes)
const activities = [
    'Walking', 'Running', 'Standing', 'Sitting', 'Lying Down',
    'Climbing Stairs', 'Descending Stairs', 'Jumping', 'Cycling',
    'Stretching', 'Bending', 'Reaching', 'Pushing', 'Pulling', 'Lifting'
];

// Handle file upload
const imageInput = document.getElementById('imageInput');
const uploadBox = document.getElementById('uploadBox');
const previewContainer = document.getElementById('previewContainer');
const previewImage = document.getElementById('previewImage');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultContainer = document.getElementById('resultContainer');

// Drag and drop functionality
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#764ba2';
    uploadBox.style.background = '#f8f9fa';
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.style.borderColor = '#667eea';
    uploadBox.style.background = 'white';
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#667eea';
    uploadBox.style.background = 'white';
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleImageUpload(files[0]);
    }
});

// File input change
imageInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleImageUpload(e.target.files[0]);
    }
});

// Handle image upload
function handleImageUpload(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please upload an image file');
        return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        uploadBox.style.display = 'none';
        previewContainer.style.display = 'block';
        resultContainer.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

// Analyze button click
analyzeBtn.addEventListener('click', async () => {
    analyzeBtn.textContent = 'Analyzing...';
    analyzeBtn.disabled = true;

    // Simulate API call with delay
    await new Promise(resolve => setTimeout(resolve, 1500));

    // Get random prediction (in real app, this would be from your ML model API)
    const prediction = getPrediction();
    
    displayResults(prediction);
    
    analyzeBtn.textContent = 'Analyze Activity';
    analyzeBtn.disabled = false;
});

// Simulate prediction (replace with actual API call)
function getPrediction() {
    const randomIndex = Math.floor(Math.random() * activities.length);
    const confidence = (Math.random() * 15 + 85).toFixed(1); // 85-100%
    
    return {
        activity: activities[randomIndex],
        confidence: confidence
    };
}

// Display results
function displayResults(prediction) {
    const predictionLabel = document.getElementById('predictionLabel');
    const confidenceFill = document.getElementById('confidenceFill');
    const confidenceText = document.getElementById('confidenceText');

    predictionLabel.textContent = prediction.activity;
    confidenceFill.style.width = prediction.confidence + '%';
    confidenceText.textContent = prediction.confidence + '% Confidence';

    resultContainer.style.display = 'block';
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// API Integration (uncomment and modify when you have a backend)
/*
async function analyzeImage(imageFile) {
    const formData = new FormData();
    formData.append('image', imageFile);

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Prediction failed');
        }

        const data = await response.json();
        return {
            activity: data.predicted_class,
            confidence: data.confidence
        };
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to analyze image. Please try again.');
        return null;
    }
}
*/
