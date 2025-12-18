#!/usr/bin/env python3
"""Test the simple upload form (non-AJAX)"""

import requests
import json
from PIL import Image
import io

def test_simple_upload():
    """Test the simple upload form"""
    try:
        session = requests.Session()
        
        print("📄 Getting simple upload form...")
        response = session.get('http://localhost:8000/simple-upload/')
        
        if response.status_code != 200:
            print(f"❌ Failed to get form: {response.status_code}")
            print(f"Response: {response.text[:500]}")
            return
            
        print("✅ Got simple upload form")
        
        # Create a test image
        test_img = Image.new('RGB', (224, 224), color='green')
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Submit the form
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("🚀 Submitting simple upload form...")
        response = session.post('http://localhost:8000/simple-upload/', files=files)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Simple upload form submitted successfully!")
            print(f"Response contains: {len(response.text)} characters")
            
            # Check if results are in the response
            if 'results' in response.text.lower() or 'confidence' in response.text.lower():
                print("✅ Results appear to be displayed!")
            else:
                print("⚠️  Results may not be displayed, checking content...")
                # Look for error messages
                if 'error' in response.text.lower():
                    print("❌ Error message found in response")
                else:
                    print("📄 Response seems to be HTML page content")
                    
        elif response.status_code == 500:
            print("❌ Server error 500 - check server logs")
            print(f"Error response: {response.text[:1000]}")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            print(f"Response: {response.text[:500]}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on localhost:8000")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_simple_upload()