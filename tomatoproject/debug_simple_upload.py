#!/usr/bin/env python3
"""Debug the simple upload form response"""

import requests
import re
import json
from PIL import Image
import io

def debug_simple_upload():
    """Debug the simple upload response"""
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
        csrf_token = csrf_match.group(1) if csrf_match else None
        print(f"✅ Found CSRF token: {csrf_token[:10] if csrf_token else 'None'}")
        
        # Create a test image
        test_img = Image.new('RGB', (224, 224), color='green')
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Submit the form
        data = {'csrfmiddlewaretoken': csrf_token} if csrf_token else {}
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("🚀 Submitting form...")
        response = session.post('http://localhost:8000/simple-upload/', data=data, files=files)
        
        print(f"📡 Response status: {response.status_code}")
        print(f"📊 Response length: {len(response.text)} characters")
        
        # Save full response for analysis
        with open('/home/ogega/Projects/Tomato_Disease_Detection-main/tomatoproject/debug_response.html', 'w') as f:
            f.write(response.text)
        print("💾 Full response saved to debug_response.html")
        
        # Look for specific content
        print("\n🔍 Analyzing response:")
        
        # Check for Django error page
        if 'django' in response.text.lower() and 'error' in response.text.lower():
            print("❌ Django error page detected")
            
        # Look for specific error patterns
        error_patterns = [
            r'<div[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</div>',
            r'<li[^>]*>([^<]*error[^<]*)</li>',
            r'<p[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</p>',
            r'<span[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</span>'
        ]
        
        for pattern in error_patterns:
            matches = re.findall(pattern, response.text, re.IGNORECASE)
            if matches:
                print(f"❌ Error messages found:")
                for match in matches[:3]:  # Show first 3 matches
                    print(f"   - {match.strip()}")
                break
        
        # Look for prediction results
        if 'confidence' in response.text.lower():
            print("✅ 'confidence' found in response")
        if 'prediction' in response.text.lower():
            print("✅ 'prediction' found in response")
            
        # Extract and show key sections
        sections = [
            (r'<div[^>]*class="[^"]*results[^"]*"[^>]*>(.*?)</div>', 'Results section'),
            (r'<div[^>]*class="[^"]*error[^"]*"[^>]*>(.*?)</div>', 'Error section'),
            (r'<div[^>]*class="[^"]*alert[^"]*"[^>]*>(.*?)</div>', 'Alert section'),
        ]
        
        for pattern, name in sections:
            match = re.search(pattern, response.text, re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
                print(f"\n📋 {name} (first 200 chars):")
                print(re.sub(r'<[^>]+>', '', content)[:200] + "...")
                
        # Show first 500 characters of cleaned content
        print(f"\n📄 First 500 characters (cleaned):")
        cleaned = re.sub(r'<[^>]+>', '', response.text)
        print(cleaned[:500])
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on localhost:8000")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_simple_upload()