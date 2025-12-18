#!/usr/bin/env python3
"""Test the API endpoint with CSRF token"""

import requests
import json

def test_api_with_csrf():
    """Test the /api/predict/ endpoint with proper CSRF handling"""
    try:
        # First, get a CSRF token by visiting any page
        session = requests.Session()
        
        print("🍪 Getting CSRF token...")
        response = session.get('http://localhost:8000/client-side-upload/')
        
        if response.status_code != 200:
            print(f"❌ Failed to get CSRF token: {response.status_code}")
            return
            
        # Extract CSRF token from cookies
        csrf_token = session.cookies.get('csrftoken')
        if not csrf_token:
            print("❌ No CSRF token found in cookies")
            print("Available cookies:", session.cookies.get_dict())
            return
            
        print(f"✅ Got CSRF token: {csrf_token[:10]}...")
        
        # Create a simple test image
        from PIL import Image
        import io
        
        test_img = Image.new('RGB', (224, 224), color='green')
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Test the API endpoint with CSRF token
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        headers = {'X-CSRFToken': csrf_token}
        
        print("🧪 Testing API endpoint with CSRF token...")
        response = session.post('http://localhost:8000/api/predict/', files=files, headers=headers)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✅ API response: {json.dumps(data, indent=2, default=str)}")
                print("\n🎉 API endpoint with CSRF test PASSED!")
                
                # Verify the response structure
                if data.get('success') and data.get('prediction'):
                    pred = data['prediction']
                    print(f"\n📊 Prediction Summary:")
                    print(f"   Disease: {pred['class']}")
                    print(f"   Confidence: {pred['confidence']:.1f}%")
                    if pred.get('disease_info'):
                        print(f"   Symptoms: {pred['disease_info'].get('symptoms', 'N/A')[:100]}...")
                
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
    test_api_with_csrf()