#!/usr/bin/env python3
"""Test the API endpoint directly"""

import requests
import json

def test_api_endpoint():
    """Test the /api/predict/ endpoint"""
    try:
        # Create a simple test image
        from PIL import Image
        import io
        
        # Create a small test image
        test_img = Image.new('RGB', (224, 224), color='green')
        
        # Save to bytes
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Test the API endpoint
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("🧪 Testing API endpoint: http://localhost:8000/api/predict/")
        response = requests.post('http://localhost:8000/api/predict/', files=files)
        
        print(f"📡 Response status: {response.status_code}")
        print(f"📊 Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✅ API response: {json.dumps(data, indent=2, default=str)}")
                print("\n🎉 API endpoint test PASSED!")
            except json.JSONDecodeError as e:
                print(f"❌ Invalid JSON response: {e}")
                print(f"Response text: {response.text[:500]}")
        else:
            print(f"❌ API error {response.status_code}: {response.text[:500]}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on localhost:8000")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_api_endpoint()