#!/usr/bin/env python3
"""Test upload with CSRF token from form"""

import requests
import re
import json
from PIL import Image
import io

def test_with_form_csrf():
    """Test upload by extracting CSRF token from form"""
    try:
        session = requests.Session()
        
        print("📄 Getting simple upload form...")
        response = session.get('http://localhost:8000/simple-upload/')
        
        if response.status_code != 200:
            print(f"❌ Failed to get form: {response.status_code}")
            return
            
        print("✅ Got simple upload form")
        
        # Extract CSRF token from form
        csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
        if not csrf_match:
            print("❌ No CSRF token found in form")
            print("Looking for CSRF token in cookies...")
            print("Available cookies:", session.cookies.get_dict())
            return
            
        csrf_token = csrf_match.group(1)
        print(f"✅ Found CSRF token in form: {csrf_token[:10]}...")
        
        # Create a test image
        test_img = Image.new('RGB', (224, 224), color='green')
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Submit the form with CSRF token
        data = {'csrfmiddlewaretoken': csrf_token}
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("🚀 Submitting form with CSRF token...")
        response = session.post('http://localhost:8000/simple-upload/', data=data, files=files)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Form submitted successfully!")
            print(f"Response contains: {len(response.text)} characters")
            
            # Check for results or errors
            if 'error' in response.text.lower():
                print("❌ Error message found in response")
                # Try to extract error message
                error_match = re.search(r'<div[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</div>', response.text, re.IGNORECASE)
                if error_match:
                    print(f"Error: {error_match.group(1).strip()}")
            elif 'results' in response.text.lower() or 'confidence' in response.text.lower():
                print("✅ Results appear to be displayed!")
                # Try to extract prediction
                pred_match = re.search(r'<h3[^>]*>([^<]+)</h3>', response.text, re.IGNORECASE)
                if pred_match:
                    print(f"Prediction found: {pred_match.group(1).strip()}")
            else:
                print("📄 Response content (first 500 chars):")
                print(response.text[:500])
                
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
    test_with_form_csrf()