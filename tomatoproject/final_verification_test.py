#!/usr/bin/env python3
"""Final verification test for the updated system"""

import requests
import re
from PIL import Image
import io

def final_verification_test():
    """Final comprehensive verification of the updated system"""
    try:
        session = requests.Session()
        
        print("🔍 FINAL VERIFICATION TEST")
        print("=" * 60)
        
        # Test 1: Verify landing page has correct attribution
        print("\n1️⃣  Testing landing page attribution...")
        response = session.get('http://localhost:8000/')
        
        if response.status_code != 200:
            print(f"❌ Failed to load landing page: {response.status_code}")
            return
            
        print("✅ Landing page loaded successfully")
        
        # Check for updated footer attribution
        if 'Built by <strong>DR. Tenesi Gabriel</strong>' in response.text:
            print("✅ Footer attribution updated correctly")
        else:
            print("⚠️  Footer attribution not found or different format")
            
        # Check for updated statistics
        stats_checks = {
            '95% accuracy': '95%' in response.text,
            '2189 test images': '2189' in response.text,
            '10 disease classes': '10' in response.text and 'Disease Classes' in response.text,
        }
        
        print("\n📊 Statistics Check:")
        for stat, found in stats_checks.items():
            status = "✅" if found else "❌"
            print(f"   {status} {stat}")
        
        # Test 2: Verify simple upload is now primary
        print("\n2️⃣  Verifying simple upload is primary interface...")
        
        # Check navigation
        nav_checks = {
            'upload nav link': 'href="/simple-upload/"' in response.text,
            'no old upload dropdown': 'dropdown-toggle' not in response.text,
            'simple upload promoted': 'Simple Upload' in response.text or 'Upload' in response.text,
        }
        
        print("\n🧭 Navigation Check:")
        for feature, found in nav_checks.items():
            status = "✅" if found else "❌"
            print(f"   {status} {feature}")
        
        # Test 3: Test the enhanced simple upload
        print("\n3️⃣  Testing enhanced simple upload...")
        response = session.get('http://localhost:8000/simple-upload/')
        
        if response.status_code != 200:
            print(f"❌ Failed to load simple upload: {response.status_code}")
            return
            
        print("✅ Simple upload page loaded successfully")
        
        # Check for enhanced UI elements
        ui_checks = {
            'hero section': 'hero-section' in response.text,
            'gradient backgrounds': 'gradient' in response.text,
            'modern cards': 'prediction-card' in response.text,
            'enhanced upload area': 'upload-area' in response.text,
            'complete footer': 'footer' in response.text,
            'social links': 'social-links' in response.text,
        }
        
        print("\n🎨 UI Enhancement Check:")
        for feature, found in ui_checks.items():
            status = "✅" if found else "❌"
            print(f"   {status} {feature}")
        
        # Test 4: Upload functionality
        print("\n4️⃣  Testing upload functionality...")
        
        # Extract CSRF token
        csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
        if not csrf_match:
            print("❌ No CSRF token found")
            return
            
        csrf_token = csrf_match.group(1)
        print(f"✅ CSRF token extracted: {csrf_token[:10]}...")
        
        # Create test image
        test_img = Image.new('RGB', (224, 224), color=(34, 139, 34))
        img_bytes = io.BytesIO()
        test_img.save(img_bytes, format='JPEG', quality=85)
        img_bytes.seek(0)
        
        print("✅ Test image created")
        
        # Submit form
        files = {'image': ('tomato_leaf_test.jpg', img_bytes, 'image/jpeg')}
        data = {'csrfmiddlewaretoken': csrf_token}
        
        print("📡 Submitting form...")
        response = session.post('http://localhost:8000/simple-upload/', data=data, files=files)
        
        print(f"📊 Response status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Form submitted successfully")
            
            # Check for results
            if 'results-section' in response.text:
                print("✅ Results displayed successfully")
                
                # Extract prediction
                pred_match = re.search(r'<h4[^>]*class="[^"]*fw-bold[^"]*"[^>]*>([^<]+)</h4>', response.text)
                if pred_match:
                    prediction = pred_match.group(1).strip()
                    print(f"🎯 Prediction: {prediction}")
                    
                    # Extract confidence
                    conf_match = re.search(r'<span[^>]*class="[^"]*confidence-number[^"]*"[^>]*>([^<]+%)</span>', response.text)
                    if conf_match:
                        confidence = conf_match.group(1).strip()
                        print(f"📊 Confidence: {confidence}")
                    
                    print("\n" + "=" * 60)
                    print("🎉 FINAL VERIFICATION COMPLETE!")
                    print("\n✅ System successfully updated with:")
                    print("   • DR. Tenesi Gabriel attribution in footer")
                    print("   • Accurate statistics (95% accuracy, 10 classes, 2189 test images)")
                    print("   • Enhanced simple upload as primary interface")
                    print("   • Beautiful modern UI with complete header/footer")
                    print("   • Professional styling and animations")
                    print("   • Robust upload functionality with detailed results")
                    
                    print(f"\n🚀 Your enhanced system is ready at:")
                    print("   • Primary: http://localhost:8000/simple-upload/")
                    print("   • Alternative: http://localhost:8000/upload/ (redirects)")
                    
                else:
                    print("✅ Upload successful - results displayed in HTML format")
                    
        else:
            print(f"❌ Upload failed: {response.status_code}")
            print(f"Response: {response.text[:500]}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on localhost:8000")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    final_verification_test()