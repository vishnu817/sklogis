SK LOGISTICS — Mobile App Setup
================================

OPTION A: Netlify (Easiest - Internet Required)
-------------------------------------------------
1. Go to https://netlify.com/drop on your PC
2. Drag SKL_Mobile_App.html onto the page
3. Get a free HTTPS link (e.g. https://skl-abc123.netlify.app)
4. Open that link on your phone — camera works!

OPTION B: Local HTTPS Server (Works on WiFi, No Internet Needed)
-----------------------------------------------------------------
STEP 1 — Install Python (if not installed):
   Download from https://python.org/downloads
   During install, tick "Add Python to PATH"

STEP 2 — Put these files in ONE folder on your PC:
   - SKL_Mobile_App.html
   - serve.py
   - cert.pem
   - key.pem
   - START_SERVER.bat

STEP 3 — Double-click START_SERVER.bat
   It will show a link like:
   https://192.168.1.5:8443/SKL_Mobile_App.html

STEP 4 — Open that link on your phone
   (Phone must be on same WiFi as your PC)

STEP 5 — Phone shows a security warning:
   Tap "Advanced" → "Proceed to 192.168.x.x (unsafe)"
   This is safe — it's your own PC.

STEP 6 — Camera will now work!
   Allow camera when prompted.

NOTE: Keep the server running (don't close the black window)
      while using the app on your phone.
