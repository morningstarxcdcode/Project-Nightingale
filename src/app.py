# Flask API for Project Nightingale

from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data, evaluate_model
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def get_health():
    """Get health status of the API"""
    return jsonify({
        "status": "healthy",
        "message": "Project Nightingale API is running",
        "version": "1.0.0"
    })

@app.route('/api/data', methods=['POST'])
def post_data():
    """Process data using the AI model"""
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"error": "Missing 'data' field in request"}), 400
        
        input_data = data['data']
        # Preprocess the data
        processed_input = preprocess_data(input_data)
        
        # Run through AI model
        result = simple_ai_model(processed_input)
        
        logging.info(f"Processed data: {input_data} -> {result}")
        
        return jsonify({
            "success": True,
            "original_data": input_data,
            "processed_data": processed_input,
            "ai_result": result
        })
    
    except Exception as e:
        logging.error(f"Error processing data: {str(e)}")
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    """Make predictions using the AI model"""
    try:
        data = request.get_json()
        if not data or 'input' not in data:
            return jsonify({"error": "Missing 'input' field in request"}), 400
        
        input_data = data['input']
        prediction = simple_ai_model(input_data)
        
        return jsonify({
            "success": True,
            "input": input_data,
            "prediction": prediction,
            "confidence": 0.95  # Placeholder confidence score
        })
    
    except Exception as e:
        logging.error(f"Error making prediction: {str(e)}")
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to Project Nightingale API",
        "endpoints": {
            "health": "/api/health",
            "data": "/api/data (POST)",
            "predict": "/api/predict (POST)"
        }
    })

if __name__ == '__main__':
    logging.info("Starting Project Nightingale Flask API...")
    app.run(host='0.0.0.0', port=5000, debug=True)